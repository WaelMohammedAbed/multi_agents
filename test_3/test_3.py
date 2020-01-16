# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 18:41:19 2020

@author: Wael Abed
"""
import numpy as np
import pandas as pd 

# ------------------------------------------------ list of voting functions
def bordaCount(data):
    cols_sum=data.sum(axis = 0, skipna = True)
    cols_max_sum=cols_sum.max()
    print("----------Borda Count result------")
    print(" columns header =",data.columns.values)
    print("sum of all cols = ",cols_sum.values)
    print("max sum for col = ",cols_max_sum)
    print("name of the max sum  col = ",data.columns[cols_sum.values.tolist().index(cols_max_sum)])
    print("order of the max sum of col = ",cols_sum.values.tolist().index(cols_max_sum)+1)
    print("----------------------------------")

#--------------------- Pairwise Comparison
def comparePairs(row,index):
    count=0
    for value in row:
        if(row[index]>value):
            count=count+1
    return count
def sumPairscol(column,data,col_index):
    count=0
    for i in range(len(column)):
        count=count+comparePairs(data[i],col_index)
    return count
        
    
    
def pairwiseComparison(df):
    data=df.values
    sumPairs=[]
    col_index=0
    for column in data.T:
        sumPairs.append(sumPairscol(column,data,col_index))
        col_index+=1
    print("----------Pairwise Comparison result------")
    print(" columns header =",df.columns.values)
    print("sum of all cols = ",sumPairs)
    print("max sum for col = ",max(sumPairs))
    print("name of the max sum  col = ",df.columns[sumPairs.index(max(sumPairs))])
    print("order of the max sum of col = ",sumPairs.index(max(sumPairs))+1)
    print("----------------------------------")

#----------------Plurality Vote-------------------------
def countMaxInCOl(column,maxValue):
    count=0
    for i in range(len(column)):
        if(column[i]==maxValue):
            count+=1
    return count
def pluralityVote(df):
    data=df.values
    countMaxValues=[]
    for column in data.T:
        countMaxValues.append(countMaxInCOl(column,data.max()))
    print("----------Plurality Vote result------")
    print(" columns header =",df.columns.values)
    print("sum of all cols = ",countMaxValues)
    print("max sum for col = ",max(countMaxValues))
    print("name of the max sum  col = ",df.columns[countMaxValues.index(max(countMaxValues))])
    print("order of the max sum of col = ",countMaxValues.index(max(countMaxValues))+1)
    print("----------------------------------")

#-------------------Runoff -----------------------------
def updateRow(row,index):
    for i in range(len(row)):
        if(row[index]>row[i]):
            row[i]+=1
    return row
def updateCol(column,data,col_index):
    for i in range(len(column)):
        data[i]=updateRow(data[i],col_index)
    return data

def pluralityVoteTwo(df,roundNo):
    data=df.values
    countMaxValues=[]
    for column in data.T:
        countMaxValues.append(countMaxInCOl(column,data.max()))
    print("----------Runoff result Round ",roundNo," ------")
    print(" columns header =",df.columns.values)
    print("sum of all cols = ",countMaxValues)
    print("min sum for col = ",min(countMaxValues))
    return countMaxValues.index(min(countMaxValues))
    
def runoff(df,roundNo=0):
    data=df.values
    if(data.shape[1]>2):
        min_col_index=pluralityVoteTwo(df,roundNo)
        columns=data.T
        data=updateCol(columns[min_col_index],data,min_col_index)
        df = pd.DataFrame(data, index=df.index, columns=df.columns)
        df.drop(df.columns[min_col_index],axis=1,inplace=True)
        #data = np.delete(data, min_col_index, 1)
        runoff(df,roundNo+1)
    else:
        countMaxValues=[]
        for column in data.T:
            countMaxValues.append(countMaxInCOl(column,data.max()))
        print("---------- Runoff result------")
        print(" columns header =",df.columns.values)
        print("sum of all cols = ",countMaxValues)
        print("max sum for col = ",max(countMaxValues))
        print("name of the max sum  col = ",df.columns[countMaxValues.index(max(countMaxValues))])
        print("order of the max sum of col = ",countMaxValues.index(max(countMaxValues))+1)
        print("----------------------------------")
    
#---------------------------------------------- end functions 

data = pd.read_csv("test_3.csv") 
bordaCount(data)
pairwiseComparison(data)
pluralityVote(data)
runoff(data)


