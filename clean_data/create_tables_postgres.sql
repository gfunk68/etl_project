-- create database called houston_statistics_db


CREATE TABLE "oilprice" (
    "year" int   NOT NULL,
    "oilprice_usd" float(2)   NOT NULL,
    CONSTRAINT "pk_oilprice" PRIMARY KEY (
        "year"
     )
);

CREATE TABLE "population" (
    "year" int   NOT NULL,
    "population" int   NOT NULL,
    CONSTRAINT "pk_population" PRIMARY KEY (
        "year"
     )
);

CREATE TABLE "nonfarm_employees" (
    "year" int   NOT NULL,
    "employees" int   NOT NULL,
    CONSTRAINT "pk_nonfarm_employees" PRIMARY KEY (
        "year"
     )
);

CREATE TABLE "energy_extraction_employees" (
    "year" int   NOT NULL,
    "employees" int   NOT NULL,
    CONSTRAINT "pk_energy_extraction_employees" PRIMARY KEY (
        "year"
     )
);

CREATE TABLE "housing_index" (
    "year" int   NOT NULL,
    "housing_price_index" float(4)   NOT NULL,
    CONSTRAINT "pk_housing_index" PRIMARY KEY (
        "year"
     )
);

