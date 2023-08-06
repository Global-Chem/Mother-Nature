---
title: 'Mother Nature: An Open Source Generative Chemical Artificial Intelligence ChatBot!'
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
  - name: Suliman Sharif
    orcid: 0000-0002-1342-9258
    affiliation: 1
affiliations:
 - name: None
   index: 1
date: 08/06/2023
bibliography: paper.bib
---

# Introduction

Generative Artifical Intelligence (AI) Programs for chemistry are emerging as common tools for predicting viable new structures for based on select chemical lists with machine learning. Generated chemicals are presented to an audience of scientists across different disciplines for selection of compounds based on intuition and rules as to which one bests solve a targeted problem. However, no platform exists where the general public can access the chemical data and vote to select chemical compounds based on a collective knowledge. With the demand of transparency in the chemical design of drugs, food, cosmetics, materials, etc. a need has grown for a platform in which the general public can communicate with scientists and have the right to vote and choose chemicals for the greater good. Herein, we present a study in which we create a chatbot system coined "Mother Nature" where she generates chemicals based on different chemical lists. Users can interact and vote to remove or add chemicals based on they see fit.

# Methodology and Implementation

```MotherNature``` operates across two different platforms: `Discord` and `Github`. Users can interact with `MotherNature` via a chat system on discord with pre-fixed commands and parameters. Commands are outlined in the documentation. In `Figure 1`, a user prompts `MotherNature` and executes a command, it files an issue on a `workers` repository with a specified label that contains the parameters and the chemical list of interest. The repository then runs an associated Github Actions Workflow tied to the to generate chemical compounds using a machine learning program. The chemicals are then projected as an image into the dedicated discord channel where users can observe the results and suggest edits. All generated chemical data is stored in a separate repository called `Forbidden Fruit`.

![diagram](https://github.com/Global-Chem/Mother-Nature/assets/11812946/890fc035-e01c-485f-925d-dd2d7a846464)

```MotherNature``` uses the generative model, REINVENT, that establishes a policy while training based off select chemical lists. Based on the chemical list, the "Prior", builds a network that learns the SMILES language. A positive side for example if the letter "F", Fluoring, does not exist in the original data set then no fluorine compounds will be produced. REINVENT uses an Agent that learns the policy from the Prior and generates compounds based off the Tanimoto Similarity Score of how likely is this compound similar to another in the set. This makes it selective to search throhgh latent chemical space with pre-defined chemical lists. 

Training can be re-trained on a weekly basis where the community can elect compounds to search through chemical space together. 

# Conclusion

Using  ```MotherNature```, individuals, academics, industry researchers, and governments can quickly construct compound collections and generated enhanced chemical data sets based off community elected compounds. This allows for effective search through latent chemical space with a collective knowledge of the people. 

```MotherNature``` with its first version release, 1.0.0, provides an architecture for designing an open source generative AI chatbot with little to know cost. For future
releases ```MotherNature``` will be expanding into automating cheminformatic workflows for rapid information feedback and general public user growth such as permeation of the skin or legality of coloring used in Food or Cosmetic Products. As more user data is being generated with increased interactions with chatbot, we hope to implement a natural processing langauge component in hopes to understand common chemical language and integrate it with voice. With more contributions ```MotherNature``` will be an exciting Chat Tool for chemical library creation 
for the general public to enjoy. 

# Acknowledgements

We acknowledge contributions from Josh Farrell as a consultation.

# References
