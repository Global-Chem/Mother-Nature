# -*- coding: utf-8 -*-
#
# Testing content definitions.
#
# ------------------------------------------------

# imports
# -------

from mother_nature import MotherNature

def test_initializa_class():

    '''

    Test the intialize of the class, with parameters if it extends to that

    '''

    mother_nature = MotherNature()

def test_get_channel():

    '''

    Test the Retrieval of the Channel From Discord

    '''

    mother_nature = MotherNature()
    mother_nature = 

def test_get_channel_history():

    '''

    Test The Retrieval of the Channel History

    '''

    gc = GlobalChem()
    nodes_list = gc.check_available_nodes()

    assert len(nodes_list) > 0
    assert 'emerging_perfluoroalkyls' in nodes_list

def test_get_commands():

    '''

    Test the Commands Retrieval To What is Available to Users from Mother Nature

    '''

    gc = GlobalChem()
    gc.build_global_chem_network(print_output=True)
    molecules = gc.get_node_smiles('emerging_perfluoroalkyls')

    assert len(molecules) > 0

def test_check_fda_status():

    '''

    Test The Check For the FDA Status

    '''

def test_edit_smile():

    '''

    Test the Editing of the Smiles

    '''

def test_is_color_legal():

    '''

    Test Whether the Color is Legal accoridng to the FDA

    '''
  
def test_make_issue_arbitrer():

    '''

    Test The Making of The Issue of the Role Arbiterer

    '''

def test_make_issue_lorax():

    '''

    Test The Making of The Issue of the Role Lorax

    '''


def test_create_issue():

    '''

    Test The Creating Issue Function of Mother Nature

    '''

def test_create_graph_node():

    '''

    Test the Making of a Graph Node

    '''

def test_add_smile_file():

    '''

    Test The Addition of a SMILES from the training set 

    '''

def test_remove_smile_file():

    '''

    Test The Removal of a SMILES from the training set

    '''


def test_retraining():

    '''

    Test The Retraining of the Mother Nature on a Channel

    '''
def test_fetching_training_data():

    '''

    Test The Fetching of a Training Data

    '''

def test_filing_issue():

    '''

    Test The Filing of an Issue

    '''

