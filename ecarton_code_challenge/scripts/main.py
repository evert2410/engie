#!/usr/bin/env python

import sys
import json
from ecarton_code_challenge.lib.convert import convert_chars

from ecarton_code_challenge.lib.app import create_app


def main():
    """
    Doc String ... parse arguments using argparse.Argument_Parser ... etc
    """
    app = create_app()
    app.run('0.0.0.0')

    
if __name__ == '__main__':
    sys.exit(main())
