<#
.SYNOPSIS
    Build a single-file Windows executable from autoguiexercise.py using PyInstaller.

.NOTES
    - Run this from an elevated PowerShell if you need to install system-wide Python packages.
    - This script creates a virtual environment in .venv, installs requirements, installs PyInstaller,
      and runs the build to produce a single exe in the dist\ folder.

USAGE
    .\build_exe.ps1 [-Clean] [-OneFile]

#>

param(
    [switch]$Clean,
    [switch]$OneFile = $true
)

Set-StrictMode -Version Latest
cd $PSScriptRoot

function Write-Heading($m) { Write-Host "`n==> $m" -ForegroundColor Cyan }

Write-Heading 'Preparing virtual environment'
if (-Not (Test-Path -Path '.venv')) {
    py -3 -m venv .venv
}

Write-Heading 'Activating virtual environment'
. .\.venv\Scripts\Activate.ps1

Write-Heading 'Upgrading pip and installing dependencies'
py -3 -m pip install --upgrade pip
py -3 -m pip install -r requirements.txt

Write-Heading 'Installing PyInstaller'
py -3 -m pip install pyinstaller

if ($Clean) {
    Write-Heading 'Cleaning previous builds'
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue .\build, .\dist, .\autoguiexercise.spec
}

$onefileArg = $OneFile
Write-Heading 'Running PyInstaller (this can take a minute)'
if ($onefileArg) {
    py -3 -m PyInstaller --noconfirm --onefile --console .\autoguiexercise.py
}
else {
    py -3 -m PyInstaller --noconfirm --console .\autoguiexercise.py
}

Write-Heading 'Build finished'
Write-Host "Executable (if successful) will be in: $PWD\dist\" -ForegroundColor Green

Write-Heading 'Done'
