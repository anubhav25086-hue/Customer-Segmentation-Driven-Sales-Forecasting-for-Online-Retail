###################################################################################


#                                                LOADING DATA


###################################################################################
import pandas as pd #for handling dataset
import numpy as np #for mathematical calculations
import matplotlib.pyplot as plt #for making graphs
import seaborn as sns # for Statistical graphs
from google.colab import drive
import pandas as pd

drive.mount('/content/drive')
df = pd.read_excel("/content/drive/MyDrive/Online Retail.xlsx")

print("Dataset loaded successfully!")
