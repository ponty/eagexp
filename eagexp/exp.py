import os


def export_command(output, output_type, timeout=60, commands=[], showgui=False, resolution=None):
    def normpath(f):
        return os.path.abspath(os.path.expandvars(os.path.expanduser(f)))
        
    output = normpath(output)

    if resolution:
        resolution = int(resolution)
        if resolution > 2400 or resolution < 50:
            raise ValueError('resolution should be inrange 50-2400! current=' + str(resolution))
    else:
        resolution = ''
    
    if not commands:
        commands = []

    # popup window is displayed, if outfile exists
    if os.path.exists(output):
        os.remove(output)
    
    undo = len(commands)
    
    # redraw
    commands += ['WINDOW']
    
    commands += ['EXPORT {output_type} {output} {resolution}'.format(
        output_type=output_type, output=output, resolution=resolution)]
    
    # make UNDO, otherwise popup is displayed
    commands += ['UNDO'] * undo
    
    commands += ['QUIT']
    return commands
    

