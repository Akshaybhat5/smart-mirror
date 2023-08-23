import pandas as pd
import os
import random

DATA_PATH = os.path.join("affirmations_dataset_cleaned.csv")

def load_data(data_path = DATA_PATH):
    return pd.read_csv(data_path)

data = load_data()

def get_affirmations(DATA_PATH, text):
    for tags in data['Tag']:
        if text == "neutral" and tags == "beauty":
            affir = (data['Affirmation'])
            
        elif text == "blessing" and tags == "blessing":
            affir = (data['Affirmation'])
            
        elif text == "happy" and tags == "gratitude":
            affir = (data['Affirmation'])
            
        elif text == "sad" and tags == "spiritual":
            affir = (data['Affirmation'])
            
        elif text == "love" and tags == "love":
            affir = (data['Affirmation'])
            
        elif text == "happy" and tags == "happiness":
            affir = (data['Affirmation'])
            
        else:
            affir = (data['Affirmation'])
    return (random.choice(affir))
    