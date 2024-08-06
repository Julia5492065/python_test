try:
    a=list(input())
    # print(" ".join(map(str, a)))
    if len(a)<1000:
        #切片反轉列表
        contra = a[::-1]
        if a==contra:
            print("yes")
        else:
            print("no")
except ValueError:
    print()