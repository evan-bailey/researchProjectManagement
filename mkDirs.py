#!/usr/bin/python
import os, pathlib

class dirStructure(object):
    def __init__(self, root_dir, name):
        self.root_dir = root_dir
        self.name = name
        self.dir_full = os.path.join(root_dir, name)
        self.dir_parsed = os.path.expanduser(self.dir_full)

    #generate project management directory and subdirectories
    def mkProjectMgmt(self):
        with open('./paths/projectMgmt.txt') as projectMgmt_dirs:
            for dir in projectMgmt_dirs:
                p_dir = pathlib.Path(self.dir_parsed + '/1_project-management' + dir.rstrip('\n'))
                p_dir.mkdir(parents = True, exist_ok = True)

    #generate materials and methods directory and subdirectories
    def mkMatsMethods(self):
        with open('./paths/matsMethods.txt') as matsMethods_dirs:
            for dir in matsMethods_dirs:
                m_dir = pathlib.Path(self.dir_parsed + '/2_materials-and-methods' + dir.rstrip('\n'))
                m_dir.mkdir(parents = True, exist_ok = True)

    #generate data directory and subdirectories
    def mkData(self):
        with open('./paths/data.txt') as data_dirs:
            for dir in data_dirs:
                d_dir = pathlib.Path(self.dir_parsed + '/3_data' + dir.rstrip('\n'))
                d_dir.mkdir(parents = True, exist_ok = True)

    #generate analysis directory and subdirectories
    def mkAnalysis(self):
        with open('./paths/analysis.txt') as analysis_dirs:
            for dir in analysis_dirs:
                a_dir = pathlib.Path(self.dir_parsed + '/4_analysis' + dir.rstrip('\n'))
                a_dir.mkdir(parents = True, exist_ok = True)

    #generate figures directory and subdirectories
    def mkFigures(self):
        with open('./paths/figures.txt') as figures_dirs:
            for dir in figures_dirs:
                f_dir = pathlib.Path(self.dir_parsed + '/5_figures' + dir.rstrip('\n'))
                f_dir.mkdir(parents = True, exist_ok = True)

    #generate analysis directory and subdirectories
    def mkDisseminate(self):
        with open('./paths/disseminate.txt') as disseminate_dirs:
            for dir in disseminate_dirs:
                dis_dir = pathlib.Path(self.dir_parsed + '/6_dissemination' + dir.rstrip('\n'))
                dis_dir.mkdir(parents = True, exist_ok = True)

    #generate a directory tree using the UNIX tree command with html output
    def mkTree(self):
        command_args = 'tree ' + self.dir_parsed + ' -dC -H ' + self.dir_parsed + ' -o ' + self.dir_parsed + '/directory-structure.html'
        os.system(command_args)
