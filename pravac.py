import matplotlib.pyplot as plt

class line:
    def init(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.k = (self.y2-self.y1)/(self.x2-self.x1)
        self.l = self.k*(-self.x1) + self.y1
        self.x = []
        self.y = []

    def reset(self):
        del self.x1
        del self.x2
        del self.y1
        del self.y2
        del self.k
        del self.l
        del self.x 
        del self.y

    def find_the_equation(self):
        if self.k == 1:
            if self.l == 0:
                print ("Jednadzba pravca glasi: x")
            else:
                if self.l > 0:
                    print ("Jednadzba pravca glasi: x + {:.2f}".format(self.l))
                else:
                    print ("Jednadzba pravca glasi: x - {:.2f}".format(self.l))
        else:
            if self.l == 0:
                print ("Jednadzba pravca glasi: {:.2f}x".format(self.k))
            else:
                if self.l > 0:
                    print ("Jednadzba pravca glasi: {:.2f}x + {:.2f}".format(self.k,self.l))
                else:
                    print ("Jednadzba pravca glasi: {:.2f}x + {:.2f}".format(self.k,self.l))

    def __calculate(self,x):
        y = self.k * x + self.l
        self.x.append(x)
        self.y.append(y)
        return y
    
    def plot_the_line(self,a,b):
        x = a
        while x <= b:
            self.__calculate(x)
            x += 0.5
        plt.plot(self.x, self.y)
        plt.scatter(self.x1,self.y1, s = 50)
        plt.scatter(self.x2,self.y2, s = 50)
        plt.show()

    def does_it_pass(self,x,y):
        y1 = self.__calculate(x)
        if y == y1:
            print("Pravac prolazi kroz odabranu tocku.")
        else:
            print("Pravac ne prolazi kroz odabranu tocku.")