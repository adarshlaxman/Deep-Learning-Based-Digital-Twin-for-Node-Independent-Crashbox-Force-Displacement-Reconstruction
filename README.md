# Deep-Learning-Based-Digital-Twin-for-Node-Independent-Crashbox-Force-Displacement-Reconstruction


```
Crashbox_DL_Digital_Twin/
│
├── 01_data_preprocessing.ipynb
├── 02_mlp_training.ipynb
│
├── crashboxsimulationfiles/
│   ├── crashboxtest.cae
│   ├── Jobcrashboxtesr.inp
│   └── Jobcrashboxtesr.odb
│
├── data/
│   ├── raw/
│   │   └── crashbox_spatial_temporal_data_FIXED.csv
│   └── processed/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_test.csv
│       ├── scaler_X.pkl
│       └── scaler_y.pkl
│
├── models/
│   └── crashbox_mlp.pt
│
├── odbdataextractioncode/
│   └── crashbox_data.py
```

---


---

```markdown
# Deep Learning–Based Digital Twin for Node-Independent Crashbox Force–Displacement Reconstruction

This repository contains a **physics-consistent deep learning digital twin** developed to
reconstruct the **global force–displacement response of a crashbox** from **local nodal
deformation data**, while remaining **independent of nodal identity**.

The project integrates **Abaqus/Explicit finite element simulation** with **machine learning**
to enable **accurate, stable, and generalizable crash response prediction**.

---

## 🔍 Project Overview

Finite element crash simulations accurately capture nonlinear deformation and energy absorption,
but they are computationally expensive and produce **node-dependent scattered outputs**.

This project addresses these limitations by building a **node-independent digital twin** that:

- Learns the **global crashbox force–displacement law**
- Generalizes to **unseen nodes**
- Preserves physical behavior
- Enables **real-time inference**

---

## 🧠 Key Contributions

- Physics-aware data extraction from Abaqus ODB
- Spatial–temporal dataset construction
- Node-based train/test split (no data leakage)
- Deep learning regression model (MLP)
- Generalization to completely unseen nodes
- Learned spatial sensitivity envelope
- Physics-consistent force–displacement reconstruction

---

## 🧩 Methodology Pipeline

1. **Crashbox Simulation (Abaqus/Explicit)**
   - Thin-walled crashbox under axial crushing
   - Large plastic deformation and contact
   - Global reaction force measured at reference point

2. **ODB Data Extraction**
   - Global reaction force RF3
   - Local axial displacement U3 from multiple nodes
   - Spatial coordinates (X, Y, Z) and time
   - Extracted using Abaqus Python API

3. **Spatial–Temporal Dataset**
```

Input : [Time, X, Y, Z, U3]
Output: RF3

```

4. **Node-Based Learning Strategy**
- Entire nodes held out during testing
- Forces true spatial generalization

5. **Deep Learning Digital Twin**
- Multi-Layer Perceptron (MLP)
- Learns mapping from local deformation to global force

---

 

---

## 📊 Key Results

- **Generalization to unseen nodes**
  - R² ≈ **0.80**
  - RMSE ≈ **0.44**

- **Physics preservation**
  - Digital twin overlaps Abaqus mean force–displacement response

- **Spatial sensitivity**
  - Learned σ-envelope highlights nonlinear crushing regions

- **Efficiency**
  - Inference in milliseconds vs minutes for FEA

---

## 🛠 Tools & Technologies

- Abaqus/Explicit — Finite element simulation
- Python — Data extraction and processing
- PyTorch — Deep learning model
- NumPy, Pandas, Matplotlib — Analysis & visualization

---

## 🚀 How to Run the Project

1. Run the Abaqus simulation (`.cae / .inp`)
2. Extract spatial–temporal data using:
```

odbdataextractioncode/crashbox_data.py

```
3. Preprocess the dataset:
```

01_data_preprocessing.ipynb

```
4. Train and evaluate the digital twin:
```

02_mlp_training.ipynb

```

---

## 📌 Future Scope

- Multi-velocity crash scenarios
- Different crashbox geometries
- Temporal models (LSTM, physics-informed networks)
- Uncertainty quantification
- Experimental data integration

---

## 📜 License

This project is intended for **academic and research use**.
Please cite appropriately if used in publications.

 
 


