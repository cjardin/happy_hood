#/bin/sh

python3 -m build
sudo pip3 install dist/happyhoodagents-0.0.6-py3-none-any.whl --force-reinstall
pip3 install dist/happyhoodagents-0.0.6-py3-none-any.whl --force-reinstall


