# -*- coding: utf-8 -*-

#============================================================
#
#  Deep Learning BLW Filtering
#  Main
#
#  author: Francisco Perdigon Romero
#  email: fperdigon88@gmail.com
#  github id: fperdigon
#
#===========================================================

import _pickle as pickle
from datetime import datetime
import time
import numpy as np

from utils.metrics import MAD, SSD, PRD, COS_SIM
from utils import visualization as vs
from Data_Preparation import data_preparation_multi_BW as dp

from digitalFilters.dfilters import FIR_test_Dataset, IIR_test_Dataset
from deepFilter.dl_pipeline_multi import train_dl, test_dl


if __name__ == "__main__":

    dl_experiments = [
                      'DRNN',
                      'FCN-DAE',
                      'Vanilla L',
                      'Vanilla NL',
                      'Multibranch LANL',
                      'Multibranch LANLD'
                      ]

    noise_versions = [1, 2]
    for nv in noise_versions:
        # Data_Preparation() function assumes that QT database and Noise Stress Test Database are uncompresed
        # inside a folder called data

        Dataset = dp.Data_Preparation(noise_version=nv)

        # Save dataset
        with open('data/dataset_nv' + str(nv) + '.pkl', 'wb') as output:  # Overwrites any existing file.
            pickle.dump(Dataset, output)
        print('Dataset saved')

        # Load dataset
        with open('data/dataset_nv' + str(nv) + '.pkl', 'rb') as input:
            Dataset = pickle.load(input)


        train_time_list = []
        test_time_list = []

        for experiment in range(len(dl_experiments)):
            start_train = datetime.now()
            train_dl(Dataset, dl_experiments[experiment])
            end_train = datetime.now()
            train_time_list.append(end_train - start_train)

            start_test = datetime.now()
            [X_test, y_test, y_pred] = test_dl(Dataset, dl_experiments[experiment])
            end_test = datetime.now()
            test_time_list.append(end_test - start_test)

            test_results = [X_test, y_test, y_pred]

            # Save Results
            with open('test_results_' + dl_experiments[experiment] + '_nv' + str(nv) + '.pkl', 'wb') as output:  # Overwrites any existing file.
                pickle.dump(test_results, output)
            print('Results from experiment ' + dl_experiments[experiment] + '_nv' + str(nv) + ' saved')

            time.sleep(60)

        # Classical Filters

        # FIR
        start_test = datetime.now()
        [X_test_f, y_test_f, y_filter] = FIR_test_Dataset(Dataset)
        end_test = datetime.now()
        train_time_list.append(0)
        test_time_list.append(end_test - start_test)

        test_results_FIR = [X_test_f, y_test_f, y_filter]

        # Save FIR filter results
        with open('test_results_FIR_nv' + str(nv) + '.pkl', 'wb') as output:  # Overwrites any existing file.
            pickle.dump(test_results_FIR, output)
        print('Results from experiment FIR filter nv ' + str(nv) + ' saved')

        # IIR
        start_test = datetime.now()
        [X_test_f, y_test_f, y_filter] = IIR_test_Dataset(Dataset)
        end_test = datetime.now()
        train_time_list.append(0)
        test_time_list.append(end_test - start_test)

        test_results_IIR = [X_test_f, y_test_f, y_filter]

        # Save IIR filter results
        with open('test_results_IIR_nv' + str(nv) + '.pkl', 'wb') as output:  # Overwrites any existing file.
            pickle.dump(test_results_IIR, output)
        print('Results from experiment IIR filter nv ' + str(nv) + ' saved')

        # Saving timing list
        timing = [train_time_list, test_time_list]
        with open('timing_nv' + str(nv) + '.pkl', 'wb') as output:  # Overwrites any existing file.
            pickle.dump(timing, output)
        print('Timing nv ' + str(nv) + ' saved')
