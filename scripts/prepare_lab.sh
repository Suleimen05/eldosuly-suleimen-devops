#!/usr/bin/env bash
set -e

project_dir="$(cd "$(dirname "$0")/.." && pwd)"
cd "$project_dir"

mkdir -p logs backup

cat > logs/application.log <<'LOG'
INFO Application started
INFO Student page requested
WARNING Example configuration was not found
INFO Configuration loaded
INFO Database connection simulated
ERROR Example database connection failed
INFO Application restarted
WARNING Example memory usage is high
INFO Request received
ERROR Example request failed
INFO Application stopped
LOG

chmod 600 private.txt
chmod 644 public.txt
chmod +x scripts/Eldosuly_Suleimen_system.sh

echo 'Lab files and permissions are ready.'
