# Mother Nature Feedback System Integration

## Overview

This implementation integrates the [Metis feedback system](https://github.com/JanoschMenke/metis) with the Mother Nature Discord chatbot to enable expert feedback collection on AI-generated molecules. The system allows chemists to provide detailed feedback on molecular properties, which is then used to improve the REINVENT AI model's molecule generation capabilities.

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

## Features

### New Discord Commands

- `/collect_feedback <category> [num_molecules]` - Start Metis GUI for feedback collection
- `/process_feedback <category>` - Process feedback results from Metis session
- `/feedback_status [category]` - Get status of feedback collection
- `/create_feedback_issue <category>` - Create GitHub issue with feedback results

### Supported Chemical Categories

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

### Feedback Properties

The system collects feedback on the following molecular properties:

- **Overall Quality** - General assessment of the molecule
- **Mutagenicity** - Potential for genetic mutations
- **Toxicity** - Harmful effects on living organisms
- **Stability** - Chemical and physical stability
- **Desirable Properties** - Positive characteristics

## Installation

### Prerequisites

1. Python 3.9+ (but < 3.11 for Metis compatibility)
2. Discord bot token
3. GitHub API token
4. Metis installation

### Setup Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Metis**
   ```bash
   pip install metis
   ```

3. **Environment Variables**
   Create a `.env` file with:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   GITHUB_TOKEN=your_github_api_token
   METIS_PATH=metis  # Path to Metis executable
   ```

4. **Directory Structure**
   The system will automatically create:
   ```
   feedback_data/
   ├── cannabis/
   ├── medicinal_chemistry/
   ├── food/
   └── ... (other categories)
   ```

## Usage

### 1. Starting Feedback Collection

```bash
# In Discord channel
/collect_feedback cannabis 20
```

This will:
- Validate the category
- Fetch molecules from Global-Chem database
- Prepare molecules in Metis format
- Launch Metis GUI for expert feedback
- Display status message in Discord

### 2. Providing Feedback

When Metis GUI opens:
1. Review each molecule's structure
2. Use sliders to rate properties (0-1 scale)
3. Highlight problematic substructures
4. Add comments on molecular properties
5. Save feedback when complete

### 3. Processing Feedback Results

```bash
# In Discord channel
/process_feedback cannabis
```

This will:
- Analyze feedback data
- Calculate average scores
- Generate summary statistics
- Display results in Discord

### 4. Creating GitHub Issues

```bash
# In Discord channel
/create_feedback_issue cannabis
```

This will:
- Process feedback results
- Create detailed GitHub issue
- Include feedback summary
- Suggest next steps for model improvement

### 5. Checking System Status

```bash
# Check all categories
/feedback_status

# Check specific category
/feedback_status cannabis
```

## Configuration

### Metis Configuration

The system automatically generates Metis configuration files with:

- **UI Settings**: Molecule viewer, property sliders, substructure highlighting
- **Data Settings**: Input/output paths, molecule selection strategy
- **Feedback Properties**: Customizable property labels and colors

### Customization

You can modify the feedback system by editing:

1. **Supported Categories**: Update `supported_categories` in `feedback_system.py`
2. **Feedback Properties**: Modify `propertyLabels` in `create_metis_config()`
3. **UI Settings**: Adjust UI configuration in Metis config generation
4. **Data Sources**: Update `_get_molecules_for_category()` to use different data sources

## Data Flow

### 1. Molecule Selection
- System fetches molecules from Global-Chem database
- Filters by chemical category
- Prepares SMILES strings for Metis format

### 2. Feedback Collection
- Metis GUI displays molecules with interactive tools
- Experts provide ratings and comments
- Feedback saved to CSV files

### 3. Data Processing
- System analyzes feedback data
- Calculates statistics and trends
- Generates summary reports

### 4. Model Integration
- Feedback data used to improve REINVENT model
- New molecules generated based on expert preferences
- Continuous learning loop established

## File Structure

```
mother_nature/
├── feedback_system.py          # Main feedback system implementation
├── mother_nature.py            # Updated with feedback integration
├── runner.py                   # Updated with new Discord commands
└── ...

feedback_data/                  # Auto-generated feedback storage
├── cannabis/
│   ├── initial_molecules.csv
│   ├── metis_config.yml
│   └── feedback_results/
├── medicinal_chemistry/
└── ...
```

## Testing

### Manual Testing

1. **Start the bot**:
   ```bash
   python mother_nature/runner.py
   ```

2. **Test feedback collection**:
   ```bash
   /collect_feedback cannabis 5
   ```

3. **Verify Metis GUI opens** and displays molecules

4. **Test feedback processing**:
   ```bash
   /process_feedback cannabis
   ```

5. **Check GitHub issue creation**:
   ```bash
   /create_feedback_issue cannabis
   ```

### Automated Testing

Run the test suite:
```bash
python -m pytest tests/
```

## Troubleshooting

### Common Issues

1. **Metis not found**
   - Ensure Metis is installed: `pip install metis`
   - Check METIS_PATH environment variable

2. **GUI not opening**
   - Verify PySide2 installation
   - Check display settings for headless systems

3. **No molecules found**
   - Verify category exists in Global-Chem
   - Check data source configuration

4. **Permission errors**
   - Ensure write permissions for feedback_data directory
   - Check GitHub token permissions

### Debug Mode

Enable debug logging by setting:
```python
self.feedback_config['debug'] = True
```

## Integration with REINVENT

### Training Data Preparation

The feedback system prepares data for REINVENT training:

1. **Positive Examples**: Molecules with high feedback scores
2. **Negative Examples**: Molecules with low feedback scores
3. **Property Weights**: Based on expert ratings
4. **Substructure Filters**: Based on highlighted problematic groups

### Model Retraining

Feedback data triggers automatic model retraining:

1. **Data Validation**: Ensure feedback quality
2. **Dataset Preparation**: Format for REINVENT
3. **Model Training**: Update with new preferences
4. **Validation**: Test on held-out molecules

## Contributing

### Development Guidelines

1. **Code Style**: Follow existing Python conventions
2. **Documentation**: Add docstrings for all functions
3. **Testing**: Include tests for new features
4. **Error Handling**: Implement proper exception handling

### Adding New Features

1. **Extend MetisFeedbackSystem class** with new methods
2. **Add Discord commands** in runner.py
3. **Update command list** in mother_nature.py
4. **Add tests** for new functionality

## License

This implementation follows the same license as the original Mother Nature project.

## Acknowledgments

- [Metis](https://github.com/JanoschMenke/metis) - Expert feedback collection system
- [REINVENT](https://github.com/MarcusOlivecrona/REINVENT) - Molecular generation framework
- [Global-Chem](https://github.com/Global-Chem/global-chem) - Chemical knowledge graph

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review Metis documentation
3. Open GitHub issues with detailed error messages
4. Contact the development team

---

*This feedback system enhances Mother Nature's learning capabilities by incorporating expert chemical knowledge into the AI training process.* 