Laptop Price Prediction System
----------------
📌 DESCRIPTION:
---------------
This is a machine learning web application built using Streamlit that predicts the price of a laptop based on various user inputs such as company, RAM, screen size, CPU brand, etc.

The model is trained on a dataset of laptop specifications and prices. It uses a preprocessed pipeline (saved as pipe.pkl) and a dataframe (df.pkl) for user inputs.

💡 KEY FEATURES:
----------------
✔ Predicts laptop price instantly  
✔ Intuitive and user-friendly interface using Streamlit  
✔ Uses machine learning regression pipeline  
✔ Converts screen resolution to PPI for better accuracy  
✔ Supports various hardware and OS configurations  

📦 FILES INCLUDED:
------------------
- `app.py`: Main Streamlit app file  
- `df.pkl`: Preprocessed dataframe with unique values for dropdowns  
- `pipe.pkl`: Trained machine learning pipeline  
- `README.txt`: Project documentation  

🔧 REQUIREMENTS:
----------------
- Python 3.7+
- Required Libraries:
    - streamlit
    - numpy
    - pandas
    - pickle
    - math


🚀 HOW TO RUN:
--------------
1. Make sure all files (`app.py`, `df.pkl`, `pipe.pkl`) are in the same directory.
2. Activate your virtual environment if you have one.
3. Run the app using:


🧠 MACHINE LEARNING MODEL:
---------------------------
- Preprocessing: Label encoding, feature engineering (e.g. PPI calculation from resolution and screen size)
- Model Type: Regression
- Training Libraries: scikit-learn (saved pipeline using pickle)

📌 NOTES:
---------
- The model uses log-transformed price values for training. The prediction is exponentiated and rounded to get the actual price.
- You should only enter realistic screen sizes (> 0) to avoid division errors in PPI calculation.
