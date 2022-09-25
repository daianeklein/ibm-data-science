try:
    #a = {}
    print(a)
except NameError as erro:
    print('Developer error')
except (IndexError, KeyError) as erro:
    print('Index or key error')
except Exception as erro:
    print('unexpected error!')
else:
    pass

    print('Keep going')