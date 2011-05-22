'''
Example for 3D image export
'''
from eagexp import image3d

brd='~/.eagle/projects/examples/tutorial/demo2.brd'

image3d.export_image3d(brd, 'api_3d.png')

# size
image3d.export_image3d(brd, 'api_3d_size1.png', size=(50,50))
image3d.export_image3d(brd, 'api_3d_size2.png', size=(50,100))
image3d.export_image3d(brd, 'api_3d_size3.png', size=(100,50))

# rotate
image3d.export_image3d(brd, 'api_3d_xrot.png', pcb_rotate=(180,0,0), size=(200,150))
image3d.export_image3d(brd, 'api_3d_yrot1.png', pcb_rotate=(0,45,0), size=(200,150))
image3d.export_image3d(brd, 'api_3d_yrot2.png', pcb_rotate=(0,90,0), size=(200,150))
image3d.export_image3d(brd, 'api_3d_yrot3.png', pcb_rotate=(0,135,0), size=(200,150))

