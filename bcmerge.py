#!/usr/bin/env python
import sys
import os
import pprint
import subprocess


DIFF3 = "/usr/bin/bcompare"

MINE  = sys.argv[-3]
MINE_TITLE = sys.argv[4]
OLDER = sys.argv[-2]
OLDER_TITLE = sys.argv[6]
YOURS = sys.argv[-1]
YOURS_TITLE = sys.argv[8]
OUT = MINE + ".bcmerge"

p = subprocess.Popen([DIFF3, 
                      MINE,
                      YOURS,
                      OLDER,
                      OUT,
                      "-title1=" + MINE_TITLE,
                      "-title2=" + YOURS_TITLE,
                      "-title3=" + OLDER_TITLE,
                      "-automerge",
                      "-reviewconflicts"
])
p.wait()

f = open(OUT)
print f.read()

if p.returncode == 101:
    sys.exit(1)
elif p.returncode == 1:
    sys.exit(-1)
else:
    sys.exit(p.returncode)
