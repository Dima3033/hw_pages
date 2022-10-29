def rev():
    try:
        rev = input("rev - ")
        rec = rev[::-1]
        if rev == rec:
            print(f'{rev},паліндром')
        else:
            print(f'{rev}не паліндром')
    except Exception as ex:
        print(f'Erorr information: {ex}')
rev()