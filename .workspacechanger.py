#!/usr/bin/python
import os, sys

class workspace_changer(object):

    def __init__(self):
        self.workspaces = os.popen('wmctrl -d').readlines()

    def find_ws(self):

        for item in self.workspaces:
            if '*' in item:
                current = item[0]
        return current

    def fwd(self):
        set_ws = int(self.find_ws()) + 1
        if set_ws >= len(self.workspaces):
            set_ws = set_ws - len(self.workspaces)
        os.popen('wmctrl -s ' + str(set_ws))

    def bwd(self):
        set_ws = int(self.find_ws()) - 1
        if set_ws < 0:
            set_ws = set_ws + len(self.workspaces)
        os.popen('wmctrl -s ' + str(set_ws))


if sys.argv[1] == 'fwd':
    CHANGE = workspace_changer().fwd()
elif sys.argv[1] == 'bwd':
    CHANGE = workspace_changer().bwd()
