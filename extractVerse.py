import sys
import clr

# This is the path to the test version of Paratext
sys.path.append("c:\\Program Files (x86)\\Paratext 7 Test")
clr.AddReference('ParatextShared')
from Paratext import *

ScrTextCollection.Initialize()
scrText = ScrTextCollection.Get("AruMH")

# Create a reference to a verse and say it is in "original" (i.e. BHS) versification
vref = VerseRef("GEN 1:1", ScrVers.Original)

# Change versification to match target language text.
# For GEN 1.1 the chapter/verse will be identical
vref.ChangeVersification(scrText.Versification)

verseText = scrText.Parser.GetVerseTextAllSegments(vref)
print verseText