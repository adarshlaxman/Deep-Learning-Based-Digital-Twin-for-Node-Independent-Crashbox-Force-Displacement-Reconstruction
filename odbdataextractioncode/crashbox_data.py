# ==========================================================
# Crashbox Spatial–Temporal Dataset Extraction
# Global RF3 from Reference Point + Local U3
# Abaqus/Explicit LE SAFE
# ==========================================================

from odbAccess import openOdb # type: ignore (uncomment before # type: ignore  running )
import csv

# ---------------- USER SETTINGS ----------------
odb_path = r"C:\temp\SIM\Jobcrashboxtesr.odb"
step_name = "Step-1"

crashbox_instance = "CRASHBOX-1"
reference_set_name = "REFERENCE_POINT_        1"  # EXACT name from ODB

MAX_NODES = 50
# ------------------------------------------------

# Open ODB
odb = openOdb(odb_path, readOnly=True)
step = odb.steps[step_name]
assembly = odb.rootAssembly

# Crashbox nodes (local deformation)
crashbox = assembly.instances[crashbox_instance]
nodes = crashbox.nodes[:MAX_NODES]

# Reference node (global force)
ref_set = assembly.nodeSets[reference_set_name]

# 👉 CORRECT way to access label
ref_node_label = ref_set.nodes[0][0].label

print("Using reference node label:", ref_node_label)
print("Crashbox nodes selected:", len(nodes))
print("Total frames:", len(step.frames))

csv_path = r"C:\temp\SIM\crashbox_spatial_temporal_data_FIXED.csv"

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Time", "NodeLabel", "X", "Y", "Z", "U3", "RF3_GLOBAL"
    ])

    for frame in step.frames:
        time = frame.frameValue

        # -------- GLOBAL FORCE (RF3 at Reference Point) --------
        rf_field = frame.fieldOutputs["RF"]
        rf3_global = 0.0

        for v in rf_field.values:
            if v.nodeLabel == ref_node_label:
                rf3_global = v.data[2]
                break

        # -------- LOCAL DISPLACEMENT (U3 at crashbox nodes) ----
        u_field = frame.fieldOutputs["U"]
        u_map = {v.nodeLabel: v.data[2] for v in u_field.values}

        for node in nodes:
            label = node.label
            x, y, z = node.coordinates
            u3 = u_map.get(label, 0.0)

            writer.writerow([
                time, label, x, y, z, u3, rf3_global
            ])

odb.close()

print("SUCCESS ✅")
print("Saved corrected dataset to:")
print(csv_path)
