# Upgrade old ODB files in Abaqus

This script automatically upgrades all the ODB files in a directory and all the subdirectories recursively.

## Before running the script

Before launching the script:

- Set a `parentDirectory` from which the recursive search will inititate.
- Make a "dry run" by setting `testMode = False`, i.e. the ODB files that require an upgrade will be identified, but won't be upgraded yet.
- The optional parameter `deleteOldOdbs` should be kept to False, until we are certain that we want to delete the old ODB files (ain't undo!).


## Running the script

In Abaqus/CAE, go to to File -> Run script and select the file 'odbupgrader.py'


## Blog post

Find more details about the development of this script for Abaqus in this [blog post](https://tecnodigitalschool.com/how-to-upgrade-old-odb-files-in-abaqus/)
