from eagexp import partlist
import pprint

sch = "/usr/share/eagle/projects/examples/singlesided/singlesided.sch"
brd = "/usr/share/eagle/projects/examples/singlesided/singlesided.brd"

LINE = "-----------------------------"
pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    print("raw_partlist of " + sch)
    print(LINE)
    print(partlist.raw_partlist(sch))
    print(LINE)

    print()

    print("raw_partlist of " + brd)
    print(LINE)
    print(partlist.raw_partlist(brd))
    print(LINE)

    print()

    print("structured_partlist of " + sch)
    pp.pprint(partlist.structured_partlist(sch))

    print()

    print("structured_partlist of " + brd)
    pp.pprint(partlist.structured_partlist(brd))
