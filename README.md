# LabVIEW VI to set up FeelTech FY6x00 Arbitrary Wave Generators

**Goal:** To load identical settings into a number of FeelTech FY6x00 arbitrary wave generators and set a phase shift so that they all cover 360 degrees.

## Step 1: Environment Setup

### 1. Installing Python3

- Visit the official [Python](https://www.python.org/downloads/) website and download the latest version of Python 3.
- Launch the installer and follow the on-screen instructions.

### 2. Installing pip

- Typically, `pip` is already included in Python3 installations. If not, open your command prompt or terminal and run:
```
pip install pyserial
```

**4. Downloading the Library and Placing the Middleware Script**
   
- In your command prompt or terminal, execute:
```
git clone https://github.com/mattwach/fygen fygenlib
```
- After downloading, place the script `fygenmidware.py` into the directory that contains the `fygenlib` folder.
- If you already have an attached version of the library, ensure it's located in a directory convenient for you, and then place the script in the same manner.

## Step 2: LabVIEW Setup

### 5. Opening the VI

- Launch LabVIEW.
- Open your VI associated with the generator control program.

![VI Full View](https://github.com/schtangel/fy6x00-labview-control/blob/main/screenshots/vi_full.png?raw=true)

### 6. Specifying the Path to the Middleware Script

- In the VI, find the control or field responsible for specifying the script path.
- Specify the absolute path to the `fygenmidware.py` script.

![VI Code](https://github.com/schtangel/fy6x00-labview-control/blob/main/screenshots/vi_midware.png?raw=true)

### 7. Specifying the Python Version

- In the VI, locate the appropriate control or field for the Python version.
- Indicate your Python version (e.g., "3.11").

### 8. Setting up Generator Connection Ports

- If necessary, add or remove connection ports adding or deleting arguments of "FY6900_Driver" block.
- The program will automatically calculate the number of generators.

### 9. Running the Program

- In the VI, input the desired parameters: frequency, output signal type, etc.
- Choose the required connection ports.
- Initiate the program execution.

![VI GUI View](https://github.com/schtangel/fy6x00-labview-control/blob/main/screenshots/vi_gui.png?raw=true)
---

**Note:** Upon completion, the program will automatically configure each generator considering the defined phase shift. Proceed to configure your equipment according to the provided parameters.
