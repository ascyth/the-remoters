# Reddit, NYTimes, Guardian Articles
ARTICLE ID: A unique identifier for each article. Ranging in length from 8 to 32 characters, each value is distinct from others. No default value. Can include alphanumeric characters as well as underscores and other special characters. We will double check in our analysis that each identifier is unique to ensure we don’t have duplicate records. This is a required value. We don’t think this contains sensitive information.

URL: A link to where the article is hosted on its respective source. A string containing alphanumeric as well as special characters. No default value. Each URL should be unique from other articles; we will check this in our analysis. We don’t think this contains sensitive information. We do not plan on using this as part of our main analysis, but rather as a sanity check to ensure distinct datapoints. 

DATE: A 12-digit numeric value representing the date in which the article was published. Defaults to 1970-01-01 but ranges up to the present date. Most popular values are within the previous 5 years (2018-2023). The values are not guaranteed to be unique from one another since some articles were published at the same time even though they are distinct from one another. We will use this value as a metric in our analysis to determine how work-from-home sentiments have changed over the years. Required value. 

PLAIN_TEXT: The bulk of the data we will be using in our analysis. A long string of text that has been cleaned to contain only alphanumeric characters. Variable range and contents, but is related to the ‘remote work’ keyword. Words within the PLAIN_TEXT can be repeated but PLAIN_TEXTs should not be duplicates of other PLAIN_TEXTs. Required value. 

SOURCE: The source of the Article. Either Reddit, the Guardian, or the New York Times. Required value, and the range is between these three values listed. No default value. 295 from the Guardian, 646 from Reddit, _ from NYT. 

# Reddit Sentiment
ARTICLE ID: Links back to the Reddit Article’s ID in the ‘Articles’ data. Optional field as not all Articles come from Reddit. 

METHOD: Optional field as not all Articles come from Reddit. Default is ‘post’.  

RATING: The total number of upvotes a post has received. Used to measure traction and popularity amongst certain ideas. Optional field as not all Articles come from Reddit. Default is ‘0’. Numeric positive integer. 
