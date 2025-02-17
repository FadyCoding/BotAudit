import yaml
import csv


def generate_audit_yaml(output_file="audit_template.yaml"):
    audit_data = {
        "audit_template": {
            "project_name": "Order to Cash",
            "company": "Company Name x From 6 Agency",
            "sections": {
                "objectives": {
                    "review_business_architecture": True,
                    "focus_on_key_topics": [
                        "key topic 1",
                        "key topic 2",
                        "key topic 3"
                    ],
                    "target_architecture": True
                },
                "as_is_situation": {
                    "description": "Current state of the Order to Cash process",
                    "pain_points": [
                        "Single opportunity process",
                        "Manual Customer, Order/subscriptions Inputs from SFDC to NETSUITE",
                        "Product catalog not aligned between systems",
                        "High complexity to handle T&Cs per product"
                    ],
                    "high_level_process": {
                        "steps": [
                            "Account Opportunity",
                            "Quote Order/Subscription Invoice",
                            "Customer Advanced Approvals",
                            "Pricing Grid"
                        ]
                    }
                },
                "target_situation": {
                    "description": "Future state with SFDC focus",
                    "gains": [
                        "Add specific rules between processes",
                        "Monitor and improve control in the sales lifecycle",
                        "Split revenue tracking between pipeline and committed revenue",
                        "Expand data model to optimize team focus"
                    ],
                    "new_process": {
                        "steps": [
                            "New Sales Opportunity",
                            "Upsell/Cross-sell Opportunity",
                            "Renewal Opportunity",
                            "Order Contract",
                            "Pipeline Revenue",
                            "Committed Revenue"
                        ]
                    }
                }
            }
        }
    }

    with open(output_file, "w") as file:
        yaml.dump(audit_data, file, default_flow_style=False, allow_unicode=True)

    print(f"YAML file '{output_file}' generated successfully.")

#my first commit#
def generate_audit_csv(output_file="audit_template.csv"):
    audit_data = [
        ["Section", "Category", "Details"],
        ["Objectives", "Review Business Architecture", "True"],
        ["Objectives", "Focus on Key Topics", ", ".join(["key topic 1", "key topic 2", "key topic 3"])],
        ["Objectives", "Target Architecture", "True"],
        ["As-Is Situation", "Description", "Current state of the Order to Cash process"],
        ["As-Is Situation", "Pain Points", ", ".join([
            "Single opportunity process",
            "Manual Customer, Order/subscriptions Inputs from SFDC to NETSUITE",
            "Product catalog not aligned between systems",
            "High complexity to handle T&Cs per product"
        ])],
        ["Target Situation", "Description", "Future state with SFDC focus"]
    ]

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(audit_data)

    print(f"CSV file '{output_file}' generated successfully.")


# Run the functions
generate_audit_yaml()
generate_audit_csv()