""" Loads a file containing closed class words to be used in automatic
    exclusion of words from lexicons

    LAST EXAMINED: 8-23-18
	LAST CODED: 2018?
    STATUS: - used in dissertation to remove previously compiled set of closed class words
            - works as desired


 """
from completed_projects.rajaram_dissertation.locations import Locations

class ClosedClass():
    def __init__(self):
        self.l = Locations()
        self.myBASE = self.l.mybase
        self.closedclass = set()
        self.loadClosedClass()

    def loadClosedClass(self):
        closed_file = self.l.closed_class
        f = open(closed_file, "r")
        closedLines = f.readlines()
        f.close()
        for line in closedLines:
            line = line.rstrip('\n')
            words = line.split(' ')
            for word in words:
                self.closedclass.add(word)
                self.closedclass.add(word+"'s")
                self.closedclass.add(word+"'")

if __name__ == "__main__":

    TEST = ClosedClass()
    print(len(TEST.closedclass))