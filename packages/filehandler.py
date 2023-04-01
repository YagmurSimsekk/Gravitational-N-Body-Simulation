from abc import abstractmethod
import h5py
import numpy as np

'''
Class for all file operations
Files in different formats can be saved or read by inheriting the FileHander class
Object is instantianized with the file name

'''

class FileHandler:
    @abstractmethod

    def __init__(self,filename:str):
        self.filename = filename

    def read(data) -> np.array :
        '''This is an abstract method reads data from file and returns it as numpy array'''

    def write(data):
        '''This is an abstract method writes data to a file'''


'''Class for Numpy operations'''
class NumpyFileHandler(FileHandler):
  
    def read(self) -> any:
        with open(self.filename, 'rb') as f:
            data_loaded = np.load(f, allow_pickle=True)
            return data_loaded

    def write(self, _data: np.array):
        with open(self.filename, 'wb') as outfile:
            np.save(outfile, _data)


'''Class for HDF5 operations'''
class HDF5FileHandler(FileHandler):

    def read(self, data: np.array):
        '''Use h5py or numby to save the data as output file'''
        
    def write(self, data: np.array)-> any :
        '''Use h5py or numby to save the data as output file'''
        with h5py.File(self.filename, 'w') as outfile:
            dataset = outfile.create_dataset("init", data=data)
            return outfile


