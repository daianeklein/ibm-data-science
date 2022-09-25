try:
    a = {}
    print(a)
except NameError as erro:
    print('Developer error')
except (IndexError, KeyError) as erro:
    print('Index or key error')
except Exception as erro:
    print('unexpected error!')
else:
    print('Sucess!')
finally:
    pass

print('Keep going')


## example 02
try:
    b = 'hey'
    #a = 1/0
except NameError as erro:
    print('erro 01')
else:
    pass
finally:
    a = None

print(a)