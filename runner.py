from subprocess import Popen
import argparse
from os.path import isfile

"""
Trick learned from: https://www.alexkras.com/how-to-restart-python-script-after-exception-and-run-it-forever/

"""

if __name__ == '__main__':
    # Define command line arguments
    parser = argparse.ArgumentParser(
        'Starting runner'
    )

    parser.add_argument(
        '-f',
        action='store',
        nargs='+',
        dest='files',
        help='List of files to run'
    )

    main_args = parser.parse_args()
    files = main_args.files
    print(files)
    processes = {}

    while True:
        # Add the processes:
        for file in files:
            if file not in processes and isfile(file):
                print(" == Starting " + file + " == ")
                proc = Popen(file, shell=True)
                processes[file] = proc

        keys = list(processes ) # get keys

        for key in keys:
            if processes[key].poll() is not None:
                # It's no longer alive
                processes.pop(key, None)
