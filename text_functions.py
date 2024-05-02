import sys,time

class Text():
    def slow_print(str):
        for c in str + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(2./90)
            time.sleep(4./90)

    def fast_print(str):
        for c in str + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1./90)
    
    def delete():
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
    
    def delete_all(x):
        i = 0
        while i < x:
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            i += 1