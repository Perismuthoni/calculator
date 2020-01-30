
class Calculator(object):

    def __init__(self, num_one, num_two):
        self.num_one = float(num_one)
        self.num_two = float(num_two)
    
    def add(self):
        result = self.num_one + self.num_two
        return result

    def sub(self):
        result = self.num_one - self.num_two
        return result

    def mul(self):
        result = self.num_one * self.num_two
        return result

    def div (self):
        result = self.num_one / self.num_two
        return result  
         
    
