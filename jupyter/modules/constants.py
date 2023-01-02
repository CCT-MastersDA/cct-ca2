"""
constants.py

This file contains the constants used in the Jupyter notebooks of this project.

They are defined in a separate file to avoid code duplicate and for easier reference.
"""
# importing modules
import os
import warnings
from pathlib import Path
from os.path import isfile, join, abspath

# path to the users directory
HOME_DIR = str(Path.home())

# path to the current directory
CURR_PATH = abspath(os.getcwd())

# path to input dataset folder
DATASETS_FOLDER = join(CURR_PATH, 'datasets')

# path to the images folder
IMAGES_FOLDER = join(CURR_PATH, 'images')

# path to output dataset folder
DATA_PREP_FOLDER = join(DATASETS_FOLDER, 'dataprep')

# path to store collected tweets
TWEETS_DIR = join(DATASETS_FOLDER, 'tweets-online')

# input/output dataset names
ORG_FARM_DATASET = 'eurostat-organic-farming.csv'
ORG_FARM_DATASET_IRE = 'eurostat-organic-farming_ire.csv'

IMP_EXP_DATASET = 'fao-import-export-eu.csv'
IMP_EXP_DATASET_VAL = 'fao-import-export-eu-val.csv'
IMP_EXP_DATASET_VAL_AVG = 'fao-import-export-eu-val-avg.csv'
IMP_EXP_DATASET_QTT = 'fao-import-export-eu-qtt.csv'
IMP_EXP_DATASET_QTT_AVG = 'fao-import-export-eu-qtt-avg.csv'
IMP_EXP_DATASET_TOP10_QTT = 'fao-import-export-eu-top10-qtt.csv'
IMP_EXP_DATASET_TOP10_VAL = 'fao-import-export-eu-top10-val.csv'

FOOD_INF_DATASET = 'fao-food-inflation-eu.csv'
FOOD_INF_DATASET_AVG = 'fao-food-inflation-eu-avg.csv'

TWEETS_DATASET = 'tapi-agri-tweets.csv'
TWEETS_DF_FILE = 'tweets_df'

# twitter env file
TWITTER_ENV_FILE = '.twitter_env'

# images names
GRAPH_IMP_EXP_QTT = 'imp-exp-qtt-year.png'
GRAPH_IMP_EXP_VAL = 'imp-exp-val-year.png'
GRAPH_FOOD_PRICE_INF = 'food-price-inf-year.png'

# ignore warnings
warnings.filterwarnings('ignore')