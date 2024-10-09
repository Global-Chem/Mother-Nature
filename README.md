Mother Nature: An Open Source Generative Chemical Artificial Intelligence ChatBot!
==================================================================================

Welcome to Mother Nature! Mother Nature is generative Artificial Intelligence ChatBot for the Open Source Community to Interact and Build Molecules Together
while the chatbot learns from the people. 

| [Admins Account](#user-account) | [Server invite](#server-invite) | Documentation |
|:-:|:-:|:-:|
| ![](https://dcbadge.vercel.app/api/shield/562726584272814092) | [![](https://dcbadge.vercel.app/api/server/global-chem)](https://discord.gg/global-chem) | [![saythanks](https://img.shields.io/badge/Technical-Documentation-ff69b4.svg)](https://globalchem.gitbook.io/mother-nature/) | 

![623d94fd33a658c54a05789a_mother nature ](https://github.com/Global-Chem/Mother-Nature/assets/11812946/e0f412ee-0e7a-47b4-81f3-8b68cc22bb41)

Introduction
============

Mother Nature is designed using the Recurrent Neural Network Program, REINVENT, that learns from chemicals separated into different categories according to GlobalChem. 
Each Category is assigned a discord channel in which community users can interact with the chat system and find, design, and learn about chemicals for different general
things. 

Please Join Our Discord to try it out and to leave any feedback.

Public Channels & Permissions
=============================

### Channel Operations

Status Updates of the Working Channels on Our Discord about what the bot can do. Some Channels might not start working depending on the training. 


| MotherNature Version | Platform/Version                | Channel                                  | Status               | Date                | Test  User |
|----------------------|---------------------------------|------------------------------------------|----------------------| --------------------| -----------| 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Cannabis                                 | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                 | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Sexual-Wellness                          | [![Maintenance](https://img.shields.io/badge/Working%3F-no-red.svg)]()                 | 08/04/2023          | Sulstice   |  
| 1.0.0                | Discord Stable 215115 (c05cd54) | Contraceptives                           | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Medicinal Chemistry                      | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Education                                | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Food                                     | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Environment                              | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Space                                    | [![Maintenance](https://img.shields.io/badge/Working%3F-no-red.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Materials                                | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Narcotics                                | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Solar Cells                              | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Global                                   | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Emerging Medicines                       | [![Maintenance](https://img.shields.io/badge/Working%3F-no-red.svg)]()                                | 08/04/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | Performance Enhancement Drugs            | [![Maintenance](https://img.shields.io/badge/Working%3F-yes-green.svg)]()                                | 08/04/2023          | Sulstice   | 


System Architecture
===================

Mother Nature has three major components that describe how the chatbot system learns from the community and operates.

Mother Nature Design Overview:

```
    User Interface (Discord) -> Execute Actions (Github Actions) ->  Generative Recurrent Neural Network (Python)
```


- **1st Component**: The first component is a Recurrent Neural Network that learns from select chemical inputs, SMILES( a 1-D representation of a molecule), of a given category in where we 
                     have a private repository performing machine learning using an Agent and Prior network that work as a generative and judge model to determine new chemicals of interest.
                     
- **2nd Component**: A Scalable Github Actions Architecture that trains neural networks and performs actions of the bot based on issue labels that then kick off requests. 

- **3rd Component**: As a user interface for interacting with the community we created a Discord Webhook that links to each individual channel where users can sign on for free and then 
                     issue requests based on their role. 

Tests
=====

### Operational Testing

| MotherNature Version | Platform/Version                | Command                                  | Expected Output      | Date                | Test  User |
|----------------------|---------------------------------|------------------------------------------|----------------------| --------------------| -----------| 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /commands                                | PASS                 | 07/26/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /is_color_legal chemical_name            | PASS                 | 07/26/2023          | Sulstice   |  
| 1.0.0                | Discord Stable 215115 (c05cd54) | /check_fda_color_status                  | PASS                 | 07/26/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /remove_smile_file                       | FAIL                 | 07/26/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /add_smile_file                          | FAIL                 | 07/26/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /retrain_mother_nature                   | FAIL                 | 07/26/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /make_github_issue_lorax                 | FAIL                 | 07/26/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /make_github_issue_arbiter               | NONE                 | 07/26/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /create_graph_node                       | PASS                 | 07/26/2023          | Sulstice   | 
| 1.0.0                | Discord Stable 215115 (c05cd54) | /fetch_training_set                      | FAIL                 | 07/26/2023          | Sulstice   | 

Announcements
=============

- Mother Nature 0.1.0 Released July 21st 2023

Genesis
=======

DataCity was designed for capsulehack.io and is the dream for three young developers who want to follow their path in centralizing all data. 

- Project Lead [Suliman sharif](http://sulstice.github.io/)
- Lead Developer [Sevien Schulhoff]()
- Quality Assurance Tester []()

* * * * *

External links
==============

- [Global-Chem](https://github.com/Global-Chem/global-chem): A 1-D Knowledge Graph of Common Chemical SMILES to their 1-D molecular representation.
- [REINVENT](https://github.com/MarcusOlivecrona/REINVENT): Molecular De Novo design using Recurrent Neural Networks and Reinforcement Learning

<<<<<<< HEAD
=======
# Feedback System Implementation
## Overview of the Feedback System
The feedback system consists of two main classes: FeedbackSystem and MotherNatureCommands. The FeedbackSystem handles the storage and retrieval of feedback in a CSV file, while the MotherNatureCommands class interacts with the Discord bot to facilitate user commands for submitting and viewing feedback.

Diagram of the System Architecture
Below is a simplified architecture diagram of the feedback system:

```
┌──────────────────────┐        ┌────────────────────────┐
│   Discord Bot       │        │   FeedbackSystem       │
│ ┌─────────────────┐ │        │ ┌───────────────────┐  │
│ │   Commands      │ │        │ │   add_feedback()  │  │
│ │   ┌──────────┐  │ │        │ │   get_feedback()  │  │
│ │   │give_feedback│<───────>│ │   ┌───────────────┐ │
│ │   └──────────┘  │ │      │ │   │   CSV File     │ │
│ │                 │ │      │ │   │ myfile.csv      │ │
│ │   ┌──────────┐  │ │      │ │   └───────────────┘ │
│ │   │view_feedback│<───────>│ │                     │
│ │   └──────────┘  │ │      │ └─────────────────────┘
│ └─────────────────┘ │
└──────────────────────┘

```
Detailed Explanation
1. FeedbackSystem Class
The FeedbackSystem class is responsible for managing feedback storage in a CSV file.

Code Overview:
```
python
Copy code
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
```
Key Functions:

**1) __init__ Method**: Initializes the feedback system and ensures that the feedback CSV file exists. If it doesn’t exist, it creates one with headers: Timestamp, User, and Feedback.

**2) ensure_feedback_file Method**: Checks if the CSV file exists. If it doesn't, it creates the file and writes the headers.

**3) add_feedback Method**: Takes a username and feedback string as parameters and appends a new row with the current timestamp, user, and feedback to the CSV file.

**4) get_feedback Method**: Reads all entries from the CSV file (skipping the header) and returns them as a list.

Diagram for FeedbackSystem Flow:

```
┌────────────────────────────────────────────┐
│          FeedbackSystem Class              │
│                                            │
│ ┌───────────────┐                          │
│ │ __init__      │                          │
│ │ (checks file) │                          │
│ └───────┬───────┘                          │
│         ┌┴┐                                  │
│ ┌───────┐ ├──────────────────────┐          │
│ │ ensure_feedback_file            │          │
│ │ (creates file if necessary)    │          │
│ └───────┘ ┌──────────────────────┘          │
│           ├──────────────────────┐          │
│ ┌─────────┴────────┐ ┌────────────┴────────┐ │
│ │ add_feedback     │ │ get_feedback        │ │
│ │ (appends feedback)│ │ (retrieves feedback)│ │
│ └───────────────────┘ └────────────────────┘ │
└────────────────────────────────────────────────┘

```
2. MotherNatureCommands Class
The MotherNatureCommands class integrates the feedback system with the Discord bot commands.

Code Overview:

```
from feedback_system import FeedbackSystem

class MotherNatureCommands:
    def __init__(self, github, repo, global_chem_repo, client, bot):
        self.feedback_system = FeedbackSystem()  # Initialize feedback system

    async def add_feedback(self, user: str, feedback: str):
        """Add user feedback to the system."""
        self.feedback_system.add_feedback(user, feedback)

    async def get_feedback(self):
        """Retrieve user feedback."""
        return self.feedback_system.get_feedback()

```
Key Functions:

**1) __init__ Method**: Initializes the MotherNatureCommands class and creates an instance of FeedbackSystem for managing feedback.

**2) add_feedback Method**: An asynchronous method that takes a username and feedback, calling the add_feedback method of the FeedbackSystem instance.

**3) get_feedback Method**: An asynchronous method that retrieves feedback using the get_feedback method of the FeedbackSystem instance.

Diagram for MotherNatureCommands Flow:

```
┌──────────────────────────┐
│   MotherNatureCommands   │
│                          │
│ ┌──────────────────────┐ │
│ │ __init__            │ │
│ │ (initialize system) │ │
│ └─────────┬──────────┘ │
│           ├────────────┘
│ ┌─────────┴────────────┐
│ │ add_feedback         │
│ │ (calls FeedbackSystem│
│ │ .add_feedback)      │
│ └─────────┬───────────┘
│           ├────────────┘
│ ┌─────────┴────────────┐
│ │ get_feedback         │
│ │ (calls FeedbackSystem│
│ │ .get_feedback)      │
│ └──────────────────────┘
└──────────────────────────┘
```

>>>>>>> parent of c76c7a1 (Update README.md)

