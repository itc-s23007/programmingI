def test_function():
    try:
        print('try')
        return
    except:
        print('else')
    finally:
        print('finally')

test_function()

A = 1
