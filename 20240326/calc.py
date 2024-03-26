class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        """
        Adds two numbers and returns the result.
        """
        result = num1 + num2
        return result

    def subtract(self, num1, num2):
        """
        Subtracts num2 from num1 and returns the result.
        """
        #result = num2 - num1 
        result = num1 - num2    # keep an eye on the correct order
        return result

    def multiply(self, num1, num2):
        """
        Multiplies two numbers and returns the result.
        """
        if isinstance(num1,str):    # strings can't be multiplied, they just print the string multiple times
            try:
                num1 = int(num1)    # try to cast the string to something numeric
            except ValueError:
                num1=1              # if not possible, give back, what ever you want
                
        if isinstance(num2,str):
            try:
                num2 = int(num2)
            except ValueError:
                num2=1
            
        result = num1 * num2
        return result

    def divide(self, num1, num2):
        """
        Divides num1 by num2 and returns the result.
        """
        if num2 == 0:   # you can't devide by 0 of cause...either you just try to prefent it
        #     print("devision by 0 is not possible")
        #     return 0
            raise ZeroDivisionError     # or know this might happen and handle ist where the func. is called
        
        
        result = num1 / num2
        return result

    def power(self, base, exponent):
        """
        Calculates the power of base raised to the exponent and returns the result.
        """
        result = base ** exponent
        return result

    def factorial(self, num):
        """
        Calculates the factorial of a number and returns the result.
        """
        # ! - 5! -> 5*4*3*2*1
        if num < 0: # factorial is not possible for negative value...either don't use them, or use the absolut value
            num = num * -1
            
        result = 1
        for i in range(1, num + 1): # range has to start from 1, not 0 (5*4*3*2*1*0 is 0)
            result *= i
        return result
    
# Testing the Calculator class
if __name__ == "__main__":
    calc = Calculator()

    # Test add function
    print(f"Addition: {calc.add(5, 3)}")

    # Test subtract function
    print(f"Subtraction: {calc.subtract(5, 3)}")

    # Test multiply function
    print(f"Multiplication: {calc.multiply(5, '3')}")

    # Test divide function
    try:
        print(f"Division: {calc.divide(5, 0)}")
    except ZeroDivisionError:
        print("Devision by 0 is not possible!")
        
    # Test power function
    print(f"Power: {calc.power(2, 3)}")

    # Test factorial function
    print(f"Factorial: {calc.factorial(-5)}")