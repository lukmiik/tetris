import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent.absolute()
if BASE_DIR not in sys.path:
    sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))
