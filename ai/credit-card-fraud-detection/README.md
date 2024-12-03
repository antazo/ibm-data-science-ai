# Credit Card Fraud Detection

This final project will be developed using **VSCode**, with a dedicated **virtual environment** for package management. The primary reason for this setup is the use of **TensorFlow** to train a neural network model. Since TensorFlow is officially released on PyPI, it requires the latest stable version of `pip` for seamless installation and compatibility.

The installation process, along with detailed setup instructions, will be documented in this README file to ensure reproducibility and ease of use.

## Language and Reference

Although the Certificate Program was originally conducted in Spanish, I have chosen to complete this final project in English. For context and reference, relevant sections will include links to the original Spanish materials.

## Installation

Clone (or fork) this repository:

```bash
git clone https://github.com/antazo/ibm-data-science-ai
cd ibm-data-science-ai
```

## Virtual environment

We invoke the `venv` module to create our environment, then activate it. In my case, I'm calling it `myenv`:

```bash
python3 -m venv myvenv
source ./myvenv/bin/activate
# On Windows:
#.\myvenv\Scripts\activate
```

## Packages

```bash
cd ai/credit-card-fraud-detection/
pip install -r requirements.txt
```

This will install the following packages in our virtual environment:

* pandas, numpy, matplotlib, seaborn.
* **scikit-learn**: To train different Models (Support Vector Classifier, Random Forest Classifier, Logistic Regression).
* **tensorflow**: To try a Neural Network Model (without **CUDA** support).
* **torch**: To try a Neural Network Model with PyTorch (no **CUDA**).
* **xgboost**: To try a Gradient Boosting Model.

## Dataset

Download the needed dataset from here: <https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud>, and place the `creditcard.csv` in the `ai/credit-card-fraud-detection/dataset` folder.

## Models

The specified times may vary, I've been training the Models in this repository using an average 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz.
