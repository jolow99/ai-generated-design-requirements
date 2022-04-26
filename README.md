# ai-generated-design-requirements

## Background
This project involves the design of a new product line that improves sustainabiity for the Italian Small Appliance Manufacturer De'Longhi. Technical specifications from existing product lines and sentiment analysis of Youtube comments was used alongside classification models to  flag out comments relating to certain terms.  

## Folder Structures
There are 3 folders in the project:
1. Scraping - contains the code to scrape technical specifications from Delonghi's which makes use of Selenium and BeautifulSoup.
2. Utilities - Contains the AI models for classification and sentiment analysis
3. Youtube - Querying Youtube API to search for associated viddeos and save all comments
4. Root - Contains specification_score.py and the usability_score.py files

## Usage
1. Clone the repository to your local machine and ensure you are in the root directory

      `` git clone https://github.com/jolow99/ai-generated-design-requirements.git ``

      `` cd ai-generated-design-requirements ``


2. Create a new virtual environment

      Windows: 
      `` python -m venv venv``

      Mac: 
      `` venv venv``

3. Install all requirements
`` pip install -r requirements.txt``

## Read More
