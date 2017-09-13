# https://github.com/Surufel/surufel-scanner

import sys
import pyclamd
import os

# Python 2
#import Tkinter
#import tkMessageBox

# Python 3
import tkinter
from tkinter import messagebox

class SurufelCore:
    '''A Surufel core that does the magic.'''
    version = 1.001
    filesScannedCount = 0

    def __init__(self):
        if sys.platform == "darwin":
            try:
                self.scanner = pyclamd.ClamdAgnostic()
                self.scanner.ping()
            except pyclamd.ConnectionError:
                self.scanner = pyclamd.ClamdNetworkSocket()
                try:
                    self.scanner.ping()
                except pyclamd.ConnectionError:
                    raise ValueError('I could not connect to Unix or network socket.')
        elif sys.platform == "linux":
            pass
        elif sys.platform == "win32":
            # One day.
            pass

    def surufelReload(self):
        print(self.scanner.reload())

    def versionCallback(self):
        versionMessage = "Surufel Version: " + str(self.version) + "\n" + "pyClamd Version: " + self.scanner.version()
        messagebox.showinfo("Version", versionMessage)

    def fileScanner(self, file):
	    return self.scanner.scan_file(file)

    #def scanCurrentDirectory(self):


    def traverse(self):
        # Optimize with list_files.py
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                print(os.path.join(root, name))
        #for name in dirs:
        #    print(os.path.join(root, name))

    def scannerMainframe(self):
        front = tkinter.Tk()

        # Title
        front.title("Surufel Scanner Core")

        # Message
        message = "Program Information\n" + "Setting the scanner...\n"
        theFrontMessage = tkinter.Message(front, text=message, width=1000)
        theFrontMessage.pack()

        # Version
        versionButton = tkinter.Button(front, text="Version", command=self.versionCallback)
        versionButton.pack(side='left')

        # Quit Button
        quitButton = tkinter.Button(front, text="Quit", command=quit)
        quitButton.pack(side='left')

        # Loop
        front.mainloop()

def main():
    firstRun = SurufelCore()
    firstRun.scannerMainframe()

if __name__ == '__main__':
    main()
