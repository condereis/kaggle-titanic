import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import json
import numpy as np
import os
import pandas as pd
import pickle


def get_paths():
    root = path.dirname(path.dirname(path.abspath(__file__)))
    paths = json.loads(open(os.path.join(root, 'SETTINGS.json')).read())
    for key in paths:
        paths[key] = os.path.expandvars(paths[key])
    paths['root'] = root
    return paths

def get_train_df():
    train_path = get_paths()["train_data_path"]
    root_path = get_paths()["root"]
    return pd.read_csv(os.path.join(root_path, train_path))

def get_test_df():
    test_path = get_paths()["test_data_path"]
    root_path = get_paths()["root"]
    return pd.read_csv(os.path.join(root_path, test_path))

def save_model(model, name='model.pkl'):
    model_dir = get_paths()["models_dir"]
    root_path = get_paths()["root"]
    pickle.dump(model, open(os.path.join(root_path, model_dir, name), 'wb'))

def load_model(name='model.pkl'):
    model_dir = get_paths()["models_dir"]
    root_path = get_paths()["root"]
    return pickle.load(open(os.path.join(root_path, model_dir, name), 'rb'))