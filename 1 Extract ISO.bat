@echo off
where uv >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: uv is not installed or not in PATH
    echo Please install uv from https://docs.astral.sh/uv/getting-started/installation/
    pause
    exit /b 1
)

uv run scripts\extract_iso.py