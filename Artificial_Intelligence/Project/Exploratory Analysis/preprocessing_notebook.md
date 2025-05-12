# CSE 4705 Project: Data Pre-Processing

We are using the following structured datasets:

https://catalog.data.gov/dataset/real-estate-sales-2001-2018
This dataset contains information of real estate sales in Connecticut from 2001 to 2022. Each row contains sale information including town, date of sale, property type, sales price, property assessment and sales ratio (assessed value divided by the sale price).

https://catalog.data.gov/dataset/municipal-fiscal-indicators-economic-and-grand-list-data-2019-2024
This dataset is a compilation of financial and demographic information on municipalities in Connecticut between the years 2019 and 2024. It includes aggregate information like net current education expenditures, and per capita values like median household income.

The real estate dataset is very big (over 1 million rows) so we did pre-processing using SQL to construct a new CSV with summarized features to run further analysis on with Python.

1. Loading csvs into databases

Table realestate20012022 (raw real estate data)

```
CREATE TABLE `realestate20012022` (
  `serialnumber` bigint(20) DEFAULT NULL,
  `listyear` int(11) DEFAULT NULL,
  `daterecorded` date DEFAULT NULL,
  `town` varchar(50) DEFAULT NULL,
  `address` varchar(256) DEFAULT NULL,
  `assessedvalue` double DEFAULT NULL,
  `saleamount` double DEFAULT NULL,
  `salesratio` double DEFAULT NULL,
  `propertytype` varchar(50) DEFAULT NULL,
  `residentialtype` varchar(50) DEFAULT NULL,
  `nonusecode` varchar(50) DEFAULT NULL,
  `remarks` varchar(256) DEFAULT NULL,
  `opm_remarks` varchar(256) DEFAULT NULL,
  `geo_coordinates` varchar(256) DEFAULT NULL
);
CREATE INDEX idx_realestate20012022 ON realestate20012022(listyear, daterecorded, town, assessedvalue, saleamount, salesratio, propertytype, residentialtype);
LOAD DATA LOCAL INFILE '/home/tomkm/Downloads/Real_Estate_Sales_2001-2022_GL.csv'
INTO TABLE realestate20012022
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
ESCAPED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(serialnumber, listyear, @daterecorded, town, address, assessedvalue, saleamount, salesratio, propertytype, residentialtype, nonusecode, remarks, opm_remarks, geo_coordinates)
set daterecorded = STR_TO_DATE( @daterecorded, '%m/%d/%Y');
```
Table mun20192024 (raw munucipal data)

```
CREATE TABLE mun20192024 (
	municipal_fiscal_indicators_report_edition VARCHAR(256),
	year INT,
	year_type VARCHAR(50),
	town VARCHAR(50),
    municipality_fips_geoid INT,
    municipality_fips INT,
    tax_code INT,
    metric VARCHAR(256),
    value DOUBLE
);

ALTER TABLE mun20192024 ADD PRIMARY KEY (year, town, metric);
CREATE INDEX idx_mun20192024 ON mun20192024(year, town, metric);

LOAD DATA LOCAL INFILE '/home/tomkm/Downloads/Municipal_Fiscal_Indicators__Economic_and_Grand_List_Data__2019-2024.csv'
INTO TABLE mun20192024
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(municipal_fiscal_indicators_report_edition, year, year_type, town, @municipality_fips_geoid, @municipality_fips, @tax_code, metric, @value)
set municipality_fips_geoid = nullif(@municipality_fips_geoid, ''), municipality_fips = nullif(@municipality_fips, ''), tax_code = nullif(@tax_code, ''), value = nullif(@value, '');
```

2. Pre-Processing the raw data

The municipal data is structured so that each metric-value combination is on a separate row. For ease of use when doing relationship analysis, we created another table where each distinct metric is its own column.

```
create table muncleaned(
	year INT,
	town VARCHAR(50),
	Equalized_net_grand_list DOUBLE,
	Estimated_population_DPH DOUBLE,
	FYE_total_net_grand_list DOUBLE,
	Grand_list_apartment DOUBLE,
	Grand_list_commercial DOUBLE,
	Grand_list_income_and_expense DOUBLE,
	Grand_list_industrial DOUBLE,
	Grand_list_land_use DOUBLE,
	Grand_list_motor_vehicle DOUBLE,
	Grand_list_net_personal_property DOUBLE,
	Grand_list_net_real_property DOUBLE,
	Grand_list_personal_property DOUBLE,
	Grand_list_public_utility DOUBLE,
	Grand_list_residential DOUBLE,
	Grand_list_ten_mill_land DOUBLE,
	Grand_list_total_net_motor_vehicle DOUBLE,
	Grand_list_total_real_property DOUBLE,
	Grand_list_vacant_land DOUBLE,
	Median_value_of_owner_occupied_homes_ACS DOUBLE,
	Mill_rate_motor_vehicle DOUBLE,
	Mill_rate_real_and_personal_property DOUBLE,
	Net_current_education_expenditures_CSDE DOUBLE,
	Net_current_education_expenditures_per_pupil_CSDE DOUBLE,
	Per_capita_income_ACS DOUBLE,
	School_enrollment_average_daily_membershipCSDE DOUBLE,
	Total_net_grand_list DOUBLE,
	Median_household_income_ACS DOUBLE,
	Median_per_capita_income_ACS DOUBLE,
	Area_in_sq_miles_2020_census DOUBLE,
	Tax_exempt_property_as_a_percent_of_total DOUBLE,
	Tax_exempt_property_assessment DOUBLE,
	Total_exempt_and_taxable_property_assessment DOUBLE
);
-- insert into table
SET @sql = '';

SELECT GROUP_CONCAT(
    CONCAT('MAX(CASE WHEN metric = \'', metric, '\' THEN value END)\n')
) INTO @sql
FROM (SELECT DISTINCT metric FROM mun20192024) as  sub;

SET @sql = CONCAT('Insert into muncleaned select year, town,',
@sql, ' FROM mun20192024 GROUP BY year, town;');

select @sql

select * from muncleaned

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

## Interesting Observation: Missing Property Types pose challenges to our analysis
We wanted to focus our analysis on residential sales, but we noticed there were 382446 rows out of 1097629 where the propertytype was blank. 
```
select count(*) from realestate20012022 where propertytype = ''
```
![no_property_type.png](no_property_type.png)

There were also multiple sales of $0 which are likely garbage values.

```
select count(*) from realestate20012022 where saleamount = 0
```
![saleamount_0.png](saleamount_0.png)

As a reasonable metric we used the 1st percentile sale amount of $10,000 as a cutoff for removing outliers before generating the summary csv
```
select
	PERCENTILE_CONT(0.01) WITHIN GROUP (ORDER BY saleamount) OVER () AS p1
from realestate20012022
where propertytype in ('Residential', 'Condo', 'Four Family', 'Single Family', 'Three Family', 'Two Family', '')
```
![percentile_1](percentile_1.png)

We created a table of real estate values with outliers removed using the above rule, as well as removing any that are more than 3 z-scores away.
```
insert into realestatecleaned (serialnumber, listyear, daterecorded, town, address, assessedvalue, saleamount, salesratio, propertytype, residentialtype, nonusecode, remarks, opm_remarks, geo_coordinates)
with stats as (
select year(daterecorded) as year, town, avg(saleamount) as avgsale, stddev(saleamount) as salestddev, avg(assessedvalue) as avgassvalue, stddev(assessedvalue) as assvaluestddev
from realestate20012022
group by year(daterecorded), town
)
,
zscores AS (
   SELECT r.*,
       (saleamount - s.avgsale) / s.salestddev AS salezscore, (assessedvalue - s.avgassvalue) / s.assvaluestddev AS assvaluezscore
   FROM
realestate20012022 r join stats s on s.salestddev <> 0 and s.assvaluestddev <> 0 and year(r.daterecorded) = s.year and r.town = s.town
)
select serialnumber, listyear, daterecorded, town, address, assessedvalue, saleamount, salesratio, propertytype, residentialtype, nonusecode, remarks, opm_remarks, geo_coordinates
from zscores where propertytype in ('Residential', 'Condo', 'Four Family', 'Single Family', 'Three Family', 'Two Family', '') 
and saleamount > 10000 and assessedvalue > 10000 and salezscore between -3 and 3 and assvaluezscore between -3 and 3
```

3. Constructing a summary csv

We join the two datasets into one csv such that each row is a distinct year-town combination with municipal data metrics and summary statistics of real estate numerical data.

```
with median_raw as (
select year(daterecorded) as year, town, 
	PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY assessedvalue) OVER (PARTITION BY year(daterecorded), town) AS q1_assessed,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY assessedvalue) OVER (PARTITION BY year(daterecorded), town) AS q2_assessed,
	PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY assessedvalue) OVER (PARTITION BY year(daterecorded), town) AS q3_assessed,
	PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY saleamount) OVER (PARTITION BY year(daterecorded), town) AS q1,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY saleamount) OVER (PARTITION BY year(daterecorded), town) AS q2,
	PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY saleamount) OVER (PARTITION BY year(daterecorded), town) AS q3,
	PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salesratio) OVER (PARTITION BY year(daterecorded), town) AS q1_ratio,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salesratio) OVER (PARTITION BY year(daterecorded), town) AS q2_ratio,
	PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salesratio) OVER (PARTITION BY year(daterecorded), town) AS q3_ratio
from realestatecleaned
),
median as (
select * from median_raw
group by year, town
),
centrals as (
select year(daterecorded) as year, town, count(*) as cnt_sales, avg(assessedvalue) as avgassessed, avg(saleamount) as avgsale, avg(salesratio) as avgsalesratio from realestatecleaned
group by year(daterecorded), town
),
combined as (
select c.year, c.town, c.cnt_sales, c.avgassessed as avg_assessed_value, c.avgsale AS avg_sale_price, c.avgsalesratio as avg_sales_ratio,
m.q1_assessed as assessed_value_q1, m.q2_assessed as median_assessed_value, m.q3_assessed as assessed_value_q3,
m.q1 as sale_price_q1,m.q2 as median_sale_price,m.q3 as sale_price_q3,
m.q1_ratio as sales_ratio_q1, m.q2_ratio as median_sales_ratio, m.q3_ratio as sales_ratio_q3
from centrals c join median m on (c.year = m.year and c.town = m.town)
)
select IFNULL(c.year, ''),IFNULL(c.town, ''),IFNULL(c.cnt_sales, ''),IFNULL(c.avg_sale_price, ''),IFNULL(c.sale_price_q1, ''),IFNULL(c.median_sale_price, ''),IFNULL(c.sale_price_q3, ''),
IFNULL(c.avg_sales_ratio, ''),IFNULL(c.sales_ratio_q1, ''),IFNULL(c.median_sales_ratio, ''),IFNULL(c.sales_ratio_q3, ''),IFNULL(c.avg_assessed_value, ''),IFNULL(c.assessed_value_q1, ''),
IFNULL(c.median_assessed_value, ''),IFNULL(c.assessed_value_q3, ''),IFNULL(m.Equalized_net_grand_list, ''),IFNULL(m.Estimated_population_DPH, ''),
IFNULL(m.FYE_total_net_grand_list, ''),IFNULL(m.Grand_list_apartment, ''),IFNULL(m.Grand_list_commercial, ''),IFNULL(m.Grand_list_income_and_expense, ''),
IFNULL(m.Grand_list_industrial, ''),IFNULL(m.Grand_list_land_use, ''),IFNULL(m.Grand_list_motor_vehicle, ''),IFNULL(m.Grand_list_net_personal_property, ''),
IFNULL(m.Grand_list_net_real_property, ''),IFNULL(m.Grand_list_personal_property, ''),IFNULL(m.Grand_list_public_utility, ''),IFNULL(m.Grand_list_residential, ''),
IFNULL(m.Grand_list_ten_mill_land, ''),IFNULL(m.Grand_list_total_net_motor_vehicle, ''),IFNULL(m.Grand_list_total_real_property, ''),IFNULL(m.Grand_list_vacant_land, ''),
IFNULL(m.Median_value_of_owner_occupied_homes_ACS, ''),IFNULL(m.Mill_rate_motor_vehicle, ''),IFNULL(m.Mill_rate_real_and_personal_property, ''),
IFNULL(m.Net_current_education_expenditures_CSDE, ''),IFNULL(m.Net_current_education_expenditures_per_pupil_CSDE, ''),IFNULL(m.Per_capita_income_ACS, ''),
IFNULL(m.School_enrollment_average_daily_membershipCSDE, ''),IFNULL(m.Total_net_grand_list, ''),IFNULL(m.Median_household_income_ACS, ''),IFNULL(m.Median_per_capita_income_ACS, ''),
IFNULL(m.Area_in_sq_miles_2020_census, ''),IFNULL(m.Tax_exempt_property_as_a_percent_of_total, ''),IFNULL(m.Tax_exempt_property_assessment, ''),IFNULL(m.Total_exempt_and_taxable_property_assessment, '')
from combined c join muncleaned m on c.year = m.year and c.town = m.town
INTO OUTFILE '/tmp/cse4705_project_summary.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

We also construct a summary csv for just real estate information going back to 2001, which includes years not covered by the municipal dataset
```
with median_raw as (
select year(daterecorded) as year, town, 
	PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY assessedvalue) OVER (PARTITION BY year(daterecorded), town) AS q1_assessed,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY assessedvalue) OVER (PARTITION BY year(daterecorded), town) AS q2_assessed,
	PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY assessedvalue) OVER (PARTITION BY year(daterecorded), town) AS q3_assessed,
	PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY saleamount) OVER (PARTITION BY year(daterecorded), town) AS q1,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY saleamount) OVER (PARTITION BY year(daterecorded), town) AS q2,
	PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY saleamount) OVER (PARTITION BY year(daterecorded), town) AS q3,
	PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salesratio) OVER (PARTITION BY year(daterecorded), town) AS q1_ratio,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salesratio) OVER (PARTITION BY year(daterecorded), town) AS q2_ratio,
	PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salesratio) OVER (PARTITION BY year(daterecorded), town) AS q3_ratio
from realestatecleaned
),
median as (
select * from median_raw
group by year, town
),
centrals as (
select year(daterecorded) as year, town, count(*) as cnt_sales, avg(assessedvalue) as avgassessed, avg(saleamount) as avgsale, avg(salesratio) as avgsalesratio from realestatecleaned
group by year(daterecorded), town
),
combined as (
select c.year, c.town, c.cnt_sales, c.avgassessed as avg_assessed_value, c.avgsale AS avg_sale_price, c.avgsalesratio as avg_sales_ratio,
m.q1_assessed as assessed_value_q1, m.q2_assessed as median_assessed_value, m.q3_assessed as assessed_value_q3,
m.q1 as sale_price_q1,m.q2 as median_sale_price,m.q3 as sale_price_q3,
m.q1_ratio as sales_ratio_q1, m.q2_ratio as median_sales_ratio, m.q3_ratio as sales_ratio_q3
from centrals c join median m on (c.year = m.year and c.town = m.town)
)
select IFNULL(c.year, ''),IFNULL(c.town, ''),IFNULL(c.cnt_sales, ''),IFNULL(c.avg_sale_price, ''),IFNULL(c.sale_price_q1, ''),IFNULL(c.median_sale_price, ''),IFNULL(c.sale_price_q3, ''),
IFNULL(c.avg_sales_ratio, ''),IFNULL(c.sales_ratio_q1, ''),IFNULL(c.median_sales_ratio, ''),IFNULL(c.sales_ratio_q3, ''),IFNULL(c.avg_assessed_value, ''),IFNULL(c.assessed_value_q1, ''),
IFNULL(c.median_assessed_value, ''),IFNULL(c.assessed_value_q3, '')
from combined c
INTO OUTFILE '/tmp/cse4705_realestate_summary.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```