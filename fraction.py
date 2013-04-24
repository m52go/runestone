# a class that simulates fractions, i.e., a/b for some integers a and b instead
# representing them as floating-point numbers

class Fraction():
    def __init__(self, top, bottom):
        if(type(top) is int) and (type(bottom) is int):
            newgcd = self.gcd(top, bottom)
            self.num = top/newgcd
            self.den = bottom/newgcd
        else:
            raise RuntimeError("Non-integer input for new Fraction!")    

    @staticmethod 
    def gcd(num1, num2):
        while (num1 % num2) != 0:
            num1, num2 = num2, num1%num2
        return(num2)
    
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

    def __add__(self, frac):
        num = (self.num * frac.den) + (frac.num * self.den)
        den = self.den * frac.den
        return(Fraction(num, den))

    def __sub__(self, frac):
        num = (self.num * frac.den) - (frac.num * self.den)
        den = self.den * frac.den
        return(Fraction(num, den))

    def __eq__(self, frac):
        num = False; den = False
        if (self.num%frac.num == 0) or (frac.num%self.num == 0):
            num = True
        if (self.den%frac.den == 0) or (frac.den%self.den == 0):
            den = True
        return(num and den)

    def __mul__(self, frac):
        num = self.num * frac.num
        den = self.den * frac.den
        return(Fraction(num, den))

    def __div__(self, frac):
        reciprocal = Fraction(frac.den, frac.num)
        return(self.__mul__(reciprocal))

    def __gt__(self, frac):
        if self.num*frac.den > frac.num*self.den:
            return True
        return False

    def __lt__(self, frac):
        if self.num*frac.den < frac.num*self.den:
            return True
        return False

    def __unicode__(self):
        return("{}/{}".format(self.num, self.den))

    def __str__(self):
        return unicode(self).encode('utf-8')
