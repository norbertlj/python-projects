import sys, getopt, os

class FileDoesNotExistError(Exception):
  pass

class File:
  def __init__(self, name, path = ''):
    self.name = os.path.normpath(name)
    self.relpath = os.path.normpath(path + os.sep + name) if path != '' else self.name
    if not os.path.exists(self.relpath):
      raise FileDoesNotExistError(f"{self.relpath} does not exist!")
    self.is_dir = os.path.isdir(self.relpath)
    self.is_hidden = self.name.startswith('.') and self.name != '.'
      

class Dirtree:
  INDENT_MULTIPLAYER = 3
  NO_DIR_IND = '|  '
  MID_DIR_IND = '├──'
  END_DIR_IND = '└──'
  EMPTY_IND = '   '
  
  def __init__(self, current_dir, show_hidden = False):
    self.current_dir = File(current_dir)
    self.show_hidden = show_hidden
  
  def print(self):
    self._print_level(self.current_dir)
  
  def _print_level(self, _dir, _parents = [], _last = []):
    if self.show_hidden or not _dir.is_hidden:
      _indent = ""
      if _parents:
        for i in range(0, len(_parents) - 1):
          if _parents[i]:
            _indent += self.EMPTY_IND if _last[i] else self.NO_DIR_IND
        _indent += self.END_DIR_IND if _last[-1] else self.MID_DIR_IND
      print(f"{_indent}{_dir.name}")
      if _dir.is_dir:
        _list = os.listdir(_dir.relpath)
        for _f in range(0, len(_list)):
          _p = _parents.copy()
          _p.append(True)
          _file = File(_list[_f], _dir.relpath)
          _l = _last.copy()
          _l.append(False if _f < len(_list) - 1 else True)
          self._print_level(_file, _p, _l)

def main(argv):
  show_hidden = False
  try:
    opts, args = getopt.getopt(argv, 'ah', ['all', 'help'] )
  except getopt.GetoptError:
    print('dirtree.py [directory]')
    sys.exit(1)
  for opt, arg in opts:
    if opt == '-a' or opt == '--all':
      show_hidden = True
    elif opt == '-h' or opt == '--help':
      print('''dirtree.py [directory]

Prints directory tree. By default prints current directory.
-a, --all        Prints hidden files and directories.
-h, --help       Prints this help message.''')
      sys.exit()
  current_directory = args[0] if len(args) > 0 else './'
  dtree = Dirtree(current_directory, show_hidden)
  dtree.print()

if __name__ == "__main__":
  main(sys.argv[1:])