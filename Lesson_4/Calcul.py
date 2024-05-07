class Calculator:
    
    def sum(self, a, b):
        c = a + b
        return c
    
    def sub(self, a, b):
        d = a - b
        return d
    
    def mult(self, a, b):
        c = a * b
        return c
    
    def div(self, a, b):
        if (b == 0):
            raise ArithmeticError("на 0 делить нельзя")
        
        return (a / b)
    
 
    def pow(self, a, b=2):
        c = a ** b
        return c
    
    def avg(self, nums):
        if (len(nums)==0):
            return 0
              
        c = 0
        for i in nums:
            c = self.sum(c, i)
           
        return self.div(c, len(nums))
        
        

 

