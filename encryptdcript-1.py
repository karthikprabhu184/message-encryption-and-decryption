data=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
CH=int(input('enter as 1 for encrption and 2 for decryption'))
#print(len(data))
l=list(input('enter the sentance '))
l1=[]
l2=[]
'''for i in l:
    l1.append(i)
'''
def encr(l):
  for i in l:
    if i==' ' :
        l1.append(' ')

    else:

        i=str(i)
        i=i.upper()
        j = data.index(i)
        if j<23:
            j = data.index(i) + 3
            a = data[j]
            l1.append(a)
        else:
            j=j-25+2
            a = data[j]
            l1.append(a)
  return l1

def dcr(l):
        for i in l:
            if i == ' ':
                l1.append(' ')

            else:

                i = str(i)
                i = i.upper()
                j = data.index(i)
                if j >2:
                    j = data.index(i) - 3
                    a = data[j]
                    l2.append(a)
                else:
                    j = 25+j-2
                    a = data[j]
                    l2.append(a)


if CH==1:
    A=encr(l)
    ENCRY = ''
    for k in A:
     ENCRY = ENCRY + k


else:
    B=dcr(l)
    DCRY = ''
    for k in B:
        DCRY = DCRY + k

if CH==1:
 print(ENCRY)
else:
    print(DCRY)


