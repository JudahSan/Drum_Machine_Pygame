## Simple drum machine project

![drum machine](/img/drum_machine.png)


Setup
-

1. Clone the repo

```
git clone git@github.com:JudahSan/Drum_Machine_Pygame.git
```

2. Cd into the directory and create a virtual environment

```
cd Drum_Machine_Pygame
python -m venv .venv
```

3. Activate the virtual environment and install dependecies

```
source .venv/bin/activate # this might change depending on the directory you are in
pip install -r requirements.txt # install dependecies
```

4. Run the game

```
python3 main.go
```

Android port instructions
-

Install [buildozer](https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android) or follow [guide video](https://www.youtube.com/watch?v=L6XOqakZOeA)

>> Compatibility issues with python 3.11.x

1. Install buildozer in the virtual environment

```
pip install --upgrade buildozer
```

2. Run these

```
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv

# add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/
```

3. Install automate : `sudo apt install -y automake`
4. Install `libtinfo5`: `sudo apt install libtinfo5`
5. Install setuptools: `pip install setuptools`


- Clean command: `buildozer appclean`

- Start build: `buildozer -v android debug deploy run`