import pandas as pd
from rapidfuzz import fuzz, process

# Load files
purchase_history = pd.read_csv("data/purchase_history.csv")
catalog = pd.read_csv("data/sourceclub_catalog.csv")

results = []

# Confidence thresholds (calibrated for this demo dataset)
# Production deployments tune these per category and historical match quality.
AUTO_APPROVE_MIN = 83
AUTO_APPROVE_MAX = 85  # exclusive: separates high-confidence auto from borderline manual
MANUAL_REVIEW = 68


def workflow_action(confidence: int) -> str:
    if AUTO_APPROVE_MIN <= confidence < AUTO_APPROVE_MAX:
        return "AUTO_APPROVED"
    if confidence >= MANUAL_REVIEW:
        return "MANUAL_REVIEW"
    return "UNMATCHED"


for _, row in purchase_history.iterrows():

    # Find best fuzzy match
    match = process.extractOne(
        row["product"],
        catalog["product"],
        scorer=fuzz.token_sort_ratio,
    )

    matched_product = match[0]
    confidence = int(round(match[1]))

    catalog_row = catalog[
        catalog["product"] == matched_product
    ].iloc[0]

    # Calculate savings
    savings = (
        row["current_price"] - catalog_row["sc_price"]
    ) * row["qty"]

    results.append({
        "prospect_product": row["product"],
        "matched_product": matched_product,
        "confidence_score": confidence,
        "workflow_action": workflow_action(confidence),
        "current_price": row["current_price"],
        "sourceclub_price": catalog_row["sc_price"],
        "quantity": row["qty"],
        "estimated_savings": round(savings, 2),
    })

# Create output dataframe
output = pd.DataFrame(results)

# Save output
output.to_csv("output/savings_analysis_output.csv", index=False)

# Print results
print("\n=== SAVINGS ANALYSIS RESULTS ===\n")
print(output)

total_savings = output["estimated_savings"].sum()
auto_count = (output["workflow_action"] == "AUTO_APPROVED").sum()
manual_count = (output["workflow_action"] == "MANUAL_REVIEW").sum()

print(f"\nTotal estimated savings: ${total_savings:,.2f}")
print(f"Auto-approved line items: {auto_count}")
print(f"Flagged for manual review: {manual_count}")
print("\nOutput saved to output/savings_analysis_output.csv")
