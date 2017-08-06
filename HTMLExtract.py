#! -*- coding:UTF-8 -*-
import sys
from sgmllib import SGMLParser
 
class ListCmds(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_a = ""
		self.cmds = []
	def start_a(self, attrs):
		self.is_a = 1
	def end_a(self):
		self.is_a = ""
	def handle_data(self, text):
		if self.is_a == 1:
			self.cmds.append(text)

if __name__ == '__main__':
    path = sys.argv[1]
    save_path = path[0:-4] + "tcl"
    with open(path, 'r') as fr: 
        content = fr.read()
    listcmds = ListCmds()
    listcmds.feed(content)
    with open(save_path, 'w') as fw:
        for command in listcmds.cmds:
#	    print command.decode('utf8').encode('gbk')    
            fw.write(command + "\n")
