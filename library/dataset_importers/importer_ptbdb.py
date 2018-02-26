"""
Importer - MITBIH
"""

# libraries
import numpy as np
import os
import sys
import pickle
import wfdb
import pdb
from library.timenet_record import TimeNetRecord
import urllib.request
# download and save the original data into the temporary folder


def download_the_original(parameters):

    # clean the data folder
    os.system('rm ' + parameters['path_to_database'] + '*.pkl')
    counter = 1
    records = urllib.request.urlopen('https://www.physionet.org/physiobank/database/ptbdb/RECORDS').readlines()

    # for each possible patient number we have to check
    # whether we have any data in the online repository
    for i in range(len(records)):
        record_row = records[i].decode("utf-8").rstrip().split('/')
        if record_row[1][-1] == '\n':
            record_row[1] = record_row[1][:-1]
        ecg_record = wfdb.rdsamp(record_row[1], channels=None, physical=True, pbdir='ptbdb/' + record_row[0] + '/',
                                 m2s=False)
        ecg_X = ecg_record.p_signals
        timenet_record = TimeNetRecord(
            record_data=ecg_X,
            channel_names=ecg_record.signame,
            meta_data={
                'label': ecg_record.comments[4],
                'extra_info': ecg_record.comments
            }
        )
        timenet_record.save(parameters['path_to_database'] + str(counter))
        print('Number of processed records: ' + str(counter))
        counter += 1
