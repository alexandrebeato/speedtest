# Speed test automation

This is a simple script to automate the speed test using the speedtest-cli library. Download the executable file from releases and run it. The script will run the speed test and save the results in a CSV file in the same directory.

## Building the executable

First of all, create an virtual environment and install the dependencies:

```bash
python -m venv speedtest
source speedtest/bin/activate
pip install -r requirements.txt
```

Then, build the executable:

```bash
python -m PyInstaller --onefile main.py
```

The executable will be in the `dist` directory.