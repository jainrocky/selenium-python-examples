# selenium-python-examples

## Setup

### Manually
* Install chromedriver
* Create virtualenv
* Install requirements.txt, `pip install -r requirements.txt`

### Using `setup.sh` file
* Make `setup.sh` an executable file, `chmod +x setup.sh`
* Execute ./setup.sh (It will create virtualenv, install requirements and install chromedriver)


## Run 
- Activate virtual env `source env/bin/activate`

1. **Live World Population**
* python live_world_population.py

2. **Result CLI**
* Run help command to check all options, `python result.py -h`
* Overall result, `python result.py -id 01415002716 -o`
* Per semester result, `python result.py -id 01415002716 -s 3`, (-s <sem-number>)
