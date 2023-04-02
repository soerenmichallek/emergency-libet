# emergency-libet
Psychopy Code, files, and explanations for my modified Libet Clock experiment run in PsychoPy. The main goal of the experiment was to investigate the timing of action awareness in prosocial behavior in 1 victim, 1 bystander emergency scenarios.

# Important:
Make sure to set the default units of PsychoPy to 'pix'. Otherwise the positioning of the clock elements will be off. To avoid having to do this you could update the clock elements in the clock_init components to set their units argument as whatever you prefer.

# Available Files

| File  | Description|
| ------------- | ------------- |
| emergency-libet/emergency-libet.psyexp  | PsychoPy experiment file for the standalone application|
| emergency-libet/emergency-libet_lastrun.py  | Python code for the experiment |
| emergency-libet/scenarios.xlsx | List of all scenario descriptions in Dutch |
| emergency-libet/stimuli/x.ogg | Sound files for scenarios and action words |
| emergency-libet/stimuli/x.png/jpg | Pictures for instructions |
| emergency-libet/conditionfiles/x.xlsx | Condition files for all practice and experimental trials including critical variables. For use with PsychoPy trial loops. |




# Purpose of the Experiment
This is my experiment coded for my master thesis project "**From Observer to Actor:
The Role of Action Awareness in Helping in Social Emergency Situations**" in the Social and Health Psychology Research master's program at Utrecht University, Utrecht, Netherlands.

# Summary of the Experiment
There are four phases to the experiment.
1. Information letter & consent
2. Instructions and practice trials
3. 48 Free choice experimental trials
4. 48 Forced choice experimental trials

In the experimental trials, participants see a rotating Libet clock on their screen. At the beginning of each trial a different auditory description of a social emergency scenario is played, e.g. "your friend spilled a liquid in the laboratory at work. It is a toxic liquid that emits fumes which she inhales."
In the free choice trials, participants then can decide whether to approach and thus help the person in the scenario or not, indicated by key press. 
In the forced choice trials, participants are instructed to either help or not.

After the keypress the clock stops rotating and participants are asked to give an M-judgement (Haggard & Libet, 2001) "where was the clock hand in the moment you pressed the key?"


# Running the Experiment
Using PsychoPy Builder/Standalone PsychoPy version 2022.2.5 and upwards:
1. Install the standalone PsychoPy application (see https://www.psychopy.org/download.html)
2. Download the files from this repository
3. Open "emergency-libet.psyexp" from within PsychoPy 
4. Click on "run experiment"

Using Python:
1. Install a version of Python equal to or greater than 3.8 
2. Install the latest version of the PsychoPy module (see https://www.psychopy.org/download.html). In most cases that means running:
```
     pip install psychopy
```
3. Download the files from this repository
4. run "emergency-libet_lastrun.py"
