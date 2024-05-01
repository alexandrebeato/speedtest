# Speed test automation

This is a simple script to automate the speed test using the speedtest-cli library. Download the executable file from [releases](https://github.com/alexandrebeato/speedtest/releases) and run it. The script will run the speed test and save the results in a CSV file in the same directory.

## Running or building the executable

First of all, create an virtual environment and install the dependencies:

```bash
py -m venv speedtest
source speedtest/bin/activate
pip install -r requirements.txt
```

To run the script, just execute the `main.py` file:

```bash
py main.py
```

Then, build the executable:

```bash
py -m PyInstaller --onefile main.py
```

The executable will be in the `dist` directory.