#!/usr/bin/env bash
set -e

project_dir="$(cd "$(dirname "$0")/.." && pwd)"
info_file="$project_dir/Eldosuly_Suleimen_info.txt"

echo '=============================='
echo 'Student Information'
echo '=============================='
echo 'Name: Сүлеймен'
echo 'Surname: Елдосұлы'
echo 'Group: IT2-2310'
echo 'Student ID: 38320'
echo
echo '=============================='
echo 'System Information'
echo '=============================='
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -s)"
echo "Disk Usage: $(df -h / | tail -n 1)"
echo "Memory Usage: $(free -h | grep '^Mem:')"
echo

if [ -f "$info_file" ]; then
    echo 'Student information file exists.'
else
    echo 'Student information file does not exist.'
fi
