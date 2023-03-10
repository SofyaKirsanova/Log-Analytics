# часто используемые бибилиотеки
import numpy as np


# управление файлами
import os
# import easygui
from shutil import rmtree
import pandas as pd
import csv
from pandas.core.groupby.generic import DataFrameGroupBy


# предобработка
from sklearn import preprocessing


# наборы данных
from sklearn.model_selection import train_test_split


# машинное обучение
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation


# обработка естественного языка
import nltk
from gensim.models import Word2Vec

# визуализация
import matplotlib

# метрики
from sklearn.metrics import roc_auc_score

# собственные модули
# from code.core.file_config import *

# os.chdir(r'../..') # установка рабочей директории
output_dir = 'tmp_data' # выбор директории для сохранения данных в формате .csv

# спесификация датасета
input_file = '../data/HDFS_small.txt' # выбор файла с данными
columns = [0, 1, 2] # выбор столбцов для удаления
