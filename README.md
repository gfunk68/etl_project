# ETL Project
## Houston's Real Estate Data, Oiled up and ready to go!
### 1/7/2020
### Authors
David Nassif, Phillip Wirth, Michael Dowlin

!['Image not available'](/images/oil_house.jpg)

#### Description
Houston's ties with oil run deeper than the Permian Basin.  This project pulls together various real-estate and employement data for the city, and greater area, of Houston by year, going back to the 1970's.  We also brought in the average closing? price of crude for the same time span.  How closely correlated are the oil prices with Houston's employment and housing data?  How much of a lag, if any, is there between a significant change in crude prices and the job/housing market?  Grab this data and find out!

#### Datasets Used
| Data                         | Method Retrieved           | URL                                                                 |
|------------------------------|----------------------------|---------------------------------------------------------------------|
|Oil prices by year	           |Web-scraping	              | https://www.macrotrends.net/1369/crude-oil-price-history-chart         |
|Greater Houston population by year|	csv	| https://fred.stlouisfed.org/series/HTNPOP         |
|Houston housing prices by year|	csv	|https://fred.stlouisfed.org/series/ATNHPIUS26420Q |
|Houston non-farm employee population by year	|csv	|https://fred.stlouisfed.org/series/HOUS448NA |
|Houston energy extaction employee population by year|	csv	|https://fred.stlouisfed.org/series/SMU48264201021100001SA |

#### Contents
| File                         | Description                                                                                     |
|------------------------------|-------------------------------------------------------------------------------------------------|
|fed_employee.ipynb               | Jupyter notebook to import and clean the fed employee data |
|fed_energy_employee.ipynb            | Jupyter notebook to import and clean the fed energy employment data |
|fed_housing.ipynb               | Jupyter notebook to import and clean the fed housing quarterly data (transform to annual)|
|population.ipynb             | Jupyter notebook to import and clean the fed population data|
|oilprices.ipynb                 | Jupyter notebook that scrapes the oil prices, and then stores in a dataframe |

  
