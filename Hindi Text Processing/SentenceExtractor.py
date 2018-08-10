# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:25:29 2018

@author: Gayatri
"""

import os
import codecs

#Extracting sentences beginning with <s> from a downloaded  corpus and adding to the sentence to build a new one
outfile = codecs.open("downloadedcorpus.txt", "w", "utf-8")
for filelineno, line in enumerate(open(
        "hindmonocorp05.plaintext", encoding="utf-8")):
        line = line.strip()
        if line.find("<s>") != -1:
            line = (line[line.find("<s>")+3:]).strip()
            line = line.replace("”","'")
            line = line.replace("\"","'")
            line = "web,misc,na,na,\""+line+"\""   
            print(line)
            outfile.write(line+"\n")
       
    