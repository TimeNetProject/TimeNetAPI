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

# download and save the original data into the temporary folder
def download_the_original(parameters):

    # clean the data folder
    os.system('rm ' + parameters['path_to_database'] + '*.pkl')
    counter = 1
    # for each possible patient number we have to check
    # whether we have any data in the online repository
    for record_name_number in range(100, 235):
        record_name = str(record_name_number)

        try:
            record = wfdb.rdsamp(
                record_name,
                physical=True,
                pbdir='mitdb',
                channels=None,
                m2s=False
            )

            annotation = wfdb.rdann(
                record_name,
                'atr',
                pbdir='mitdb'
            )

        except:
            continue

        raw_data = record.p_signals
        beat_annotation_temp = annotation.sample
        beat_annotation = np.zeros(beat_annotation_temp.shape[0] + 2)
        beat_annotation[1:-1] = beat_annotation_temp
        beat_annotation[-1] = record.p_signals.shape[0]
        beat_annotation = beat_annotation[1:]
        beat_classes = annotation.symbol

        timenet_record = TimeNetRecord(
            record_data = raw_data,
            channel_names=['MLII', 'V1'],
            meta_data={
                'sampling_frequency': 360,
                'patient_diagnosis': record.comments
            },
            annotations={
                'start_indexes': beat_annotation[:-1],
                'end_indexes': beat_annotation[1:],
                'annotations': beat_classes
            }
        )

        timenet_record.save(parameters['path_to_database'] + str(counter))
        print('Number of processed records: ' + str(counter))
        counter += 1