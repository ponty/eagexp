from eagexp import image

brd='~/.eagle/projects/examples/singlesided/singlesided.brd'

image.export_image(brd, 'docs/api_brd_50.png' , resolution=50)
image.export_image(brd, 'docs/api_brd_100.png', resolution=100)
image.export_image(brd, 'docs/api_brd_150.png', resolution=150)
