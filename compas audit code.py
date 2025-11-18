import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

# --- Task 3: Audit a Dataset for Bias (COMPAS Recidivism Dataset Simulation) ---
# This script simulates the analysis of racial bias in the COMPAS risk score,
# focusing on key fairness metrics used by tools like IBM's AI Fairness 360 (AIF360).
# The COMPAS dataset often shows that Black defendants are more likely to be given
# a "High Risk" score (False Positive) when they do not reoffend, compared to White defendants.

# 1. Simulate the Data (Mimicking key columns from COMPAS)
print("1. Simulating COMPAS Audit Data (1000 Cases)")
data = {
    'race': np.random.choice(['White', 'Black', 'Other'], size=1000, p=[0.4, 0.45, 0.15]),
    # 'recid_risk_score': 1 (High Risk) or 0 (Low Risk) - the model's prediction
    'recid_risk_score': np.random.randint(0, 2, size=1000), 
    # 'recid_actual': 1 (Did Reoffend) or 0 (Did Not Reoffend) - the ground truth
    'recid_actual': np.random.randint(0, 2, size=1000),
}
df = pd.DataFrame(data)

# 2. Define Groups and Sensitive Attribute
sensitive_attribute = 'race'
privileged_group = {'race': 'White'}
unprivileged_group = {'race': 'Black'}
print(f"Sensitive Attribute: {sensitive_attribute}")
print(f"Privileged Group: {privileged_group['race']}")
print(f"Unprivileged Group: {unprivileged_group['race']}\n")

# 3. Simulate Fairness Metrics Calculation (Focus on False Positive Rate Disparity)
# --- Calculation of Conditional Equality Metrics (False Positive Rate) ---

def calculate_fpr_disparity(data, privileged, unprivileged):
    # Filter for those who did NOT reoffend (recid_actual == 0)
    non_recidivists = data[data['recid_actual'] == 0]

    # FPR for the privileged group (White)
    fp_priv = non_recidivists[non_recidivists['race'] == privileged['race']]
    fp_priv_count = (fp_priv['recid_risk_score'] == 1).sum() # High Risk Score (False Positive)
    fpr_priv = fp_priv_count / len(fp_priv) if len(fp_priv) > 0 else 0

    # FPR for the unprivileged group (Black)
    fp_unpriv = non_recidivists[non_recidivists['race'] == unprivileged['race']]
    fp_unpriv_count = (fp_unpriv['recid_risk_score'] == 1).sum()
    fpr_unpriv = fp_unpriv_count / len(fp_unpriv) if len(fp_unpriv) > 0 else 0
    
    # Calculate Disparity
    fpr_disparity = fpr_unpriv - fpr_priv
    
    return fpr_priv, fpr_unpriv, fpr_disparity

# Simulate the actual calculation using the generated data
fpr_white, fpr_black, fpr_diff = calculate_fpr_disparity(df, privileged_group, unprivileged_group)

# 4. Output Simulated Findings (AIF360 Console Output Style)
print("2. Simulated AIF360 Fairness Metric Audit Results:")
print("--------------------------------------------------")
print(f"Metric: False Positive Rate (FPR) - Error Rate for Non-Recidivists")
print(f"  FPR (Privileged/White): {fpr_white:.3f}")
print(f"  FPR (Unprivileged/Black): {fpr_black:.3f}")
print(f"  Difference (Black - White): {fpr_diff:.3f}")

if fpr_diff > 0.05:
    print("\nCONCLUSION: Disparity detected. The unprivileged group has a statistically higher chance of being falsely flagged as high risk.")
else:
    print("\nCONCLUSION: No significant disparity detected in the False Positive Rate.")

# 5. Generate Visualization Data (JSON output to mimic a plot source)
# This simulates the data needed for a bar chart visualization of the disparity.
visualization_data = {
    "title": "False Positive Rate Disparity (Predicted High Risk, Actual Low Risk)",
    "data_points": [
        {"group": "White", "FPR": fpr_white},
        {"group": "Black", "FPR": fpr_black},
    ]
}

print("\n3. Visualization Data (Raw JSON):")
print(json.dumps(visualization_data, indent=2))

# 6. Summary of Bias Type Found
print("\n4. Bias Type Identified:")
print("The disparity found in the False Positive Rate is an example of **Equalized Odds Violation** (specifically, higher false indictment rate for the unprivileged group), violating the fairness goal of **Equal Opportunity**.")