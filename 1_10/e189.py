while True:
    try:
        n = int(input())

        if n % 3==0:
            print("YES")
        else:
           print("NO")
    
    except EOFError:
        break