# Computer-Architecture
# CMPEN 431 Projects

This repository contains two projects from the CMPEN 431 course (Introduction to Computer Architecture) at Pennsylvania State University. Both projects aim to provide practical experience in exploring computer architecture design, simulation, and optimization.

---

## 1. Design Space Exploration Project

### Overview
This project utilizes the **SimpleScalar simulator** to conduct Design Space Exploration (DSE) over an 18-dimensional architecture design space. The objective is to optimize computer architecture configurations based on two metrics:
- **Performance:** Minimizing execution time.
- **Energy Efficiency:** Minimizing the Energy-Delay Product (EDP).

### Key Features
- Systematic exploration of processor pipeline and memory hierarchy parameters.
- Implementation of heuristic algorithms to intelligently navigate the design space.
- Evaluation of multiple design points through normalized execution time and energy-delay measurements.

### Tools & Technologies
- **SimpleScalar Simulator**
- Shell scripting for automation
- C/C++ for modifying and compiling simulation code

---

## 2. Branch Predictor Simulator Project

### Overview
This project implements a Python-based Branch Predictor Simulator that evaluates various branch prediction algorithms. The simulator generates synthetic branch traces and computes the prediction accuracy for multiple predictors.

### Key Features
- Simulates several branch prediction techniques: Static, One-Bit, Two-Bit, Bimodal, GShare, and Hybrid predictors.
- Uses a trace generator to create synthetic branch execution traces.
- Logs real-time statistics and detailed predictor logs for performance analysis.

### Tools & Technologies
- **Python 3.x** for the simulator and trace generation scripts
- Logging and file analysis for monitoring prediction accuracy

