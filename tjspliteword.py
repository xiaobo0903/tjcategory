#encoding=utf-8
import sys
import re
import codecs
import os
import shutil
import jieba
import jieba.analyse
 
#导入自定义词典
jieba.load_userdict("qiche.txt")
jieba.analyse.set_stop_words("stopword.txt")
 
#Read file and cut
def read_file_cut(p_path):
    #create path
    path = p_path+"/"
    respath = p_path+"_cut/"
    if os.path.isdir(respath):
        shutil.rmtree(respath, True)
    os.makedirs(respath)
 
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    num = 1
    while num<=204:
        name = "%04d" % num 
        fileName = path + str(name) + ".txt"
        resName = respath + str(name) + ".txt"
        source = open(fileName, 'r')
        if os.path.exists(resName):
            os.remove(resName)
        result = codecs.open(resName, 'w', 'utf-8')
        line = source.readline()
        line = line.rstrip('\n')
        line = line.rstrip('\r')
        
        while line!="":
            line = unicode(line, "utf-8")
            seglist = jieba.cut(line,cut_all=False)  #精确模式
            output = ''
            for letter in seglist:
                #本程序只处理中文，对于标点符号和单字都不做处理，另外一个文件当做一条信息，去除掉换行符等；
                leng = len(re.findall(ur"[\u4e00-\u9fff]", letter))
                match = zhPattern.search(letter)
                #print letter+' '+str(leng)
                if match and leng == 1:
                    continue
                output = output+" "+letter
            #output = ' '.join(list(seglist))         #空格拼接
            #print output
            result.write(output + '\r\n')
            #result.write(output)
            line = source.readline()
        else:
            print 'End file: ' + str(num)
            source.close()
            result.close()
        num = num + 1
    else:
        print 'End All'
 
#Run function
if __name__ == '__main__':
    read_file_cut(sys.argv[1])
    
