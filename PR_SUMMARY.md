# Pull Request: Mother Nature Feedback System Integration

## Overview

This PR integrates the [Metis feedback system](https://github.com/JanoschMenke/metis) with the Mother Nature Discord chatbot to enable expert feedback collection on AI-generated molecules. The system allows chemists to provide detailed feedback on molecular properties, which is then used to improve the REINVENT AI model's molecule generation capabilities.

## 🚨 Important Note

**Python Version Compatibility**: Metis requires Python 3.9+ but < 3.11. The current system is running Python 3.13.3, which may cause compatibility issues. Users should either:
1. Use a compatible Python version (3.9-3.10)
2. Use a virtual environment with the correct Python version
3. Wait for Metis to support newer Python versions

## Changes Made

### 1. New Files Added

- **`mother_nature/feedback_system.py`** - Core feedback system implementation
- **`tests/test_feedback_system.py`** - Comprehensive test suite
- **`README_FEEDBACK_SYSTEM.md`** - Detailed documentation
- **`install_feedback_system.py`** - Automated installation script
- **`PR_SUMMARY.md`** - This summary document

### 2. Files Modified

#### `requirements.txt`
- Added Metis and its dependencies
- Added PyYAML for configuration management
- Added note about Python version compatibility

#### `mother_nature/mother_nature.py`
- Added import for MetisFeedbackSystem
- Added feedback system initialization
- Added 4 new feedback-related methods:
  - `collect_feedback()`
  - `process_feedback()`
  - `feedback_status()`
  - `create_feedback_issue()`
- Updated command list with new feedback commands

#### `mother_nature/runner.py`
- Added new Discord bot commands for feedback system
- Updated command descriptions
- Added proper error handling for feedback commands

## New Discord Commands

| Command | Description | Parameters |
|---------|-------------|------------|
| `/collect_feedback` | Start Metis GUI for feedback collection | `category`, `num_molecules` (optional) |
| `/process_feedback` | Process feedback results from Metis session | `category` |
| `/feedback_status` | Get status of feedback collection | `category` (optional) |
| `/create_feedback_issue` | Create GitHub issue with feedback results | `category` |

## Supported Chemical Categories

- cannabis
- medicinal_chemistry
- food
- environment
- space
- materials
- narcotics
- global
- contraceptives
- performance_enhancements
- solar_cells
- education

## Architecture

```
Discord User → Mother Nature Bot → Metis GUI → Expert Feedback → REINVENT Training → Updated Model
```

### Key Components

1. **Discord Bot Interface** - New commands for feedback collection
2. **Metis Integration** - GUI-based feedback collection system
3. **Data Processing** - Feedback analysis and summarization
4. **GitHub Integration** - Automated issue creation for feedback results
5. **Training Pipeline** - Integration with REINVENT for model improvement

## Installation Instructions

### Quick Setup

1. **Run installation script**:
   ```bash
   python install_feedback_system.py
   ```

2. **Update environment variables** in `.env`:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   GITHUB_TOKEN=your_github_api_token
   METIS_PATH=metis
   ```

3. **Start the bot**:
   ```bash
   python mother_nature/runner.py
   ```

### Manual Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install metis
   ```

2. **Create directories**:
   ```bash
   mkdir -p feedback_data/{cannabis,medicinal_chemistry,food,environment,space,materials,narcotics,global,contraceptives,performance_enhancements,solar_cells,education}
   ```

3. **Set up environment variables** (see Quick Setup)

## Usage Examples

### 1. Start Feedback Collection
```bash
/collect_feedback cannabis 20
```
- Validates category
- Fetches molecules from Global-Chem
- Launches Metis GUI for expert feedback

### 2. Process Feedback Results
```bash
/process_feedback cannabis
```
- Analyzes feedback data
- Calculates statistics
- Displays summary in Discord

### 3. Create GitHub Issue
```bash
/create_feedback_issue cannabis
```
- Processes feedback
- Creates detailed GitHub issue
- Includes feedback summary and next steps

### 4. Check System Status
```bash
/feedback_status
/feedback_status cannabis
```
- Shows feedback collection status
- Lists available feedback sessions

## Testing

### Run Tests
```bash
python -m pytest tests/test_feedback_system.py -v
```

### Manual Testing
1. Start the bot
2. Test each new command in Discord
3. Verify Metis GUI opens correctly
4. Check GitHub issue creation

## Configuration

### Metis Configuration
The system automatically generates Metis configuration files with:
- **UI Settings**: Molecule viewer, property sliders, substructure highlighting
- **Data Settings**: Input/output paths, molecule selection strategy
- **Feedback Properties**: Customizable property labels and colors

### Customization Options
- **Supported Categories**: Update `supported_categories` in `feedback_system.py`
- **Feedback Properties**: Modify `propertyLabels` in `create_metis_config()`
- **UI Settings**: Adjust UI configuration in Metis config generation
- **Data Sources**: Update `_get_molecules_for_category()` to use different data sources

## Data Flow

1. **Molecule Selection**: System fetches molecules from Global-Chem database
2. **Feedback Collection**: Metis GUI displays molecules with interactive tools
3. **Data Processing**: System analyzes feedback data and generates reports
4. **Model Integration**: Feedback data used to improve REINVENT model

## Benefits

### Enhanced Learning
- Expert chemists can provide detailed feedback on generated molecules
- AI learns from human preferences and domain expertise
- Better molecule generation for specific applications

### Quality Control
- Human oversight of AI-generated compounds
- Validation of chemical properties and safety
- Compliance with regulatory requirements

### Community Engagement
- Chemists can actively participate in improving the AI
- Transparent feedback collection process
- Educational opportunities for the community

## Technical Considerations

### GUI Integration
- Metis runs as a separate GUI application
- Communication between Discord bot and Metis handled via file system
- Consider web-based alternatives for easier integration

### Data Synchronization
- Feedback data properly synchronized between systems
- Version control for feedback datasets
- Data integrity maintained across the pipeline

### Performance Optimization
- Batch feedback collection to avoid overwhelming the system
- Caching for frequently accessed feedback data
- Optimized training loop with human feedback

## Future Enhancements

1. **Web-based Interface**: Replace GUI with web interface for easier access
2. **Real-time Collaboration**: Multiple experts can provide feedback simultaneously
3. **Advanced Analytics**: Machine learning analysis of feedback patterns
4. **Integration with Other Tools**: Connect with additional chemical analysis tools

## Troubleshooting

### Common Issues

1. **Metis not found**
   - Ensure Metis is installed: `pip install metis`
   - Check METIS_PATH environment variable

2. **GUI not opening**
   - Verify PySide2 installation
   - Check display settings for headless systems

3. **Python version issues**
   - Use Python 3.9-3.10 for Metis compatibility
   - Create virtual environment with correct Python version

4. **Permission errors**
   - Ensure write permissions for feedback_data directory
   - Check GitHub token permissions

## Dependencies

### New Dependencies Added
- **Metis**: Expert feedback collection system
- **PySide2**: GUI framework for Metis
- **PyYAML**: Configuration file management
- **Additional data science libraries**: pandas, numpy, matplotlib, seaborn

### Version Requirements
- Python: 3.9+ but < 3.11 (for Metis compatibility)
- PySide2: 5.15.2.1
- scikit-learn: 1.3.0
- Other dependencies: See requirements.txt

## Documentation

- **README_FEEDBACK_SYSTEM.md**: Complete usage guide
- **Code comments**: Detailed docstrings for all functions
- **Test files**: Examples of proper usage
- **Installation script**: Automated setup guide

## Acknowledgments

- [Metis](https://github.com/JanoschMenke/metis) - Expert feedback collection system
- [REINVENT](https://github.com/MarcusOlivecrona/REINVENT) - Molecular generation framework
- [Global-Chem](https://github.com/Global-Chem/global-chem) - Chemical knowledge graph

---

**This feedback system enhances Mother Nature's learning capabilities by incorporating expert chemical knowledge into the AI training process, creating a more robust and community-driven molecular generation system.** 