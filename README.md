Mother Nature: An Open Source Generative Chemical Artificial Intelligence ChatBot!
==================================================================================

[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![saythanks](https://img.shields.io/badge/Technical-Documentation-ff69b4.svg)](https://globalchem.gitbook.io/mother-nature/)

Welcome to Mother Nature! Mother Nature is generative Artificial Intelligence ChatBot for the Open Source Community to Interact and Build Molecules Together
while the chatbot learns from the people. 

![623d94fd33a658c54a05789a_mother nature ](https://github.com/Global-Chem/bots/assets/11812946/970dbb2a-b8b8-44d6-a58f-eb51bfcc84e5)


Mother Nature is designed using the Recurrent Neural Network Program, REINVENT, that learns from chemicals separated into different categories according to GlobalChem. 
Each Category is assigned a discord channel in which community users can interact with the chat system and find, design, and learn about chemicals for different general
things. 

Please Join Our Discord to try it out and to leave any feedback:

| [User account](#user-account) | [Server invite](#server-invite) | [Bot account](#bot-account) |
|:-:|:-:|:-:|
| ![](https://dcbadge.vercel.app/api/shield/562726584272814092) | [![](https://dcbadge.vercel.app/api/server/global-chem)](https://discord.gg/global-chem) | Mother Nature Online | 
 
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


