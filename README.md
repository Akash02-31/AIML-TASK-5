# AIML Task 5 — Ensemble Learning & Model Optimization

## 📌 Project Overview

This project demonstrates an end-to-end machine learning classification pipeline using **Ensemble Learning, Random Forest, Gradient Boosting, Hyperparameter Tuning, and Cross-Validation**.

### Dataset

**Breast Cancer Dataset** — Scikit-learn

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook
* Joblib

## 🤖 Models Used

* Logistic Regression
* Random Forest
* Gradient Boosting

## 📊 Model Performance

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------: | --------: | -----: | -------: |
| Logistic Regression |   98.25% |    98.61% | 98.61% |   98.61% |
| Random Forest       |   95.61% |    95.89% | 97.22% |   96.55% |
| Gradient Boosting   |   95.61% |    94.67% | 98.61% |   96.60% |

## ⚙️ Hyperparameter Tuning

**GridSearchCV — Random Forest**

* `n_estimators = 100`
* `max_depth = 5`
* Best CV Score: **96.33%**

## 🔄 Cross-Validation

* Mean CV Accuracy: **94.95%**
* Standard Deviation: **2.56%**

## 📈 Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Cross-Validation
* Feature Importance
* Confusion Matrix

## 📂 Project Structure

```text
AIML_TASK5/
├── models/
│   └── best_model.pkl
├── outputs/
├── task5_ensemble_learning.ipynb
├── predict.py
├── model_results.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## ▶️ Run the Project

```bash
git clone <YOUR-REPOSITORY-URL>
cd AIML_TASK5
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

Open `task5_ensemble_learning.ipynb` in VS Code/Jupyter and run all cells.

## 🏆 Conclusion

The project successfully demonstrates **model comparison, ensemble learning, hyperparameter optimization, and cross-validation**. Logistic Regression achieved the highest test-set performance in this experiment, while Random Forest was optimized using GridSearchCV.

---


