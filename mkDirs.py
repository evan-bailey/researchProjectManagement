#!/usr/bin/python
"""
Module containing a directory structure object and methods to generate part
or all of the project directory structure.
"""
import os
import pathlib


class dirStructure(object):
    def __init__(self, root_dir, name):
        self.root_dir = root_dir
        self.name = name
        self.dir_full = os.path.join(root_dir, name)
        self.dir_parsed = os.path.expanduser(self.dir_full)

    def mkProjectMgmt(self):
        """
        Method to generate the project management directory & subdirectories
        """
        with open('./paths/projectMgmt.txt') as projectMgmt_dirs:
            for directory in projectMgmt_dirs:
                p_dir = pathlib.Path(self.dir_parsed + '/1_project-management'
                                     + directory.rstrip('\n'))
                p_dir.mkdir(parents=True, exist_ok=True)

    def mkMatsMethods(self):
        """
        Method to generate the materials and methods directory & subdirectories
        """
        with open('./paths/matsMethods.txt') as matsMethods_dirs:
            for directory in matsMethods_dirs:
                m_dir = pathlib.Path(self.dir_parsed
                                     + '/2_materials-and-methods'
                                     + directory.rstrip('\n'))
                m_dir.mkdir(parents=True, exist_ok=True)

    def mkData(self):
        """
        Method to generate the data directory & subdirectories
        """
        with open('./paths/data.txt') as data_dirs:
            for directory in data_dirs:
                d_dir = pathlib.Path(self.dir_parsed
                                     + '/3_data'
                                     + directory.rstrip('\n'))
                d_dir.mkdir(parents=True,
                            exist_ok=True)

    def mkAnalysis(self):
        """
        Method to generate the analysis directory & subdirectories
        """
        with open('./paths/analysis.txt') as analysis_dirs:
            for directory in analysis_dirs:
                a_dir = pathlib.Path(self.dir_parsed
                                     + '/4_analysis'
                                     + directory.rstrip('\n'))
                a_dir.mkdir(parents=True,
                            exist_ok=True)

    def mkFigures(self):
        """
        Method to generate the figures directory & subdirectories
        """
        with open('./paths/figures.txt') as figures_dirs:
            for directory in figures_dirs:
                f_dir = pathlib.Path(self.dir_parsed
                                     + '/5_figures'
                                     + directory.rstrip('\n'))
                f_dir.mkdir(parents=True,
                            exist_ok=True)

    def mkDisseminate(self):
        """
        Method to generate the dissemination directory & subdirectories
        """
        with open('./paths/disseminate.txt') as disseminate_dirs:
            for directory in disseminate_dirs:
                dis_dir = pathlib.Path(self.dir_parsed
                                       + '/6_dissemination'
                                       + directory.rstrip('\n'))
                dis_dir.mkdir(parents=True,
                              exist_ok=True)

    def mkTree(self):
        """
        Method to generate directory tree structure and save to html
        """
        command_args = 'tree '\
                       + self.dir_parsed\
                       + ' -dC -H '\
                       + self.dir_parsed\
                       + ' -o '\
                       + self.dir_parsed\
                       + '/directory-structure.html'
        os.system(command_args)
