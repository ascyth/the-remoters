import pandas as pd
import matplotlib.pyplot as plt

sent_path = 'analysis\data\combined_scored_sentiment_ratings.json'
art_path = 'data_deliverable\data_files\combined_articles.json'
sents = pd.read_json(sent_path)
arts = pd.read_json(art_path)

df = pd.merge(sents, arts, how= 'inner', on= 'ID').reset_index()
df = df[df['METHOD'] == 'roberta_average_sentence_sentiment_conf_scaled']
df['DATE'] = pd.to_datetime(df['DATE'])
yearly_sentiment = df.groupby(pd.Grouper(key='DATE', freq='Y'))['RATING'].mean().reset_index()
print(yearly_sentiment)
# Yearly plot
plt.figure(figsize=(10,5))
plt.bar(yearly_sentiment['DATE'].dt.year, yearly_sentiment['RATING'])
plt.title('Yearly Sentiment Ratings')
plt.xlabel('Year')
plt.ylabel('Sentiment Rating')
plt.show()

monthly_sentiment = df.groupby(df['DATE'].dt.to_period('M'))['RATING'].mean()

# Monthly plot
monthly_sentiment.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Sentiment Rating')
plt.title('Monthly Sentiment Ratings (2020-2023)')
plt.show()

# Calculate rolling mean of sentiment ratings with a 3-month window
rolling_sentiment = df.sort_values('DATE').set_index('DATE')['RATING'].rolling('90D').mean()

# Create a line plot of rolling sentiment ratings
plt.plot(df['DATE'], df['RATING'], label='Raw Data')
plt.plot(rolling_sentiment.index, rolling_sentiment.values, label='Rolling Mean')
plt.xlabel('Date')
plt.ylabel('Sentiment Rating')
plt.title('Rolling Mean Sentiment Ratings (3-Month Window)')
plt.legend()
plt.show()
