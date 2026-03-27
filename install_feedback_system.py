#!/usr/bin/env python3
#
# Mother Nature Feedback System Installation Script
#
# ------------------------------------------------

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible with Metis"""
    version = sys.version_info
    if version.major != 3 or version.minor < 9 or version.minor >= 11:
        print("❌ Error: Python 3.9+ (but < 3.11) is required for Metis compatibility")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    try:
        # Install requirements
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def install_metis():
    """Install Metis feedback system"""
    print("\n🔬 Installing Metis...")
    
    try:
        # Install Metis
        subprocess.check_call([sys.executable, "-m", "pip", "install", "metis"])
        print("✅ Metis installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing Metis: {e}")
        return False

def create_env_file():
    """Create .env file template"""
    print("\n🔧 Creating environment file...")
    
    env_template = """# Mother Nature Feedback System Environment Variables
# ------------------------------------------------------------

# Discord Bot Configuration
DISCORD_TOKEN=your_discord_bot_token_here

# GitHub API Configuration
GITHUB_TOKEN=your_github_api_token_here

# Metis Configuration
METIS_PATH=metis

# Optional: Custom feedback data directory
# FEEDBACK_DATA_DIR=feedback_data
"""
    
    env_file = Path(".env")
    if env_file.exists():
        print("⚠️  .env file already exists, skipping creation")
        return True
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_template)
        print("✅ .env file created successfully")
        print("   Please update it with your actual tokens")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    
    directories = [
        "feedback_data",
        "feedback_data/cannabis",
        "feedback_data/medicinal_chemistry",
        "feedback_data/food",
        "feedback_data/environment",
        "feedback_data/space",
        "feedback_data/materials",
        "feedback_data/narcotics",
        "feedback_data/global",
        "feedback_data/contraceptives",
        "feedback_data/performance_enhancements",
        "feedback_data/solar_cells",
        "feedback_data/education"
    ]
    
    try:
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
        print("✅ Directories created successfully")
        return True
    except Exception as e:
        print(f"❌ Error creating directories: {e}")
        return False

def test_installation():
    """Test the installation"""
    print("\n🧪 Testing installation...")
    
    try:
        # Test imports
        import discord
        import pandas as pd
        import yaml
        import numpy as np
        from mother_nature.feedback_system import MetisFeedbackSystem
        
        print("✅ All imports successful")
        
        # Test MetisFeedbackSystem creation
        class MockGithub: pass
        class MockRepo: pass
        class MockClient: pass
        class MockBot: pass
        
        feedback_system = MetisFeedbackSystem(
            github=MockGithub(),
            repo=MockRepo(),
            global_chem_repo=MockRepo(),
            client=MockClient(),
            bot=MockBot()
        )
        
        print("✅ MetisFeedbackSystem created successfully")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

def main():
    """Main installation function"""
    print("🚀 Mother Nature Feedback System Installation")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Install Metis
    if not install_metis():
        sys.exit(1)
    
    # Create environment file
    if not create_env_file():
        sys.exit(1)
    
    # Create directories
    if not create_directories():
        sys.exit(1)
    
    # Test installation
    if not test_installation():
        sys.exit(1)
    
    print("\n🎉 Installation completed successfully!")
    print("\n📋 Next steps:")
    print("1. Update the .env file with your Discord and GitHub tokens")
    print("2. Start the bot: python mother_nature/runner.py")
    print("3. Test feedback collection: /collect_feedback cannabis 5")
    print("4. Read README_FEEDBACK_SYSTEM.md for detailed usage instructions")
    
    print("\n📚 Documentation:")
    print("- README_FEEDBACK_SYSTEM.md - Complete usage guide")
    print("- https://github.com/JanoschMenke/metis - Metis documentation")

if __name__ == "__main__":
    main() 