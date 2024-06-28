import os
import glob
import numpy as np
from pathlib import Path
import albumentations
from torch.utils.data import Dataset
from taming.data.base import ImagePaths, NumpyPaths, ConcatDatasetWithIndex
import pandas as pd

class CustomBase(Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = None
        self._length = None

    def __len__(self):
        return self._length

    def __getitem__(self, i):
        example = self.data.iloc[i].to_dict()
        return example


class CustomTrain(CustomBase):
    def __init__(self, file_path=None, size=None, training_images_list_file=None):
        super().__init__()
        self.paths=None
        if not file_path:
            with open(training_images_list_file, "r") as f:
                paths = f.read().splitlines()
            self.data = ImagePaths(paths=paths, size=size, random_crop=False)
        else:
            self.image_array = np.load(f'{file_path}train.npz',allow_pickle=True)['arr_0']
            with open(f'{file_path}image_list.txt', "r") as f:
                self.paths = f.read().splitlines()
            self._length = len(self.paths)
            
    def __getitem__(self, i):
        example = dict()
        example['image'] = np.squeeze(self.image_array[i], axis=0)
        example['label'] = self.paths[i]
        return example


class CustomTest(CustomBase):
    def __init__(self, file_path=None, size=None, test_images_list_file=None):
        super().__init__()
        if not file_path:
            paths=None
            with open(test_images_list_file, "r") as f:
                paths = f.read().splitlines()
            self.data = ImagePaths(paths=paths, size=size, random_crop=False)
        else:
            self.image_array = np.load(f'{file_path}test.npz',allow_pickle=True)['arr_0']
            with open(f'{file_path}image_list_test.txt', "r") as f:
                self.paths = f.read().splitlines()
            self._length = len(self.paths)
            
    def __getitem__(self, i):
        example = dict()
        example['image'] = np.squeeze(self.image_array[i], axis=0)
        example['label'] = self.paths[i]
        return example
