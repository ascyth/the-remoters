# Hypothesis Testing Analysis

Provide a description of the result and adequate complementary information describing and motivating your process:
Why did you use this statistical test? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?
What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?`

## Hypothesis 1: Work from home has received an increasingly positive sentiment in recent years (2020 - 2023)

## Hypothesis 2: Sentiments regarding work from home are differrent in news source articles compared to in Reddit posts.


2 Sample T-Test: Reddit Sentiments vs. Article (NYT & The Guardian) Sentiments

tstats:  -1.3343817237423585
pvalue:  0.18234339804003583
 
 For the first test, the null hypothesis would be that there is no difference in sentiments between Reddit and article (NYT and The Guardian) sentiments. The t-statistic is -1.334 and the p-value is 0.182, which indicates that we fail to reject the null hypothesis. This means that there is no statistically significant difference in sentiments between Reddit and article sentiments.



## Hypothesis 3: Sentiments regarding work from home are differrent in The Gaurdian articles compared to in The New York Times articles.


2 Sample T-Test: The Guardian Sentiments vs. NYT Sentiments

tstats:  -0.18621426018881315
pvalue:  0.8523396810379122

For the second test, the null hypothesis would be that there is no difference in sentiments between The Guardian and NYT sentiments. The t-statistic is -0.186 and the p-value is 0.852, which also indicates that we fail to reject the null hypothesis. This means that there is no statistically significant difference in sentiments between The Guardian and NYT sentiments.


## Hypothesis 4: Sentiments regarding work from home are not different in the ExperiencedDevs and csCareerQuestions subreddits.

2 Sample T-Test: Reddit ExperiencedDevs Subreddit Sentiments vs. csCareerQuestions Subreddit Sentiments

tstats:  -1.3413360299554022
pvalue:  0.18036903120534806

For the third test, the null hypothesis would be that there is no difference in sentiments between ExperiencedDevs and csCareerQuestions subreddits. The t-statistic is -1.341 and the p-value is 0.180, which again indicates that we fail to reject the null hypothesis. However, the p-value is close to the significance level of 0.05, which suggests that there may be a possible difference in sentiments between the two subreddits.

