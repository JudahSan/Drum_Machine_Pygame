## Simple Drum Machine Project

![Drum Machine](/img/drum_machine.png)

### Setup

1. **Clone the repository**
   ```sh
   git clone git@github.com:JudahSan/Drum_Machine_Pygame.git
   ```

2. **Navigate into the directory and create a virtual environment**
   ```sh
   cd Drum_Machine_Pygame
   python -m venv .venv
   ```

3. **Activate the virtual environment and install dependencies**
   ```sh
   source .venv/bin/activate  # Adjust this command if needed based on your shell
   pip install -r requirements.txt  # Install dependencies
   ```

4. **Run the game**
   ```sh
   python3 main.py
   ```

---

### Android Port Instructions

> **Note:** I attempted to port this project to Android but encountered issues. I will continue troubleshooting and update with a working solution soon.

To attempt building for Android, follow these steps:

1. **Install Buildozer** (See [Buildozer Docs](https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android) or [Guide Video](https://www.youtube.com/watch?v=L6XOqakZOeA))
   ```sh
   pip install --upgrade buildozer
   ```

2. **Install required system dependencies**
   ```sh
   sudo apt update
   sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config \
       zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
   pip3 install --upgrade Cython==0.29.33 virtualenv  # Remove --user if using a virtual environment
   ```

3. **Update the system PATH**
   Add this line to the end of your `~/.bashrc` file:
   ```sh
   export PATH=$PATH:~/.local/bin/
   ```

4. **Install additional dependencies**
   ```sh
   sudo apt install -y automake libtinfo5
   pip install setuptools
   ```

5. **Build the Android package**
   ```sh
   buildozer -v android debug deploy run
   ```

6. **If needed, clean the project**
   ```sh
   buildozer appclean
   ```

I'll continue debugging the Android build process and update this section when I find a reliable solution. 🚀

