class Fraction():
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    @staticmethod 
    def gcd(num1, num2):
        while (num1 % num2) != 0:
            num1, num2 = num2, num1%num2
        return(num2)

    def __add__(self, frac):
        num = (self.num * frac.den) + (frac.num * self.den)
        den = self.den * frac.den
        newgcd = self.gcd(num, den)
        return(Fraction(num/newgcd, den/newgcd))

    def __sub__(self, frac):
        num = (self.num * frac.den) - (frac.num * self.den)
        den = self.den * frac.den
        newgcd = self.gcd(num, den)
        return(Fraction(num/newgcd, den/newgcd))

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
        newgcd = self.gcd(num, den)
        return(Fraction(num/newgcd, den/newgcd))

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
