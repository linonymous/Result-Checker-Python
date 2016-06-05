# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 15:53:14 2016

@author: LINONYMOUS
"""

import winsound
import urllib
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second

#Check() function which checks if the results are announced or not
def check():
    link='http://walchandsangli.ac.in/result1.asp' #url of the website
    site = urllib.urlopen(link).read() #fetching web page here
    if 'T.Y.' in site: 	#T.Y. is searched in the site fetched, if found the beep sound is produced
        winsound.Beep(Freq,Dur)
        print "Results are out"
#Call
check()