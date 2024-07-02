import pickle
import os


def save_file_as_pickle(name,path):
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"wb") as file:
        pickle.dump(name,file)