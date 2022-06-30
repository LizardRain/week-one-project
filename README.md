![example workflow](https://github.com/LizardRain/week-one-project/actions/workflows/style.yaml/badge.svg)
# Bugsnax App

## Running locally

Requires git and python to run.
```
git clone https://github.com/LizardRain/week-one-project.git
cd week-one-project
pip install requests
python bugsnax_app.py
```


# SET-UP
1. download the files
2. ignore the db because it isn't used
3. ???
4. profit

# HOW TO RUN
1. download the files
2. double-click on bugsnax_app.py
3. ???
4. Profit

# WHAT IT DOES
* You can press a variety of buttons that have names of Bugsnax on them
* When you press the button, its name will be drawn in a new window
* When you press another button after that, the old name will be erased and the new name will be written in its place

# HOW IT WORKS
1. A GET request to the [Bugsnax API](https://github.com/samuel-pratt/bugsnax-api/) retreives the data for all Bugsnax
2. The name of each Bugsnax is parsed out of this response
3. Each name is given a button
4. When the button is pressed, a class method is run which allows a turtle to draw the word
