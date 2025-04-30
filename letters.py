seq = "AAAAABBBBCCCDDE"


l = list(seq)
# count = 1

# n = []
# for i in range (len(seq)):
#     if i == 0:
#         count+=1
#     elif seq[i] == seq[i-1]:
#         count+=1
#     else:
#         n.append(f"{l[i]}" + f"{count}")
#         count = 1
#     print(count)
# print(n)

# count = 0 
# n = []
# for i in range (len(seq)):
#     if i == 0 and l[i] != l[i+1]:
#         count = 1
#         n.append(f"{l[i]}" + f"{count}")
#     elif i == 0 and l[i] == l[i+1]:
#         count = 1
#     elif i > 0:
#         if l[i] == l[i-1]:
#             count+=1
#         else:
#             n.append(f"{l[i]}" + f"{count}")
#             count = 0
# print (n)


count = 0

n = []
for i in range (len(seq)):
    if i == 0:
        count+=1
    elif i == len(seq):
        count+=1
        n.append(f"{l[i]}" + f"{count}")
    elif i > 0 and i < len(seq):
        if seq[i] == seq[i-1]:
            count+=1
        else:
            n.append(f"{l[i-1]}" + f"{count}")
            count = 1
    
print (n)
    