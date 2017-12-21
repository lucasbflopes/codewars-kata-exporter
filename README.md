# Codewars Kata Exporter

___
## General Information

This script, although too much 'hacky' for my taste, was the best solution I came up with to export all my kata solutions from codewars to a file structure in my hard drive in an automated fashion.

It relies on the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) module to parse the kata solutions from raw HTML, and also uses the very limited [Codewars API](https://dev.codewars.com) to get each kata description.

Since the solutions in the solution's page are dynamically generated, it is necessary to keep scrolling down in order to be able to collect all of them. This task was facilitated by using [Selenium](http://selenium-python.readthedocs.io) to emulate this repetitive work for you.

After saving the HTML, the script will parse it and create a file structure like below, wherein the katas are separated by difficulty. For each folder representing a kata, there is a folder for each language you completed the problem. The kata description is placed inside the `README.md` file and the solution source code inside `solution.[language_extension]`.

```
solutions/
├── 3-kyu
│   └── the-millionth-fibonacci-kata
│       └── python
│           ├── README.md
│           └── solution.py
├── 4-kyu
│   ├── matrix-determinant
│   │   └── python
│   │       ├── README.md
│   │       └── solution.py
│   └── strip-comments
│       └── python
│           ├── README.md
│           └── solution.py
└── 6-kyu
    └── parabolic-arc-length
        ├── javascript
        │   ├── README.md
        │   └── solution.js
        └── python
            ├── README.md
            └── solution.py
```

___
## How to install

First off, you need to have [Python 3](https://www.python.org/download/releases/3.0/) installed in your machine. Then install all python dependencies required:

`$ pip3 install -r requirements.txt`

To use Selenium you need to install a webdriver to interface with a specific browser. The browser I have chosen to use in the script was Chrome, thus you can download it [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

___
## How to run

Before executing the script, it is necessary to fill some information in `setup.json`:

```
{
  "codewars": {
    "email": "foo@bar.com",   <------------ Your login email
    "password": "foo123",     <------------ Your login password
    "api_key": "foofoo"       <------------ Codewars API token. Can be found under your account settings
  },
  "download_folder": "./solutions", <------ Root directory wherein the katas will be placed
  "file_extensions": {              <------ The parser only finds the text, so in order to save a file
    "java": ".java",                        you need to provide a proper extension. Here I put some
    "python": ".py",                        extensions for some common languages. If yours is not here 
    "javascript": ".js",                    feel free to add.
    "c": ".c",                              
    "c++": ".cpp",                          OBS: If none is found for your language during runtime, the
    "c#": ".cs",                            script will leave it empty, i.e. just 'solution' instead of
    "perl": ".pl",                          'solution.js' in the case of JavaScript
    "php": ".php",
    "ruby": ".rb"
  },
  "reloads_in_browser": 100   <------------ # of attempts to reload the page while scrolling down. Each
}                                           attempt takes 2s, which is the time I deemed enough to load
                                            more katas. This is 'hacky' part I mentioned about. Feel free
                                            to fine-tune this value to suit you best
```

Now run the script responsible for fetching the HTML:

`$ python fetch_source.py`

A chrome window will open and then will start to automatically:
1. log into your account;
2. go to your solutions page;
3. scroll down and wait according to the value of `reloads_in_browser` in `setup.json`.

After finishing, the script will save the HTML in `./source.html`

***OBS**: You can skip this step altogether if you prefer to download the HTML source manually. That being the case, it is not necessary to fill both `email` and `password` in `setup.json`.*

Lastly, run the script responsible for parsing the HTML and creating the file structure:

`$ python main.py`

Done! 
