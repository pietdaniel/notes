#!/bin/bash -i

command_exists () {
  type "$1" &> /dev/null ;
}

if command_exists pip; then
  echo "pip exists"
else 
  echo "Need to install pip"
  exit 0
fi

if `python -c "import flask"`; then
  echo "flask exists"
else
  echo "Installing flask"
  sudo pip install flask
fi
