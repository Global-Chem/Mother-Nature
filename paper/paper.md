---
title: 'Mother Nature: An Open Source Generative Chemical Artificial Intelligence ChatBot'
tags:
  - Python
  - Cheminformatics
  - Large Language Models
  - Bot Architecture
  - Recurrent Neural Networks
authors:
  - name: Sevie Schulhoff
    orcid: 0000-0002-1342-9258
    affiliation: 1
  - name: Bodun Damilola
    affiliation: 1
  - name: Jonas Xavier Roper
    affiliation: 1
  - name: Suliman Sharif
    orcid: 0000-0002-1342-9258
    affiliation: 1
  - name: Lauren Angulo
    orcid: 0000-0002-1342-9258
    affiliation: 1
  - name: Josh Farrell*
    orcid: 0000-0002-1342-9258
    affiliation: 1
affiliations:
 - name: Standard Seed Corporation
   index: 1
date: 08/06/2023
bibliography: paper.bib
---

# Introduction

For chemistry, Generative Artifical Intelligence (AI) Programs are emerging as common tools for predicting viable new structures based on select chemical lists [@Walters:2020-02]. Generated chemicals are presented to an audience of scientists across different disciplines for selection of compounds based on intuition and rules as to which one bests solve a targeted problem [@Sundin:2022-12]. However, no platform exists where the general public can access the chemical data and vote to select chemical compounds based on a collective knowledge. With the demand of transparency in the chemical design of drugs, food, cosmetics, materials, etc. A need has grown for a platform in which the general public can communicate with scientists and have the right to vote and choose chemicals for general purposes [@Schymanski:2021-07]. Herein, we present a study in which we create a chatbot system coined "Mother Nature". She is capable of generating chemicals based on different chemical lists and users can interact and vote to remove or add chemicals to these lists as they see fit.

# Methodology and Implementation

```Mother Nature``` operates across two different platforms: `Discord` and `Github`. Users can interact with `Mother Nature` via a chat system on discord with pre-fixed commands and parameters. Commands are outlined in the documentation. In `Figure 1`, a user prompts `MotherNature` and executes a command, it files an issue on a `workers` repository with a specified label that contains the parameters and the chemical list of interest. The repository then runs an associated Github Actions Workflow tied to the label to generate chemical compounds using a machine learning program. The chemicals are then projected as an image into the dedicated discord channel where users can observe the results and suggest edits. All generated chemical data is stored in a separate database repository called `Forbidden Fruit` where each output is stored as an Issue with a categorical label and the body is the SMILES data. This allows for easily minability. 

```Mother Nature``` is trained on a chain of Recurrent Neural Networks (RNNs) which have been commonly used in methods for speech recognition, text summarization, and generative text [@Kanagachidambaresan:2017-04]. In chemistry, a language called Simplified Molecular Input Line Entry Specification (SMILES) was created for chemists to write molecules intuitively into the computer in their 1-D representation [@Weininger:1989-05] [@Weininger:1988-02]. SMILES strings were designed with a set of grammar rules and became a popular 1-D language amongst cheminformaticians as a sufficient way to write and retain 2D chemical connectivity information. SMILES serves as an effective medium in transporting chemical information while retaining at its core, bond order information. Segler et al. first applied an RNN to the SMILES alphabet to generate new molecules of interest based on the chemical list input [@Segler:2018-01]. This was modernized with REINVENT, a specialized RNN with a REINFORCE algorithm that takes into account the state of the input and probability of the output [@Olivecrona:2017-04]. The main network components in REINVENT are a Prior and an Agent. The Prior is the RL-Framework that establishes a policy based on the chemical list provided and the hyperparameters remain unchanged. The Agent adopts that policy and then generates new molecules of interest validating SMILES based on Tanimoto Similarity score of its similarity to the chemicals provided.

![Figure 1: Software architectural design of the `Mother Nature` chatbot system](https://github.com/Global-Chem/Mother-Nature/assets/11812946/0b52fb0c-69d2-4641-bac2-8e75ba374aad)

In `Figure 1`, users can pick which classes or chemicals to include in the training set. A Prior network then establishes a policy for that specific chemical list. Each Agent that then generates new compounds and updates the policy on the Agent per iteration when discovering new chemicals. Users can then decide if a molecule is appropiate or not for testing. Visual feedback on the molecular design fragments generated can be altered based on whether or not the community decides they want to include them in the retraining the policy for that category [@Sundin:2022-12]. This enables guided generative design through latent chemical space for compounds we select as valuable for further testing.

# Conclusion

In our study, we used common chemical lists from Global-Chem [@Sharif-Suliman:2023-01] to train multi-agents and communicate with users through a chat interface. Each chat user interface is its own agent trained on identical policy parameters. Using  ```Mother Nature``` (as an API or a chat interface), individuals, academics, industry researchers, and governments can quickly construct compound collections and generated enhanced chemical data sets based on community elected compounds. This allows for effective search through latent chemical space with a collective knowledge of the people [@Schymanski:2021-07]. 

```Mother Nature``` with its first version release, 1.0.0, provides an architecture for designing an open source generative AI chatbot with little to no cost. For future
releases ```Mother Nature``` will be expanding into automating cheminformatic workflows for rapid information feedback and general public user growth such as permeation of the skin or legality of coloring used in Food or Cosmetic Products. As more user data is being generated with increased interactions with the chat bot, we hope to implement a natural processing langauge component in hopes to understand common chemical language and integrate it with voice. With more contributions ```Mother Nature``` will be an exciting chat tool for chemical library creation for the general public to enjoy. 

# Acknowledgements

We acknowledge financial contributions from Potcoin and the Standard Seed Corporation for the development of this project.  

# References
