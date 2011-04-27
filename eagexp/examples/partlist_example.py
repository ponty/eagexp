from eagexp import partlist

sch='~/.eagle/projects/examples/singlesided/singlesided.sch'
brd='~/.eagle/projects/examples/singlesided/singlesided.brd'

print 'raw_partlist of '+sch
print "'''"
print partlist.raw_partlist(sch)
print "'''"

print

print 'raw_partlist of '+brd
print "'''"
print partlist.raw_partlist(brd)
print "'''"

print

print 'structured_partlist of '+sch
print partlist.structured_partlist(sch)

print

print 'structured_partlist of '+brd
print partlist.structured_partlist(brd)
