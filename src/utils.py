import pickle
import os


def save_file_as_pickle(name,path):
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"wb") as file:
        pickle.dump(name,file)



def load_pickle_file(path):
    with open(path,"rb") as path:
        return pickle.load(path)