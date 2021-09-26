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
        self.immuno_dir=os.path.join(root_dir,"3_data","1_raw","Histology")


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
                  newline='',
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
                  newline='',
                  encoding='utf-8') as csvfile:
            title_writer=csv.writer(csvfile)
            title_writer.writerow(['SampleID',
                                   'Condition'])


class MolBioTemplates(object):
    """Class defining templates for common molecular biology experiments"""
    def __init__(self, root_dir) -> None:
        self.root_dir=root_dir
        self.molbio_dir=os.path.join(root_dir,"3_data","1_raw","General")
   
    # Consider changing the csv writing function to have the headers saved in
    # a single txt file, and extracting the row for the specified template
    # such that the template generation function is a generic function
    # and the argument is the row identifier for the text doc
    def pcr_template(self):
        """Generate a template for planning and analysing PCR experiments"""
        pcr_dir=self.molbio_dir + "PCR.csv"

        with open(pcr_dir,
                  'w',
                  newline='',
                  encoding='utf-8') as csvfile:
            title_writer=csv.writer(csvfile)
            title_writer.writerow(['Date',
                                   'Sample_Name',
                                   'Experiment',
                                   'DNA_Template',
                                   'Amplicon_Size',
                                   'Template_Vol',
                                   'Reaction_Vol',
                                   'Enzyme_Units',
                                   'dNTPs_Conc',
                                   'Mg2+_Conc',
                                   'Primer_1',
                                   'Primer_2',
                                   'Primer_3',
                                   'Primer_4',
                                   'Primer_Conc_Final',
                                   'Denat_Time',
                                   'Denat_Init_Time',
                                   'Anneal_Temp',
                                   'Anneal_Time',
                                   'Extension_Temp',
                                   'Extension_Time',
                                   'Ext_Time_Final',
                                   'N_Cycles',
                                   'Gel_Percent',
                                   'Gel_Buffer',
                                   'Gel_Stain',
                                   'Gel_Band_1',
                                   'Gel_Band_2',
                                   'Gel_Band_3',
                                   'Gel_Band_4'])
