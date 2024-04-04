import sys,time

class Text():
    
    def sprint(str):
        for c in str + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(2./90)
    
    def delete():
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

    