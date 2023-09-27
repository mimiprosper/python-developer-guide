# enter an input i
i = int(input('Enter a number: '))

# while i is more than 5
while i > 5:
    # first print i
    print(i)
    # second minus 1 from i. go back check while condition 
    # and print the new i
    i -= i

# if i is not more than 5, execute the command below
else:
    print('Enter any number > 5')

