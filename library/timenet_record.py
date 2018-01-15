# libraries
import numpy as np
import pickle

class TimeNetRecord:
    def __init__(
            self, # the class itself
            record_data=None, # the data for that record
            channel_names=[], # channel names
            meta_data={}, # the meta data
            annotations={'start_indexes': [], 'end_indexes': [], 'annotations': []}, # annotations: list of start_indexes, end_indexes, and labels
    ):
        self.record_data = record_data
        self.channel_names = channel_names
        self.meta_data = meta_data
        self.annotations = annotations

    def save(self, file_path):
        with open(file_path+'.pkl', 'wb') as fid:
            pickle.dump(self, fid)





