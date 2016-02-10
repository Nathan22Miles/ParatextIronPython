# Output GEN for AruMH project as USX

import sys
# remove " (86)" from following line if you have 32 bit system
sys.path.append("c:\\Program Files (x86)\\Paratext 7")

import clr
clr.AddReference('System.IO')
clr.AddReference('System.Xml')
from System.Xml import XmlWriterSettings, XmlWriter

clr.AddReference('ParatextShared')
from Paratext import *

ScrTextCollection.Initialize()
scrText = ScrTextCollection.Get("AruMH")

vref = VerseRef("GEN 1:1")
bookNum = vref.BookNum

getSingleChapter = False # False means 'read entire book'
runMapinCctIfPresent = True
text = scrText.GetText(vref, getSingleChapter, runMapinCctIfPresent)

settings = XmlWriterSettings(Indent=True, NewLineChars="\r\n")

xw = XmlWriter.Create("gen.xml", settings) 
UsfmToUsx.ConvertToXmlWriter(scrText, bookNum, UsfmToken.NormalizeUsfm(scrText, bookNum, scrText.GetText(bookNum)), xw)
xw.Close()

print "gen.xml written"