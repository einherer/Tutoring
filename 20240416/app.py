def average_root(numbers: list) -> int:
    
    # first number is root
    # 2nd 2 numbers are it's decendents
    # next (up to) 4 number are decentens of decendents and so on...
    
    #               4
    #            8          5
    #        0       1           6
    
    # (4+8+5+0+1+6)/6  => 24/6 = 4
    # (5+6)/2 = 5.5  => 5
    # (8+0+1)/3) => 3
    # 0 => 0
    # 1 => 1
    # 6 => 6
    # =>> 4+5+3+0+1+6 = 19/6 = 3
    
    number_of_elements = len(numbers)
    number_of_rows = 1
    max_elements = 0
    
    while True:
        max_elements = number_of_rows ** 2 - number_of_rows + 1
        if max_elements >= number_of_elements:
            break
        else:
            number_of_rows += 1
        
    rows = []
    
    for lni in range(1,number_of_rows):
            
    
    return root


if __name__ == "__main__":
    print(average_root(4,8,5,0,1,None,6)) # 5
    
    