# GitHub Graph Display

A fun and simple tool to transform your GitHub contribution graph into a 7x52 pixel canvas—perfect for displaying personalized messages or making a statement.

## ✨ Features

* Create custom visual patterns using your GitHub contribution graph
* Display personalized text over time
* Confuse LinkedIn recruiters who judge performance by commit frequency ;)

## Getting Started

### 1. Generate Your Pattern

Use the `gen_pattern.py` script to convert your message into a `.csv` file representing a 7x52 pixel pattern (one week per column, one day per row).

```bash
python3 gen_pattern.py "Your Message Here"
```

This will save a CSV file that the commit script will use to make daily contributions.

### 2. Automate the Commits

To draw on your GitHub graph, schedule `commit.py` to run once daily. On Linux, you can use `cron`.

#### Example: Set up a daily cron job at 8 AM

Open your crontab editor:

```bash
crontab -e
```

Add the following line:

```bash
0 8 * * * /usr/bin/python3 /path/to/commit.py
```

Make sure to replace `/path/to/commit.py` with the full path to your script.

## Requirements

* Python 3.x
* A GitHub repository to use for the commit history
* `git` installed and configured on your system

## Notes

* Use a private or throwaway repository to avoid cluttering your main profile.