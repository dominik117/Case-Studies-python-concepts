import sys
from contextlib import contextmanager

@contextmanager
def add_path(path):
    sys.path.append(path)
    try:
        yield
    finally:
        sys.path.remove(path)

# Usage
with add_path('/path/to/directory'):
    # Import modules from '/path/to/directory'
    # After the block, the path is removed from sys.path
