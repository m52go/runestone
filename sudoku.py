class Sudoku(object):
    def __init__(self, loc=None):
        filename = "sudoku.txt" if not loc else loc
        h = self.makeboard(filename)
        self.rows = self.makerows(h)
        self.cols= self.makecols(self.rows)
        self.quadrants = self.makequads(self.rows)
        self.contains = self.makecontains()
        self.poss = {}
        self.allnums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def getcontain(self):
        templist = [] # list of numbers in current row, column, and quadrant
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                templist = self.rows[j] + self.cols[i] + self.quadrants[(j/3,i/3)]
                templist = set([k for k in templist if k != -1])
                self.contains[(i, j)] = self.contains[(i, j)].union(templist)
                templist = []

    def getposs(self):
        for i, j in self.contains.items():
            self.poss.update({i: self.allnums.difference(j)})
    
    def fillones(self):
        for i, j in self.poss.items():
            if len(j) == 1:
                self.makeEntry(i, j)
    
    def twos(self):
        twos = []
        for i, j in self.poss.items():
            if len(j) == 2:
                twos.append((i, j))
        print(twos)

    def solve(self):
        self.getcontain()
        self.getposs()
        self.fillones()
        self.twos()

    def makeEntry(self, i, j):
        self.rows[i[0]][i[1]] = j

    @staticmethod
    def makeboard(loc):
        # open file with data, store in h
        h = []
        with open(loc, 'r') as f:
            for line in f:
                for i in line.split(','):
                    h.append(int(i))
        return(h)

    @staticmethod
    def makerows(h):
        hi = []
        for i in range(1, 10):
            hi.append(h[(i*9 - 9) : i*9])
        return(hi)
    
    @staticmethod
    def makecols(hi):
        ci = []
        for i in range(9):
            ci.append([])
        for i in range(9):
            for j in range(9):
                ci[j].extend([hi[i][j]])
        return(ci)
       
    @staticmethod
    def makequads(hi): 
        qi = {}
        for i in range(3):
            for j in range(3):
                qi.update({(i, j):[]})
        for i in range(len(hi)):
            for j in range(len(hi[i])):
                qi[(i/3, j/3)].append(hi[i][j])
        return(qi)

    @staticmethod
    def makecontains():
        contains = {}
        for i in range(9):
            for j in range(9):
                contains.update({(i, j): set()})
        return(contains)

    def __repr__(self):
        returnstr = "-------------------------\n"
        for i in self.rows:
            returnstr += "  ".join([str(j) for j in i]) + "\n"
            if((self.rows.index(i)+1)%3 == 0):
                returnstr += "-------------------------\n"
        returnstr = returnstr.replace("-1", " ")
        return returnstr
