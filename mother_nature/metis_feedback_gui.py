from feedback import collect_feedback, process_feedback

# Collect feedback using the Metis GUI
def run_metis_feedback_gui(molecules):
    # Open GUI to collect feedback
    # Save feedback to CSV or return it directly
    feedback = collect_feedback(molecules)

    # Process the feedback and return it
    return process_feedback(feedback)
