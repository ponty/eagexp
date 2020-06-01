from backports import tempfile
from path import Path

from eagexp.cmd import command_eagle

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
        board = Path(board).expand().abspath()

        file_out = Path(temp_dir) / "out.txt"

        ulp = ulp_templ.replace("FILE_NAME", file_out)

        file_ulp = Path(temp_dir) / "out.ulp"
        file_ulp.write_text(ulp.encode("utf-8"))

        commands = [
            "run " + file_ulp,
            "quit",
        ]
        command_eagle(board, commands=commands, showgui=showgui)

        n = int(file_out.text())

        return n
