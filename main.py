# Step 1: Import required libraries
import pandas as pd

# Step 2: Load the dataset
file_path = 'Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv'
df = pd.read_csv(file_path)

# Step 3: Preview the data
print("\n✅ First 5 rows of the dataset:")
print(df.head())

# Step 4: Show all columns
print("\n📋 Columns in the dataset:")
print(df.columns)

# Step 5: Check for missing values
print("\n🧹 Missing values per column:")
print(df.isnull().sum())

# Step 6: Basic statistics on ratings
print("\n📊 Review Ratings Summary:")
print(df['reviews.rating'].describe())

# Step 7: Select important columns for sentiment analysis
df = df[['reviews.text', 'reviews.rating']]

# Step 8: Drop rows with missing values
df = df.dropna()

# Step 9: Rename columns for easier access
df = df.rename(columns={'reviews.text': 'review', 'reviews.rating': 'rating'})

# Step 10: Convert ratings to integers (in case they’re floats or strings)
df['rating'] = df['rating'].astype(int)

# Step 11: Show cleaned data preview
print("\n🧼 Cleaned data preview:")
print(df.head())

# Optional: Print shape to see how many reviews are left
print(f"\n📦 Total reviews after cleaning: {df.shape[0]}")

# Step 12: Import VADER for sentiment analysis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (only needed once)
nltk.download('vader_lexicon')

# Step 13: Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Step 14: Apply sentiment scoring
df['sentiment_score'] = df['review'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Step 15: Categorize sentiment based on score
def get_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['sentiment_score'].apply(get_sentiment)

# Step 16: Preview with sentiment added
print("\n🧠 Reviews with Sentiment:")
print(df[['review', 'rating', 'sentiment_score', 'sentiment']].head())

# Step 17: Import matplotlib
import matplotlib.pyplot as plt

# Step 18: Plot sentiment distribution
sentiment_counts = df['sentiment'].value_counts()

plt.figure(figsize=(6, 4))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Step 19: Plot sentiment vs rating (stacked bar chart)
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='rating', hue='sentiment', palette='Set2')
plt.title('Sentiment by Product Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.show()

# Step 20: Create Word Clouds for Positive and Negative Reviews
from wordcloud import WordCloud

# Combine all positive and negative reviews into one string each
positive_text = ' '.join(df[df['sentiment'] == 'Positive']['review'].astype(str))
negative_text = ' '.join(df[df['sentiment'] == 'Negative']['review'].astype(str))

# Generate word clouds
positive_wc = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate(positive_text)
negative_wc = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate(negative_text)

# Plot the Word Clouds
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.imshow(positive_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Reviews Word Cloud')

plt.subplot(1, 2, 2)
plt.imshow(negative_wc, interpolation='bilinear')
plt.axis('off')
plt.title('Negative Reviews Word Cloud')

plt.tight_layout()
plt.show()

# Step 21: Export cleaned and labeled data
df.to_csv('cleaned_amazon_reviews_with_sentiment.csv', index=False)
print("✅ Cleaned data with sentiment labels saved successfully.")


