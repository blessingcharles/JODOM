







import sys
import logging


class Logger:

    def __init__(self,file_name):

        self.terminal = sys.stdout
        self.logfile = open(file_name,"a")

    def write(self,message):

        self.terminal.write(message)
        self.logfile.write(message)

    def flush(self):
        pass

def output_Stream(filename):

    sys.stdout = Logger(filename)

#for i in range(1,100):
#   print(i)


