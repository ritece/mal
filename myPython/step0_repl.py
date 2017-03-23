import readline

readline.parse_and_bind('set editing-mode vi')

def READ(expression):
    return expression

def EVAL(expression):
    return expression

def PRINT(expression):
    print expression


def rep(expression):
    return PRINT(EVAL(READ(expression)))

while(True):
    expression = raw_input('user> ')
    rep(expression)
