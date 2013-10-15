import collections
import os

def init_syspath(rootpath):
    if 'syspath' not in globals():
        Path = collections.namedtuple("Path","BASE_PATH BASE_DIR DS")
        syspath = Path(
            rootpath,                   # BASE_PATH
            rootpath.split(os.sep)[-1], # BASE_DIR
            os.sep                      # DS
        )
        global syspath
        return True
