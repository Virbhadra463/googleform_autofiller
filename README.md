Project Overview

This project is a Python-based automation script that automatically submits responses to a Google Form using randomized data. It simulates human-like submissions by generating names, emails, demographics, and randomized answers, then sending them as HTTP POST requests to the Google Form endpoint.

The project was built as a learning exercise to explore:
    Python automation
    HTTP requests
    Web form structures
    Basic web scraping concepts

How It Works

    The script stores all Google Form entry IDs for each question.
    Answer choices for each section are defined as Python lists.

For every submission:

    A random name and email are generated.
    Random demographic values are selected.
    Random answers are chosen for each question.
    All values are placed into a dictionary where keys are entry IDs and values are responses.
    A POST request is sent to the Google Form formResponse URL.
    The script waits a short random delay and repeats until the target number of submissions is reached.

Workflow

    Load configuration (form URL, entry IDs, options).
    Generate randomized user profile.
    Build request payload.
    Submit POST request.
    Verify response status.
    Repeat.

How to Build Your Own Auto Form Filler ??
    1. Open Google Form and inspect page source. (use beautifulsoap library for webscraping instead of doing this process manually)
    2. Locate each entry.xxxxx ID.
    3. Copy the form formResponse URL.
    4. Create answer lists.
    5. Map answers to entry IDs.
    6. Send POST requests using Python requests.
    7. Add delays between requests.
    8. Test with small numbers.
    
Disclaimer:-
This project is intended for educational purposes only. For real surveys, use authentication, email verification, and response limits to collect genuine data.