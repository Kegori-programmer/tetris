MESSAGE=$(python --version)

if [[ "$MESSAGE" == 'bash: python: command not found' ]]; then
  sudo apt -y install python
  sudo apt -y install python3-pip
  pip3 install pygame
fi

python tetris.py
