# Spreadsheet Analysis Report

+ [Raw data downloaded from website](data/exam_score.csv)
+ [Clean data after scrubbing](data/clean_data.csv)
+ [Final version after doing analyze](data/final_version_data.xlsx)

## Data Set Import
+ The data file downloading website is [2013 - 2015 New York State Mathematics Exam by School](https://data.cityofnewyork.us/Education/2013-2015-New-York-State-Mathematics-Exam-by-Schoo/gcvr-n8qw/about_data)

+ The orginal data file is downloaded in CSV format.
+ The data set included the detail information about the New York State Mathematics Exam between 2013 to 2015. 

|DBN|School Name|Grade|Year|Category|Number Tested|Mean Scale Score|# Level 1|% Level 1|# Level 2|% Level 2|# Level 3|% Level 3|# Level 4|% Level 4|# Level 3+4|% Level 3+4|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|01M015|P.S. 015 ROBERTO CLEMENTE|3|2013|All Students|27|278|16|59.3|11|40.7|0|0|0|0|0|0|
|01M015|P.S. 015 ROBERTO CLEMENTE|3|2014|All Students|18|286|6|33.3|9|50|2|11.1|1|5.6|3|16.7|

## Data Set Scrubbing

+ Since the original csv version file is already fit for the excel importing, we only need to finish some one small step during scrubbing. We use python to delete the last two column **# Level 3+4** and **% Level 3+4** in the spreadsheet since our later analysis won't need to use these two column's filtering condition and data. Below is the scrubbing code. 

```
header = data[0]
indices_to_delete = [
    header.index(column_name) for column_name in ["# Level 3+4", "% Level 3+4"]]
for row in data:
    for index in sorted(indices_to_delete, reverse=True):
        del row[index]
```

+ After scrubbing, the table looks like below.

|DBN|School Name|Grade|Year|Category|Number Tested|Mean Scale Score|# Level 1|% Level 1|# Level 2|% Level 2|# Level 3|% Level 3|# Level 4|% Level 4|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|01M015|P.S. 015 ROBERTO CLEMENTE|3|2013|All Students|27|278|16|59.3|11|40.7|0|0|0|0|
|01M015|P.S. 015 ROBERTO CLEMENTE|3|2014|All Students|18|286|6|33.3|9|50|2|11.1|1|5.6|

+ **In the table, there is a list of all the schools in New York State that have mathematics exam records for 2013, 2014, 2015, and each school has its District-Borough-Number (DBN). Different exam will face different grades and student categories. In the table, there is records for the number of tests that has been taken, and the mean scale score. Also, since there is four levels for the exam score, level 1 is the lowest, and level 4 is the highest, in the table, we can see the percentage of each levels and the amount of students in each levels**

## Data Set Analyze

+ On the left side of the table, I created four tables to have a clearer overview of some important data. 

1. The orange table is used to calculate some basic information of the number of students in the test, including the mean number of students taken the test in three years, the max number of students taken the test in three years, and the min number of students taken the test in three years.

2. The yellow table is used to calculate some basic information of the test's mean score, including the mean test score for all the test in these three years, the max test score for all the test in these three years, and the min test score for all the test in these three years.

3. The grey table is used to calculate each year's total amounts of exam that have been taken, for 2013, 2014, and 2015.

4. The blue table is used to calculate the total amount of exam that haven been taken by each grades, from grade 3 to grade 8 individually, and also some applied to all the grades.

+ To make the table more analytical, I create a pivot table for it. With the pivot table, I put Year, School Name, and Category in the filter section, put Grades in the row section, and put Sum of Number Tested, Average of Mean Scale Score, Max of Mean Scale Score, Min of Mean Scale Score, Average of % Level 1, Average of % Level 2, Average of % Level 3, and Average of % Level 4 in the values section. There is also a slicer that used to filter the DBN we want to choose 

+ In this way, people can easily filter out the data they want to grab which fulfill the requirements they set up. For example, in the below table, I choose to grab the exam data from year 2013's WEST PREP ACADEMY school. We can now see the detailed exam data for seperate grades: grade 6, grade 7, and grade 8. We can also see the summarized exam data for grade 6 to grade 8.
   

|Row Labels|	Sum of Number Tested|	Average of Mean Scale Score|Max of Mean Scale Score|Min of Mean Scale Score|	Average of % Level 1|	Average of % Level 2|	Average of % Level 3|	Average of % Level 4|
|---|---|---|----|---|---|---|---|---|
|6|61|	290|	290|	290|	36.1|	50.8|	6.6|	6.6|
|7|	71|	282|	282|	282|	66.2|	25.4|	8.5|	0|
|8|	41|	279|	279|	279|	63.4|	31.7|	4.9	|0|
|Grand Total|	346|	283.75|	290|	279|	55.15|	35.925|	6.725|	2.225|

