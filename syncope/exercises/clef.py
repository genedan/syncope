
from textwrap import dedent


from syncope.lilypond import run_ly


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

run_ly(filename='syncope/cache/tmp.ly')
