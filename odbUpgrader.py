"""

Author: Miguel Herraez - TecnoDigital School
https://tecnodigitalschool.com/

Upgrade odb files in Abaqus by recursively walking from the root 
directory.

Old odbs keep their name and new odbs include a suffix with the current 
Abaqus version:

  mysimulation.odb  >>>  mysimulation_23.odb


Watch out memory! It will get about twice the memory (2 odbs).

Optional: delete outdated odbs (not recommended before testing!)


Run from Abaqus/CAE:
    File -> Run script
 
"""

# Import Abaqus modules
from abaqus import *
from abaqusConstants import *
from caeModules import *

import os
from os.path import join, getsize


# Parent folder from which odbs will be recursively upgraded
parentDirectory = r'.'


testMode = True        # If True, upgrade will not be executed.
                       # Use it to print out which odbs would be upgraded
                       
deleteOldOdbs = False  # Watch out odbs will be deleted (not in the recycle bin)!!! 

suffix = str(minorVersion)  # from abaqus module

for curDirectory, folders, files in os.walk(parentDirectory):

    print('\n*** Reading directory: {}'.format(curDirectory))
    
    odbCount = 0
    
    # 1) Identify odbs in dir
    odbs = [f for f in files if f.endswith('.odb')]


    # Iterate through all the odbs in the current directory (curDirectory)
    for odb in odbs:

        odbPath = join(curDirectory, odb)

        try:
            # 2) Check if upgrade is required
            if session.isUpgradeRequiredForOdb(odbPath):

                newOdbPath = odbPath.replace('.odb', '_' + suffix + '.odb')

                # 3) Upgrade odb
                if not testMode:
                    session.upgradeOdb(existingOdbPath=odbPath,
                                       upgradedOdbPath=newOdbPath)

                # Info: print out odb file size
                odbSizeMB = float(getsize(odbPath))/(1024. * 1024.)
                print('Upgraded: {0:s} ({1:.2f} MB)'.format(odbPath, odbSizeMB))
                
                if deleteOldOdbs:
                    os.remove(odbPath)
                
                odbCount += 1
        
        except Exception as e:
            # Skip odb file if it cannot be read or upgraded
            print('Could not be read/upgraded: {0:s}'.format(odbPath))

    print('+ Upgraded {0:d} odbs'.format(odbCount))
