# Credit Card Fraud Detection

This final project is going to be done under VSCode, using a virtual environment. The installation process will be also documented on this README file.

The Certificate Program was initially in Spanish, but I decided to do the final project in English, so there will be links pointing to the original source for reference.

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
cd ai\credit-card-fraud-detection\
pip install -r requirements.txt
```

## Dataset

Download the needed dataset from here: <https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud>, and place the `creditcard.csv` in the `ai\credit-card-fraud-detection\dataset` folder.
