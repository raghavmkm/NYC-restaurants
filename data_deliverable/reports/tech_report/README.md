1. 
There are about 600 data points in the Kaggle data set and 2500 points in the DOHMH data set. That gives us around 3000 data points in total. For the Kaggle dataset the points are queried from restaurants of all price categories from 1-4 and ratings from 1-5. There is a good mix and match when one looks at the permutations of price and reviews. This is important for us as we want to see if there is any relationship between money and quality of food services being provided. The DOHMH data set has around 200,000 datapoints from which we sampled 2500. The points we sampled we made sure to have them somewhat evenly from all the boroughs. We also made sure there is an even number of critical vs non critical violations so that way our data is split in two. We also made sure the type of violations that were caused were also evenly split whether it be basic sanitation or as bad as roaches. This is the data that existed after removing NaNs and values we didn't want or that were missing. We did this cleaning on a Jupyter notebook and Excel.

We believe this is sufficient data for the analysis we set out to do.

2. 
The identifying attribute for the Kaggle table is name plus address and for the DOHMH table is CAMIS which sort of represents the violation id number.

3. 
We found the data online from various sources. Kaggle is where one of our datasets is form and that is a source that is used by students for several projects, competitions and classes and is one many of us on this team have used several times. The other two datasets are obtained from the city of new york's government websites and one of them is also updated live so we should have no issues with regards to trust on those fronts. All these datasets were downloadable in CSV format and we used pandas library to get dataframes from these CSV files. 
The sample photos for the deliverable that are in the repo are just random. We just took a screenshot where we felt the data was sort of representative enough of the whole field of values that these columns could take. Since we didn't collect the data itself and it was done by professionals we believe they would have taken ample time to make sure there arent biasis like sampling bias and such.
As for considerations, since the data is public and is published by the government we believe it is safe to use for the purposes of this project.

4. 
Since we used professional data when we checked the cleanliness of it we found that most of the values were in the format we expected. In some cases we had missing values, but we just removed the rows where the data was missing or incorrect or in the wrong format and since we had so many data points we could go along with the analysis.

We did. We first parsed our data in excel and used the filter function to remove any values we didn't want, were missing or didn't make sense. Then we got rid of some columns that were excessive. There were some columns that were cool, but did not make a lot of sense to use for the purposes we intended to. We removed null and nan values. Laslty, we noticed that some of the restaurants in consideration were also in new jersey. While we could still consider them, we also added a filter to only show us restaurants in NYC

There are missing values, but since the datasets are so large we can just go ahead with the analysis

There are no duplicates in the data. There are several chains of different restaurants in different parts of the city and while these could be thought of as duplicates, they actually are super important cause they help remove confounding variables and thus the only causal difference would lie in the location and that is exactly what we want to test

The data is normally distributed since we have such a large dataset. Most of the restaurants fall in the middle of price and ratings. There are some that have 1 and 4 for the ratings aspect. It is a similar trend for price. The violations are uniformly distributed. We can safely say the data is not skewed in any one way.

There are no type issues that we have faced while working with this data

We did have to throw away a lot of the raw data. This is simply because the number of data points is so large. 200,000 data points is simply too much for the purposes of this project and handling that much data also saw our laptops crash consistently. We thought around 4 times the minimum of 700 data points should be enough and that is what we are working with.


5. 
The biggest challenege we faced at this step was combining the kaggle and DOHMH datasets. This proved to be very problematic as the keys for both datasets were different. While this is a small set back, we can still carry out our research in the hypothesis we wanted to test. We just will be using separate datasets to arrive at anwers to the questions. We would not need to worry about bias as both are large samples from trusted sources that also give explanations for each of the data points.
