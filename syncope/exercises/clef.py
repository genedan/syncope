from random import randint
from textwrap import dedent

from syncope.constants import CLEFS
from syncope.lilypond import run_ly

tmpclef = CLEFS[randint(0, 3)]


def make_tmpfile(clef):
    filestr = \
        dedent(
            """\
            \\version "2.22.1"
            {{
                \\relative {{
                  \\once \\override Staff.TimeSignature #'stencil = ##f
                  \\key c \\major
                  \\clef {}
                  s1
                }}
            }}""".format(clef)
        )

    with open('syncope/cache/tmp.ly', 'w') as outfile:
        outfile.write(filestr)
        outfile.close()


make_tmpfile(clef=tmpclef)

run_ly(filename='syncope/cache/tmp.ly')
