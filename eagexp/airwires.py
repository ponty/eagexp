from eagexp.cmd import command_eagle
from path import Path
import tempfile


ulp_templ = r'''
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
'''


def airwires(board, showgui=0):
    'search for airwires in eagle board'
    board = Path(board).expand().abspath()

    file_out = tempfile.NamedTemporaryFile(suffix='.txt', delete=0)
    file_out.close()

    ulp = ulp_templ.replace('FILE_NAME', file_out.name)

    file_ulp = tempfile.NamedTemporaryFile(suffix='.ulp', delete=0)
    file_ulp.write(ulp.encode('utf-8'))
    file_ulp.close()

    commands = [
        'run ' + file_ulp.name,
        'quit',
    ]
    command_eagle(board, commands=commands, showgui=showgui)

    n = int(Path(file_out.name).text())

    Path(file_out.name).remove()
    Path(file_ulp.name).remove()

    return n
