
# program to check whether a word is palindrome or not
# coder: Subhashis Ghosh
def palindrome(x):
    '''
    This function returns whether word is palindrome or not.
    '''
    n1=x.replace(' ','')
    n2=n1[::-1]
    if n1==n2:
        print('The word is palindrome .')
    else:
        print('The word is not palindrome.')

word=input('Enter a word : ')

palindrome(word)
