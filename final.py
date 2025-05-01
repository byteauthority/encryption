
def zip(data):  
    count = 0
    new = []
    for i in range (len(data)):
        if i == 0:
            count = 1

        elif len(data)-1 == i:
            if data[i] != data[i-1]:
                new.append(f'{data[i-1]}'+f'{count}')
                # print(f'{data[i-1]}'+f'{count}')
                count = 1
                new.append(f'{data[i]}'+f'{count}')
                # print(f'{data[i]}'+f'{count}')
            else:
                count+=1
                new.append(f'{data[i]}'+f'{count}')
                # print(f'{data[i]}'+f'{count}')
        elif i > 0 and data[i] == data[i-1]:
            count+=1
        elif i > 0 and data[i] != data[i-1]:
            new.append(f'{data[i-1]}'+f'{count}')
            # print(f'{data[i-1]}'+f'{count}')
            count = 1
    return (''.join(new))

def unzip(zip):
    unzip = []

    for i in range(0,len(zip),2):
        unzip.append (f'{zip[i]}'* int(zip[i+1]))

    unzip = ''.join(unzip)
    return (unzip)

user = input("Enter smth to compress: ")
print(zip(user))


user = input("Input smth to expand: ")
print (unzip(user))