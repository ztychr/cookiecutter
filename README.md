# CookieCutter
Fetch and analyse cookies from selected websites.

## Installation

Clone or download repo and optionally copy CookieCracker to ~/.local/bin
```
git clone https://github.com/ztychr/cookiecutter/
cd cookiecutter/ && chmod a+x cookiecutter.py
mv cookiecutter.py ~/.local/bin/cookiecutter
```

OR run in folder with python3
Example usage:
```
python3 cookiecutter -v youtube.com
```


## Dependencies:
Install missing or non standard libraries via pip3:
```
pip3 install bs4
pip3 install tqdm
```

If pip3 isn't installed, install with:
```
sudo apt install python3-pip
```


![example usage](https://raw.githubusercontent.com/ztychr/cookiecutter/master/cc.png)
