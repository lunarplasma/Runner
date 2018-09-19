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
    files = list(f for f in main_args.files if isfile(f))
    print(files)
    processes = {}

    if len(files) > 0:
        while True:
            # Add the processes:
            for file in files:
                if file not in processes and isfile(file):
                    print(" == Starting " + file + " == ")
                    proc = Popen('python ' + file, shell=True)
                    processes[file] = proc
                else:
                    if processes[file].poll() is not None:
                        # It's no longer alive
                        processes.pop(file, None)
    else:
        print("No valid files provided")
