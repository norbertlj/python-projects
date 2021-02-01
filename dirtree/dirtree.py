import sys, getopt, os

class FileDoesNotExistError(Exception):
  pass

class File:
  def __init__(self, name, path = '', depth = 0):
    self.name = os.path.normpath(name)
    self.relpath = os.path.normpath(path + os.sep + name) if path != '' else self.name
    if not os.path.exists(self.relpath):
      raise FileDoesNotExistError(f"{self.relpath} does not exist!")
    self.is_dir = os.path.isdir(self.relpath)
    self.is_hidden = self.name.startswith('.') and self.name != '.'
    self.depth = depth

class Dirtree:
  INDENT_MULTIPLAYER = 3
  NO_DIR_IND = '|  '
  MID_DIR_IND = '├──'
  END_DIR_IND = '└──'
  EMPTY_IND = '   '

  def __init__(self, current_dir, show_hidden = False, max_depth = -999):
    self.current_dir = File(current_dir)
    self.show_hidden = show_hidden
    self.max_depth = max_depth

  def print(self):
    self._print_level(self.current_dir)

  def _print_level(self, _dir, _parents = [], _last = []):
    if self.max_depth < _dir.depth and self.max_depth != -999:
      return None
    if not self.show_hidden and _dir.is_hidden:
      return None
    _indent = ""
    # Prepare indention if node has parent (No indention for starting node)
    if _parents:
      for i in range(0, len(_parents) - 1):
        if _parents[i]:
          _indent += self.EMPTY_IND if _last[i] else self.NO_DIR_IND
      _indent += self.END_DIR_IND if _last[-1] else self.MID_DIR_IND
    print(f"{_indent}{_dir.name}")
    if _dir.is_dir:
      _d = _dir.depth + 1
      _list = os.listdir(_dir.relpath)
      for _f in range(0, len(_list)):
        _p = _parents.copy()
        _p.append(True)
        _file = File(_list[_f], path=_dir.relpath, depth=_dir.depth + 1)
        _l = _last.copy()
        _l.append(False if _f < len(_list) - 1 else True)
        self._print_level(_file, _p, _l)

def main(argv):
  show_hidden = False
  depth = -999
  try:
    opts, args = getopt.getopt(argv, 'ad:h', ['all', 'help', 'depth='] )
  except getopt.GetoptError:
    print('dirtree.py [directory]')
    sys.exit(1)
  for opt, arg in opts:
    if opt in ['-a', '--all']:
      show_hidden = True
    elif opt in ['-d', '--depth']:
      depth = int(arg)
    elif opt in ['-h', '--help']:
      print('''dirtree.py [directory]

Prints directory tree. By default prints current directory.
-a, --all        Prints hidden files and directories.
-d, --depth      Prints tree structure up to specific depth.
-h, --help       Prints this help message.''')
      sys.exit()
  current_directory = args[0] if len(args) > 0 else './'
  dtree = Dirtree(current_directory, show_hidden, depth)
  dtree.print()

if __name__ == "__main__":
  main(sys.argv[1:])