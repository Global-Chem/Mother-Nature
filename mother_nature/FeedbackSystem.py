import csv
import os
from datetime import datetime

class FeedbackSystem:
    def __init__(self, feedback_file='myfile.csv'):
        self.feedback_file = feedback_file
        self.ensure_feedback_file()

    def ensure_feedback_file(self):
        """Create the feedback CSV file if it doesn't exist."""
        if not os.path.exists(self.feedback_file):
            with open(self.feedback_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Timestamp', 'User', 'Feedback'])  # Header

    def add_feedback(self, user: str, feedback: str):
        """Add feedback to the CSV file."""
        with open(self.feedback_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().isoformat(), user, feedback])

    def get_feedback(self):
        """Retrieve all feedback from the CSV file."""
        feedback_list = []
        with open(self.feedback_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            feedback_list = list(reader)
        return feedback_list

