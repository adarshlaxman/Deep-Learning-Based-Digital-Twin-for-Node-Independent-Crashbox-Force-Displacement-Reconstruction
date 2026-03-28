# 🚀 Deep Learning Digital Twin for Crashbox Force Prediction & Optimal Sensor Placement

## 👨‍💻 Author

**Adarsh L**
 

---

## 📌 Project Overview

This project presents a **Deep Learning-based Digital Twin** for predicting crash force in a thin-walled crashbox structure using simulation data.

Traditional crash simulations using Finite Element Analysis (FEA) are computationally expensive and time-consuming. This project replaces those simulations with a **fast and accurate neural network model**.

Additionally, it introduces a novel approach to **optimal sensor placement**, reducing hardware requirements while maintaining high prediction accuracy.

---

## 🎯 Problem Statement

Crash simulations:

* ⏳ Take hours to compute
* 💻 Require high computational resources
* ❌ Not suitable for real-time applications

### ✅ Objective:

* Develop a **surrogate model** to predict crash force instantly
* Identify **minimum number of sensors** needed for accurate monitoring

---

## ⚙️ Methodology

### 📊 Data Source

* Simulation data generated using Abaqus Explicit
* Dataset includes:

  * Time step
  * Node coordinates (X, Y, Z)
  * Displacement (U3)
  * Output: Global reaction force (RF3)

---

### 🧠 Model Architecture

A Multi-Layer Perceptron (MLP):

```
Input (5 features)
   ↓
Dense (128) → ReLU
   ↓
Dense (64) → ReLU
   ↓
Dense (32) → ReLU
   ↓
Output (1: RF3)
```

---

### 🧪 Validation Strategy

* **Spatial Train-Test Split**

  * Model tested on nodes never seen during training
  * Ensures real generalisation (not memorisation)

---

### 📍 Sensor Placement Strategy

* Used gradient-based sensitivity:

  |∂RF3 / ∂U3|

* Ranked nodes based on influence on force prediction

* Identified optimal sensor locations

---

## 📊 Results

### ✅ Model Performance

* **R² Score:** 0.949
* **RMSE:** 0.225
* **Relative Error:** ~4.34%

👉 Model accurately reproduces crash force behavior

---

### 💥 Key Finding (Major Contribution)

* **Single optimal sensor → R² = 0.997**
* Outperforms using all nodes together

👉 This proves:

* Minimal sensors can achieve maximum accuracy
* Huge reduction in cost and complexity

---

## 🧪 Sensor Reduction Study

| Number of Sensors | Accuracy (R²) |
| ----------------- | ------------- |
| 1                 | 0.997 🔥      |
| 1–5               | ~0.75–0.80    |
| All nodes         | ~0.95         |

---

## 🌟 Key Contributions

* ✅ Deep learning surrogate for crash simulation
* ✅ True spatial generalisation
* ✅ Gradient-based sensor importance ranking
* ✅ Ultra-sparse sensing (1 sensor outperforming full data)
* ✅ Real-world applicable digital twin

---

## 🚗 Applications

* Automotive crash analysis
* Structural health monitoring
* Real-time digital twin systems
* Cost-efficient sensor deployment

---

## 📂 Project Structure

```
├── 02_mlp_training.ipynb   # Main training notebook
├── data/                   # Simulation dataset
├── results/                # Graphs & outputs
├── models/                 # Saved model
└── README.md               # Project documentation
```

---

## 🚀 Future Work

* Graph Neural Networks (mesh-aware learning)
* Attention mechanisms for spatial importance
* Full vehicle crash modeling
* Real-time deployment systems

---

## 🧠 Summary

This project demonstrates that:

> Deep learning can replace expensive crash simulations and identify optimal sensor locations, enabling accurate and efficient monitoring with minimal resources.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!

---
