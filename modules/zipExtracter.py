import sys
import zipfile
from threading import Thread
class zip:
    def __init__(self, filename):
        self.zFile=zipfile.ZipFile(filename)
        self.zFile=
    def extractzip(zFile, password):
        try:
            zFile.extractall(pwd=bytes(password, 'UTF-8'))
            sys.stdout.write("!!PASSWORD FOUND!! password is '%s'\n"%password)
        except:
            pass
    def ZipDictionary(filename, dicname):
        try:
            zFile=zipfile.ZipFile(filename)
            try:
                f=open(dicname, 'r')
                for password in f.readlines():
                    password=password.strip('\n')
                    t=Thread(target=extractzip, args=(zFile, password))
                    t.start()
                f.close()
            except IOError:
                sys.stdout.write('dictionary file not found\n')
        except IOError:
            sys.stdout.write('zip file not found\n')
    def ZipBrute(filename):
        try:
            zFile=zipfile.ZipFile(filename)
            brute_range=100
            found_pass=False
            for password in range(0, 100000):
                t=Thread(target=extractzip, args=(zFile, str(password)))
                t.start()
        except IOError:
            sys.stdout.write('zip file not found\n')
    def zipExtracter(mode, filename, dicname):
        if mode=='dic':
            ZipDictionary(filename, dicname)
        else:
            ZipBrute(filename)