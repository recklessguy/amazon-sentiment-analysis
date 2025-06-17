
# 📊 Amazon Product Sentiment Analysis

This project performs **sentiment analysis** on Amazon product reviews using Natural Language Processing (NLP) techniques. It includes data cleaning, exploratory data analysis, sentiment classification, and visualization with word clouds.

> ✅ Ideal for showcasing data analysis and NLP skills on your resume or portfolio.

---

## 🚀 Project Highlights

- Cleaned and preprocessed over **30,000+** Amazon product reviews
- Built a **sentiment labeling** pipeline using review ratings
- Visualized review content using **positive/negative word clouds**
- Exported clean data with sentiment labels for further use

---

## 🔧 Tech Stack

| Tool        | Use                          |
|-------------|-------------------------------|
| Python      | Core programming language     |
| Pandas      | Data wrangling and manipulation |
| Matplotlib & Seaborn | Visualization      |
| WordCloud   | Word cloud generation         |
| VS Code     | Code editor                   |
| Git & GitHub| Version control and hosting   |

---

## 📂 Dataset

This project uses the **`Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv`** dataset.

> ⚠️ **Note:** Due to GitHub's 100MB file size limit, the dataset is not included in this repository.

### 🔽 How to Get the Data:
1. Download the dataset from your original source or trusted platforms like:
   - [Kaggle](https://www.kaggle.com/)
   - [Datafiniti](https://data.world/datafiniti/)
2. Save it in the root directory of the project, at the same level as `main.py`.

---

## 📁 Project Structure

```
amazon-sentiment-analysis/
│
├── main.py                             # Main analysis script
├── cleaned_amazon_reviews_with_sentiment.csv  # Output file with sentiment labels
├── Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv  # Original dataset (not uploaded)
├── requirements.txt                   # Required libraries
├── README.md                          # Project documentation
└── .gitignore                         # Files to ignore during git push
```

---

## 🧪 Key Steps Performed

1. **Loaded and explored** raw review data
2. **Cleaned** text (lowercasing, removing punctuation, stopwords, etc.)
3. **Created sentiment labels** using review rating:
   - Ratings ≥ 4 → Positive
   - Ratings ≤ 2 → Negative
   - Rating = 3 → Neutral (optional)
4. **Generated word clouds** for positive and negative reviews
5. **Exported** cleaned and labeled dataset as CSV

---

## 📈 Visual Output

- **Positive Word Cloud**
- **Negative Word Cloud**

These visualizations reveal the most frequent terms used in each sentiment category, helping to understand customer behavior.

---

## ▶️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/amazon-sentiment-analysis.git
   cd amazon-sentiment-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the dataset in the project folder.

4. Run the script:
   ```bash
   python main.py
   ```

---

## 💡 Future Improvements

- Train a machine learning model to predict sentiment from text
- Deploy using Streamlit or Flask for live prediction
- Integrate other product categories for broader insight

---

## 🧑‍💼 About the Author

**Vishal** – Aspiring Data Analyst with hands-on experience in Python, data wrangling, and storytelling using visualizations.

---

## 📬 Contact

- **LinkedIn**: https://www.linkedin.com/in/vishal-maurya-475981276/

---

## ⭐️ If you found this helpful, give it a star!
