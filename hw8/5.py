def grade(score):
    if 90 <= score <= 100:
        return 'a';
    elif 80 <= score <= 89:
        return 'b';
    elif 70 <= score <= 79:
        return 'c';
    elif 60 <= score <= 69:
        return 'd';
    elif 0 <= score <= 59:
        return 'e';
    else:
        return 'Invalid score';