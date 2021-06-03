# ChaturbateRecorder

This is script to automate the recording of public webcam shows from chaturbate.com. 

Tested on Windows 10 - Version 20H2

## Requirements

Requires python3.9 or newer. You can grab python3.9 from https://www.python.org/downloads/

to install required modules, run:
```
python3 -m pip install livestreamer bs4 lxml gevent
```

## Usage
Edit the config file (config.conf) to point to the directory you want to record to, where your "wanted" file is located, 
which genders, and the interval between checks (in seconds)

Add models to the "wanted.txt" file (only one model per line). 
The model should match the models name in their chatrooms URL (https://chaturbate.com/{modelname}/). 
To clarify this, it should only be the "modelname" portion, not the entire url.


## Issues
I am by no means a python wizard or even a great coder.

If you have contributions or errors, please provide as much info as possible for me to review.


### FORK
This is a fork of  Damianonymous' original script which can be found here: 
https://github.com/Damianonymous/ChaturbateRecorder

## Disclaimer
This tool is not to be used to record, trasmit, distribute, or make available in any way, copyrighted content claimed by the creators of such material.

If a model or Chaturbate claims copyright ownership over their stream, it is legally theirs and their copyright rights over their material shall not be infringed by the use of this script. 

By using this script, you affirm that you are not infringing the copyright of any parties involved.
