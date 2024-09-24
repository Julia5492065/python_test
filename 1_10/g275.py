n=int(input())
w=list()
f_aws=""
try:
    def compare(v1,v2):
        total=""
        if v1[1]==v1[3] or v1[1]!=v1[5] or v2[1]==v2[3] or v2[1]!=v2[5]:
            total+="A"
        if int(v1[6]) == 0 or int(v2[6]) == 1:
            total+="B"
        if v1[1]==v2[1] or v1[3]==v2[3] or v1[5]==v2[5]:
            total+="C"
        return total
           
    if 1<=n<=30:
        #3[0,1 /2,3 /4,5] i:[0,1,2] j:[0,1]
        for i in range(n):
            for j in range(2):
                w.append(input().replace(' ',''))  
            aws=compare(w[2*i],w[2*i+1]) #兩兩比較
            f_aws+=aws+"\n"
            if aws=="":
                f_aws+="None\n"
        # f_aws[-1].replace('\n','')
        print(f_aws)
except ValueError:
    print()
