#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

from inflammation import models, views


def main(arguments):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_file_condition = arguments.infiles
    if not isinstance(in_file_condition, list):
        in_file_condition = [arguments.infiles]


    for filename in in_file_condition:
        inflammation_data = models.load_csv(filename)

        view_data = {'average': models.daily_mean(inflammation_data),
                     'max': models.daily_max(inflammation_data), 
                     'min': models.daily_min(inflammation_data)}

        views.visualize(view_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    arguments_in_main = parser.parse_args()

    main(arguments_in_main)
