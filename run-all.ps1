# Run backend and frontend in separate PowerShell windows
# Assumes you already created the Python venv (.venv) in backend and installed npm deps in frontend

$backendArgs = "-NoExit -Command cd \"$PSScriptRoot\backend\"; if (Test-Path .venv) { . .\.venv\Scripts\Activate.ps1 }; uvicorn app.main:app --reload --port 8000"
Start-Process -FilePath powershell -ArgumentList $backendArgs

$frontendArgs = "-NoExit -Command cd \"$PSScriptRoot\frontend\"; npm run dev"
Start-Process -FilePath powershell -ArgumentList $frontendArgs
