#!/usr/bin/env bash
set -e

# start-all.sh
# Opens two terminals (if possible) and runs the backend (uvicorn) and frontend (npm run dev).
# Works on macOS (Terminal) and common Linux desktop terminals. Falls back to background run.

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

echo "Starting backend and frontend from: $ROOT_DIR"

if [ "$(uname)" = "Darwin" ]; then
  # macOS: use Terminal.app to open new windows and run commands
  echo "Detected macOS — opening Terminal windows..."
  /usr/bin/osascript <<EOF
tell application "Terminal"
    do script "cd '$BACKEND_DIR'; if [ -f .venv/bin/activate ]; then . .venv/bin/activate; fi; uvicorn app.main:app --reload --port 8000"
    do script "cd '$FRONTEND_DIR'; npm run dev"
    activate
end tell
EOF
  exit 0
fi

# Linux: try several terminal emulators
if command -v gnome-terminal >/dev/null 2>&1; then
  echo "Using gnome-terminal"
  gnome-terminal -- bash -ic "cd '$BACKEND_DIR'; if [ -f .venv/bin/activate ]; then . .venv/bin/activate; fi; uvicorn app.main:app --reload --port 8000; exec bash" \
                 -- bash -ic "cd '$FRONTEND_DIR'; npm run dev; exec bash"
  exit 0
fi

if command -v konsole >/dev/null 2>&1; then
  echo "Using konsole"
  konsole -e bash -c "cd '$BACKEND_DIR'; if [ -f .venv/bin/activate ]; then . .venv/bin/activate; fi; uvicorn app.main:app --reload --port 8000; exec bash" &
  konsole -e bash -c "cd '$FRONTEND_DIR'; npm run dev; exec bash" &
  exit 0
fi

if command -v x-terminal-emulator >/dev/null 2>&1; then
  echo "Using x-terminal-emulator"
  x-terminal-emulator -e bash -c "cd '$BACKEND_DIR'; if [ -f .venv/bin/activate ]; then . .venv/bin/activate; fi; uvicorn app.main:app --reload --port 8000; exec bash" &
  x-terminal-emulator -e bash -c "cd '$FRONTEND_DIR'; npm run dev; exec bash" &
  exit 0
fi

# Last resort: run in background in the same terminal
echo "No supported terminal emulator found — running processes in background."

(cd "$BACKEND_DIR" && if [ -f .venv/bin/activate ]; then . .venv/bin/activate; fi; uvicorn app.main:app --reload --port 8000 &) 
(cd "$FRONTEND_DIR" && npm run dev &) 

echo "Started backend and frontend in background. Use 'ps' to see running processes or check logs."
