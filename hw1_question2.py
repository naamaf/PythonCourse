def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False

def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.
    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    num = 100000
    count = 0
    while num < 1000000:
        if (is_palindrome(str(num)[2:]) == True) and (is_palindrome(str(num + 1)[1:]) == True) and (is_palindrome(str(num + 2)[1:5]) == True) and (is_palindrome(str(num + 3)[:6]) == True) and (len(str(num + 3)) == 6):
            print(num)
        num += 1


check_palindrome()