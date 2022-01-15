import glob
import logging
import os

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyvirtualdisplay.smartdisplay import SmartDisplay

# (cmd,grab,background)
commands = [
    "python3 -m eagexp.examples.image_example",
    "python3 -m eagexp.examples.partlist_example",
    "python3 -m eagexp.examples.image3d_example",
    "python3 -m eagexp.examples.airwires",
    "python3 -m eagexp.image /usr/share/eagle/projects/examples/singlesided/singlesided.sch cli_sch.png",
    "python3 -m eagexp.partlist /usr/share/eagle/projects/examples/singlesided/singlesided.sch",
    "python3 -m eagexp.image /usr/share/eagle/projects/examples/singlesided/singlesided.brd cli_brd.png",
    "python3 -m eagexp.image3d /usr/share/eagle/projects/examples/singlesided/singlesided.brd cli_3d.png",
    "python3 -m eagexp.partlist /usr/share/eagle/projects/examples/singlesided/singlesided.brd",
    "python3 -m eagexp.image --help",
    "python3 -m eagexp.image3d --help",
    "python3 -m eagexp.partlist --help",
]

# python -m eagexp.image ~/.eagle/projects/examples/singlesided/singlesided.brd cli_brd.png


def empty_dir(dir):
    files = glob.glob(os.path.join(dir, "*"))
    for f in files:
        os.remove(f)


@entrypoint
def main():
    gendir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen")
    logging.info("gendir: %s", gendir)
    os.makedirs(gendir, exist_ok=True)
    empty_dir(gendir)
    pls = []
    try:
        os.chdir("gen")
        for cmd in commands:
            with SmartDisplay():
                logging.info("cmd: %s", cmd)
                fname_base = cmd.replace(" ", "_").replace("/", "_").replace("~", "_")
                fname = fname_base + ".txt"
                logging.info("cmd: %s", cmd)
                print("file name: %s" % fname)
                with open(fname, "w") as f:
                    f.write("$ " + cmd + "\n")
                    p = EasyProcess(cmd).call()
                    f.write(p.stdout)
                    f.write(p.stderr)
                    pls += [p]
    finally:
        os.chdir("..")
        for p in pls:
            p.stop()
    embedme = EasyProcess(["npx", "embedme", "../README.md"])
    embedme.call()
    print(embedme.stdout)
    assert embedme.return_code == 0
    assert "but file does not exist" not in embedme.stdout
