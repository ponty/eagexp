'''
Example for image export with various options
'''

from eagexp import image

brd='~/.eagle/projects/examples/tutorial/demo2.brd'

# set resolution in DPI
image.export_image(brd, 'api_brd_50.png' , resolution=50)
image.export_image(brd, 'api_brd_100.png', resolution=100)
image.export_image(brd, 'api_brd_150.png', resolution=150)

# mirror image
image.export_image(brd, 'api_brd_mirror.png', mirror=True)

# display only 2 layers
image.export_image(brd, 'api_brd_layer.png', layers=['dimension', 'pads'])

# display layer using eagle command
image.export_image(brd, 'api_brd_command.png', command='display none dimension')
