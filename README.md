# 💎 Diamond Price Analysis & Prediction

This project predicts **diamond prices** using **machine learning models** based on physical and quality attributes such as carat, cut, color, clarity, and dimensions.  
The project also includes a **Streamlit web application** for real-time price prediction.

---

**Project is live at:** https://diamond-price-analysis-afjjg4hc5hsqktt6xuxtwx.streamlit.app/

---

## 🎯 Problem Statement

Diamond prices depend on multiple factors and are difficult to estimate manually.  
This project uses machine learning to analyze these factors and predict diamond prices accurately.

---

## 🧠 Machine Learning Approach

- Data preprocessing & cleaning
- Encoding categorical features
- Feature scaling
- Model training:
  - Linear Regression
  - Random Forest Regressor
- Model evaluation

---

## 📊 Features Used

- **Carat** - Weight of the diamond
- **Cut** - Quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- **Color** - Diamond color grade (D to J)
- **Clarity** - Clarity grade (IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1)
- **Depth** - Total depth percentage
- **Table** - Width of top of diamond relative to widest point
- **Dimensions** - Length (x), width (y), and depth (z) in mm

---

## 🚀 Streamlit App

The Streamlit app allows users to:
- Enter diamond properties through an intuitive interface
- Get instant price predictions using trained ML models
- View prediction confidence and model performance metrics

---

## 🛠️ Tech Stack

- **Python** - Core programming language
- **Pandas & NumPy** - Data manipulation and analysis
- **Scikit-learn** - Machine learning models and preprocessing
- **Streamlit** - Web application framework
- **Matplotlib & Seaborn** - Data visualization

---

## 📁 Project Structure

```
diamond-price-analysis/
│
├── data/
│   └── diamonds.csv                 # Dataset
│
├── notebooks/
│   └── diamond_analysis.ipynb       # Exploratory data analysis
│
├── models/
│   ├── model.pkl                    # Trained model
│   └── scaler.pkl                   # Feature scaler
│
├── app.py                           # Streamlit application
├── train_model.py                   # Model training script
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 📥 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/diamond-price-analysis.git
cd diamond-price-analysis
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 🎓 Usage

### Training the Model

To retrain the model with your own data:

```bash
python train_model.py
```

### Using the Web App

1. Open the Streamlit app
2. Enter diamond characteristics:
   - Carat weight
   - Cut quality
   - Color grade
   - Clarity grade
   - Depth percentage
   - Table percentage
   - Dimensions (x, y, z)
3. Click "Predict Price"
4. View the estimated price

---

## 📈 Model Performance

| Model | R² Score | RMSE | MAE |
|-------|----------|------|-----|
| Linear Regression | 0.XX | $XXX | $XXX |
| Random Forest | 0.XX | $XXX | $XXX |

*(Update with your actual metrics)*

---

## 📊 Dataset

The dataset contains information about diamonds including:
- Nearly 54,000 diamonds
- 10 features (carat, cut, color, clarity, depth, table, price, x, y, z)
- Price range: $326 to $18,823

**Source:** [Specify your data source]

---

## 🔍 Key Insights

- Carat weight has the strongest correlation with price
- Cut quality significantly impacts price for similar carat weights
- Color and clarity grades show moderate correlation with price
- Dimensions (x, y, z) are highly correlated with carat weight

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---



---



---


---

**⭐ If you found this project helpful, please consider giving it a star!**
