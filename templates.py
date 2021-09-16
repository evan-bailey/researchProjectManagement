#!/usr/bin/python
"""
Functions to generate templates for common tasks
"""

import csv
import os

class ImmunoTemplates(object):
    """Class defining templates for IHC data"""
    def __init__(self, root_dir) -> None:
        self.root_dir=root_dir
        self.immuno_dir=os.path.join(root_dir,"3_data","1_raw")


    def cell_counts(self):
        """Generate a template for recording cell counts"""
        cellcounts_dir=self.immuno_dir + "cell_counts.csv"

        with open(cellcounts_dir,
                  'w',
                  newline='',
                  encoding="utf-8") as csvfile:
            title_writer=csv.writer(csvfile)
            title_writer.writerow(['Filename',
                                   'Marker',
                                   'X',
                                   'Y',
                                   'MeanGrey'])

    def section_info(self):
        """Generate a template for recording information regarding
        histological sections"""
        sectioninfo_dir=self.immuno_dir + "section_info.csv"

        with open(sectioninfo_dir,
                  'w',
                  newling='',
                  encoding="utf-8") as csvfile:
            title_writer=csv.writer(csvfile)
            title_writer.writerow(['Filename',
                        'ROI_X1',
                        'ROI_X2',
                        'ROI_Y1',
                        'ROI_Y2',
                        'Ventricle_Y',
                        'Meninges_Y',
                        'Thickness',
                        'LaminarA_1',
                        'LaminarA_2',
                        'LaminarB_1',
                        'LaminarB_2'])

    def conditions(self):
        """Generate a template for recording information on
        experimental conditions"""
        conditions_dir=self.immuno_dir + "conditions.csv"

        with open(conditions_dir,
                  'w',
                  newling='',
                  encoding="utf-8") as csvfile:
            title_writer=csv.writer(csvfile)
            title_writer.writerow(['SampleID',
                                   'Condition'])
