def incr2D(t):
    for row in t:
        for column in row:
            print(column+1, end=' ')
        print('')


t=[[4,7,2,5], [5,1,9,2],[8,3,6,6]]
a=incr2D(t)


