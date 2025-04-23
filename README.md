# P04: Makers Makin' It, Act II -- The Seequel by PretendingGreatness

## Roster
- Michelle Zhu: Full-stack/Project Lead
- Victor Casado: Backend
- Mark Ma: APIs
- Jessica Yu: Frontend

## Site Description
This project implements a web application that incorporates data visualization to identify interesting patterns and correlations between Elon Musk’s tweets and Tesla stock market prices.

## Direct Access
Type https://mzhu.tech in the search bar of your web browser.

## Install Guide

**Prerequisites**

Ensure that **Git** is installed on your machine. For help, refer to the following documentation: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### How to clone/install
1. In terminal, clone the repository to your local machine:

HTTPS METHOD:

```
git clone https://github.com/jzhu50/PretendingGreatness_jiayingz16_victorc353_chongtianm_jessicay3632.git      
```

SSH METHOD (requires the SSH key):

```
git clone git@github.com:jzhu50/PretendingGreatness_jiayingz16_victorc353_chongtianm_jessicay3632.git
```
2. Navigate to project directory:

```
cd PATH/TO/PretendingGreatness_jiayingz16_victorc353_chongtianm_jessicay3632
```
3. Install dependencies

```
pip install -r requirements.txt
```

## Launch Codes

**Prerequisites**

Ensure that **Git** and **Python** are installed on your machine. It is recommended that you use a virtual machine when running this project to avoid any possible conflicts. For help, refer to the following documentation:
   1. Installing Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
   2. Installing Python: https://www.python.org/downloads/

### How to run

1. Create Python virtual environment:

```
python3 -m venv foo
```

2. Activate virtual environment

   - Linux: `. PATH/TO/venv_name/bin/activate`
   - Windows (PowerShell): `. .\PATH\TO\venv_name\Scripts\activate`
   - Windows (Command Prompt): `>PATH\TO\venv_name\Scripts\activate`
   - macOS: `source PATH/TO/venv_name/bin/activate`

   *Notes*

   - If successful, command line will display name of virtual environment: `(venv_name) `

   - Type `deactivate` in the terminal to close a virtual environment

3. Navigate to project app directory

```
 cd PATH/TO/PretendingGreatness_jiayingz16_victorc353_chongtianm_jessicay3632/app/
```

4. Run App

```
 python3 __init__.py
```
5. Open the link that appears in the terminal to be brought to the website
    - You can visit the link via several methods:
        - Control + Clicking on the link
        - Typing/Pasting http://127.0.0.1:6969 in any browser
    - To close the app, press control + C in the terminal

```    
* Running on http://127.0.0.1:6969
```

### FEATURE SPOTLIGHT
* AI Prompting at line 64 in file `__init__.py`
* AI API Integration in file `AI.py`
* Database Population using API in `FMP.py`
* Data is parsed in `graphloading.py`, then passed in `static/tesla_charts.js` for displaying the graph.

### KNOWN BUGS/ISSUES
* AI Does not take context (i.e. the recent tweets) into its analysis.
* Images/videos in the tweet are not rendered in tweet analysis, which may influence predictions.
* Original tweet of retweets are not factored into tweet analysis.
