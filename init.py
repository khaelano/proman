#!/usr/bin/python

import os
import argparse
from pathlib import Path

class Initialize():
    def __init__(self, main_dir):
        self.target_dir = main_dir
        if arg.work_dir == True:
            #Changing target directory to current directory
            print('Changing target to current working directory...')
            self.target_dir = os.getcwd()
        #Making 'projects' directory
        try:
            os.chdir(self.target_dir)
        except:
            print('Not detecting projects directory')
            print('Makng projects directory inside $HOME...')
            os.makedirs(main_dir)

    def make(self, name, extension):
        main = f'main{extension}'
        #Initializing python project
        print(f'Creating {name} folder...')
        os.mkdir(name)
        print(f'Making {main} file...')
        Path(f'{name}/{main}').touch()
        print(f'Opening {text_editor}...')
        os.system(f'{text_editor} {name}/{main}')


PROJECT_DIR = str(os.getenv('HOME')) + '/projects/'
text_editor = 'vim'
lang_extension = {
        'python' : '.py',
        'javascript' : '.js'
        }

#Argument parser
parser = argparse.ArgumentParser(description='Initialize project (defaults to ~/.projects)')
parser.add_argument(
        'language', 
        type=str, 
        help='Define what language to initialize',
        choices=lang_extension
        )
parser.add_argument(
        'name', 
        type=str, 
        help='Define the project name'
        )
parser.add_argument(
        '-d', '--current-dir', 
        action='store_true', 
        dest='work_dir', 
        help='Initialize project in current working directory'
        )



arg = parser.parse_args()
init = Initialize(PROJECT_DIR)

init.make(arg.name, lang_extension[arg.language])
