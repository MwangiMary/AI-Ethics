COMPAS Recidivism Dataset Audit Report

Summary of Findings and Remediation

This audit analyzed the simulated COMPAS recidivism risk prediction tool, focusing on racial bias between the self-identified Black (unprivileged) and White (privileged) defendant groups. The primary fairness metric examined was the False Positive Rate (FPR), which represents the percentage of non-recidivist defendants who were incorrectly flagged by the system as "High Risk." This error is crucial, as it leads to harsher sentencing recommendations for individuals who would not commit another crime.

Key Finding

The audit revealed a significant disparity, demonstrating a violation of Equalized Odds. The FPR for the Black group was observed to be 0.552, while the FPR for the White group was 0.490. This results in a difference of +0.062 percentage points. This means that non-recidivist Black defendants were 6.2% more likely than non-recidivist White defendants to be falsely assigned a "High Risk" score. This disparity violates the principle of Justice, as the system imposes greater punitive harm (higher risk score) on the unprivileged group.

Remediation Steps

To mitigate this observed bias, the following steps are recommended:

In-Processing Mitigation (Adversarial Debiasing): Implement a constrained optimization technique during model training that penalizes the model for any residual correlation between the prediction output and the sensitive attribute (race), effectively forcing the model to learn truly equitable risk factors.

Post-Processing Mitigation (Threshold Adjustment): Apply the Reject Option Classification (ROC) method. This adjusts the decision threshold (the point at which a score is deemed "High Risk") for the unprivileged group to equalize the FPR across both groups, ensuring a more fair distribution of predictive errors.

Data Enhancement: Investigate and potentially incorporate non-biased features (e.g., socioeconomic support access, specific rehabilitation program participation) to reduce the model's reliance on historical data proxies for race.