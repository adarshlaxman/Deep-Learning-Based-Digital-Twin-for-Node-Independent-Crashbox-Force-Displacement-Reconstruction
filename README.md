# Deep Learning Digital Twin for Crashbox Force–Displacement Reconstruction and Optimal Sensor Placement

## Author

**Adarsh L**

---

## Abstract

Finite Element Analysis (FEA) of crash events is computationally intensive and limits rapid design iteration and real-time monitoring. This work proposes a **deep learning-based digital twin** that learns the mapping between local nodal kinematics and global reaction force in a thin-walled crashbox.

A Multi-Layer Perceptron (MLP) surrogate model is trained on Abaqus Explicit simulation data and evaluated using a **strict spatial holdout strategy**. The model demonstrates strong predictive performance and generalisation.

Further, a **gradient-based sensitivity analysis** is introduced to identify optimal sensor locations. Results show that a **single optimally placed sensor can outperform full-field input**, enabling ultra-sparse and cost-efficient monitoring systems.

---

## 1. Introduction

Crashworthiness analysis using FEA is a standard approach in automotive engineering; however, it suffers from high computational cost and limited scalability.

Digital twins provide a data-driven alternative by approximating physical systems using machine learning models trained on simulation data. This project focuses on:

* Learning force–displacement relationships from local deformation
* Reducing dependence on full-field simulation data
* Enabling intelligent sensor placement

---

## 2. Problem Statement

Traditional crash simulation workflows:

* Require significant computational time (hours to days)
* Depend on full-field spatial data
* Are unsuitable for real-time applications

### Objectives

* Develop a **surrogate model** for rapid prediction of global crash force
* Ensure **robust spatial generalisation**
* Minimise sensing requirements via **optimal sensor placement**

---

## 3. Methodology

### 3.1 Data Generation

Simulation data is generated using **Abaqus Explicit** for a thin-walled crashbox undergoing progressive deformation.

Each data sample consists of:

* Time step
* Node coordinates: (X, Y, Z)
* Local displacement: (U3)
* Target output: Global reaction force (RF3)

---

### 3.2 Model Architecture

A fully connected neural network (MLP) is employed:

```
Input Layer (5 features: t, X, Y, Z, U3)
→ Dense (128, ReLU)
→ Dense (64, ReLU)
→ Dense (32, ReLU)
→ Output Layer (1: RF3)
```

---

### 3.3 Training Strategy

* Loss Function: Mean Squared Error (MSE)
* Optimisation: Adam
* Data split: **Spatial holdout (node-wise separation)**

This ensures the model is evaluated on **unseen spatial regions**, preventing data leakage and validating true generalisation.

---

### 3.4 Sensitivity-Based Sensor Placement

A gradient-based importance metric is computed:

|∂RF3 / ∂U3|

This quantifies the influence of local displacement on global force prediction. Nodes are ranked based on this metric to identify **optimal sensor locations**.

---

## 4. Results

### 4.1 Predictive Performance

* **R² Score:** 0.949
* **RMSE:** 0.225
* **MAE:** 0.055

The model accurately reconstructs nonlinear force–displacement behavior across the deformation history.

---

### 4.2 Generalisation

The spatial holdout evaluation demonstrates that the model:

* Does not rely on memorisation
* Learns physically meaningful relationships
* Generalises to unseen node locations

---

### 4.3 Sensor Reduction and Optimal Placement

* Random sensor selection (1–5 sensors): R² ≈ 0.75–0.80
* Full-field input: R² ≈ 0.95

### Key Finding

* **Single gradient-optimal sensor → R² = 0.997**

This result indicates that:

* A strategically placed sensor can outperform dense measurements
* Structural monitoring can be achieved with minimal instrumentation

---

## 5. Key Contributions

* Development of a **deep learning-based digital twin** for crash force prediction
* Implementation of **spatially robust validation methodology**
* Introduction of **gradient-based sensor importance ranking**
* Demonstration of **ultra-sparse sensing capability**
* Bridging machine learning with **physics-informed engineering analysis**

---

## 6. Applications

* Automotive crash safety analysis
* Structural health monitoring systems
* Real-time digital twin deployment
* Cost-optimised sensor network design

---

## 7. Future Work

* Integration of **Graph Neural Networks (GNNs)** for mesh-aware learning
* Incorporation of **attention mechanisms** for adaptive feature weighting
* Extension to full vehicle crash simulations
* Deployment in real-time monitoring environments

---

## 8. Conclusion

This work demonstrates that deep learning can effectively replace computationally expensive crash simulations while preserving high predictive accuracy.

The integration of gradient-based sensitivity analysis enables intelligent sensor placement, revealing that **minimal sensing can achieve superior performance**.

This establishes a scalable framework for **data-driven digital twins and smart sensing systems** in structural engineering.

---

## Repository Structure

```
├── 02_mlp_training.ipynb
├── data/
├── models/
├── results/
└── README.md
```

---

## License

This project is intended for academic and research purposes.

---
