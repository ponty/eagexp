from eagexp.airwires import airwires

brd1 = '/usr/share/eagle/projects/examples/singlesided/singlesided.brd'
brd2 = '/usr/share/eagle/projects/examples/tutorial/demo2.brd'

if __name__ == "__main__":
    print( airwires(brd1) )    
    print( airwires(brd2) )

