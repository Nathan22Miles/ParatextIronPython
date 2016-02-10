# Print the names of all the Scrpture Text Projects present

import sys
import clr

# This is the path to the test version of Paratext
# You could use the path to the non-test version instead
sys.path.append("c:\\Program Files (x86)\\Paratext 7 Test")
clr.AddReference('ParatextShared')
from Paratext import *

ScrTextCollection.Initialize()

includeResources = True
includeNonScripture = False   # e.g. Consultant notes project

for scrText in ScrTextCollection.ScrTexts(includeResources, includeNonScripture):
    print scrText.Name

