for i in range(1, 101):
    temp = ''
    if (i % 3 == 0):
        temp = temp + 'fizz'
    if (i % 5 == 0):
        temp = temp + 'buzz'
    if (temp == ''):
        temp = str(i)
    print(temp)