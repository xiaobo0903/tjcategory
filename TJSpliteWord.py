#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author:xiaobo
# Date:2019-09-25
#The programe is save profession word in file; Load data into memory; Update data online;

import time, os, shutil
import re
import json
import logging
import jieba
import jieba.analyse

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)
word_table = {}

class TJSpliteWord():


    #Stop word file path;
    wfile = "qiche.txt"
    swfile = "stopword.txt"
    
    
    def __init__(self):

        if not word_table:
            self.Loadword() 


    def get(self):
        return {'hello': 'world'}

#load word into memory;

    def Loadword(self):

        f = open("./"+self.wfile, 'r')
        i = 0

        for line in f.readlines():

            line = line.replace("\n", "").replace("\r", "")
            i = i+1
            word_table[line] = line
            logging.debug("load text is :"+line)

        f.close()
        print(len(word_table))
        print(i)
        return

#save car_word in file;

    def Saveword(self):

        #if file exit, rename old file name;  
        if os.path.isfile("./"+self.wfile):

            crtime = os.path.getctime("./"+self.wfile)
            ctime = time.time() 
            print(crtime, ctime)

            #if ctime-crttime >7200 rename old filename,and save word_table data in wpath;
            if ctime-crtime > 7200:

                opath = "./old"
                isExists=os.path.exists(opath)                

                if not isExists:
                    os.makedirs(opath)

                shutil.move("./"+self.wfile, opath+"/"+self.wfile+str(crtime)) 

        f = open("./"+self.wfile, "w+") 
        
        for key in word_table.keys():

            f.write(key+"/r/n")
        print(len(word_table))

        f.close()

#get car_word list;
      
    def Getword(self, page=1, number=10):

        if (page == 0 and number == 0):        

           jtxt = json.dumps(word_table, ensure_ascii=False)
           logging.debug(jtxt)
           return  jtxt

        if page < 1:
            page = 1
       
        if number < 1:
            number = 10

        total = len(word_table)

        tp = total//number

        if (total % number) > 0:
           tp = tp + 1
         
        subword = {}

        i = 0

        for key in word_table.keys():
             
            i = i + 1

            if i < (page - 1) * number:
                continue

            if i > (page+1)*number or i > total :
                break;
            
            subword[key] = key;

        jtext = json.dumps(subword, ensure_ascii=False)

        logging.debug(jtext)


    def Addword(self, nword):

        word_table[nword] = nword; 
        logging.debug("add new word:"+nword)
        return;

    def Spliteword(self, cstr):

        line = str(cstr)
        seglist = jieba.cut(line,cut_all=False)  #精确模式
        output = ''

        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        for letter in seglist:

            if len(letter) == 1 :
                continue
           
            leng = len(re.findall(u'[\u4e00-\u9fff]', letter))
            match = zhPattern.search(letter)

            if match and leng == 1:
                continue
            output = output+" "+letter
        logging.debug(output)
        return output

    def WordCount(self, cstr):
        
        csdict = {}
        line = str(cstr)
        seglist = jieba.cut(line,cut_all=False)  #精确模式
        output = ''

        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        for letter in seglist:

            if len(letter) == 1 :
                continue
           
            leng = len(re.findall(u'[\u4e00-\u9fff]', letter))
            match = zhPattern.search(letter)

            if match and leng == 1:
                continue

            if csdict.get(letter) == None:
                csdict[letter] = 0                
 
            csdict[letter] = csdict[letter]+1

        #csdict.sort(key=lambda d: d.values()[0], reversed=True)
 

        #ccdict = [ v for v in sorted(csdict.values())] 
        ccdict = sorted(csdict.items(), key=lambda d: d[1], reverse=True) 
        
        return json.dumps(ccdict, ensure_ascii=False)

if __name__ == '__main__':

    tjspliteword = TJSpliteWord()

    tjspliteword.Loadword()                
    #tjspliteword.Saveword()                
    #tjspliteword.Getword(0, 0)                
    #tjspliteword.Addword("真不错")                
    f = open("../ll.txt", 'r')
    line = f.readline()
    f.close();
    tjspliteword.Spliteword(line)
