# github-graph-display

Simple tool to turn your the github commit graph into a 7x52 pixel display.

### Features:

- Display personalized texts
- Mess with possible LinkedIn recruiters who think one should evaluate performance by the number of commits..

### Usage

Use `gen_pattern.py` to save a personalized text as .csv

Use a scheduler to execute the commit script every day

i.e. linux OS scheduler

```bash
crontab -e    
```

And add this to start the script every day at 8 AM

```
0 8 * * * /usr/bin/python3 /path/to/commit.py
```