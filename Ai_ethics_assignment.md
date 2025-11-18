Part 1: Theoretical Understanding (30%)

1. Short Answer Questions

Q1: Define algorithmic bias and provide two examples of how it manifests in AI systems.

Algorithmic bias is the systematic and repeatable error in an AI system that creates unfair outcomes, such as favoring one group of people over others. It is not necessarily malicious, but often results from flaws in the data, the assumptions made during model development, or the way the model is deployed and used.

Manifestation Examples:

Gender Bias in Natural Language Processing (NLP): Large language models, trained on historical text that reflects societal stereotypes, may associate words like "engineer" or "CEO" with male pronouns and words like "nurse" or "assistant" with female pronouns. This manifests in auto-completion features or translation services reinforcing these stereotypes, which can negatively affect career guidance tools or professional communications.

Racial Bias in Credit Scoring: If a system is trained on historical loan data where certain racial groups were unfairly denied loans, the AI will learn to associate features correlated with that group (e.g., neighborhood demographics, which are proxies for race) with higher risk, even if the individuals are equally creditworthy. This perpetuates historical discrimination, making it harder for these groups to access capital.

Q2: Explain the difference between transparency and explainability in AI. Why are both important?

Feature

Transparency (The What)

Explainability (The Why)

Definition

Knowing the structure of the AI system, including the data used, the algorithms employed, and the rules governing its output.

Being able to articulate why a specific decision or prediction was made by the model for a given input.

Focus

The overall system, data, and code.

Individual decision paths and feature contribution.

Example

Knowing that a bank's loan application uses an XGBoost classifier trained on the last 10 years of applicant data.

Knowing that this specific loan application was rejected because the applicant's debt-to-income ratio exceeded 40% (the threshold learned by the model).

Importance:

Transparency is crucial for governance and accountability. It allows auditors and regulators to ensure the system complies with laws (like GDPR) and ethical standards, and to verify the input data quality.

Explainability is essential for trust and rectification. It allows users to understand and challenge decisions (the "right to explanation"), and it enables developers to debug the model, identify bias, and improve performance. Both are necessary to achieve responsible AI.

Q3: How does GDPR (General Data Protection Regulation) impact AI development in the EU?

The General Data Protection Regulation (GDPR) imposes strict rules on how personal data must be collected, processed, and stored, fundamentally impacting AI development in the EU:

Right to Explanation (Article 22): GDPR gives individuals the right not to be subject solely to a decision based on automated processing, especially if it significantly affects them. This effectively mandates a degree of explainability for AI systems making high-stakes decisions (e.g., loan applications or hiring).

Data Minimization and Purpose Limitation: AI developers must ensure they only collect the minimum amount of personal data strictly necessary for a specific, explicit purpose. This restricts the use of large, general datasets often favored in AI research, pushing developers toward techniques like Federated Learning or Differential Privacy.

Data Subject Consent: Processing personal data requires explicit, informed consent. This means AI systems cannot simply scrape public data or reuse data for new, unanticipated purposes without obtaining new consent, limiting model flexibility.

2. Ethical Principles Matching

Match the following principles to their definitions:

Principle

Definition

B) Non-maleficence

Ensuring AI does not harm individuals or society.

C) Autonomy

Respecting users’ right to control their data and decisions.

D) Sustainability

Designing AI to be environmentally friendly.

A) Justice

Fair distribution of AI benefits and risks.

Part 2: Case Study Analysis (40%)

Case 1: Biased Hiring Tool (Amazon)

Tasks:

1. Identify the source of bias:

The primary source of bias was the training data (historical résumés). Because Amazon's tech workforce historically favored men, the training data contained implicit patterns reflecting this historical gender disparity. The AI learned to associate words common on female candidates' résumés (e.g., attendance at all-women's colleges, or the word "women's") with poor performance scores, and keywords common on male candidates' résumés with success. The model was not intentionally sexist; it merely amplified existing historical inequalities present in the data it learned from.

2. Propose three fixes to make the tool fairer:

Data Pre-processing (Masking): Remove sensitive attributes and highly correlated proxies (e.g., specific college names, gender-coded language) from the input data before training.

In-Processing (Adversarial Debiasing): Train the model with an adversarial network that tries to predict the sensitive attribute (gender) from the model's intermediate representations. The main model is simultaneously penalized for giving out signals that reveal the sensitive attribute, forcing it to focus on truly merit-based features.

Post-Processing (Reject Option Classification): Adjust the model's final scores or decision thresholds after inference, specifically for candidates near the decision boundary, to ensure equal success rates between gender groups.

3. Suggest metrics to evaluate fairness post-correction:

Equal Opportunity Difference (EOD): Measures the difference in True Positive Rates (TPR) between the privileged and unprivileged groups. For a hiring tool, this ensures that the algorithm is equally effective at identifying successful candidates regardless of gender. An EOD close to zero indicates fairness.

Disparate Impact Ratio (DIR): Calculates the ratio of selection rates (hiring rate) for the unprivileged group compared to the privileged group. The DIR should ideally be between 0.8 and 1.25 (the "four-fifths rule") to indicate that the tool is not systematically screening out one group.

Case 2: Facial Recognition in Policing

Tasks:

1. Discuss ethical risks:

Violation of Justice/Wrongful Arrests: Studies (e.g., by NIST) have repeatedly shown that facial recognition systems exhibit significantly higher error rates for women and darker-skinned individuals (False Positives). This disparity means minority groups are statistically more likely to be falsely identified as a suspect, leading to wrongful stops, questioning, and arrest, violating the principle of Justice.

Chilling Effect on Autonomy and Privacy: Pervasive, always-on facial recognition tracking creates a "chilling effect" where citizens self-censor their activities, knowing they are constantly being monitored. This undermines the democratic rights of autonomy and freedom of association.

2. Recommend policies for responsible deployment:

Mandatory Human Review: The output of a facial recognition system should never be the sole basis for an arrest or search warrant. The AI's match score must serve only as a lead, requiring independent confirmation by trained human analysts before any action is taken.

Audit and Accuracy Reporting: Agencies must be required to conduct and publish independent annual audits of the system's accuracy, specifically broken down by demographic groups (race, gender). If the system fails to meet a minimum equity threshold (e.g., if the False Positive Rate disparity exceeds 10% across groups), its use should be suspended until it is recalibrated.