#! /usr/bin/env python

import datetime
import generate_all_possible as gap

def main():
    """workaround for known issue http://bugs.python.org/issue5509"""
    now = datetime.datetime.now
    print now()
    print 'Making root...'
    root = gap.make_root()
    print now()
    print 'Dumping root to %s...' % gap.PICKLE_FILENAME
    gap.dump_root(root)
    print now()

if __name__ == '__main__':
    main()
