# runner.py

This is an extremely simple Python script whose purpose is to run other Python scripts. Should any of those scripts stop, then `runner.py` will restart them.

## Usage
 Use the -f and provide a list of Python scripts to run.
 `eg. python runner.py -f testfiles//testfile_1.py testfiles//testfile_2.py`
 
### Note:
A couple of files (testfile_1.py and testfile_2.py) are provided. These files are designed to raise an exception after a few seconds.