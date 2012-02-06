from eagexp import __version__
from eagexp.cmd import command_eagle
from eagexp.exp import export_command
from eagexp.util import norm_path
from entrypoint2 import entrypoint
from path import path
import logging
import os
import tempfile

log = logging.getLogger(__name__)
log.debug('version=' + __version__)


    
def export_partlist_to_file(input, output, timeout=20, showgui=False):
    '''
    call eagle and export sch or brd to partlist text file
    
    :param input: .sch or .brd file name
    :param output: text file name
    :param timeout: int
    :param showgui: Bool, True -> do not hide eagle GUI
    :rtype: None    
    '''
    input=norm_path(input)
    output=norm_path(output)

    commands = export_command(output=output, output_type='partlist')
    command_eagle(input=input, timeout=timeout, commands=commands, showgui=showgui)

    
def header_index(lines):
    for i, x in enumerate(lines):
        if '   ' in x:
            return i
        
def parse_partlist(str):
    '''parse partlist text delivered by eagle.
    
    header is converted to lowercase
    
    :param str: input string
    :rtype: tuple of header list and dict list: (['part','value',..], [{'part':'C1', 'value':'1n'}, ..])    
    '''
    lines = str.strip().splitlines()
    lines = filter(len, lines)
    hind = header_index(lines)
    if hind is None:
        log.debug('empty partlist found')
        return ([], [])

    header_line = lines[hind]
    header = header_line.split('  ')
    header = filter(len, header)
    positions = [header_line.index(x) for x in header]
    header = [x.strip().split()[0].lower() for x in  header]
    
    
    data_lines = lines[hind + 1:]
    
    def parse_data_line(line):
        y = [(h, line[pos1:pos2].strip()) for h, pos1, pos2 in zip(header, positions , positions[1:] + [1000]) ]
        return dict(y)
    
    data = [parse_data_line(x) for x in data_lines]
    return (header, data)
    
    
    
    
def raw_partlist(input, timeout=20, showgui=False):
    '''export partlist by eagle, then return it
    
    :param input: .sch or .brd file name
    :param timeout: int
    :param showgui: Bool, True -> do not hide eagle GUI
    :rtype: string    
    '''
    
    output = tempfile.NamedTemporaryFile(prefix='eagexp_', suffix='.partlist', delete=0).name
    export_partlist_to_file(input=input, output=output, timeout=timeout, showgui=showgui)
    s = open(output).read()
    os.remove(output)
    return s

def structured_partlist(input, timeout=20, showgui=False):
    '''export partlist by eagle, then parse it
    
    :param input: .sch or .brd file name
    :param timeout: int
    :param showgui: Bool, True -> do not hide eagle GUI
    :rtype: tuple of header list and dict list: (['part','value',..], [{'part':'C1', 'value':'1n'}, ..])    
    '''
    
    s = raw_partlist(input=input, timeout=timeout, showgui=showgui)
    return parse_partlist(s)
    
@entrypoint
def print_partlist(input, timeout=20, showgui=False):
    '''print partlist text delivered by eagle
    
    :param input: .sch or .brd file name
    :param timeout: int
    :param showgui: Bool, True -> do not hide eagle GUI
    :rtype: None    
    '''
    print raw_partlist(input=input, timeout=timeout, showgui=showgui)
