


import os
import pdb
import glob
import urllib.request
import zipfile

import numpy as np

from library.timenet_record import TimeNetRecord


def download_the_original(parameters):
    db_path = parameters['path_to_database']
    db_name = parameters['database_name']
    db_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00341/HAPT%20Data%20Set.zip'
    # download compressed data
    orig_path = db_path + 'tmp/' + db_name + '/'
    zip_file = db_path + 'tmp/' + db_name + '/orig.zip'
    if not os.path.exists(db_path + 'tmp/' + db_name):
            os.makedirs(db_path + 'tmp/' + db_name)
    urllib.request.urlretrieve(db_url, db_path + 'tmp/' + db_name + '/orig.zip')
    # extract the file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(db_path + 'tmp/' + db_name + '/orig')

    # read raw files
    for (ind, fname) in enumerate(glob.glob(orig_path + 'orig/RawData/acc_*.txt')):
        fname_gyro = fname[:-20] + 'gyro' + fname[-17:]
        print('Processing: ', fname, fname_gyro)
        data_csv_acc = np.loadtxt(fname, delimiter=' ')
        data_csv_gyro = np.loadtxt(fname_gyro, delimiter=' ')
        meta = {}
        meta['user'] = fname.split('/')[-1].split('_')[-1]
        meta['exp'] = fname.split('/')[-1].split('_')[-2]
        
        timenet_record = TimeNetRecord(
                record_data=np.hstack([data_csv_acc, data_csv_gyro]), 
                channel_names = ['Acc1', 'Acc2', 'Acc3', 'Gyro1', 'Gyro2', 'Gyro3'], 
                meta_data = meta
                )

        if not os.path.exists(db_path + db_name):
            os.makedirs(db_path + db_name)
        timenet_record.save(db_path + db_name + '/' + str(ind))


    
