
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real , self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real , self.imaginary - no.imaginary)       
        
    def __mul__(self, no):
        prod = complex(self.real , self.imaginary)*complex(no.real , no.imaginary)
        return Complex(prod.real , prod.imag)

    def __truediv__(self, no):
        div = complex(self.real , self.imaginary)/complex(no.real , no.imaginary)
        return Complex(div.real , div.imag)


    def mod(self):
        m = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(m,0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    
