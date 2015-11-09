from easyprocess import Proc
from entrypoint2 import entrypoint
from pyvirtualdisplay.display import Display


def extract_version(txt):
    '''This function tries to extract the version from the help text
    '''
    words = txt.replace(',', ' ').split()
    version = None
    for x in reversed(words):
        if len(x) > 2:
            if x[0].lower() == 'v':
                x = x[1:]
            if '.' in x and x[0].isdigit():
                version = x
                break
    return version

def version():
    '''
    return eagle version. 
    It does not work without X!

    :rtype: string
    '''
    return extract_version(Proc('eagle -?').call().stdout)

@entrypoint
def print_version():
    with Display(visible=False):
        print (version())