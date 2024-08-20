a = ['aa\n', 'asdasdasd\n']

for i in a:

    v = i.replace('\n' , '') 
    print(v)

    if 'aa' in i:
        print('asdasdasd')