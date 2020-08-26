# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:31:39 2020

@author: LIN CHUAN
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
from sklearn import datasets
from fancyimpute import KNN
from fancyimpute import IterativeImputer

# Contamination of dataset
dataset = pd.read_csv("G:/1/original_part_dataset_polyrandom.csv")
original_dataset = dataset
contamination_array = np.random.binomial(1, 0.1, dataset.shape).astype(bool) # 10 percentage = 0.1, 20 percentage = 0.2
contamination_array[:,0] = False
dataset[contamination_array] = np.nan
contaminated_dataset = dataset
contaminated_dataset.to_csv("1.Contaminated_part_dataset_80%.csv")

# Visualization of missing data
msno.matrix(contaminated_dataset, labels=True)

# Data imputation by List-wise delection
Listwise_dataset = dataset.dropna(axis=0)
Listwise_dataset.to_csv("2.Listwise_part_dataset_80%.csv")

# Data imputataion by Mean filling
Mean_dataset = dataset.fillna(dataset.mean())
Mean_dataset.to_csv("3.Mean_part_dataset_80%.csv")

# Data imputataion by KNN
KNN_pre_processing_dataset = contaminated_dataset.iloc[:,1:]
KNN_part1 = contaminated_dataset.iloc[:,:1]
KNN_part1_df = pd.DataFrame(KNN_part1)
KNN_dataset = KNN(k=6).fit_transform(KNN_pre_processing_dataset)
KNN_dataset_output = pd.DataFrame(KNN_dataset)
KNN_dataset_output.columns = ['Check_A_Part_Price','Check_B_Part_Price','Check_C_Part_Price']

KNN_finalout = KNN_part1_df.join(KNN_dataset_output)
KNN_finalout.to_csv("4.KNN_part_dataset_80%.csv")

# Data imputataion by IterativeImputer
II_pre_processing_dataset = contaminated_dataset.iloc[:,1:]
II_part1 = contaminated_dataset.iloc[:,:1]
II_part1_df = pd.DataFrame(II_part1)
II_dataset = IterativeImputer().fit_transform(II_pre_processing_dataset)
II_dataset_output = pd.DataFrame(II_dataset)
II_dataset_output.columns = ['Check_A_Part_Price','Check_B_Part_Price','Check_C_Part_Price']
II_finalout = II_part1_df.join(II_dataset_output)
II_finalout.to_csv("5.II_part_dataset_80%.csv")

# Calculation of check price after different data imputation methods

print("Calculation for Listwise")
print("Listwise_A319_Check_A_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A319'].iloc[:,1])/0.8)
print("Listwise_A319_Check_B_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A319'].iloc[:,2])/0.8)
print("Listwise_A319_Check_C_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A319'].iloc[:,3])/0.8)
print("Listwise_A320_Check_A_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A320'].iloc[:,1])/0.8)
print("Listwise_A320_Check_B_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A320'].iloc[:,2])/0.8)
print("Listwise_A320_Check_C_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A320'].iloc[:,3])/0.8)
print("Listwise_A321_Check_A_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A321'].iloc[:,1])/0.8)
print("Listwise_A321_Check_B_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A321'].iloc[:,2])/0.8)
print("Listwise_A321_Check_C_cost:", np.sum(Listwise_dataset.loc[Listwise_dataset.Aircraft_Type == 'A321'].iloc[:,3])/0.8)
print("--------------------------------------------------------------------------------------------------------")
print("Calculation for MeanFilling")
print("Mean_A319_Check_A_cost:", np.sum(Mean_dataset.iloc[:1000,1])/0.8)
print("Mean_A319_Check_B_cost:", np.sum(Mean_dataset.iloc[:1000,2])/0.8)
print("Mean_A319_Check_C_cost:", np.sum(Mean_dataset.iloc[:1000,3])/0.8)
print("Mean_A320_Check_A_cost:", np.sum(Mean_dataset.iloc[1000:2000,1])/0.8)
print("Mean_A320_Check_B_cost:", np.sum(Mean_dataset.iloc[1000:2000,2])/0.8)
print("Mean_A320_Check_C_cost:", np.sum(Mean_dataset.iloc[1000:2000,3])/0.8)
print("Mean_A321_Check_A_cost:", np.sum(Mean_dataset.iloc[2000:3000,1])/0.8)
print("Mean_A321_Check_B_cost:", np.sum(Mean_dataset.iloc[2000:3000,2])/0.8)
print("Mean_A321_Check_C_cost:", np.sum(Mean_dataset.iloc[2000:3000,3])/0.8)
print("--------------------------------------------------------------------------------------------------------")
print("Calculation for KNN")
print("KNN_A319_Check_A_cost:", np.sum(KNN_finalout.iloc[:1000,1])/0.8)
print("KNN_A319_Check_B_cost:", np.sum(KNN_finalout.iloc[:1000,2])/0.8)
print("KNN_A319_Check_C_cost:", np.sum(KNN_finalout.iloc[:1000,3])/0.8)
print("KNN_A320_Check_A_cost:", np.sum(KNN_finalout.iloc[1000:2000,1])/0.8)
print("KNN_A320_Check_B_cost:", np.sum(KNN_finalout.iloc[1000:2000,2])/0.8)
print("KNN_A320_Check_C_cost:", np.sum(KNN_finalout.iloc[1000:2000,3])/0.8)
print("KNN_A321_Check_A_cost:", np.sum(KNN_finalout.iloc[2000:3000,1])/0.8)
print("KNN_A321_Check_B_cost:", np.sum(KNN_finalout.iloc[2000:3000,2])/0.8)
print("KNN_A321_Check_C_cost:", np.sum(KNN_finalout.iloc[2000:3000,3])/0.8)
print("--------------------------------------------------------------------------------------------------------")
print("Calculation for II")
print("II_A319_Check_A_cost:", np.sum(II_finalout.iloc[:1000,1])/0.8)
print("II_A319_Check_B_cost:", np.sum(II_finalout.iloc[:1000,2])/0.8)
print("II_A319_Check_C_cost:", np.sum(II_finalout.iloc[:1000,3])/0.8)
print("II_A320_Check_A_cost:", np.sum(II_finalout.iloc[1000:2000,1])/0.8)
print("II_A320_Check_B_cost:", np.sum(II_finalout.iloc[1000:2000,2])/0.8)
print("II_A320_Check_C_cost:", np.sum(II_finalout.iloc[1000:2000,3])/0.8)
print("II_A321_Check_A_cost:", np.sum(II_finalout.iloc[2000:3000,1])/0.8)
print("II_A321_Check_B_cost:", np.sum(II_finalout.iloc[2000:3000,2])/0.8)
print("II_A321_Check_C_cost:", np.sum(II_finalout.iloc[2000:3000,3])/0.8)