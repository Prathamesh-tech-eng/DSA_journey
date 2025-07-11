import string
def print_rangoli_size(n):
    
    width = 4*n - 3
    half = (n-1)//2
    p1 = "-"

    letters = list(string.ascii_lowercase)
    lst1 = letters[:n]                 #lst1 = ['a', 'b', 'c', 'd']
                                    #lst2 = ['d', 'c', 'b', 'a']
    lst2 = lst1[::-1]
    lst3 = []

   #Upper Part
    for i in range(n):                # i = 0 to 4 lst3 = [['d'], ['d', 'c'], ['d', 'c', 'b'], ['d', 'c', 'b', 'a']]
        lst3.append(lst2[:i+1])
        lst3[i].extend(lst1[n-i:])
        p2 = "-".join(lst3[i])
        p1_width = (width - len(p2))//2
        print((p1*p1_width) + p2 + (p1*p1_width))

    #Lower Part
    for i in range(n-2,-1,-1):                # i = 0 to 4 lst3 = [['d'], ['d', 'c'], ['d', 'c', 'b'], ['d', 'c', 'b', 'a']]
        lst3.append(lst2[:i+1])
        #lst3[i].extend(lst1[i:])
        p2 = "-".join(lst3[i])
        p1_width = (width - len(p2))//2
        print((p1*p1_width) + p2 + (p1*p1_width))

print_rangoli_size(10)



