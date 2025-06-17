
# 🛍️ Amazon Product Review Sentiment Analysis

This project performs **sentiment analysis** on Amazon consumer product reviews using Natural Language Processing (NLP) techniques. The goal is to understand customer feedback by classifying reviews as **positive, negative, or neutral**, and uncover patterns between sentiment and product ratings.

> 🔍 Ideal for showcasing data science and NLP skills in interviews or on your resume.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Results](#results)
- [Sample Visualizations](#sample-visualizations)
- [License](#license)

---

## 📖 Overview

With the growth of e-commerce, businesses rely on customer reviews for feedback. This project analyzes such reviews using Python NLP tools to:
- Clean and preprocess raw text
- Perform sentiment scoring (using TextBlob)
- Visualize polarity and subjectivity
- Correlate sentiment with star ratings

---

## 📂 Dataset

- **Source**: [Datafiniti Amazon Consumer Reviews Dataset](https://data.world/datafiniti/amazon-product-reviews)
- **File**: `Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv`
- **Note**: The full dataset is excluded from this repo due to size constraints. A sample file can be used for testing.

---

## ⚙️ Technologies Used

| Tool/Library      | Purpose                          |
|------------------|----------------------------------|
| Python           | Core programming language        |
| Pandas           | Data loading and manipulation    |
| TextBlob         | Sentiment analysis (NLP)         |
| Matplotlib       | Visualization                    |
| Seaborn          | Enhanced plots and styling       |
| re (Regex)       | Text cleaning                    |
| Jupyter / VS Code| Development and testing          |

---

## 📁 Project Structure

```plaintext
amazon-sentiment-analysis/
├── data/                             # Raw or sample data files (not committed)
├── main.py                          # Main sentiment analysis script
├── cleaned_amazon_reviews.csv       # Processed data file (optional)
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── .gitignore                       # Files/folders ignored by Git
└── sample_outputs/                  # (Optional) Saved plots or results
```

---

## ▶️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/recklessguy/amazon-sentiment-analysis.git
   cd amazon-sentiment-analysis
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script:**
   ```bash
   python main.py
   ```

> 💡 Tip: Use a Jupyter notebook for interactive exploration (optional).

---

## 📊 Results

- Reviews are classified as **Positive**, **Negative**, or **Neutral** based on polarity score.
- Average polarity and subjectivity by star rating are calculated.
- Cleaned and labeled data can be used for further machine learning or dashboarding.

---

## 🖼️ Sample Visualizations

> *(Add the following after generating plots in your script)*

- **Sentiment Distribution Pie Chart**
- **Subjectivity vs. Polarity Scatter Plot**
- **Average Polarity by Star Rating (Bar Plot)**

> 🧩 Feel free to save these in an `/images` folder and embed here.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Vishal**  
💼 [LinkedIn Profile (Add your URL here)](https://linkedin.com/)  
📧 [Your Email (Optional)]  

---

## ⭐ Highlights for Resume

```
• Built an NLP-based sentiment analysis pipeline to classify 30,000+ Amazon reviews into positive, neutral, or negative classes using TextBlob.
• Applied text cleaning, polarity scoring, and subjectivity analysis to uncover patterns in customer sentiment and product ratings.
• Visualized insights through matplotlib and seaborn to support data-driven business decisions.
```
