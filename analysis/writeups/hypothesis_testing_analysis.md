# Hypothesis Testing Analysis

Provide a description of the result and adequate complementary information describing and motivating your process:
Why did you use this statistical test? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?
What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?`

## Hypothesis 1: Work from home has received an increasingly positive sentiment in recent years (2020 - 2023)

## Hypothesis 2: Sentiments regarding work from home are differrent in news source articles compared to in Reddit posts.


2 Sample T-Test: Reddit Sentiments vs. Article (NYT & The Guardian) Sentiments

tstats:  -1.3343817237423585
pvalue:  0.18234339804003583
 
## Hypothesis 3: Sentiments regarding work from home are differrent in The Gaurdian articles compared to in The New York Times articles.


2 Sample T-Test: The Guardian Sentiments vs. NYT Sentiments

tstats:  -0.18621426018881315
pvalue:  0.8523396810379122

## Hypothesis 4: Sentiments regarding work from home are not different in the ExperiencedDevs and csCareerQuestions subreddits.

2 Sample T-Test: Reddit ExperiencedDevs Subreddit Sentiments vs. csCareerQuestions Subreddit Sentiments

tstats:  -1.3413360299554022
pvalue:  0.18036903120534806
