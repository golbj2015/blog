# test try/except raise
def fetcher(obj,index):
    try:
        return obj[index]
    except IndexError:
        print "out index error"
        raise IndexError

class Bad(Exception):
    pass

def doomed():
    try:
        doomed()
    except Bad:
        print "bad excetion"

#try/finally
def fina():
    try:
        print "goto finally"
    finally:
        print "finally over"

#main 
if __name__=='__main__':
    print "start "
else:
    print "can not run"
    fetcher("aabc",4)
    doomed()
