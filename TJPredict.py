#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author:xiaobo
# Date:2019-09-25
#The programe is save profession word in file; Load data into memory; Update data online;

import fasttext
from TJSpliteWord import TJSpliteWord 
import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)
classifier = fasttext.load_model("./model/qicheGZLX.bin")


class TJPredict():

    def Predict(self, cstr):

        result = {}
        presult = classifier.predict(cstr)

        result["label"] =  presult[0][0]
        
        return result

if __name__ == '__main__':

    tjspliteword = TJSpliteWord()
    tjpredict = TJPredict()

    tjspliteword.Loadword()                
    #tjspliteword.Saveword()                
    #tjspliteword.Getword(0, 0)                
    #tjspliteword.Addword("真不错")                
    f = open("../ll.txt", 'r')
    line = f.readline()
    f.close();
    aa = tjspliteword.Spliteword(line)
    tjpredict.Predict(aa)
