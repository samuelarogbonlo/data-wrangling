# Data Wrangling Implementation

This repository displays how a python script could be used to generate a section of a raw ```csv``` file from (https://www.eia.gov/dnav/ng/hist/rngwhhdm.htm). 

Over the years, it has become increasingly difficult to process data files in ```csv``` ormat to read, parse and process the contents because engineers and analyst have to always copy and paste data into Excel/Google Docs by hand, and then export the CSV. But that would be tedious, time consuming and error prone to do month after month. This is why a script is needed to automate this process with respect to the original ```csv``` file in this case while using all the required libraries as well. 

The original file has the rates and dates for the gas prices but the resulting ```csv``` files sort them out in ascending order, required rates, months details and other relevant information.


## Core Structure
    PYTEST
      ├── Data
      │   ├── datapackage.json
      │   │
      │   ├── gas-details_day.csv
      │   ├── gas-details_month.csv
      │   │
      │   └── gas-details_year.csv
      │   └── README.md
      │   
      │
      ├── Data Visualization
      │   ├── index.css
      │   ├── index.html
      │   └── index.js
      │
      ├── Henry_Hub_Natural_Gas_Spot_Price.csv
      │  
      ├── package-lock.json
      │  
      ├── main.py
      │
      └── README.md (you are here)

# Stack
Python 
Pandas
JSON
Comma Seperated Values (```csv```)

# Running The Program
- Install required dependencies for python, pandas and the likes.
- Clone repository ```git clone (https://github.com/samuelarogbonlo/data-wrangling.git)```
- Enter the root directory and enter ```python3 main.py``` to confirm the ```csv``` extraction or else you could study the previously generated ```csv``` file in the ```data``` directory.
- For the data visualization, you can just open the ```index.html``` on your browser (prefferbly chrome) to load the chart (this part is challenging and still in progress).

## Authors
Samuel Arogbonlo - [Github](https://github.com/samuelarogbonlo). [Twitter](https://twitter.com/SamuelArogbonlo)
 
## Resources and Inspirations
Study materials on data wrangling, visualization and ```csv``` manipulation.

## Hire Me
Looking for an SRE(DevOps) Engineer to build your next infrastruture to work remotely on your data platform in Datopian? Get in touch: (sbayo971@gmail.com)

## License 
The MIT License (http://www.opensource.org/licenses/mit-license.php)
