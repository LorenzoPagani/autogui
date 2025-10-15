"""Helper script to build an executable for autoguiexercise.py using PyInstaller.

Usage:
    python build.py [--clean] [--onefile]

This script will create a virtual environment in .venv, install requirements, install pyinstaller,
and then call pyinstaller to produce the exe.
"""

import argparse
import os
import shutil
import subprocess
import sys


ROOT = os.path.abspath(os.path.dirname(__file__))
VENV_DIR = os.path.join(ROOT, '.venv')


def run(cmd, **kwargs):
    print('> ' + ' '.join(cmd))
    subprocess.check_call(cmd, **kwargs)


def ensure_venv():
    if not os.path.exists(VENV_DIR):
        print('Creating virtual environment...')
        run([sys.executable, '-m', 'venv', VENV_DIR])


def activate_pip():
    if os.name == 'nt':
        python_exec = os.path.join(VENV_DIR, 'Scripts', 'python.exe')
    else:
        python_exec = os.path.join(VENV_DIR, 'bin', 'python')
    return python_exec


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true')
    parser.add_argument('--onefile', action='store_true', default=True)
    args = parser.parse_args()

    ensure_venv()
    python_exec = activate_pip()

    print('Upgrading pip and installing dependencies...')
    run([python_exec, '-m', 'pip', 'install', '--upgrade', 'pip'])
    run([python_exec, '-m', 'pip', 'install', '-r', os.path.join(ROOT, 'requirements.txt')])
    run([python_exec, '-m', 'pip', 'install', 'pyinstaller'])

    if args.clean:
        for p in ('build', 'dist', 'autoguiexercise.spec'):
            pth = os.path.join(ROOT, p)
            if os.path.exists(pth):
                print('Removing', pth)
                if os.path.isdir(pth):
                    shutil.rmtree(pth)
                else:
                    os.remove(pth)

    cmd = [python_exec, '-m', 'PyInstaller', '--noconfirm']
    if args.onefile:
        cmd.append('--onefile')
    cmd += ['--console', os.path.join(ROOT, 'autoguiexercise.py')]
    print('Running PyInstaller...')
    run(cmd)

    print('\nBuild complete. Check the dist/ folder for the executable.')


if __name__ == '__main__':
    main()
