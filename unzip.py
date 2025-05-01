zip = 'A4B5N7K8'
unzip = []

for i in range(0,len(zip),2):
    unzip.append (f'{zip[i]}'* int(zip[i+1]))

unzip = ''.join(unzip)
print(unzip)