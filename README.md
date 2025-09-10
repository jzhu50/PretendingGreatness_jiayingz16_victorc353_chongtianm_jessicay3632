# P04: Makers Makin' It, Act II -- The Seequel by PretendingGreatness

## Roster
- Michelle Zhu: Full-stack/Project Lead
- Victor Casado: Backend
- Mark Ma: APIs
- Jessica Yu: Frontend

## Site Description
This project implements a web application that leverages data visualization to explore and analyze potential patterns and correlations between Elon Musk’s tweets and Tesla’s stock market performance.

## Install Guide

**Prerequisites**

- Ensure that **Git** and **Python 3** are installed on your machine.
  - Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
  - Python: https://www.python.org/downloads/

### Installation Steps
1. Clone the repository to your local machine:
    - HTTPS:
      ```
      git clone https://github.com/jzhu50/PretendingGreatness_jiayingz16_victorc353_chongtianm_jessicay3632.git
      ```
    - SSH (requires SSH key):
      ```
      git clone git@github.com:jzhu50/PretendingGreatness_jiayingz16_victorc353_chongtianm_jessicay3632.git
      ```
2. Navigate to the project directory:
    ```
    cd PretendingGreatness_jiayingz16_victorc353_chongtianm_jessicay3632
    ```
3. (Recommended) Create and activate a Python virtual environment:
    ```
    python3 -m venv foo
    source foo/bin/activate
    ```
4. Install Python dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Obtain a free Gemini API key:
    - Visit [Google AI Studio](https://aistudio.google.com/).
    - Sign in with your Google account.
    - Go to [Google AI Studio API Key page](https://aistudio.google.com/apikey).
    - Click on "Create API Key" to generate your own Gemini API key and copy it.

6. Add your Gemini API key:
    - Navigate to `.env` at the root of the repository:
    - Replace the placeholder with your obtained Gemini API Key in the following line:
      ```
      GEMINI_API_KEY=your_gemini_api_key_here
      ```

## Launch Codes

**How to Launch the App**

Assuming you have completed the Install Guide and your virtual environment is activated:

1. Navigate to the app directory:
    ```
    cd app
    ```
2. Run the application:
    ```
    python3 __init__.py
    ```
3. Open the link that appears in the terminal to access the website:
    - Control + Click the link
    - Or type/paste `http://127.0.0.1:5006` in your browser
    - To stop the app, press `Control + C` in the terminal

### Feature Spotlight
* AI Prompting at line 66 in file `__init__.py`
* Gemini AI API Integration in file `AI.py`
* Database Population using API in `FMP.py`
* Data is parsed in `graphloading.py`, then passed in `static/tesla_charts.js` for displaying the graph

### Known Bugs/Issues
* AI does not take context (i.e. the recent tweets) into its analysis.
* Images/videos in the tweet are not rendered in tweet analysis, which may influence predictions.
* Original tweet of retweets are not factored into tweet analysis.