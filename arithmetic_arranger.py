def arithmetic_arranger(st,ans=False):
    key = 0
    total = ''
    if len(st)>5:
        error ='Error: Too many problems.'
        return error
    for i in range(len(st)):
        x = st[i].split()
        if not (x[1] =='+' or x[1] == '-'):
            error = 'Error: Operator must be \'+\' or \'-\'.'
            key = 1
            break
        if len(x[0])>4 or len(x[2])>4:
            error = 'Error: Numbers cannot be more than four digits.'
            key = 1
            break
        try:
            int(x[0])
            int(x[2])
        except:
            error = 'Error: Numbers must only contain digits.'
            key = 1
            break
    if key ==1:
        return error
    
    for i in range(len(st)):
        x = st[i].split()
        c = len(str(max(int(x[0]),int(x[2]))))
        if i == (len(st)-1):
            total = total + ('{}'.format(x[0].rjust(c+2)))
            break
        total = total + ('{}    '.format(x[0].rjust(c+2)))

    total = total + '\n'
    for i in range(len(st)):
        x = st[i].split()
        c = len(str(max(int(x[0]),int(x[2]))))
        if i == (len(st)-1):
            total = total + ('{}{}'.format(x[1],x[2].rjust(c+1)))
            break
        total = total + ('{}{}    '.format(x[1],x[2].rjust(c+1)))

    total = total+'\n'
    for i in range(len(st)):
        x = st[i].split()
        c = len(str(max(int(x[0]),int(x[2]))))
        if i == (len(st)-1):
            total = total + ('{}'.format('-'.rjust(c+2,'-')))
            break
        total = total + ('{}    '.format('-'.rjust(c+2,'-')))
    
    
    if ans == True:
        total = total+'\n'
        for i in range(len(st)):
            x = st[i].split()
            c = len(str(max(int(x[0]),int(x[2]))))
            if x[1] == '+':
                if i == (len(st)-1):
                    total = total + '{}'.format(str(int(x[0])+int(x[2])).rjust(c+2))
                    break
                total = total + '{}    '.format(str(int(x[0])+int(x[2])).rjust(c+2))
            elif x[1] == '-':
                if i == (len(st)-1):
                    total = total + '{}'.format(str(int(x[0])-int(x[2])).rjust(c+2))
                    break
                total = total + '{}    '.format(str(int(x[0])-int(x[2])).rjust(c+2))
    
    return total
