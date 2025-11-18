Ethical AI Principles and Auditing Assignment

This repository contains a comprehensive academic assignment focusing on the theoretical, ethical, and practical aspects of Responsible AI, including algorithmic bias, fairness auditing, and governance principles.

Assignment Structure

The assignment is divided into four main parts, with corresponding files in this repository:

Part

Description

File Path

Part 1 & 2

Theoretical Understanding & Case Study Analysis (Definitions, Principles, Case Studies)

ai_ethics_assignment_theory.md

Part 3 (Code)

Practical Audit: Python simulation of COMPAS dataset bias using AI Fairness 360 concepts.

compas_audit_code.py

Part 3 (Report)

Report summarizing the COMPAS audit findings and remediation steps.

compas_audit_report.md

Part 4

Ethical Reflection on a personal AI project's principles and governance.

ethical_reflection.md

Part 3: Practical Audit Details (Simulated COMPAS Analysis)

The Python script (compas_audit_code.py) simulates the process of performing a fairness audit, focusing on the historical bias found in the COMPAS recidivism dataset.

Analysis Focus

The audit targets Disparate False Positive Rates (FPR)—a measure of Equalized Odds.

Sensitive Attribute: Race (Black vs. White)

Goal: Ensure that the rate at which non-recidivists are incorrectly flagged as "High Risk" is equal across both groups.

Key Simulation Steps:

Data Generation: Simulates a dataset with race, recid_risk_score (prediction), and recid_actual (ground truth).

Metric Calculation: Computes the False Positive Rate for both the privileged (White) and unprivileged (Black) groups.

Disparity Reporting: Calculates the difference in FPR, which indicates the level of bias present in the simulated model.

How to View the Code Output

The Python script is designed to print the simulated audit results, including the FPR for each group and the resulting disparity.

# To run this script and see the simulated findings:
python compas_audit_code.py


Getting Started

To view the assignment's content, you can simply browse the markdown files directly on GitHub. The code file provides the practical context for the accompanying report.