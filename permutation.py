from itertools import permutations
def  calcpermute(setence):
    list1=list(setence.split())
    # print(list1)
    permetute=permutations(list1)
    # print(permetute)
    for i in permetute:
        permetutelist=list(i)
        # print(permetutelist)
        for j in permetutelist:
            print(j,end=" ")
        print()
if __name__=="__main__":
    setence="sky is blue"
    calcpermute(setence)
