def classify_even_odd(numbers) :
    if not numbers :
        return None;
    d = {
        'singular' : [] ,
        'even' : []
    }
    for n in numbers :
        if n % 2 == 0 :
            d['even'].append(n);
        else :
            d['singular'].append(n);
    return d;
a = [6,5,4,3,2,1,0];
print(classify_even_odd(a));