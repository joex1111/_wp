def find_max(number) :
    if not number :
        return None;
    max_num = number[0];
    for now in number[1:] :
        if now > max_num :
            max_num = now;
    return max_num;
a = [1,3,6,8,5];
print(find_max(a));
print(a);