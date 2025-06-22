#!/usr/bin/env python3
#
# Test Feedback System Integration
#
# ---------------------------------

# Python Internals
# ----------------
import os
import tempfile
import shutil
from pathlib import Path

# Python Externals
# ----------------
import pytest
import pandas as pd
import yaml

# Mother Nature Imports
# ---------------------
from mother_nature.feedback_system import MetisFeedbackSystem

class TestMetisFeedbackSystem:
    """Test cases for MetisFeedbackSystem integration"""
    
    @pytest.fixture
    def feedback_system(self):
        """Create a test instance of MetisFeedbackSystem"""
        # Mock GitHub and Discord objects for testing
        class MockGithub:
            pass
            
        class MockRepo:
            pass
            
        class MockClient:
            pass
            
        class MockBot:
            pass
            
        github = MockGithub()
        repo = MockRepo()
        global_chem_repo = MockRepo()
        client = MockClient()
        bot = MockBot()
        
        return MetisFeedbackSystem(
            github=github,
            repo=repo,
            global_chem_repo=global_chem_repo,
            client=client,
            bot=bot
        )
    
    @pytest.fixture
    def temp_feedback_dir(self):
        """Create temporary feedback directory for testing"""
        temp_dir = tempfile.mkdtemp()
        feedback_dir = Path(temp_dir) / "feedback_data"
        feedback_dir.mkdir()
        
        # Create category subdirectories
        categories = ['cannabis', 'medicinal_chemistry', 'food']
        for category in categories:
            category_dir = feedback_dir / category
            category_dir.mkdir()
            
        yield feedback_dir
        
        # Cleanup
        shutil.rmtree(temp_dir)
    
    def test_initialization(self, feedback_system):
        """Test MetisFeedbackSystem initialization"""
        assert feedback_system is not None
        assert hasattr(feedback_system, 'feedback_config')
        assert 'metis_path' in feedback_system.feedback_config
        assert 'supported_categories' in feedback_system.feedback_config
    
    def test_supported_categories(self, feedback_system):
        """Test supported categories configuration"""
        categories = feedback_system.feedback_config['supported_categories']
        expected_categories = [
            'cannabis', 'medicinal_chemistry', 'food', 'environment',
            'space', 'materials', 'narcotics', 'global', 'contraceptives',
            'performance_enhancements', 'solar_cells', 'education'
        ]
        
        assert len(categories) == len(expected_categories)
        for category in expected_categories:
            assert category in categories
    
    def test_create_metis_config(self, feedback_system, temp_feedback_dir):
        """Test Metis configuration file creation"""
        # Override feedback data directory for testing
        feedback_system.feedback_config['feedback_data_dir'] = str(temp_feedback_dir)
        
        category = 'cannabis'
        num_molecules = 10
        
        config_path = feedback_system.create_metis_config(category, num_molecules)
        
        # Check if config file exists
        assert Path(config_path).exists()
        
        # Load and validate config
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        # Check required fields
        assert 'data' in config
        assert 'ui' in config
        assert config['data']['num_molecules'] == num_molecules
        assert config['data']['run_name'].startswith('mother_nature_feedback_cannabis')
    
    def test_prepare_molecules_for_feedback(self, feedback_system, temp_feedback_dir):
        """Test molecule preparation for feedback"""
        # Override feedback data directory for testing
        feedback_system.feedback_config['feedback_data_dir'] = str(temp_feedback_dir)
        
        category = 'medicinal_chemistry'
        smiles_list = [
            'CC(=O)OC1=CC=CC=C1C(=O)O',
            'CC(C)CC1=CC=C(C=C1)C(C)C(=O)O',
            'CC1=C(C(=CC=C1)NC(=O)C2=CC=C(C=C2)CN3CCN(CC3)C)NC4=NC=CC(=N4)C5=CN=CC=C5'
        ]
        names = ['Aspirin', 'Ibuprofen', 'Gefitinib']
        
        csv_path = feedback_system.prepare_molecules_for_feedback(
            category, smiles_list, names
        )
        
        # Check if CSV file exists
        assert Path(csv_path).exists()
        
        # Load and validate CSV
        df = pd.read_csv(csv_path)
        
        assert len(df) == 3
        assert 'SMILES' in df.columns
        assert 'Name' in df.columns
        assert 'activity' in df.columns
        assert 'ugly' in df.columns
        assert 'tox' in df.columns
        assert 'stability' in df.columns
        assert 'like' in df.columns
        
        # Check data
        assert df['SMILES'].iloc[0] == smiles_list[0]
        assert df['Name'].iloc[0] == names[0]
        assert all(df['activity'] == 0.5)  # Default neutral score
    
    def test_get_feedback_status(self, feedback_system, temp_feedback_dir):
        """Test feedback status retrieval"""
        # Override feedback data directory for testing
        feedback_system.feedback_config['feedback_data_dir'] = str(temp_feedback_dir)
        
        # Test status for all categories
        status = feedback_system.get_feedback_status()
        assert "Feedback System Status:" in status
        
        # Test status for specific category
        status = feedback_system.get_feedback_status('cannabis')
        assert "cannabis" in status
    
    def test_invalid_category(self, feedback_system):
        """Test handling of invalid categories"""
        invalid_category = 'invalid_category'
        
        # This should not raise an exception but return an error message
        # The actual test would be in the async methods, but we can test the validation logic
        assert invalid_category not in feedback_system.feedback_config['supported_categories']
    
    def test_config_file_structure(self, feedback_system, temp_feedback_dir):
        """Test Metis configuration file structure"""
        # Override feedback data directory for testing
        feedback_system.feedback_config['feedback_data_dir'] = str(temp_feedback_dir)
        
        category = 'food'
        config_path = feedback_system.create_metis_config(category, 15)
        
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        # Test required configuration sections
        assert 'seed' in config
        assert 'max_iterations' in config
        assert 'activity_label' in config
        assert 'introText' in config
        assert 'propertyLabels' in config
        assert 'data' in config
        assert 'ui' in config
        
        # Test data configuration
        data_config = config['data']
        assert 'initial_path' in data_config
        assert 'path' in data_config
        assert 'selection_strategy' in data_config
        assert 'num_molecules' in data_config
        assert 'run_name' in data_config
        
        # Test UI configuration
        ui_config = config['ui']
        assert 'show_atom_contributions' in ui_config
        assert 'tab' in ui_config
        assert 'navigationbar' in ui_config
        assert 'general' in ui_config
        assert 'substructures' in ui_config
        assert 'global_properties' in ui_config
    
    def test_property_labels(self, feedback_system, temp_feedback_dir):
        """Test property labels configuration"""
        # Override feedback data directory for testing
        feedback_system.feedback_config['feedback_data_dir'] = str(temp_feedback_dir)
        
        category = 'environment'
        config_path = feedback_system.create_metis_config(category, 10)
        
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        property_labels = config['propertyLabels']
        expected_labels = ['activity', 'ugly', 'tox', 'stability', 'like']
        
        for label in expected_labels:
            assert label in property_labels
        
        # Check label descriptions
        assert property_labels['activity'] == 'Overall Quality'
        assert property_labels['ugly'] == 'Mutagenicity'
        assert property_labels['tox'] == 'Toxicity'
        assert property_labels['stability'] == 'Stability'
        assert property_labels['like'] == 'Desirable Properties'
    
    def test_substructure_configuration(self, feedback_system, temp_feedback_dir):
        """Test substructure highlighting configuration"""
        # Override feedback data directory for testing
        feedback_system.feedback_config['feedback_data_dir'] = str(temp_feedback_dir)
        
        category = 'materials'
        config_path = feedback_system.create_metis_config(category, 10)
        
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        substructures = config['ui']['substructures']['liabilities']
        
        # Check liability configurations
        assert 'ugly' in substructures
        assert 'tox' in substructures
        assert 'stability' in substructures
        assert 'like' in substructures
        
        # Check color configurations
        assert substructures['ugly']['color'] == '#ff7f7f'
        assert substructures['tox']['color'] == '#51d67e'
        assert substructures['stability']['color'] == '#eed358'
        assert substructures['like']['color'] == '#9542f5'

if __name__ == "__main__":
    pytest.main([__file__]) 