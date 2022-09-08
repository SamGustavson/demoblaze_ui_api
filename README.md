# Demoblaze
I am using Page Object Model for this Automation.

## Installation
I have used requirements.txt file for package installation. 
```
pip install -r requirements.txt
```

## Configuration
You can use config.ini to provide username and password. 
For more information, please see: https://docs.python.org/3.8/library/configparser.html

## Run
```
pytest -s test_general.py
```

## Notes
1. I have used Chrome for automation. I would extend it to use all sorts of browsers 
for testing by extending configuration. 
2. I will make a Singleton class that will provide a driver and that's how
we don't have to pass driver in every method call.
3. I will take snapshots of automation as I move through different pages.


Thank you so much for giving me this opportunity.
