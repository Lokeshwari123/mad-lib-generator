# python implementation to check and replace palindrome 
def palindrome(string):
    if string==string[::-1]:
        return True
    else:
        return False
def getvale(sentence):
    list1=[]
    newlist=list(sentence.split())
    for i in newlist:
        if palindrome(i):
            list1.append(i)
    list1.sort()

    j=0
    for i in range(len(newlist)):
        if palindrome(newlist[i]):
            newlist[i]=list1[j]
            j+=1
    for i in newlist:
        print(i,end=" ")
sentence="please refer to thr madam to know the level"
getvale(sentence)