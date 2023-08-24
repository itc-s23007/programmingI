x = 'Happy'
def evet1():
    print('In event1:', x, end=' ->')

def event2():
    x = 'Sad'
    print('In event2:', x, end=' ->')

def event3():
    global x
    x = 'Tired'
    print('In event3:', x, end=' -> ')

def event4():
    x = 'Excite'
    def happening():
        print('In event4:', c, end='->')
    happening()

def event5():
    x = 'Fun'
    def happening():
        nonlocal x
        x = 'Scare'
    happening()
    print('In event5:', x, end='->')

func_list = [event1, event2, event3, event4, event5]
for f in func_list:
    f()
    print('After {}: {}'.format(f.__name__, x))

In event1: (Happy)-> After event1:(Happy)
In event2: (Sad)-> After event2:(Happy)
In event3: (Tired)-> After event3:(Tired)
In event4: (Excite)-> After event4:(Tired)
In event5: (Scare)-> After event5:(Tired)
