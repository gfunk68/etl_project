# ETL Project
## Houston's Real Estate Data, Oiled up and ready to go!
### 1/7/2020
### Authors
David Nassif, Phillip Wirth, Michael Dowlin

!['Image not available'](/images/oil_house.jpg)

#### Description
Houston's ties with oil run deeper than the Permian Basin.  This project pulls together various real-estate and employement data for the city, and greater area, of Houston by year, going back to the 1970's.  We also brought in the average closing? price of crude for the same time span.  How closely correlated are the oil prices with Houston's employment and housing data?  How much of a lag, if any, is there between a significant change in crude prices and the job/housing market?  Grab this data and find out!

#### Steps to Create
| Step #| Step                               | Description                                                                        |
|-------|------------------------------------|------------------------------------------------------------------------------------|
|1      |Open Postgres                       |The PosgreSQL service needs to be running                                           |
|2      |Create a PosgreSQL DB called "houston_statistics_db"|This will be the db used to store the data that is scraped/downloaded.|
|3      |Run the following jupyter notebooks to import the CSVs, and scrape the oil prices|(order not important)            |
| a     |fed_employee.ipynb                  |This will import the houston_employees.csv, which is all non-farm employees in the Houston metropoliton statistical area (MSA).  The data is already by year, so the cleaning done here is column and index renaming.  Data is stored in the nonfarm_employees table.|

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
|app.py                         |Flask api that will return multiple datasets.|
|clean_data\create_tables_postgres.sql | sql Script that will create all the tables and relationships in a Postgres database    |
|clean_data\quickDBD diagram screenshot.pdf | ERD for the houston_statistics_db database                  |
|fed_employee.ipynb               | Jupyter notebook to import and clean the fed employee data |
|fed_energy_employee.ipynb            | Jupyter notebook to import and clean the fed energy employment data |
|fed_housing.ipynb               | Jupyter notebook to import and clean the fed housing quarterly data (transform to annual)|
|images\oil_house.jpg             | silly picture, 1st thing that came up on oil+house google...|
|oilprices.ipynb                 | Jupyter notebook that scrapes the oil prices, and then stores in a dataframe |
|population.ipynb             | Jupyter notebook to import and clean the fed population data|
|Project Proposal.docx        | 1 page project proposal                                     |

  
