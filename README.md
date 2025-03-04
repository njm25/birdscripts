
# birdscripts 

## Description

These scripts are designed to scrape bird call recordings, and train an AI model to classify bird calls based on these recordings. The scripts implement different stages of data processing, analysis, and model training.

## Features

- **Data Scraping**: Fetch bird call recordings from the xeno-canto API.
- **Data Analysis**: Generate and display statistics about the bird recordings.
- **Data Cleaning**: Filter and clean the dataset for training.
- **Model Training**: Train a convolutional neural network (CNN) to classify bird calls based on audio recording.

## Requirements

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nicomilette/birdscripts.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Global configuration variables are stored in `src/config.py`. This file includes settings for file paths, thresholds, and other parameters used across different scripts.

## Usage

Run the main script to access all functionalities via a menu:
```bash
python main.py
```

## Data Licensing

The data collected and used by these scripts is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). For more information, visit [Creative Commons License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
