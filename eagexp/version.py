from easyprocess import Proc, extract_version
from entrypoint2 import entrypoint

@entrypoint
def export_version():
    '''
    return eagle version
    
    :rtype: string
    '''
    return extract_version(Proc('eagle -?').call().stdout)