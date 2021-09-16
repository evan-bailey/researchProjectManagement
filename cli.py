#!/usr/bin/python
"""
Front-end CLI for researchProjectManagement tools
"""

import argparse


def parse_arguments():
    """
    Parses arguments given to the CLI app at the command line
    """
    parser = argparse.ArgumentParser(description="A CLI application for generati\
                                     ing a project directory structure and sen\
                                     sible templates for use in molecular biol\
                                     ogy laboratories. Future versions will ad\
                                     d database functionality and dashboardin\
                                     g features.",
                                     allow_abbrev=True)
    subparser = parser.add_subparsers(dest='command')
    # generate a command and subparser for generating project directory
    start = subparser.add_parser('start',
                                 description="Initiate a new project")
    # generate a command and subparser for template generation
    templates = subparser.add_parser('templates',
                                     description="Populate project directories\
                                     with templates")
    # add two sub-commands to 'start': directory and name
    start.add_argument('-d', '--directory',
                       type=str,
                       default='./',
                       help="The directory where the project will be generated\
                       (include / at the end of path)")
    start.add_argument('-n', '--name',
                       type=str,
                       default='1_project',
                       help="The name of the project directory.  Alpha numeric,\
                       underscores and dashes only")
    # add tree argument parser, potentially remove tree argument from the
    # mkDirs module into own module

    # To do, implement mutually exlusive subcommands for template generation
    templates.add_argument('--all',
                           action="store_true",
                           default=False,
                           help="Generate all project templates")

    return parser.parse_args()


def startup_args():
    """
    Get the startup arguments from the parser
    """
    parsed_args = parse_arguments()
    return vars(parsed_args)


args = startup_args()

# empty string
DIRNAME = ""

# command == 'start'
if args.get('command') == 'start':
    root_dir = args.get('directory')
    project_name = args.get('name')

    # # generate a project database if not already initiated
    # from metaHandler import metaDB
    #
    # # can change where the project database is stored, potentially option for
    # # first init?
    # project_meta = metaDB('./databases/')
    # project_meta.init_db()

    # generate the project directory structure
    from mk_dirs import DirStructure

    projectStructure = DirStructure(root_dir, project_name)

    print('Creating project in: ', projectStructure.dir_full)

    projectStructure.mk_projectmgmt()
    projectStructure.mk_matsmethods()
    projectStructure.mk_data()
    projectStructure.mk_analysis()
    projectStructure.mk_figures()
    projectStructure.mk_disseminate()

elif args.get('command') == 'templates':

    print('Generating templates for project: ')
