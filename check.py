#  for this work one have to install the termcolor module
try:
    from termcolor import colored, cprint
    cprint('Hello BitOverFlow', 'red', attrs=['blink'])
except:
    print("Hello BitOverFlow")
