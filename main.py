def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################
    
    inta = int(input('Enter an integer that is greater than 1  ')) 
    intb = int(input('Enter an integer that is greater than 1 and is greater than the first integer  '))
    
    if inta <= 1 or intb <= 1 or intb < inta:
        print ('Try again with the correct format')
    else:
        for i in range (inta, intb + 1):
            count = 0
            for j in range (2, i):
                if i % j == 0:
                    count = count + 1
                    break
            if count == 0:
                plist.append(i)
        print (plist)        
            
                
  
            
        
        

    return plist


if __name__ == '__main__':
    main()
