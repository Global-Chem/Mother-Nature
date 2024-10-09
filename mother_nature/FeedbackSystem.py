import pandas as pd

def collect_feedback(molecules):
    # Example function to collect feedback
    # This could involve using Metis or reading from a CSV
    feedback_df = pd.read_csv("feedback.csv")  # Assuming feedback.csv is the file with feedback from Metis

    # Here you would match feedback to molecules and process it
    return feedback_df

def process_feedback(feedback):
    # Example function to process feedback and adjust REINVENT scoring function
    # You can update the scoring function for REINVENT based on feedback
    updated_scoring_function = adjust_scoring_function(feedback)
    return updated_scoring_function

def adjust_scoring_function(feedback):
    # Logic to adjust REINVENT's scoring/reward function based on feedback
    # For example, reduce the weight for toxicity, or increase the reward for solubility
    return {
        "scoring_function": "adjusted",
        "parameters": {
            "toxicity_weight": 0.5,
            "solubility_weight": 1.0
        }
    }

import json

def update_reinvent_config(feedback):
    # Load existing config
    with open("reinvent_config.json", "r") as f:
        config = json.load(f)

    # Adjust scoring function or other parameters based on feedback
    config['parameters']['scoring_function']['weight'] = feedback['toxicity_weight']

    # Save updated config
    with open("reinvent_config.json", "w") as f:
        json.dump(config, f)



