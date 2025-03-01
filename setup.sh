sudo apt update
sudo apt install -y python3.9 python3.9-venv python3.9-dev
python3.9 -m venv BitDistillerVenv
source BitDistillerVenv/bin/activate
pip install -r requirements.txt

