def int2roman(value:int) -> str:
    
    alphabet = {'M':1000,
                'CM':900,
                'D':500,
                'CD':400,
                'C':100,
                'LC':90,
                'L':50,
                'XL':40,
                'X':10,
                'IX':9,
                'V':5,
                'IV':4,
                'I':1}
    
    # some rulz to mention...
    # if a smaller letter is in fromt of a bigger one, we need to substract
    # CM = 900 -> 1000 - 100
    # up o 3 times the same letter like XXX = 30
    
    result =""
    
    helper = value 
    
    while helper > 0:
        for letter in alphabet: # goint trough the given number
            #the number // the value of a letter will tell us, how often to write that letter
            xtimes = helper // alphabet[letter] # devide and round down to the next int (5//2=2)
            if xtimes > 0 and xtimes <= 3: # but the same letter is only possible 3 times in a row
                result += letter * (xtimes)
                # after we added the letter, we substract the value of the letters from our helper
                helper = helper - (xtimes) * alphabet[letter]
                
            #after that, we go to the next letter from our dictionary 
            #and if helper reaches 0, we should have all letters in our string
        
    return result


if __name__ == '__main__':
    print(int2roman(1911)) #MCMXI   
    print(int2roman(354)) #CCCLIV