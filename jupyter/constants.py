"""
Constants.py

This file contains the constants defined in this project.

They are defined in a separate file to avoid code duplicate and for easier reference.
"""
import os
import warnings
from os.path import isfile, join, abspath

# path to the current directory
CURR_PATH = abspath(os.getcwd())

# path to input dataset folder
DATASETS_FOLDER = join(CURR_PATH, 'datasets')

# path to the images folder
IMAGES_FOLDER = join(CURR_PATH, 'images')

# path to output dataset folder
DATA_PREP_FOLDER = join(DATASETS_FOLDER, 'dataprep')

# input/output dataset names
ORG_FARM_DATASET = 'organic-farming.csv'
ORG_FARM_DATASET_IRE = 'organic-farming_ire.csv'
IMP_EXP_DATASET = 'fao-import-export-eu.csv'
IMP_EXP_DATASET_VAL = 'fao-import-export-eu-val.csv'
IMP_EXP_DATASET_QTT = 'fao-import-export-eu-qtt.csv'
IMP_EXP_DATASET_TOP10_QTT = 'fao-import-export-eu-top10-qtt.csv'
IMP_EXP_DATASET_TOP10_VAL = 'fao-import-export-eu-top10-val.csv'
FOOD_INF_DATASET = 'fao-food-inflation-eu.csv'
FOOD_INF_DATASET_AVG = 'fao-food-inflation-eu-avg.csv'

# images names
GRAPH_IMP_EXP_QTT = 'imp-exp-qtt-year.png'
GRAPH_IMP_EXP_VAL = 'imp-exp-val-year.png'
GRAPH_FOOD_PRICE_INF = 'food-price-inf-year.png'

warnings.filterwarnings('ignore')