def print_stars(n) :
    i = 1;
    for i in range(1,n+1) :
        print('*'*i );
        i += 1;
    return 'end';
a = int(input("請選擇最大星星數： "));
print(print_stars(a));