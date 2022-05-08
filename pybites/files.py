from os import walk, getcwd
from pathlib import Path
from logger import log

def list_files(dir: str, glob: str):
    for file_path in Path(dir).glob(glob):
        print(file_path)

def walk_dir(dir: str):

    output = {"dir_paths": [], "file_paths": []}

    for _, dirs, files in walk(dir):
        for dir in dirs:
            output['dir_paths'].append(dir)
        for file in files:
            output['file_paths'].append(file)
    return output


log.info('List python files in current directory')
list_files(getcwd(), '*.py')

log.info('List python files in current directory + one deep')
list_files(getcwd(), '*/*.py')

log.info('List all python files in current directory + any beneath it (recursively)')
list_files(getcwd(), '**/*.py')

log.info('Walk from current directory')
print(walk_dir(getcwd()))
