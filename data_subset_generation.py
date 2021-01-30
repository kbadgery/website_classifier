# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:02:26 2021

@author: Kip
"""

import pandas as pd

full_dataset = pd.read_csv('URL Classification.csv')                          
unique_classes = list(full_dataset.Category.unique())

def generate_subset(dataset, n_per_class, unique_classes):    
    """
    Takes a larger dataset (as a dataframe) and returns a smaller subset that contains
    "n_per_class" samples from each classification category.
    
    Parameters
    ----------
    dataset : Dataframe
        Larger Dataset to be downsampled.
    n_per_class : Integer
        Number of samples per class to be returned in the downsampled dataset.
    unique_classes : List
        A list of all of the unique classification labels that exist in the dataset

    Returns
    -------
    downsampled_dataset : Dataframe
        The subset of the original dataset.    
    """   
        
    downsampled_dataset = pd.DataFrame(columns=dataset.columns)    

    for category in unique_classes:
        
        category_subset = dataset.loc[dataset['Category'] == category].iloc[:n_per_class]        
        downsampled_dataset = pd.concat([downsampled_dataset, category_subset])
        
    return downsampled_dataset

data_subset = generate_subset(full_dataset.loc[full_dataset['Category'] != 'Adult'], 50, unique_classes)    
data_subset.to_csv('URL classification downsampled.csv')              
