def roman2int(string: str) -> int:
    
    alphabet = {'M':1000,
                'D':500,
                'C':100,
                'L':50,
                'X':10,
                'V':5,
                'I':1}
    
    # some rulz to mention...
    # if a smaller letter is in fromt of a bigger one, we need to substract
    # CM = 900 -> 1000 - 100
    # up o 3 times the same letter like XXX = 30
    
    def go_through_string(letter, next):
        letter_value = alphabet.get(letter)
        
        if next:
            next_value = alphabet.get(next)
        else:
            next_value = 0
            
        if letter_value < next_value:
            letter_value = letter_value * (-1)
            
        return letter_value

    result = 0
    
    for i in range(len(string)):
        letter = string[i]
        try:
            next = string[i+1]
        except:
            next = None
        
        result += go_through_string(letter, next)
        
    return result


if __name__ == '__main__':
    print(roman2int("MCMXI")) #1911       
    print(roman2int("MCMXXIII")) #1923      
    print(roman2int("MMMDDDCCCLLLXXXVVVIII")) #4999      
        