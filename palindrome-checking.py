n = int(input('Enter an integer number (negative or 0 to quit): '))

while n > 0:
    rev = 0
    temp = n
    
    while n != 0:
        rev = 10 * rev + n % 10
        n //= 10
        
    if temp == rev:
        print(temp, 'is Palindrome')
    else:
        print(temp, 'is not Palindrome')
        
    n = int(input('Enter an integer number (negative or 0 to quit): '))