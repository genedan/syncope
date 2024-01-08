import subprocess


def run_ly(filename: str):
    subprocess.run(['lilypond', "-dcrop=#t", '-dresolution=500', '--png', filename])
