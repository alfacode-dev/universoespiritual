#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
FRONTEND_DIR="$ROOT_DIR/frontend"
TARGET_DIR="$ROOT_DIR/src/frontend"

echo "Building frontend in $FRONTEND_DIR"
cd "$FRONTEND_DIR"
if ! command -v npm >/dev/null 2>&1; then
  echo "npm not found. Install Node.js and npm to build the frontend." >&2
  exit 2
fi
npm ci
npm run build

echo "Copying built files to $TARGET_DIR"
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"
cp -r "$FRONTEND_DIR/dist"/* "$TARGET_DIR/"
echo "Done. The backend will now serve the built frontend at /"
