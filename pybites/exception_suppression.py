# this sounds like in general a bad idea, but trying it anyway

import os
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('/tmp/file-that-does-not-exist.tmp')
