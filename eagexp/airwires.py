import tempfile
from os.path import join

from eagexp.cmd import command_eagle
from eagexp.util import norm_path, read_text, write_text

ulp_templ = r"""
int count=0;

if (board) {
    board(B) {
        B.signals(S) {
            S.wires(W) {
                if (W.layer == 19) {
                    count++;
                }
            }
        }
    }
  output("FILE_NAME", "wt")
  {
    printf("%d\n", count);
  };
}
"""


def airwires(board, showgui=0):
    "search for airwires in eagle board"
    with tempfile.TemporaryDirectory() as temp_dir:
        board = norm_path(board)

        file_out = join(temp_dir, "out.txt")

        ulp = ulp_templ.replace("FILE_NAME", file_out)

        file_ulp = join(temp_dir, "out.ulp")
        write_text(file_ulp, ulp)

        commands = [
            "run " + file_ulp,
            "quit",
        ]
        command_eagle(board, commands=commands, showgui=showgui)

        n = int(read_text(file_out))

        return n
