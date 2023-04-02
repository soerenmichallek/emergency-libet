#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on April 02, 2023, at 23:03
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.5')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from shuffle_init
# this component aids with the randomisation of forced trials.
# 50% of forced trials should be "heen" trials and 50% "weg" trials.

training_4_n = 4 # amount of trials per conditions file
forced_n = 48

# create a balanced list:
training_4_action_word = [0, 1] * (training_4_n//2)

forced_action_word = [0, 1] * (forced_n//2)

# randomise list order:
shuffle(training_4_action_word)

shuffle(forced_action_word)
# Run 'Before Experiment' code from clock_init
# imports needed libraries, some of this might be redundant
from math import *
from psychopy import gui
import random




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'emergency-libet'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\soeren\\Desktop\\psychopy_lab_version\\emergency-libet_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "hide_mouse" ---

# --- Initialize components for Routine "info1" ---
# Run 'Begin Experiment' code from text_init
# create some variables used in event listeners
keys = ['up','down']
judge_keys_correct = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # allowed keys for M judgement
mouse = event.Mouse(visible=False,win=win)
was_incorrect = False

question = visual.TextBox2(win=win, text= "Waar was de wijzer van de klok toen je de toetsen indrukte?", # the critical question for the M judgement
                             pos=(0, .4),
                             size=(.4,.1), color = 'black', borderColor = 'black', units = 'height')

pre_hint = visual.TextBox2(win=win, text= "door in het tekstveld een getal van 0 tot 59 in te voeren op het nummerbord met je rechterhand.", # before training 3 trials
                             pos=(0, .4),
                             size=(.4,.1), color = 'black', borderColor = 'black', units = 'height')

judgement_box = visual.TextBox2(win=win, text = "", # create editable textbox in which participants can input the M judgement
                             pos=(0, -0.4),
                             size=(.2,.1), color = 'black', borderColor = 'black', units = 'height', editable = True, alignment='center')
                             
hint_box = visual.TextBox2(win=win, text = "voer een getal in tussen 0 en 59:", # tooltip for the M judgement
                             pos=(0, -0.33),
                             size=(.4,.1), color = 'black', borderColor = 'none', units = 'height')                             
                             

next_text_2 = visual.TextBox2(win=win, text = "druk op 'enter' om door te gaan", # tooltip to press "enter" to move to next routine"
                             pos=(.45, -0.4),
                             size=(.2,.08), color = 'black', borderColor = 'black', units = 'height', alignment='center')
                             
                             
incorrect = visual.TextBox2(win=win, text= "Je drukte op de verkeerde toets. Druk op de toets die overeenkomt met de mededeling.", # gives feedback about wrong key pressed in forced trials
                             pos=(.15, 0),
                             size=(1,1), color = 'black', borderColor = 'none', units = 'height', letterHeight = .025)      
                                                    
# Run 'Begin Experiment' code from sounds_init
# initialises sounds used in most trials
buffer = 0.75 # delay between the playing of a soundfile and the next sound to be played.
# Critical to avoid audio overlap

beep = sound.Sound(value='A', secs=0.2, # beep sound to indicate that a keypress is now possible
    loops = 0,
    volume = 1)
    
kies = sound.Sound("stimuli/kies.ogg", # action word: here participants can choose to help or not
    stopTime = 1,
    loops = 0,
    volume = 1)
    
heen = sound.Sound("stimuli/heen.ogg", # action word: here participants should help
    stopTime = 1,
    loops = 0,
    volume = 1)
    
weg = sound.Sound("stimuli/weg.ogg", # action word: here participants should not help
    stopTime = 1,
    loops = 0,
    volume = 1)
    

# Run 'Begin Experiment' code from clock_init
# create a circle for the clock face
clock_circle = visual.Circle(
    win = win,
    radius = 280,
    edges = 100,
    lineColor = "black",
    lineWidth = 5,
    interpolate = True
)

# create center dot
center_dot = visual.Circle(
    win = win,
    radius = 6,
    edges = 512,
    lineColor = "black",
    fillColor = "black",
    interpolate = True
)

# create clock hand
second_hand = visual.Line(
    win = win,
    start = (0, 0),
    end = (0, 265),
    lineColor = "black",
    lineWidth = 5,
    ori = 0
)
# create clock details
ticks_large = []
ticks_small = []
clock_labels = []
for i in range(12):
    ticks_a = visual.Line(win, start=(clock_circle.radius*cos(2*pi/12*i),
    clock_circle.radius*sin(2*pi/12*i)), 
    end=((clock_circle.radius+20)*cos(2*pi/12*i),
    (clock_circle.radius+20)*sin(2*pi/12*i)), # the "-20" offsets the label so that they don't overlap with the circle
    lineColor = "black",
    lineWidth = 3
    )
    ticks_large.append(ticks_a)
    
# create  labels
    labels = visual.TextStim(
        win = win,
        pos = [clock_circle.pos[0] + ((clock_circle.radius + 40) * cos(radians(-(270+i*30)))), # the "+20" offsets the label so that they don't overlap with the circle
        clock_circle.pos[0] + ((clock_circle.radius + 40) * sin(radians(-(270+i*30))))],
        text = str(i*5),
        color = "black"
    )
    clock_labels.append(labels)
    

def clock_static(): # function for drawing the static clock without animation
    clock_circle.draw()
    center_dot.draw()
    for labels in clock_labels:
        labels.draw()
    for ticks_a in ticks_large:
        ticks_a.draw()
        
def clock_full(): # function for drawing animated clock
    clock_static()
    second_hand.setOri(timer.getTime() * (360 / 2.56) % 360)
    second_hand.draw()
    
def clock_judgement(): # function for drawing M judgement screen elements
    clock_static() 
    judgement_box.draw()
    next_text_2.draw()
    question.draw()
    hint_box.draw() 

next_press = keyboard.Keyboard()
next_text = visual.TextBox2(
     win, text='druk op "enter" om akkoord te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text',
     autoLog=False,
)
info1_text = visual.TextBox2(
     win, text='Informatiebrief voor deelnemers\n\nHelpende handen studie\n\nGeachte deelnemer,\n\nJe heeft interesse getoond in deelname aan mijn studie over gedrag in ongewone situaties. Op deze pagina vindt je een overzicht van de studie waaraan je wordt uitgenodigd deel te nemen. Lees deze informatie zorgvuldig door voordat je toestemming geeft voor deelname aan deze studie. Voordat je kunt deelnemen aan wetenschappelijk onderzoek is een verklaring vereist waarin je verklaart dat je volledig geïnformeerd bent en bereid bent om deel te nemen. Dit wordt geïnformeerde toestemming genoemd. \n\nOnderwerp en doel van de studie\n\nDit onderzoek is onderdeel van de masterscriptie van Sören Michallek, research master student Social and Health Psychology aan de Universiteit Utrecht. Voor zijn afstudeerproject onderzoekt hij hoe mensen zich gedragen in ongewone situaties.\n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='info1_text',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "info2" ---
info2_text = visual.TextBox2(
     win, text="Inhoud en opzet van het experiment\n\nTijdens dit onderzoek luisteren de deelnemers naar beschrijvingen van verschillende scenario's. Vervolgens wordt de deelnemers gevraagd bepaalde beslissingen te nemen.\n\nVertrouwelijkheid en toegang door derden\n\nDit onderzoek is een project van de Universiteit Utrecht. De in dit onderzoek verzamelde gegevens zijn uitsluitend bestemd voor wetenschappelijk onderzoek. De gegevens worden gecontroleerd door de Universiteit Utrecht volgens de General Data Protection Regulation (GDPR). Anonieme gegevens uit dit onderzoek kunnen worden gedeeld in een openbare repository voor onderzoeksdoeleinden en worden gepresenteerd in wetenschappelijke publicaties. Je heeft het recht om het onderzoek op elk moment te beëindigen en je kunt ons binnen 24 uur na indiening laten weten uw gegevens te verwijderen.\n", font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(.95, .95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='info2_text',
     autoLog=False,
)
next_press_2 = keyboard.Keyboard()
next_text_2 = visual.TextBox2(
     win, text='druk op "enter" om akkoord te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_2',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "info3" ---
info3_text = visual.TextBox2(
     win, text='Deelname aan de studie\n\nDeelname aan dit onderzoek is geheel vrijwillig. Je hebt het recht om helemaal niet deel te nemen of om het onderzoek op elk moment zonder opgaaf van reden te verlaten. Zelfs als je de geïnformeerde toestemming nu ondertekent, kunt je zich op elk moment terugtrekken. Het verlaten van de studie heeft op geen enkel moment gevolgen.', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(.95, .95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='info3_text',
     autoLog=False,
)
next_press_3 = keyboard.Keyboard()
next_text_3 = visual.TextBox2(
     win, text='druk op "enter" om akkoord te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_3',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "info4" ---
info4_text = visual.TextBox2(
     win, text='Administratieve zaken\n\nDe internationale richtlijnen die op dit onderzoek van toepassing zijn, worden zorgvuldig nageleefd.\nAls je bereid bent deel te nemen aan dit onderzoek, vragen wij op "enter" te drukken om je toestemming te geven. Mocht je op een later tijdstip nog vragen hebben met betrekking tot dit onderzoek, neemt je dan gerust contact op met de studentonderzoeker of de facultaire begeleider via onderstaande contactgegevens. \n\nMet vriendelijke groet,\n\nSören Michallek (s.michallek@students.uu.nl)\nMasterstudent Sociale en Gezondheidspsychologie - Universiteit Utrecht\nHans Marien (h.marien@uu.nl)\n\nBegeleider scriptieproject - Universitair Hoofddocent - Universiteit Utrecht\nHenk Aarts (h.aarts@uu.nl)\nBegeleider afstudeerproject - Hoogleraar - Universiteit Utrecht\n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(.95, .95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='info4_text',
     autoLog=False,
)
next_press_4 = keyboard.Keyboard()
next_text_4 = visual.TextBox2(
     win, text='druk op "enter" om akkoord te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_4',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "consent" ---
consent_text = visual.TextBox2(
     win, text='Geïnformeerde toestemming: Spoedonderzoek\n\nIk heb de informatiebrief voor deelnemers gelezen.\n\nIk kreeg de gelegenheid om vragen te stellen.\n\nIk heb voldoende tijd gehad om te beslissen of ik wilde deelnemen of niet. \n\nIk weet dat deelname geheel vrijwillig is. Ik weet dat ik te allen tijde kan besluiten om niet deel te nemen.\n\nIk geef toestemming om mijn gegevens te gebruiken voor de in de informatiebrief genoemde doeleinden.\n\nIk weet dat sommige mensen toegang zullen hebben tot mijn gegevens. Deze mensen worden genoemd in de informatiebrief.\n\nIk wil deelnemen aan dit onderzoek.\n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(1, 1), borderWidth=0.05,
     color='Black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='consent_text',
     autoLog=False,
)
next_press_5 = keyboard.Keyboard()
next_text_5 = visual.TextBox2(
     win, text='Ik heb de bovenstaande informatie gelezen en begrepen en door op "enter" te drukken geef ik toestemming om deel te nemen aan dit experiment in de wetenschap dat de gegevens zullen worden geregistreerd.', font='Open Sans',
     pos=(0, -0.4),units='height',     letterHeight=0.0175,
     size=(.7,.1), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_5',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "pre_instructions_1" ---
pre_instructions_1_text = visual.TextBox2(
     win, text='Dit onderzoek gaat over je vermogen om je in te leven in sociale situaties. Het inlevingsvermogen is van belang om in te schatten hoe anderen mensen zich voelen, wat ze denken en wat ze gaan doen. Door je in te leven zit je als het ware in een situatie en weet je wat je aan anderen hebt en wat jij voor hen kunt doen.\n\nIn dit onderzoek gaan we je een aantal situaties voorleggen waar iemand iets overkomt. Deze situaties zijn gekozen n.a.v. een groot onderzoek. In dit onderzoek gaven mensen aan dat ze de situaties wel eens mee hebben gemaakt. In elke situatie kan het zijn dat iemand hulp of geen hulp nodig heeft. Dit hangt af van de context in de situatie. We gaan je in elke situatie vragen wat je zou doen: helpen of niet helpen. Probeer je alsjeblieft in iedere situatie in te leven en voor te stellen hoe het zou zijn in de situatie.  \n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.2, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='pre_instructions_1_text',
     autoLog=False,
)
next_press_6 = keyboard.Keyboard()
next_text_6 = visual.TextBox2(
     win, text='druk op "enter" om door te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_6',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "pre_instructions_2" ---
pre_instructions_2_text = visual.TextBox2(
     win, text='Zet de hoofdtelefoon op. Elke situatie wordt via de hoofdtelefoon vertelt. De uitleg van de situatie is kort, dus het is van belang om iedere keer goed op te letten en dat je je probeert in te leven. \nWe gaan dit eerst oefenen zodat je later weet wat je te wachten staat.\n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(1, 1), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.15, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='pre_instructions_2_text',
     autoLog=False,
)
next_press_7 = keyboard.Keyboard()
next_text_7 = visual.TextBox2(
     win, text='druk op "enter" om door te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_7',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_1_instructions" ---
training_1_instructions_text = visual.TextBox2(
     win, text='Je gaat nu luisteren naar een situatie. Luister er aandachtig naar.\n\nProbeer je in de situatie in te leven alsof je er zelf aanwezig bent. \n\nEr zal ook een klok op het scherm staan, daarover later meer.\n\nVoor nu is het alleen belangrijk dat je op de klok focust terwijl je naar de situatie luistert. \n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.15, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='training_1_instructions_text',
     autoLog=False,
)
next_press_8 = keyboard.Keyboard()
next_text_8 = visual.TextBox2(
     win, text='druk op “enter” om naar het scenario te luisteren', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_8',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_1_trial_1" ---

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "likert" ---
# Run 'Begin Experiment' code from likert_code
# Likert questions to check whether participants can empathize well with the scenarios, can hear them well, and whether they believed someone was in need of help or not
choice= ["heel slecht", "slecht", "redelijk","goed","uitstekend"]
label = []

likert_1 = visual.RatingScale( # 1-5 Likert
    win, low = 1, high = 5,
    markerStart = 12, markerColor = 'Black', textSize = 0.5, tickMarks = label, textColor = 'Black', lineColor = 'Black', showAccept = False,
    pos=(0,300), size= 1, marker = 'circle', labels = None, scale = None, choices = choice)
    
likert_2 = visual.RatingScale( # 1-5 Likert
    win, low = 1, high = 5,
    markerStart = 12, markerColor = 'Black', textSize = 0.5, tickMarks = label, textColor = 'Black', lineColor = 'Black', showAccept = False,
    pos=(0,0), size= 1, marker = 'circle', labels = None, scale = None, choices = choice)
    
likert_3 = visual.RatingScale( # dichotomous
    win, low = 1, high = 5, choices =["hulp nodig", "geen hulp nodig"],
    markerStart = 12, markerColor = 'Black', textColor = 'Black', lineColor = 'Black', showAccept = False,
    pos=(0,-300), size=1, marker = 'circle', textSize = 0.5)    
    
item_1 = visual.TextStim(win, text="Heb je goed kunnen horen wat de stem zei? Geef je antwoord aan met een muisklik.", height=.02, units='height', pos=(0, .4), color = 'Black') #"were you able to hear the scenario well?" "indicate with mouseclick"
item_2 = visual.TextStim(win, text="Heb je je kunnen inleven in de situatie?", height=.02, units='height', pos=(0, 0.125), color = 'Black') #"were you able to empathize/be able to visualize the situation"
item_3 = visual.TextStim(win, text="Wat gebeurde er? Iemand had:", height=.02, units='height', pos=(0, -0.175), color = 'Black') #"Was someone in need of help or not?"


# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_2_instructions_1" ---
training_2_instructions_1_text = visual.TextBox2(
     win, text='We gaan nu iets toevoegen aan de luister taak. D.w.z.: we gaan je vragen om te helpen of om niet te helpen door op een knop te drukken. De knop met de pijl omhoog betekent HEEN en de knop met de pijl omlaag betekent WEG. HEEN staat dan voor: er heen gaan en helpen, en WEG staat voor weggaan en niet helpen. We gaan dit eerst een paar keer oefenen.', font='Open Sans',
     pos=(0, -.2),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='training_2_instructions_1_text',
     autoLog=False,
)
arrowkeys = visual.ImageStim(
    win=win,
    name='arrowkeys', units='height', 
    image='stimuli/arrowkeys_1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, .2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
next_press_9 = keyboard.Keyboard()
next_text_9 = visual.TextBox2(
     win, text='druk op "enter" om door te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_9',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_2_instructions_2" ---
training_2_instructions_2_text = visual.TextBox2(
     win, text='Kijk goed naar het volgende plaatje. Plaats de middelvinger van je linkerhand op de bovenste pijltjestoets. Plaats de wijsvinger van je linkerhand op de onderste pijltoets. Gebruik je rechterhand om op "enter" te drukken om vooruit te gaan.\n\n', font='Open Sans',
     pos=(0, .3),units='height',     letterHeight=0.025,
     size=(1, 1), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='training_2_instructions_2_text',
     autoLog=False,
)
next_press_10 = keyboard.Keyboard()
next_text_10 = visual.TextBox2(
     win, text='druk op "enter" om door te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_10',
     autoLog=False,
)
keyboard_instr = visual.ImageStim(
    win=win,
    name='keyboard_instr', units='height', 
    image='stimuli/keyboard.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "pre_t3_instructions" ---
pre_t3_instructions_text_1 = visual.TextBox2(
     win, text='Je gaat nu oefenen met er heen gaan en helpen.', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.15, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='pre_t3_instructions_text_1',
     autoLog=False,
)
next_press_17 = keyboard.Keyboard()
next_text_16 = visual.TextBox2(
     win, text='druk op “HEEN” ', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_16',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "pre_t3_instructions_2" ---
pre_t3_instructions_text = visual.TextBox2(
     win, text='Je gaat nu oefenen met weggaan en niet helpen.', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.15, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='pre_t3_instructions_text',
     autoLog=False,
)
next_press_18 = keyboard.Keyboard()
next_text_17 = visual.TextBox2(
     win, text='druk op “WEG”', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_17',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_2_instructions_3" ---
next_press_14 = keyboard.Keyboard()
next_text_14 = visual.TextBox2(
     win, text='druk op “enter” om naar het scenario te luisteren', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_14',
     autoLog=False,
)
training_2_instructions_3_text = visual.TextBox2(
     win, text='Je gaat nu weer luisteren naar een situatie. Luister er aandachtig naar.\n\nProbeer je in de situatie in te leven alsof je er zelf aanwezig bent.\n\nDaarna vragen we wat je kiest om te doen: helpen of niet helpen? \n\nDus na iedere situatie hoor je het woord “Kies” gevolgd door een pieptoon. Je komt pas “in actie” als je een pieptoon hebt gehoord. Je kiest dan HEEN of WEG en drukt dan op de bijbehorende knop. \n\nHEEN {pijl omhoog} staat dus voor: er heen gaan en helpen\n\nWEG {pijl omlaag} staat voor weggaan en niet helpen.\n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='training_2_instructions_3_text',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_2_trial_1" ---

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_3_instructions" ---
training_3_instructions_text = visual.TextBox2(
     win, text='We gaan tenslotte nog een stap toevoegen aan de luister taak. Op het scherm wordt ook een klok getoond. Deze wijzer van de klok gaat op een bepaald moment ook ronddraaien, ook nadat je op de HEEN of WEG knop hebt gedrukt. Het is de bedoeling dat je op deze klok aangeeft wanneer je op de HEEN of WEG knop drukte om te helpen of niet. De roterende klok wordt in beeld gebracht voordat je “Kies” en de pieptoon hoort.  \n\nDaarna druk je op de HEEN knop (= helpen), \n\nof druk je op de WEG knop (= niet helpen). \n\nJe komt pas “in actie” als je een pieptoon hebt gehoord. \nFocus op de roterende klok en onthoud waar de wijzer stond wanneer je op de knop drukte.\n\nDe wijzers van de klok draaien nog even door. Na een tijdje verdwijnt de wijzer en daarna geef je op het nummerbord met je rechterhand aan wanneer je op de HEEN of WEG knop drukte.\n\nWe gaan dit eerst een paar keer oefenen.\n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.15, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='training_3_instructions_text',
     autoLog=False,
)
next_press_11 = keyboard.Keyboard()
next_text_11 = visual.TextBox2(
     win, text='druk op “enter” om naar het scenario te luisteren', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_11',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_3_trial_1" ---

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_3_trial_2" ---
t3_text = visual.TextStim(win=win, name='t3_text',
    text='',
    font='Open Sans',
    units='height', pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyResp = keyboard.Keyboard()
t3_border = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -.4),units='height',     letterHeight=0.05,
     size=(.2, .1), borderWidth=2.0,
     color=None, colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='t3_border',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "instr_free" ---
instr_free_text_5 = visual.TextBox2(
     win, text='We beginnen nu met het eerste deel van het onderzoek. Dit deel gaat over wat je in verschillende situaties zelf wilt doen. Wat je zou willen doen kan best per situatie en moment verschillen. Probeer iedere keer op je gevoel af te gaan wat je wilt doen.  \n\nJe geeft aan wat je wilt doen door op de HEEN of WEG knop te drukken. \n\nDaarna geef je op het nummerbord met je rechterhand aan wanneer je op de HEEN of WEG knop drukte.\n', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='instr_free_text_5',
     autoLog=False,
)
next_press_12 = keyboard.Keyboard()
next_text_12 = visual.TextBox2(
     win, text='druk op “enter” om naar het scenario te luisteren', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_12',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "free_trial" ---

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "free_trial_2" ---
free_text = visual.TextStim(win=win, name='free_text',
    text='',
    font='Open Sans',
    units='height', pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyResp_4 = keyboard.Keyboard()
free_border = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -.4),units='height',     letterHeight=0.05,
     size=(.2, .1), borderWidth=2.0,
     color=None, colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='free_border',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "free_debrief" ---
free_debrief_text = visual.TextBox2(
     win, text='Je bent nu klaar met het eerste deel van het onderzoek.', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='free_debrief_text',
     autoLog=False,
)
free_debrief_next_text = visual.TextBox2(
     win, text='druk op "enter" om door te gaan', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='free_debrief_next_text',
     autoLog=False,
)
next_press_16 = keyboard.Keyboard()

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_4_instructions" ---
training_4_text = visual.TextBox2(
     win, text=' In het eerste deel was je vrij om te beslissen of je wilde helpen of niet, nadat je het woord “kies” hoorde. In het tweede deel kan je niet meer zelf beslissen wat je doet. Je krijgt dan het woord “heen” of “weg” te horen en na de pieptoon moet je dan op de overeenkomstige pijltjestoets drukken. Volg altijd de gesproken aanwijzingen op na het horen van de pieptoon.\n\nWe gaan dit eerst een paar keer oefenen.', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='training_4_text',
     autoLog=False,
)
next_text_13 = visual.TextBox2(
     win, text='druk op “enter” om naar het scenario te luisteren', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_13',
     autoLog=False,
)
next_press_13 = keyboard.Keyboard()

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "training_4" ---

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "t4_incorrect" ---

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "t4_trial_2" ---
t4_2_text = visual.TextStim(win=win, name='t4_2_text',
    text='',
    font='Open Sans',
    units='height', pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyResp_3 = keyboard.Keyboard()
t4_border = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -.4),units='height',     letterHeight=0.05,
     size=(.2, .1), borderWidth=2.0,
     color=None, colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='t4_border',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "instr_forced" ---
instr_forced_text = visual.TextBox2(
     win, text='Je bent nu klaar met oefenen. Nu gaan we verder met de scenario’s. Dus nogmaals: Volg altijd de gesproken aanwijzingen op na het horen van de pieptoon.', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='instr_forced_text',
     autoLog=False,
)
next_text_15 = visual.TextBox2(
     win, text='druk op “enter” om naar het scenario te luisteren', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_15',
     autoLog=False,
)
next_press_15 = keyboard.Keyboard()

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "forced_trial_1" ---

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "forced_trial_incorrect" ---

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "forced_trial_2" ---
forced_2_text = visual.TextStim(win=win, name='forced_2_text',
    text='',
    font='Open Sans',
    units='height', pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyResp_2 = keyboard.Keyboard()
forced_2_border = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -.4),units='height',     letterHeight=0.05,
     size=(.2, .1), borderWidth=2.0,
     color=None, colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='forced_2_border',
     autoLog=False,
)

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "check_instruction" ---
instr_forced_text_2 = visual.TextBox2(
     win, text="In het laatste deel van het experiment zijn wij geïnteresseerd in de manier waarop je de scenario's die je tijdens het experiment hebt gehoord, hebt waargenomen. Beantwoord de vragen die je op je scherm ziet door je buikgevoel te volgen.\n\nBeantwoord de vragen met een muisklik.", font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.05,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.1, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='instr_forced_text_2',
     autoLog=False,
)
next_text_18 = visual.TextBox2(
     win, text='druk op “enter” om naar het scenario te luisteren', font='Open Sans',
     pos=(.45, -0.4),units='height',     letterHeight=0.02,
     size=(.2,.08), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.01, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='next_text_18',
     autoLog=False,
)
next_press_19 = keyboard.Keyboard()

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "check_likert" ---
# Run 'Begin Experiment' code from check_likert_code
# Likert questions to check whether participants can empathize well with the scenarios, can hear them well, and whether they believed someone was in need of help or not
labels_2 = ['1', '2', '3', '4', '5']

check_1 = visual.RatingScale( # 1-5 Likert
    win, low = 1, high = 5,
    markerStart = 12, markerColor = 'Black', textSize = .6, textColor = 'Black', lineColor = 'Black', showAccept = False, mouseOnly = True,
    pos=(0,300), size= 1, marker = 'circle', textFont = 'Open Sans', labels = labels_2,
    acceptKeys = 'b', scale = '1 = helemaal niet gevaarlijk                    5 = heel erg gevaarlijk')
    
check_2 = visual.RatingScale( # 1-5 Likert
    win, low = 1, high = 5,
    markerStart = 12, markerColor = 'Black', textSize = .6, textColor = 'Black', lineColor = 'Black', showAccept = False, mouseOnly = True,
    pos=(0,0), size= 1, marker = 'circle', textFont = 'Open Sans', labels = labels_2,
    acceptKeys = 'b', scale = '1 = helemaal niet belangrijk                    5 = heel erg belangrijk')
    
check_3 = visual.RatingScale( # dichotomous
    win, low = 1, high = 5, scale = '1 = helemaal niet realistisch                    5 = heel erg realistisch', mouseOnly = True,
    markerStart = 12, markerColor = 'Black', textColor = 'Black', lineColor = 'Black', showAccept = False,
    pos=(0,-300), size=1, marker = 'circle', textSize = .6, labels = labels_2,
    acceptKeys = 'b', textFont = 'Open Sans')

check_text = visual.TextStim(win, text="", height=.025, units='height', pos=(0, .4), color = 'Black') 
#tickMarks = label,

# --- Initialize components for Routine "w" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "debriefing" ---
debriefing_text = visual.TextBox2(
     win, text='Je bent klaar met het experiment. Bedankt voor je deelname. Ga nu naar de proefleider.', font='Open Sans',
     pos=(0, 0),units='height',     letterHeight=0.025,
     size=(0.95, 0.95), borderWidth=0.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.15, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='debriefing_text',
     autoLog=True,
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "hide_mouse" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from hide_mouse_code
win.mouseVisible = True 


# keep track of which components have finished
hide_mouseComponents = []
for thisComponent in hide_mouseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "hide_mouse" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hide_mouseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "hide_mouse" ---
for thisComponent in hide_mouseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from hide_mouse_code
win.mouseVisible = False # hides the mouse, did not find another way to make this work.
# the Routine "hide_mouse" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "info1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from clock_init








next_press.keys = []
next_press.rt = []
_next_press_allKeys = []
next_text.reset()
info1_text.reset()
# keep track of which components have finished
info1Components = [next_press, next_text, info1_text]
for thisComponent in info1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "info1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *next_press* updates
    waitOnFlip = False
    if next_press.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press.frameNStart = frameN  # exact frame index
        next_press.tStart = t  # local t and not account for scr refresh
        next_press.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press, 'tStartRefresh')  # time at next scr refresh
        next_press.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press.status == STARTED and not waitOnFlip:
        theseKeys = next_press.getKeys(keyList=['return'], waitRelease=False)
        _next_press_allKeys.extend(theseKeys)
        if len(_next_press_allKeys):
            next_press.keys = _next_press_allKeys[-1].name  # just the last key pressed
            next_press.rt = _next_press_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text* updates
    if next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text.frameNStart = frameN  # exact frame index
        next_text.tStart = t  # local t and not account for scr refresh
        next_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text, 'tStartRefresh')  # time at next scr refresh
        next_text.setAutoDraw(True)
    
    # *info1_text* updates
    if info1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info1_text.frameNStart = frameN  # exact frame index
        info1_text.tStart = t  # local t and not account for scr refresh
        info1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info1_text, 'tStartRefresh')  # time at next scr refresh
        info1_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "info1" ---
for thisComponent in info1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "info1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "info2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
info2_text.reset()
next_press_2.keys = []
next_press_2.rt = []
_next_press_2_allKeys = []
next_text_2.reset()
# keep track of which components have finished
info2Components = [info2_text, next_press_2, next_text_2]
for thisComponent in info2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "info2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *info2_text* updates
    if info2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info2_text.frameNStart = frameN  # exact frame index
        info2_text.tStart = t  # local t and not account for scr refresh
        info2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info2_text, 'tStartRefresh')  # time at next scr refresh
        info2_text.setAutoDraw(True)
    
    # *next_press_2* updates
    waitOnFlip = False
    if next_press_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_2.frameNStart = frameN  # exact frame index
        next_press_2.tStart = t  # local t and not account for scr refresh
        next_press_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_2, 'tStartRefresh')  # time at next scr refresh
        next_press_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_2.status == STARTED and not waitOnFlip:
        theseKeys = next_press_2.getKeys(keyList=['return'], waitRelease=False)
        _next_press_2_allKeys.extend(theseKeys)
        if len(_next_press_2_allKeys):
            next_press_2.keys = _next_press_2_allKeys[-1].name  # just the last key pressed
            next_press_2.rt = _next_press_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_2* updates
    if next_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_2.frameNStart = frameN  # exact frame index
        next_text_2.tStart = t  # local t and not account for scr refresh
        next_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_2, 'tStartRefresh')  # time at next scr refresh
        next_text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "info2" ---
for thisComponent in info2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "info2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "info3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
info3_text.reset()
next_press_3.keys = []
next_press_3.rt = []
_next_press_3_allKeys = []
next_text_3.reset()
# keep track of which components have finished
info3Components = [info3_text, next_press_3, next_text_3]
for thisComponent in info3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "info3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *info3_text* updates
    if info3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info3_text.frameNStart = frameN  # exact frame index
        info3_text.tStart = t  # local t and not account for scr refresh
        info3_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info3_text, 'tStartRefresh')  # time at next scr refresh
        info3_text.setAutoDraw(True)
    
    # *next_press_3* updates
    waitOnFlip = False
    if next_press_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_3.frameNStart = frameN  # exact frame index
        next_press_3.tStart = t  # local t and not account for scr refresh
        next_press_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_3, 'tStartRefresh')  # time at next scr refresh
        next_press_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_3.status == STARTED and not waitOnFlip:
        theseKeys = next_press_3.getKeys(keyList=['return'], waitRelease=False)
        _next_press_3_allKeys.extend(theseKeys)
        if len(_next_press_3_allKeys):
            next_press_3.keys = _next_press_3_allKeys[-1].name  # just the last key pressed
            next_press_3.rt = _next_press_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_3* updates
    if next_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_3.frameNStart = frameN  # exact frame index
        next_text_3.tStart = t  # local t and not account for scr refresh
        next_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_3, 'tStartRefresh')  # time at next scr refresh
        next_text_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "info3" ---
for thisComponent in info3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "info3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "info4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
info4_text.reset()
next_press_4.keys = []
next_press_4.rt = []
_next_press_4_allKeys = []
next_text_4.reset()
# keep track of which components have finished
info4Components = [info4_text, next_press_4, next_text_4]
for thisComponent in info4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "info4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *info4_text* updates
    if info4_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info4_text.frameNStart = frameN  # exact frame index
        info4_text.tStart = t  # local t and not account for scr refresh
        info4_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info4_text, 'tStartRefresh')  # time at next scr refresh
        info4_text.setAutoDraw(True)
    
    # *next_press_4* updates
    waitOnFlip = False
    if next_press_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_4.frameNStart = frameN  # exact frame index
        next_press_4.tStart = t  # local t and not account for scr refresh
        next_press_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_4, 'tStartRefresh')  # time at next scr refresh
        next_press_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_4.status == STARTED and not waitOnFlip:
        theseKeys = next_press_4.getKeys(keyList=['return'], waitRelease=False)
        _next_press_4_allKeys.extend(theseKeys)
        if len(_next_press_4_allKeys):
            next_press_4.keys = _next_press_4_allKeys[-1].name  # just the last key pressed
            next_press_4.rt = _next_press_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_4* updates
    if next_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_4.frameNStart = frameN  # exact frame index
        next_text_4.tStart = t  # local t and not account for scr refresh
        next_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_4, 'tStartRefresh')  # time at next scr refresh
        next_text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in info4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "info4" ---
for thisComponent in info4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "info4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "consent" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
consent_text.reset()
next_press_5.keys = []
next_press_5.rt = []
_next_press_5_allKeys = []
next_text_5.reset()
# keep track of which components have finished
consentComponents = [consent_text, next_press_5, next_text_5]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "consent" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consent_text* updates
    if consent_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_text.frameNStart = frameN  # exact frame index
        consent_text.tStart = t  # local t and not account for scr refresh
        consent_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_text, 'tStartRefresh')  # time at next scr refresh
        consent_text.setAutoDraw(True)
    
    # *next_press_5* updates
    waitOnFlip = False
    if next_press_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_5.frameNStart = frameN  # exact frame index
        next_press_5.tStart = t  # local t and not account for scr refresh
        next_press_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_5, 'tStartRefresh')  # time at next scr refresh
        next_press_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_5.status == STARTED and not waitOnFlip:
        theseKeys = next_press_5.getKeys(keyList=['return'], waitRelease=False)
        _next_press_5_allKeys.extend(theseKeys)
        if len(_next_press_5_allKeys):
            next_press_5.keys = _next_press_5_allKeys[-1].name  # just the last key pressed
            next_press_5.rt = _next_press_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_5* updates
    if next_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_5.frameNStart = frameN  # exact frame index
        next_text_5.tStart = t  # local t and not account for scr refresh
        next_text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_5, 'tStartRefresh')  # time at next scr refresh
        next_text_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "consent" ---
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "pre_instructions_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
pre_instructions_1_text.reset()
next_press_6.keys = []
next_press_6.rt = []
_next_press_6_allKeys = []
next_text_6.reset()
# keep track of which components have finished
pre_instructions_1Components = [pre_instructions_1_text, next_press_6, next_text_6]
for thisComponent in pre_instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pre_instructions_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pre_instructions_1_text* updates
    if pre_instructions_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre_instructions_1_text.frameNStart = frameN  # exact frame index
        pre_instructions_1_text.tStart = t  # local t and not account for scr refresh
        pre_instructions_1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre_instructions_1_text, 'tStartRefresh')  # time at next scr refresh
        pre_instructions_1_text.setAutoDraw(True)
    
    # *next_press_6* updates
    waitOnFlip = False
    if next_press_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_6.frameNStart = frameN  # exact frame index
        next_press_6.tStart = t  # local t and not account for scr refresh
        next_press_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_6, 'tStartRefresh')  # time at next scr refresh
        next_press_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_6.status == STARTED and not waitOnFlip:
        theseKeys = next_press_6.getKeys(keyList=['return'], waitRelease=False)
        _next_press_6_allKeys.extend(theseKeys)
        if len(_next_press_6_allKeys):
            next_press_6.keys = _next_press_6_allKeys[-1].name  # just the last key pressed
            next_press_6.rt = _next_press_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_6* updates
    if next_text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_6.frameNStart = frameN  # exact frame index
        next_text_6.tStart = t  # local t and not account for scr refresh
        next_text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_6, 'tStartRefresh')  # time at next scr refresh
        next_text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pre_instructions_1" ---
for thisComponent in pre_instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pre_instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "pre_instructions_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
pre_instructions_2_text.reset()
next_press_7.keys = []
next_press_7.rt = []
_next_press_7_allKeys = []
next_text_7.reset()
# keep track of which components have finished
pre_instructions_2Components = [pre_instructions_2_text, next_press_7, next_text_7]
for thisComponent in pre_instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pre_instructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pre_instructions_2_text* updates
    if pre_instructions_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre_instructions_2_text.frameNStart = frameN  # exact frame index
        pre_instructions_2_text.tStart = t  # local t and not account for scr refresh
        pre_instructions_2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre_instructions_2_text, 'tStartRefresh')  # time at next scr refresh
        pre_instructions_2_text.setAutoDraw(True)
    
    # *next_press_7* updates
    waitOnFlip = False
    if next_press_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_7.frameNStart = frameN  # exact frame index
        next_press_7.tStart = t  # local t and not account for scr refresh
        next_press_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_7, 'tStartRefresh')  # time at next scr refresh
        next_press_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_7.status == STARTED and not waitOnFlip:
        theseKeys = next_press_7.getKeys(keyList=['return'], waitRelease=False)
        _next_press_7_allKeys.extend(theseKeys)
        if len(_next_press_7_allKeys):
            next_press_7.keys = _next_press_7_allKeys[-1].name  # just the last key pressed
            next_press_7.rt = _next_press_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_7* updates
    if next_text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_7.frameNStart = frameN  # exact frame index
        next_text_7.tStart = t  # local t and not account for scr refresh
        next_text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_7, 'tStartRefresh')  # time at next scr refresh
        next_text_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pre_instructions_2" ---
for thisComponent in pre_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pre_instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "training_1_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
training_1_instructions_text.reset()
next_press_8.keys = []
next_press_8.rt = []
_next_press_8_allKeys = []
next_text_8.reset()
# keep track of which components have finished
training_1_instructionsComponents = [training_1_instructions_text, next_press_8, next_text_8]
for thisComponent in training_1_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "training_1_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *training_1_instructions_text* updates
    if training_1_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        training_1_instructions_text.frameNStart = frameN  # exact frame index
        training_1_instructions_text.tStart = t  # local t and not account for scr refresh
        training_1_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(training_1_instructions_text, 'tStartRefresh')  # time at next scr refresh
        training_1_instructions_text.setAutoDraw(True)
    
    # *next_press_8* updates
    waitOnFlip = False
    if next_press_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_8.frameNStart = frameN  # exact frame index
        next_press_8.tStart = t  # local t and not account for scr refresh
        next_press_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_8, 'tStartRefresh')  # time at next scr refresh
        next_press_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_8.status == STARTED and not waitOnFlip:
        theseKeys = next_press_8.getKeys(keyList=['return'], waitRelease=False)
        _next_press_8_allKeys.extend(theseKeys)
        if len(_next_press_8_allKeys):
            next_press_8.keys = _next_press_8_allKeys[-1].name  # just the last key pressed
            next_press_8.rt = _next_press_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_8* updates
    if next_text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_8.frameNStart = frameN  # exact frame index
        next_text_8.tStart = t  # local t and not account for scr refresh
        next_text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_8, 'tStartRefresh')  # time at next scr refresh
        next_text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_1_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "training_1_instructions" ---
for thisComponent in training_1_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "training_1_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# set up handler to look after randomisation of conditions etc
training_1_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition files/conditions_training_1.xlsx'),
    seed=None, name='training_1_trials')
thisExp.addLoop(training_1_trials)  # add the loop to the experiment
thisTraining_1_trial = training_1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_1_trial.rgb)
if thisTraining_1_trial != None:
    for paramName in thisTraining_1_trial:
        exec('{} = thisTraining_1_trial[paramName]'.format(paramName))

for thisTraining_1_trial in training_1_trials:
    currentLoop = training_1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_1_trial.rgb)
    if thisTraining_1_trial != None:
        for paramName in thisTraining_1_trial:
            exec('{} = thisTraining_1_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "training_1_trial_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from training_1_trial_1_code
    # create sound and set its parameters
    training_1_sound = sound.Sound(soundpath_t1,
        stopTime = duration_t1,
        loops = 0,
        volume = 1) 
        
    training_1_sound.play()
    
    # draw all clock objects
    clock_static()
        
    win.flip() # update the screen
    
    core.wait(duration_t1 + 1) # need to wait slightly longer than the duration of the audio to prevent audio overlap
    
    if t > duration_t1 + 1:
        continueRoutine = False
     
    # check for escape key press to exit
    if event.getKeys(keyList=['escape']):
        win.close()
            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
        
    
            
        
    
    
    
    # keep track of which components have finished
    training_1_trial_1Components = []
    for thisComponent in training_1_trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "training_1_trial_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_1_trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_1_trial_1" ---
    for thisComponent in training_1_trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "training_1_trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "likert" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from likert_code
    win.mouseVisible = True 
    while continueRoutine == True: # main loop
        item_1.draw() # draw all items, likert scales, and the next button text
        item_2.draw()
        item_3.draw()
        likert_1.draw()
        likert_2.draw()
        likert_3.draw()
        next_text_2.draw()
        win.flip()
        
        if event.getKeys(keyList=['escape']): # quit experiment
            core.quit()
        if event.getKeys(keyList=['return']):
            training_1_trials.addData('likert_1', likert_1.getRating()) # crucially, add likert data once enter is pressed
            training_1_trials.addData('likert_2', likert_2.getRating())
            training_1_trials.addData('likert_3', likert_3.getRating())
            likert_1.reset() 
            likert_2.reset()
            likert_3.reset()
            likert_1.markerStart = 12 # resets marker to a value beyond the scale. This means in the next trial it is not visible before a value has been entered
            likert_2.markerStart = 12
            likert_3.markerStart = 12
            continueRoutine = False # go to next routine
     
    
    
    
    
    # keep track of which components have finished
    likertComponents = []
    for thisComponent in likertComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "likert" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from likert_code
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in likertComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "likert" ---
    for thisComponent in likertComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from likert_code
    win.mouseVisible = False
    # the Routine "likert" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'training_1_trials'

# get names of stimulus parameters
if training_1_trials.trialList in ([], [None], None):
    params = []
else:
    params = training_1_trials.trialList[0].keys()
# save data for this loop
training_1_trials.saveAsExcel(filename + '.xlsx', sheetName='training_1_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "training_2_instructions_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
training_2_instructions_1_text.reset()
next_press_9.keys = []
next_press_9.rt = []
_next_press_9_allKeys = []
next_text_9.reset()
# keep track of which components have finished
training_2_instructions_1Components = [training_2_instructions_1_text, arrowkeys, next_press_9, next_text_9]
for thisComponent in training_2_instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "training_2_instructions_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *training_2_instructions_1_text* updates
    if training_2_instructions_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        training_2_instructions_1_text.frameNStart = frameN  # exact frame index
        training_2_instructions_1_text.tStart = t  # local t and not account for scr refresh
        training_2_instructions_1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(training_2_instructions_1_text, 'tStartRefresh')  # time at next scr refresh
        training_2_instructions_1_text.setAutoDraw(True)
    
    # *arrowkeys* updates
    if arrowkeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arrowkeys.frameNStart = frameN  # exact frame index
        arrowkeys.tStart = t  # local t and not account for scr refresh
        arrowkeys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arrowkeys, 'tStartRefresh')  # time at next scr refresh
        arrowkeys.setAutoDraw(True)
    
    # *next_press_9* updates
    waitOnFlip = False
    if next_press_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_9.frameNStart = frameN  # exact frame index
        next_press_9.tStart = t  # local t and not account for scr refresh
        next_press_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_9, 'tStartRefresh')  # time at next scr refresh
        next_press_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_9.status == STARTED and not waitOnFlip:
        theseKeys = next_press_9.getKeys(keyList=['return'], waitRelease=False)
        _next_press_9_allKeys.extend(theseKeys)
        if len(_next_press_9_allKeys):
            next_press_9.keys = _next_press_9_allKeys[-1].name  # just the last key pressed
            next_press_9.rt = _next_press_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_9* updates
    if next_text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_9.frameNStart = frameN  # exact frame index
        next_text_9.tStart = t  # local t and not account for scr refresh
        next_text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_9, 'tStartRefresh')  # time at next scr refresh
        next_text_9.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_2_instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "training_2_instructions_1" ---
for thisComponent in training_2_instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "training_2_instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "training_2_instructions_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
training_2_instructions_2_text.reset()
next_press_10.keys = []
next_press_10.rt = []
_next_press_10_allKeys = []
next_text_10.reset()
# keep track of which components have finished
training_2_instructions_2Components = [training_2_instructions_2_text, next_press_10, next_text_10, keyboard_instr]
for thisComponent in training_2_instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "training_2_instructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *training_2_instructions_2_text* updates
    if training_2_instructions_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        training_2_instructions_2_text.frameNStart = frameN  # exact frame index
        training_2_instructions_2_text.tStart = t  # local t and not account for scr refresh
        training_2_instructions_2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(training_2_instructions_2_text, 'tStartRefresh')  # time at next scr refresh
        training_2_instructions_2_text.setAutoDraw(True)
    
    # *next_press_10* updates
    waitOnFlip = False
    if next_press_10.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_10.frameNStart = frameN  # exact frame index
        next_press_10.tStart = t  # local t and not account for scr refresh
        next_press_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_10, 'tStartRefresh')  # time at next scr refresh
        next_press_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_10.status == STARTED and not waitOnFlip:
        theseKeys = next_press_10.getKeys(keyList=['return'], waitRelease=False)
        _next_press_10_allKeys.extend(theseKeys)
        if len(_next_press_10_allKeys):
            next_press_10.keys = _next_press_10_allKeys[-1].name  # just the last key pressed
            next_press_10.rt = _next_press_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_10* updates
    if next_text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_10.frameNStart = frameN  # exact frame index
        next_text_10.tStart = t  # local t and not account for scr refresh
        next_text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_10, 'tStartRefresh')  # time at next scr refresh
        next_text_10.setAutoDraw(True)
    
    # *keyboard_instr* updates
    if keyboard_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyboard_instr.frameNStart = frameN  # exact frame index
        keyboard_instr.tStart = t  # local t and not account for scr refresh
        keyboard_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyboard_instr, 'tStartRefresh')  # time at next scr refresh
        keyboard_instr.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_2_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "training_2_instructions_2" ---
for thisComponent in training_2_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "training_2_instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "pre_t3_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
pre_t3_instructions_text_1.reset()
next_press_17.keys = []
next_press_17.rt = []
_next_press_17_allKeys = []
next_text_16.reset()
# keep track of which components have finished
pre_t3_instructionsComponents = [pre_t3_instructions_text_1, next_press_17, next_text_16]
for thisComponent in pre_t3_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pre_t3_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pre_t3_instructions_text_1* updates
    if pre_t3_instructions_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre_t3_instructions_text_1.frameNStart = frameN  # exact frame index
        pre_t3_instructions_text_1.tStart = t  # local t and not account for scr refresh
        pre_t3_instructions_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre_t3_instructions_text_1, 'tStartRefresh')  # time at next scr refresh
        pre_t3_instructions_text_1.setAutoDraw(True)
    
    # *next_press_17* updates
    waitOnFlip = False
    if next_press_17.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_17.frameNStart = frameN  # exact frame index
        next_press_17.tStart = t  # local t and not account for scr refresh
        next_press_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_17, 'tStartRefresh')  # time at next scr refresh
        next_press_17.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_17.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_17.status == STARTED and not waitOnFlip:
        theseKeys = next_press_17.getKeys(keyList=['up'], waitRelease=False)
        _next_press_17_allKeys.extend(theseKeys)
        if len(_next_press_17_allKeys):
            next_press_17.keys = _next_press_17_allKeys[-1].name  # just the last key pressed
            next_press_17.rt = _next_press_17_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_16* updates
    if next_text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_16.frameNStart = frameN  # exact frame index
        next_text_16.tStart = t  # local t and not account for scr refresh
        next_text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_16, 'tStartRefresh')  # time at next scr refresh
        next_text_16.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_t3_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pre_t3_instructions" ---
for thisComponent in pre_t3_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pre_t3_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "pre_t3_instructions_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
pre_t3_instructions_text.reset()
next_press_18.keys = []
next_press_18.rt = []
_next_press_18_allKeys = []
next_text_17.reset()
# keep track of which components have finished
pre_t3_instructions_2Components = [pre_t3_instructions_text, next_press_18, next_text_17]
for thisComponent in pre_t3_instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pre_t3_instructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pre_t3_instructions_text* updates
    if pre_t3_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre_t3_instructions_text.frameNStart = frameN  # exact frame index
        pre_t3_instructions_text.tStart = t  # local t and not account for scr refresh
        pre_t3_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre_t3_instructions_text, 'tStartRefresh')  # time at next scr refresh
        pre_t3_instructions_text.setAutoDraw(True)
    
    # *next_press_18* updates
    waitOnFlip = False
    if next_press_18.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_18.frameNStart = frameN  # exact frame index
        next_press_18.tStart = t  # local t and not account for scr refresh
        next_press_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_18, 'tStartRefresh')  # time at next scr refresh
        next_press_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_18.status == STARTED and not waitOnFlip:
        theseKeys = next_press_18.getKeys(keyList=['down'], waitRelease=False)
        _next_press_18_allKeys.extend(theseKeys)
        if len(_next_press_18_allKeys):
            next_press_18.keys = _next_press_18_allKeys[-1].name  # just the last key pressed
            next_press_18.rt = _next_press_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_17* updates
    if next_text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_17.frameNStart = frameN  # exact frame index
        next_text_17.tStart = t  # local t and not account for scr refresh
        next_text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_17, 'tStartRefresh')  # time at next scr refresh
        next_text_17.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_t3_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pre_t3_instructions_2" ---
for thisComponent in pre_t3_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pre_t3_instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "training_2_instructions_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
next_press_14.keys = []
next_press_14.rt = []
_next_press_14_allKeys = []
next_text_14.reset()
training_2_instructions_3_text.reset()
# keep track of which components have finished
training_2_instructions_3Components = [next_press_14, next_text_14, training_2_instructions_3_text]
for thisComponent in training_2_instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "training_2_instructions_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *next_press_14* updates
    waitOnFlip = False
    if next_press_14.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_14.frameNStart = frameN  # exact frame index
        next_press_14.tStart = t  # local t and not account for scr refresh
        next_press_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_14, 'tStartRefresh')  # time at next scr refresh
        next_press_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_14.status == STARTED and not waitOnFlip:
        theseKeys = next_press_14.getKeys(keyList=['return'], waitRelease=False)
        _next_press_14_allKeys.extend(theseKeys)
        if len(_next_press_14_allKeys):
            next_press_14.keys = _next_press_14_allKeys[-1].name  # just the last key pressed
            next_press_14.rt = _next_press_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_14* updates
    if next_text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_14.frameNStart = frameN  # exact frame index
        next_text_14.tStart = t  # local t and not account for scr refresh
        next_text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_14, 'tStartRefresh')  # time at next scr refresh
        next_text_14.setAutoDraw(True)
    
    # *training_2_instructions_3_text* updates
    if training_2_instructions_3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        training_2_instructions_3_text.frameNStart = frameN  # exact frame index
        training_2_instructions_3_text.tStart = t  # local t and not account for scr refresh
        training_2_instructions_3_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(training_2_instructions_3_text, 'tStartRefresh')  # time at next scr refresh
        training_2_instructions_3_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_2_instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "training_2_instructions_3" ---
for thisComponent in training_2_instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "training_2_instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# set up handler to look after randomisation of conditions etc
training_2_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition files/conditions_training_2.xlsx'),
    seed=None, name='training_2_trials')
thisExp.addLoop(training_2_trials)  # add the loop to the experiment
thisTraining_2_trial = training_2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_2_trial.rgb)
if thisTraining_2_trial != None:
    for paramName in thisTraining_2_trial:
        exec('{} = thisTraining_2_trial[paramName]'.format(paramName))

for thisTraining_2_trial in training_2_trials:
    currentLoop = training_2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_2_trial.rgb)
    if thisTraining_2_trial != None:
        for paramName in thisTraining_2_trial:
            exec('{} = thisTraining_2_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "training_2_trial_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from training_2_trial_code
    # create scenario sound
    training_2_trial_1_sound = sound.Sound(soundpath_t2,
        stopTime = duration_t2,
        loops = 0,
        volume = 1,)
    
    clock_static() # draw all clock objects & update window
    win.flip()
    
    # play sound
    training_2_trial_1_sound.play() 
    core.wait(duration_t2) # wait for length of scenario file
    core.wait(buffer) # delay to prevent audio overlap
    kies.play() # play action word 
    core.wait(0.843) # wait for 0.25 + 0.593 (length of action word soundfiles)
    beep.play() 
    
    # wait for and record the key pressed
    response = event.waitKeys(keyList = keys)
    while continueRoutine == True:
        if response[0] in keys:
            training_2_trials.addData('response', response)
            continueRoutine = False
    # keep track of which components have finished
    training_2_trial_1Components = []
    for thisComponent in training_2_trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "training_2_trial_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_2_trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_2_trial_1" ---
    for thisComponent in training_2_trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "training_2_trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'training_2_trials'

# get names of stimulus parameters
if training_2_trials.trialList in ([], [None], None):
    params = []
else:
    params = training_2_trials.trialList[0].keys()
# save data for this loop
training_2_trials.saveAsExcel(filename + '.xlsx', sheetName='training_2_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "training_3_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
training_3_instructions_text.reset()
next_press_11.keys = []
next_press_11.rt = []
_next_press_11_allKeys = []
next_text_11.reset()
# keep track of which components have finished
training_3_instructionsComponents = [training_3_instructions_text, next_press_11, next_text_11]
for thisComponent in training_3_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "training_3_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *training_3_instructions_text* updates
    if training_3_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        training_3_instructions_text.frameNStart = frameN  # exact frame index
        training_3_instructions_text.tStart = t  # local t and not account for scr refresh
        training_3_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(training_3_instructions_text, 'tStartRefresh')  # time at next scr refresh
        training_3_instructions_text.setAutoDraw(True)
    
    # *next_press_11* updates
    waitOnFlip = False
    if next_press_11.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_11.frameNStart = frameN  # exact frame index
        next_press_11.tStart = t  # local t and not account for scr refresh
        next_press_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_11, 'tStartRefresh')  # time at next scr refresh
        next_press_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_11.status == STARTED and not waitOnFlip:
        theseKeys = next_press_11.getKeys(keyList=['return'], waitRelease=False)
        _next_press_11_allKeys.extend(theseKeys)
        if len(_next_press_11_allKeys):
            next_press_11.keys = _next_press_11_allKeys[-1].name  # just the last key pressed
            next_press_11.rt = _next_press_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_11* updates
    if next_text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_11.frameNStart = frameN  # exact frame index
        next_text_11.tStart = t  # local t and not account for scr refresh
        next_text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_11, 'tStartRefresh')  # time at next scr refresh
        next_text_11.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_3_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "training_3_instructions" ---
for thisComponent in training_3_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "training_3_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# set up handler to look after randomisation of conditions etc
training_3_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition files/conditions_training_3.xlsx'),
    seed=None, name='training_3_trials')
thisExp.addLoop(training_3_trials)  # add the loop to the experiment
thisTraining_3_trial = training_3_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_3_trial.rgb)
if thisTraining_3_trial != None:
    for paramName in thisTraining_3_trial:
        exec('{} = thisTraining_3_trial[paramName]'.format(paramName))

for thisTraining_3_trial in training_3_trials:
    currentLoop = training_3_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_3_trial.rgb)
    if thisTraining_3_trial != None:
        for paramName in thisTraining_3_trial:
            exec('{} = thisTraining_3_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "training_3_trial_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from training_3_trial_1_code
    # create some init variables
    objective_time = []
    revolutions = []
    delay = random.uniform(1.28, 2.56)
    
    timer = clock.Clock()
    # define trial sound
    t3_sound = sound.Sound(soundpath_t3,
        startTime = 0,
        stopTime = duration_t3 + buffer, 
        loops = 0,
        volume = 1) 
        
    dur_t3 = duration_t3 + buffer # prevents audio overlap    
    
    t3_sound.play() # animate clock and play scenario soundfile
    
    while timer.getTime() <= (dur_t3):
        clock_full()   
        win.flip()
        
    t3_sound.stop()    
    kies.play() # animate clock and play action word
    while timer.getTime() >= (dur_t3) and timer.getTime() <= (dur_t3+0.843):
        clock_full()   
        win.flip()
    
    kies.stop()
    
    while timer.getTime() >= (dur_t3+0.843) and timer.getTime() <= (dur_t3+1.043): # animate clock and play beep
        clock_full()   
        win.flip()
     
    beep.play()
    response_t3 = event.getKeys(keyList = keys)
    
    while True:
        response_t3 = event.getKeys(keyList = keys)
        if len(response_t3)>0:
            objective_time.append(timer.getTime()-(dur_t3+1.043)) # store the objective timing
            training_3_trials.addData('objective', objective_time)
            training_3_trials.addData('judgement', response_t3) # store M judgement
            break
        clock_full()   
        win.flip()
    
    delay_clock = clock.Clock()
    while delay_clock.getTime() <= delay: # see above
        clock_full()   
        win.flip()
                 
    continueRoutine = False
    
    
    
    
    # keep track of which components have finished
    training_3_trial_1Components = []
    for thisComponent in training_3_trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "training_3_trial_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_3_trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_3_trial_1" ---
    for thisComponent in training_3_trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "training_3_trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "training_3_trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keyResp.keys = []
    keyResp.rt = []
    _keyResp_allKeys = []
    # Run 'Begin Routine' code from training_3_trial_2_code
    #clock_static()
    resp_display = ""
    maxDigits = 2
    
    #key logger defaults
    last_len = 0
    key_list = []
    # draw all required objects
    next_text_2.setAutoDraw(True) 
    question.setAutoDraw(True)
    hint_box.setAutoDraw(True)
    clock_circle.setAutoDraw(True)
    center_dot.setAutoDraw(True)
    for labels in clock_labels:
        labels.setAutoDraw(True)
    for ticks_a in ticks_large:
        ticks_a.setAutoDraw(True)
    win.flip()
    t3_border.reset()
    # keep track of which components have finished
    training_3_trial_2Components = [t3_text, keyResp, t3_border]
    for thisComponent in training_3_trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "training_3_trial_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *t3_text* updates
        if t3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t3_text.frameNStart = frameN  # exact frame index
            t3_text.tStart = t  # local t and not account for scr refresh
            t3_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t3_text, 'tStartRefresh')  # time at next scr refresh
            t3_text.setAutoDraw(True)
        if t3_text.status == STARTED:  # only update if drawing
            t3_text.setText(resp_display, log=False)
        
        # *keyResp* updates
        waitOnFlip = False
        if keyResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            keyResp.frameNStart = frameN  # exact frame index
            keyResp.tStart = t  # local t and not account for scr refresh
            keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
            keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyResp.status == STARTED and not waitOnFlip:
            theseKeys = keyResp.getKeys(keyList=['return','backspace','0','1','2','3','4','5','6','7','8','9','num_0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9'], waitRelease=False)
            _keyResp_allKeys.extend(theseKeys)
            if len(_keyResp_allKeys):
                keyResp.keys = [key.name for key in _keyResp_allKeys]  # storing all keys
                keyResp.rt = [key.rt for key in _keyResp_allKeys]
        # Run 'Each Frame' code from training_3_trial_2_code
        #if a new key has been pressed since last time
        if(len(keyResp.keys) > last_len):
            
            #increment the key logger length
            last_len = len(keyResp.keys)
            
            #grab the last key added to the keys list
            key_list.append(keyResp.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
                
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 1):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            key_list = [keys.replace('num_', '') for keys in key_list]
            resp_display = ''.join(key_list)
        
        # *t3_border* updates
        if t3_border.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t3_border.frameNStart = frameN  # exact frame index
            t3_border.tStart = t  # local t and not account for scr refresh
            t3_border.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t3_border, 'tStartRefresh')  # time at next scr refresh
            t3_border.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_3_trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_3_trial_2" ---
    for thisComponent in training_3_trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyResp.keys in ['', [], None]:  # No response was made
        keyResp.keys = None
    training_3_trials.addData('keyResp.keys',keyResp.keys)
    if keyResp.keys != None:  # we had a response
        training_3_trials.addData('keyResp.rt', keyResp.rt)
    # Run 'End Routine' code from training_3_trial_2_code
    training_3_trials.addData('subj_rating', key_list)
    
    next_text_2.setAutoDraw(False)
    question.setAutoDraw(False)
    hint_box.setAutoDraw(False)
    clock_circle.setAutoDraw(False)
    center_dot.setAutoDraw(False)
    for labels in clock_labels:
        labels.setAutoDraw(False)
    for ticks_a in ticks_large:
        ticks_a.setAutoDraw(False)
    
    win.flip()
    # the Routine "training_3_trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'training_3_trials'

# get names of stimulus parameters
if training_3_trials.trialList in ([], [None], None):
    params = []
else:
    params = training_3_trials.trialList[0].keys()
# save data for this loop
training_3_trials.saveAsExcel(filename + '.xlsx', sheetName='training_3_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "instr_free" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_free_text_5.reset()
next_press_12.keys = []
next_press_12.rt = []
_next_press_12_allKeys = []
next_text_12.reset()
# keep track of which components have finished
instr_freeComponents = [instr_free_text_5, next_press_12, next_text_12]
for thisComponent in instr_freeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instr_free" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_free_text_5* updates
    if instr_free_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_free_text_5.frameNStart = frameN  # exact frame index
        instr_free_text_5.tStart = t  # local t and not account for scr refresh
        instr_free_text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_free_text_5, 'tStartRefresh')  # time at next scr refresh
        instr_free_text_5.setAutoDraw(True)
    
    # *next_press_12* updates
    waitOnFlip = False
    if next_press_12.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_12.frameNStart = frameN  # exact frame index
        next_press_12.tStart = t  # local t and not account for scr refresh
        next_press_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_12, 'tStartRefresh')  # time at next scr refresh
        next_press_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_12.status == STARTED and not waitOnFlip:
        theseKeys = next_press_12.getKeys(keyList=['return'], waitRelease=False)
        _next_press_12_allKeys.extend(theseKeys)
        if len(_next_press_12_allKeys):
            next_press_12.keys = _next_press_12_allKeys[-1].name  # just the last key pressed
            next_press_12.rt = _next_press_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *next_text_12* updates
    if next_text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_12.frameNStart = frameN  # exact frame index
        next_text_12.tStart = t  # local t and not account for scr refresh
        next_text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_12, 'tStartRefresh')  # time at next scr refresh
        next_text_12.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_freeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instr_free" ---
for thisComponent in instr_freeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_free" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# set up handler to look after randomisation of conditions etc
free_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition files/conditions_free.xlsx'),
    seed=None, name='free_trials')
thisExp.addLoop(free_trials)  # add the loop to the experiment
thisFree_trial = free_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFree_trial.rgb)
if thisFree_trial != None:
    for paramName in thisFree_trial:
        exec('{} = thisFree_trial[paramName]'.format(paramName))

for thisFree_trial in free_trials:
    currentLoop = free_trials
    # abbreviate parameter names if possible (e.g. rgb = thisFree_trial.rgb)
    if thisFree_trial != None:
        for paramName in thisFree_trial:
            exec('{} = thisFree_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "free_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from free_code
    # create some init variables
    objective_time = []
    revolutions = []
    delay = random.uniform(1.28, 2.56)
    
    timer = clock.Clock()
    # define trial sound
    free_sound = sound.Sound(soundpath_free,
        startTime = 0,
        stopTime = duration_free + buffer, 
        loops = 0,
        volume = 1) 
        
    dur_free = duration_free + buffer # prevents audio overlap    
    
    free_sound.play() # animate clock and play scenario soundfile
    
    while timer.getTime() <= (dur_free):
        clock_full()   
        win.flip()
        
    free_sound.stop()    
    kies.play() # animate clock and play action word
    while timer.getTime() >= (dur_free) and timer.getTime() <= (dur_free+0.843):
        clock_full()   
        win.flip()
    
    kies.stop()
    
    while timer.getTime() >= (dur_free+0.843) and timer.getTime() <= (dur_free+1.043): # animate clock and play beep
        clock_full()   
        win.flip()
     
    beep.play()
    response_free = event.getKeys(keyList = keys)
    
    while True:
        response_free = event.getKeys(keyList = keys)
        if len(response_free)>0:
            objective_time.append(timer.getTime()-(dur_free+1.043)) # store the objective timing
            free_trials.addData('objective', objective_time)
            free_trials.addData('judgement', response_free) # store M judgement
            break
        clock_full()   
        win.flip()
    
    delay_clock = clock.Clock()
    while delay_clock.getTime() <= delay: # see above
        clock_full()   
        win.flip()
                 
    continueRoutine = False
    
    
    
    
    # keep track of which components have finished
    free_trialComponents = []
    for thisComponent in free_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "free_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in free_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "free_trial" ---
    for thisComponent in free_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "free_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "free_trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keyResp_4.keys = []
    keyResp_4.rt = []
    _keyResp_4_allKeys = []
    # Run 'Begin Routine' code from free_2_code
    #clock_static()
    resp_display = ""
    maxDigits = 2
    
    #key logger defaults
    last_len = 0
    key_list = []
    # draw all required objects
    next_text_2.setAutoDraw(True)
    question.setAutoDraw(True)
    hint_box.setAutoDraw(True)
    clock_circle.setAutoDraw(True)
    center_dot.setAutoDraw(True)
    for labels in clock_labels:
        labels.setAutoDraw(True)
    for ticks_a in ticks_large:
        ticks_a.setAutoDraw(True)
    win.flip()
    free_border.reset()
    # keep track of which components have finished
    free_trial_2Components = [free_text, keyResp_4, free_border]
    for thisComponent in free_trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "free_trial_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *free_text* updates
        if free_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            free_text.frameNStart = frameN  # exact frame index
            free_text.tStart = t  # local t and not account for scr refresh
            free_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(free_text, 'tStartRefresh')  # time at next scr refresh
            free_text.setAutoDraw(True)
        if free_text.status == STARTED:  # only update if drawing
            free_text.setText(resp_display, log=False)
        
        # *keyResp_4* updates
        waitOnFlip = False
        if keyResp_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            keyResp_4.frameNStart = frameN  # exact frame index
            keyResp_4.tStart = t  # local t and not account for scr refresh
            keyResp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResp_4, 'tStartRefresh')  # time at next scr refresh
            keyResp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyResp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyResp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyResp_4.status == STARTED and not waitOnFlip:
            theseKeys = keyResp_4.getKeys(keyList=['return','backspace','0','1','2','3','4','5','6','7','8','9','num_0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9'], waitRelease=False)
            _keyResp_4_allKeys.extend(theseKeys)
            if len(_keyResp_4_allKeys):
                keyResp_4.keys = [key.name for key in _keyResp_4_allKeys]  # storing all keys
                keyResp_4.rt = [key.rt for key in _keyResp_4_allKeys]
        # Run 'Each Frame' code from free_2_code
        #if a new key has been pressed since last time
        if(len(keyResp_4.keys) > last_len):
            
            #increment the key logger length
            last_len = len(keyResp_4.keys)
            
            #grab the last key added to the keys list
            key_list.append(keyResp_4.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
                
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 1):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            key_list = [keys.replace('num_', '') for keys in key_list]
            resp_display = ''.join(key_list)
        
        # *free_border* updates
        if free_border.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            free_border.frameNStart = frameN  # exact frame index
            free_border.tStart = t  # local t and not account for scr refresh
            free_border.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(free_border, 'tStartRefresh')  # time at next scr refresh
            free_border.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in free_trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "free_trial_2" ---
    for thisComponent in free_trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyResp_4.keys in ['', [], None]:  # No response was made
        keyResp_4.keys = None
    free_trials.addData('keyResp_4.keys',keyResp_4.keys)
    if keyResp_4.keys != None:  # we had a response
        free_trials.addData('keyResp_4.rt', keyResp_4.rt)
    # Run 'End Routine' code from free_2_code
    training_3_trials.addData('subj_rating', key_list)
    
    next_text_2.setAutoDraw(False)
    question.setAutoDraw(False)
    hint_box.setAutoDraw(False)
    clock_circle.setAutoDraw(False)
    center_dot.setAutoDraw(False)
    for labels in clock_labels:
        labels.setAutoDraw(False)
    for ticks_a in ticks_large:
        ticks_a.setAutoDraw(False)
    
    win.flip()
    # the Routine "free_trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'free_trials'

# get names of stimulus parameters
if free_trials.trialList in ([], [None], None):
    params = []
else:
    params = free_trials.trialList[0].keys()
# save data for this loop
free_trials.saveAsExcel(filename + '.xlsx', sheetName='free_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "free_debrief" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
free_debrief_text.reset()
free_debrief_next_text.reset()
next_press_16.keys = []
next_press_16.rt = []
_next_press_16_allKeys = []
# keep track of which components have finished
free_debriefComponents = [free_debrief_text, free_debrief_next_text, next_press_16]
for thisComponent in free_debriefComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "free_debrief" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *free_debrief_text* updates
    if free_debrief_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        free_debrief_text.frameNStart = frameN  # exact frame index
        free_debrief_text.tStart = t  # local t and not account for scr refresh
        free_debrief_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(free_debrief_text, 'tStartRefresh')  # time at next scr refresh
        free_debrief_text.setAutoDraw(True)
    
    # *free_debrief_next_text* updates
    if free_debrief_next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        free_debrief_next_text.frameNStart = frameN  # exact frame index
        free_debrief_next_text.tStart = t  # local t and not account for scr refresh
        free_debrief_next_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(free_debrief_next_text, 'tStartRefresh')  # time at next scr refresh
        free_debrief_next_text.setAutoDraw(True)
    
    # *next_press_16* updates
    waitOnFlip = False
    if next_press_16.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_16.frameNStart = frameN  # exact frame index
        next_press_16.tStart = t  # local t and not account for scr refresh
        next_press_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_16, 'tStartRefresh')  # time at next scr refresh
        next_press_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_16.status == STARTED and not waitOnFlip:
        theseKeys = next_press_16.getKeys(keyList=['return'], waitRelease=False)
        _next_press_16_allKeys.extend(theseKeys)
        if len(_next_press_16_allKeys):
            next_press_16.keys = _next_press_16_allKeys[-1].name  # just the last key pressed
            next_press_16.rt = _next_press_16_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in free_debriefComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "free_debrief" ---
for thisComponent in free_debriefComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "free_debrief" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# --- Prepare to start Routine "training_4_instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
training_4_text.reset()
next_text_13.reset()
next_press_13.keys = []
next_press_13.rt = []
_next_press_13_allKeys = []
# keep track of which components have finished
training_4_instructionsComponents = [training_4_text, next_text_13, next_press_13]
for thisComponent in training_4_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "training_4_instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *training_4_text* updates
    if training_4_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        training_4_text.frameNStart = frameN  # exact frame index
        training_4_text.tStart = t  # local t and not account for scr refresh
        training_4_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(training_4_text, 'tStartRefresh')  # time at next scr refresh
        training_4_text.setAutoDraw(True)
    
    # *next_text_13* updates
    if next_text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_13.frameNStart = frameN  # exact frame index
        next_text_13.tStart = t  # local t and not account for scr refresh
        next_text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_13, 'tStartRefresh')  # time at next scr refresh
        next_text_13.setAutoDraw(True)
    
    # *next_press_13* updates
    waitOnFlip = False
    if next_press_13.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_13.frameNStart = frameN  # exact frame index
        next_press_13.tStart = t  # local t and not account for scr refresh
        next_press_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_13, 'tStartRefresh')  # time at next scr refresh
        next_press_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_13.status == STARTED and not waitOnFlip:
        theseKeys = next_press_13.getKeys(keyList=['return'], waitRelease=False)
        _next_press_13_allKeys.extend(theseKeys)
        if len(_next_press_13_allKeys):
            next_press_13.keys = _next_press_13_allKeys[-1].name  # just the last key pressed
            next_press_13.rt = _next_press_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_4_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "training_4_instructions" ---
for thisComponent in training_4_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "training_4_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# set up handler to look after randomisation of conditions etc
training_4_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition files/conditions_training_4.xlsx'),
    seed=None, name='training_4_trials')
thisExp.addLoop(training_4_trials)  # add the loop to the experiment
thisTraining_4_trial = training_4_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_4_trial.rgb)
if thisTraining_4_trial != None:
    for paramName in thisTraining_4_trial:
        exec('{} = thisTraining_4_trial[paramName]'.format(paramName))

for thisTraining_4_trial in training_4_trials:
    currentLoop = training_4_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_4_trial.rgb)
    if thisTraining_4_trial != None:
        for paramName in thisTraining_4_trial:
            exec('{} = thisTraining_4_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "training_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from t4_clock
    # create some init variables
    objective_time = []
    revolutions = []
    current_action_word = training_4_action_word.pop()
    training_4_trials.addData('action_word', current_action_word)
    delay = random.uniform(1.28, 2.56)
    
    timer = clock.Clock()
    # define trial sound
    t4_sound = sound.Sound(soundpath_t4,
        startTime = 0,
        stopTime = duration_t4 + buffer, 
        loops = 0,
        volume = 1) 
        
    dur_t4 = duration_t4 + buffer # prevents audio overlap    
    
    t4_sound.play() # animate clock and play scenario soundfile
    
    while timer.getTime() <= (dur_t4):
        clock_full()   
        win.flip()
        
    t4_sound.stop()
    
    if current_action_word == 0: # choose action word
        heen.play()
    elif current_action_word == 1:
        weg.play()
    while timer.getTime() >= (dur_t4) and timer.getTime() <= (dur_t4+0.843):
        clock_full()   
        win.flip()
    
    if current_action_word == 0: # stop action word depending on which one it is
        heen.stop()
    elif current_action_word == 1:
        weg.stop()
    
    while timer.getTime() >= (dur_t4+0.843) and timer.getTime() <= (dur_t4+1.043): # animate clock and play beep
        clock_full()   
        win.flip()
     
    beep.play()
    response_t4 = event.getKeys(keyList = keys)
    
    while True:
        response_t4 = event.getKeys(keyList = keys)
        if len(response_t4)>0:
            if response_t4[0] == 'up' and current_action_word == 0: # correct reponse for help action word
                objective_time.append(timer.getTime()-(dur_t4+1.043)) # store the objective timing
                training_4_trials.addData('objective', objective_time)
                training_4_trials.addData('judgement', response_t4) # store M judgement
                training_4_trials.addData('was_incorrect', was_incorrect) # default is False
                break
            elif response_t4[0] == 'up' and current_action_word == 1: # wrong reponse for non-help action word
                objective_time.append(timer.getTime()-(dur_t4+1.043)) 
                training_4_trials.addData('objective', objective_time)
                training_4_trials.addData('judgement', response_t4) 
                was_incorrect = True
                training_4_trials.addData('was_incorrect', was_incorrect) 
                break
            elif response_t4[0] == 'down' and current_action_word == 0: # wrong reponse for help action word
                objective_time.append(timer.getTime()-(dur_t4+1.043)) 
                training_4_trials.addData('objective', objective_time)
                training_4_trials.addData('judgement', response_t4) 
                was_incorrect = True
                training_4_trials.addData('was_incorrect', was_incorrect) 
                break
            elif response_t4[0] == 'down' and current_action_word == 1: # correct reponse for non-help action word
                objective_time.append(timer.getTime()-(dur_t4+1.043)) 
                training_4_trials.addData('objective', objective_time)
                training_4_trials.addData('judgement', response_t4) 
                training_4_trials.addData('was_incorrect', was_incorrect) 
                break
        clock_full()   
        win.flip()
    
    delay_clock = clock.Clock()
    while delay_clock.getTime() <= delay: # see above
        clock_full()   
        win.flip()
    
    continueRoutine = False
    # keep track of which components have finished
    training_4Components = []
    for thisComponent in training_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "training_4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_4" ---
    for thisComponent in training_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "training_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "t4_incorrect" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from t4_inc_code
    if was_incorrect == True:
        incorrect.draw()
        win.flip()
        core.wait(3)
        continueRoutine = False
    # keep track of which components have finished
    t4_incorrectComponents = []
    for thisComponent in t4_incorrectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "t4_incorrect" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in t4_incorrectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "t4_incorrect" ---
    for thisComponent in t4_incorrectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "t4_incorrect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "t4_trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keyResp_3.keys = []
    keyResp_3.rt = []
    _keyResp_3_allKeys = []
    # Run 'Begin Routine' code from t4_2_code
    if was_incorrect == True:
        win.flip()
        core.wait(0.5)
        continueRoutine = False
    #clock_static()
    resp_display = ""
    maxDigits = 2
    
    #key logger defaults
    last_len = 0
    key_list = []
    # draw all required objects
    next_text_2.setAutoDraw(True)
    question.setAutoDraw(True)
    hint_box.setAutoDraw(True)
    clock_circle.setAutoDraw(True)
    center_dot.setAutoDraw(True)
    for labels in clock_labels:
        labels.setAutoDraw(True)
    for ticks_a in ticks_large:
        ticks_a.setAutoDraw(True)
    win.flip()
    t4_border.reset()
    # keep track of which components have finished
    t4_trial_2Components = [t4_2_text, keyResp_3, t4_border]
    for thisComponent in t4_trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "t4_trial_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *t4_2_text* updates
        if t4_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t4_2_text.frameNStart = frameN  # exact frame index
            t4_2_text.tStart = t  # local t and not account for scr refresh
            t4_2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t4_2_text, 'tStartRefresh')  # time at next scr refresh
            t4_2_text.setAutoDraw(True)
        if t4_2_text.status == STARTED:  # only update if drawing
            t4_2_text.setText(resp_display, log=False)
        
        # *keyResp_3* updates
        waitOnFlip = False
        if keyResp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            keyResp_3.frameNStart = frameN  # exact frame index
            keyResp_3.tStart = t  # local t and not account for scr refresh
            keyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResp_3, 'tStartRefresh')  # time at next scr refresh
            keyResp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyResp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyResp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyResp_3.status == STARTED and not waitOnFlip:
            theseKeys = keyResp_3.getKeys(keyList=['return','backspace','0','1','2','3','4','5','6','7','8','9','num_0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9'], waitRelease=False)
            _keyResp_3_allKeys.extend(theseKeys)
            if len(_keyResp_3_allKeys):
                keyResp_3.keys = [key.name for key in _keyResp_3_allKeys]  # storing all keys
                keyResp_3.rt = [key.rt for key in _keyResp_3_allKeys]
        # Run 'Each Frame' code from t4_2_code
        #if a new key has been pressed since last time
        if(len(keyResp_3.keys) > last_len):
            
            #increment the key logger length
            last_len = len(keyResp_3.keys)
            
            #grab the last key added to the keys list
            key_list.append(keyResp_3.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
                
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 1):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            key_list = [keys.replace('num_', '') for keys in key_list]
            resp_display = ''.join(key_list)
        
        # *t4_border* updates
        if t4_border.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t4_border.frameNStart = frameN  # exact frame index
            t4_border.tStart = t  # local t and not account for scr refresh
            t4_border.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t4_border, 'tStartRefresh')  # time at next scr refresh
            t4_border.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in t4_trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "t4_trial_2" ---
    for thisComponent in t4_trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyResp_3.keys in ['', [], None]:  # No response was made
        keyResp_3.keys = None
    training_4_trials.addData('keyResp_3.keys',keyResp_3.keys)
    if keyResp_3.keys != None:  # we had a response
        training_4_trials.addData('keyResp_3.rt', keyResp_3.rt)
    # Run 'End Routine' code from t4_2_code
    training_3_trials.addData('subj_rating', key_list)
    
    # reset some variables and attributes to default for the next trial(s)
    
    was_incorrect = False 
    next_text_2.setAutoDraw(False)
    question.setAutoDraw(False)
    hint_box.setAutoDraw(False)
    clock_circle.setAutoDraw(False)
    center_dot.setAutoDraw(False)
    for labels in clock_labels:
        labels.setAutoDraw(False)
    for ticks_a in ticks_large:
        ticks_a.setAutoDraw(False)
    
    win.flip()
    # the Routine "t4_trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'training_4_trials'

# get names of stimulus parameters
if training_4_trials.trialList in ([], [None], None):
    params = []
else:
    params = training_4_trials.trialList[0].keys()
# save data for this loop
training_4_trials.saveAsExcel(filename + '.xlsx', sheetName='training_4_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "instr_forced" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_forced_text.reset()
next_text_15.reset()
next_press_15.keys = []
next_press_15.rt = []
_next_press_15_allKeys = []
# keep track of which components have finished
instr_forcedComponents = [instr_forced_text, next_text_15, next_press_15]
for thisComponent in instr_forcedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instr_forced" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_forced_text* updates
    if instr_forced_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_forced_text.frameNStart = frameN  # exact frame index
        instr_forced_text.tStart = t  # local t and not account for scr refresh
        instr_forced_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_forced_text, 'tStartRefresh')  # time at next scr refresh
        instr_forced_text.setAutoDraw(True)
    
    # *next_text_15* updates
    if next_text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_15.frameNStart = frameN  # exact frame index
        next_text_15.tStart = t  # local t and not account for scr refresh
        next_text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_15, 'tStartRefresh')  # time at next scr refresh
        next_text_15.setAutoDraw(True)
    
    # *next_press_15* updates
    waitOnFlip = False
    if next_press_15.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_15.frameNStart = frameN  # exact frame index
        next_press_15.tStart = t  # local t and not account for scr refresh
        next_press_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_15, 'tStartRefresh')  # time at next scr refresh
        next_press_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_15.status == STARTED and not waitOnFlip:
        theseKeys = next_press_15.getKeys(keyList=['return'], waitRelease=False)
        _next_press_15_allKeys.extend(theseKeys)
        if len(_next_press_15_allKeys):
            next_press_15.keys = _next_press_15_allKeys[-1].name  # just the last key pressed
            next_press_15.rt = _next_press_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_forcedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instr_forced" ---
for thisComponent in instr_forcedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_forced" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# set up handler to look after randomisation of conditions etc
forced_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition files/conditions_forced.xlsx'),
    seed=None, name='forced_trials')
thisExp.addLoop(forced_trials)  # add the loop to the experiment
thisForced_trial = forced_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisForced_trial.rgb)
if thisForced_trial != None:
    for paramName in thisForced_trial:
        exec('{} = thisForced_trial[paramName]'.format(paramName))

for thisForced_trial in forced_trials:
    currentLoop = forced_trials
    # abbreviate parameter names if possible (e.g. rgb = thisForced_trial.rgb)
    if thisForced_trial != None:
        for paramName in thisForced_trial:
            exec('{} = thisForced_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "forced_trial_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from clock_forced
    # create some init variables
    objective_time = []
    revolutions = []
    current_action_word = forced_action_word.pop()
    forced_trials.addData('action_word', current_action_word)
    delay = random.uniform(1.28, 2.56)
    
    timer = clock.Clock()
    # define trial sound
    forced_sound = sound.Sound(soundpath_forced,
        startTime = 0,
        stopTime = duration_forced + buffer, 
        loops = 0,
        volume = 1) 
        
    dur_forced = duration_forced + buffer # prevents audio overlap    
    
    forced_sound.play() # animate clock and play scenario soundfile
    
    while timer.getTime() <= (dur_forced):
        clock_full()   
        win.flip()
        
    forced_sound.stop()
    
    if current_action_word == 0: # choose action word
        heen.play()
    elif current_action_word == 1:
        weg.play()
    while timer.getTime() >= (dur_forced) and timer.getTime() <= (dur_forced+0.843):
        clock_full()   
        win.flip()
    
    if current_action_word == 0: # stop action word depending on which one it is
        heen.stop()
    elif current_action_word == 1:
        weg.stop()
    
    while timer.getTime() >= (dur_forced+0.843) and timer.getTime() <= (dur_forced+1.043): # animate clock and play beep
        clock_full()   
        win.flip()
     
    beep.play()
    response_forced = event.getKeys(keyList = keys)
    
    while True:
        response_forced = event.getKeys(keyList = keys)
        if len(response_forced)>0:
            if response_forced[0] == 'up' and current_action_word == 0: # correct reponse for help action word
                objective_time.append(timer.getTime()-(dur_forced+1.043)) # store the objective timing
                forced_trials.addData('objective', objective_time)
                forced_trials.addData('judgement', response_forced) # store M judgement
                forced_trials.addData('was_incorrect', was_incorrect) # default is False
                break
            elif response_forced[0] == 'up' and current_action_word == 1: # wrong reponse for non-help action word
                objective_time.append(timer.getTime()-(dur_forced+1.043)) 
                forced_trials.addData('objective', objective_time)
                forced_trials.addData('judgement', response_forced) 
                was_incorrect = True
                forced_trials.addData('was_incorrect', was_incorrect) 
                break
            elif response_forced[0] == 'down' and current_action_word == 0: # wrong reponse for help action word
                objective_time.append(timer.getTime()-(dur_forced+1.043)) 
                forced_trials.addData('objective', objective_time)
                forced_trials.addData('judgement', response_forced) 
                was_incorrect = True
                forced_trials.addData('was_incorrect', was_incorrect) 
                break
            elif response_forced[0] == 'down' and current_action_word == 1: # correct reponse for non-help action word
                objective_time.append(timer.getTime()-(dur_forced+1.043)) 
                forced_trials.addData('objective', objective_time)
                forced_trials.addData('judgement', response_forced) 
                forced_trials.addData('was_incorrect', was_incorrect) 
                break
        clock_full()   
        win.flip()
    
    delay_clock = clock.Clock()
    while delay_clock.getTime() <= delay: # see above
        clock_full()   
        win.flip()
        
    win.flip()
    core.wait(0.5)            
    continueRoutine = False
    # keep track of which components have finished
    forced_trial_1Components = []
    for thisComponent in forced_trial_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "forced_trial_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in forced_trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "forced_trial_1" ---
    for thisComponent in forced_trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "forced_trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "forced_trial_incorrect" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from incorrect_code
    if was_incorrect == True:
        incorrect.draw()
        win.flip()
        core.wait(3)
        continueRoutine = False
    # keep track of which components have finished
    forced_trial_incorrectComponents = []
    for thisComponent in forced_trial_incorrectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "forced_trial_incorrect" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in forced_trial_incorrectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "forced_trial_incorrect" ---
    for thisComponent in forced_trial_incorrectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "forced_trial_incorrect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "forced_trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keyResp_2.keys = []
    keyResp_2.rt = []
    _keyResp_2_allKeys = []
    # Run 'Begin Routine' code from forced_2_code
    if was_incorrect == True:
        continueRoutine = False
    
    #clock_static()
    resp_display = ""
    maxDigits = 2
    
    #key logger defaults
    last_len = 0
    key_list = []
    # draw all required objects
    next_text_2.setAutoDraw(True)
    question.setAutoDraw(True)
    hint_box.setAutoDraw(True)
    clock_circle.setAutoDraw(True)
    center_dot.setAutoDraw(True)
    for labels in clock_labels:
        labels.setAutoDraw(True)
    for ticks_a in ticks_large:
        ticks_a.setAutoDraw(True)
    win.flip()
    forced_2_border.reset()
    # keep track of which components have finished
    forced_trial_2Components = [forced_2_text, keyResp_2, forced_2_border]
    for thisComponent in forced_trial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "forced_trial_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *forced_2_text* updates
        if forced_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            forced_2_text.frameNStart = frameN  # exact frame index
            forced_2_text.tStart = t  # local t and not account for scr refresh
            forced_2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forced_2_text, 'tStartRefresh')  # time at next scr refresh
            forced_2_text.setAutoDraw(True)
        if forced_2_text.status == STARTED:  # only update if drawing
            forced_2_text.setText(resp_display, log=False)
        
        # *keyResp_2* updates
        waitOnFlip = False
        if keyResp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            keyResp_2.frameNStart = frameN  # exact frame index
            keyResp_2.tStart = t  # local t and not account for scr refresh
            keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResp_2, 'tStartRefresh')  # time at next scr refresh
            keyResp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyResp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyResp_2.status == STARTED and not waitOnFlip:
            theseKeys = keyResp_2.getKeys(keyList=['return','backspace','0','1','2','3','4','5','6','7','8','9','num_0','num_1','num_2','num_3','num_4','num_5','num_6','num_7','num_8','num_9'], waitRelease=False)
            _keyResp_2_allKeys.extend(theseKeys)
            if len(_keyResp_2_allKeys):
                keyResp_2.keys = [key.name for key in _keyResp_2_allKeys]  # storing all keys
                keyResp_2.rt = [key.rt for key in _keyResp_2_allKeys]
        # Run 'Each Frame' code from forced_2_code
        #if a new key has been pressed since last time
        if(len(keyResp_2.keys) > last_len):
            
            #increment the key logger length
            last_len = len(keyResp_2.keys)
            
            #grab the last key added to the keys list
            key_list.append(keyResp_2.keys.pop())
        
            #check for backspace
            if("backspace" in key_list):
                key_list.remove("backspace")
        
                #if we have at least 1 character, remove it
                if(len(key_list) > 0):
                    key_list.pop()
                
            #if enter is pressed then...
            elif("return" in key_list):
                #remove the enter key
                key_list.pop()
        
                #and end the trial if we have at least 2 digits
                if(len(key_list) >= 1):
                    continueRoutine = False
        
        
            #now loop through and remove any extra characters that may exist
            while(len(key_list) > maxDigits):
                key_list.pop()
                
            #create a variable to display
            key_list = [keys.replace('num_', '') for keys in key_list]
            resp_display = ''.join(key_list)
        
        # *forced_2_border* updates
        if forced_2_border.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            forced_2_border.frameNStart = frameN  # exact frame index
            forced_2_border.tStart = t  # local t and not account for scr refresh
            forced_2_border.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forced_2_border, 'tStartRefresh')  # time at next scr refresh
            forced_2_border.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in forced_trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "forced_trial_2" ---
    for thisComponent in forced_trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyResp_2.keys in ['', [], None]:  # No response was made
        keyResp_2.keys = None
    forced_trials.addData('keyResp_2.keys',keyResp_2.keys)
    if keyResp_2.keys != None:  # we had a response
        forced_trials.addData('keyResp_2.rt', keyResp_2.rt)
    # Run 'End Routine' code from forced_2_code
    training_3_trials.addData('subj_rating', key_list)
    
    # reset some variables and attributes to default for the next trial(s)
    was_incorrect = False
    next_text_2.setAutoDraw(False)
    question.setAutoDraw(False)
    hint_box.setAutoDraw(False)
    clock_circle.setAutoDraw(False)
    center_dot.setAutoDraw(False)
    for labels in clock_labels:
        labels.setAutoDraw(False)
    for ticks_a in ticks_large:
        ticks_a.setAutoDraw(False)
    
    win.flip()
    core.wait(0.1)
    win.flip()
    
    # the Routine "forced_trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'forced_trials'

# get names of stimulus parameters
if forced_trials.trialList in ([], [None], None):
    params = []
else:
    params = forced_trials.trialList[0].keys()
# save data for this loop
forced_trials.saveAsExcel(filename + '.xlsx', sheetName='forced_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "check_instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instr_forced_text_2.reset()
next_text_18.reset()
next_press_19.keys = []
next_press_19.rt = []
_next_press_19_allKeys = []
# keep track of which components have finished
check_instructionComponents = [instr_forced_text_2, next_text_18, next_press_19]
for thisComponent in check_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "check_instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_forced_text_2* updates
    if instr_forced_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_forced_text_2.frameNStart = frameN  # exact frame index
        instr_forced_text_2.tStart = t  # local t and not account for scr refresh
        instr_forced_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_forced_text_2, 'tStartRefresh')  # time at next scr refresh
        instr_forced_text_2.setAutoDraw(True)
    
    # *next_text_18* updates
    if next_text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_text_18.frameNStart = frameN  # exact frame index
        next_text_18.tStart = t  # local t and not account for scr refresh
        next_text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_text_18, 'tStartRefresh')  # time at next scr refresh
        next_text_18.setAutoDraw(True)
    
    # *next_press_19* updates
    waitOnFlip = False
    if next_press_19.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        next_press_19.frameNStart = frameN  # exact frame index
        next_press_19.tStart = t  # local t and not account for scr refresh
        next_press_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_press_19, 'tStartRefresh')  # time at next scr refresh
        next_press_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next_press_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next_press_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_press_19.status == STARTED and not waitOnFlip:
        theseKeys = next_press_19.getKeys(keyList=['return'], waitRelease=False)
        _next_press_19_allKeys.extend(theseKeys)
        if len(_next_press_19_allKeys):
            next_press_19.keys = _next_press_19_allKeys[-1].name  # just the last key pressed
            next_press_19.rt = _next_press_19_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in check_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "check_instruction" ---
for thisComponent in check_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "check_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "w" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
wComponents = [text]
for thisComponent in wComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "w" ---
while continueRoutine and routineTimer.getTime() < 0.3:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "w" ---
for thisComponent in wComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.300000)

# set up handler to look after randomisation of conditions etc
likerttest = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition files/conditions_likert_check.xlsx'),
    seed=None, name='likerttest')
thisExp.addLoop(likerttest)  # add the loop to the experiment
thisLikerttest = likerttest.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLikerttest.rgb)
if thisLikerttest != None:
    for paramName in thisLikerttest:
        exec('{} = thisLikerttest[paramName]'.format(paramName))

for thisLikerttest in likerttest:
    currentLoop = likerttest
    # abbreviate parameter names if possible (e.g. rgb = thisLikerttest.rgb)
    if thisLikerttest != None:
        for paramName in thisLikerttest:
            exec('{} = thisLikerttest[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "check_likert" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from check_likert_code
    win.mouseVisible = True 
    while continueRoutine == True: # main loop
        check_1.draw() # draw all items, likert scales, and the next button text
        check_2.draw()
        check_3.draw()
        check_text.draw()
        check_text.setText(scenario_text)
        next_text_2.draw()
        win.flip()
        
        if event.getKeys(keyList=['escape']): # quit experiment
            core.quit()
        if event.getKeys(keyList=['return']):
            likerttest.addData('danger', check_1.getRating()) # crucially, add likert data once enter is pressed
            likerttest.addData('relevance', check_2.getRating())
            likerttest.addData('realism', check_3.getRating())
            check_1.reset() 
            check_2.reset()
            check_3.reset()
            check_1.markerStart = 12 # resets marker to a value beyond the scale. This means in the next trial it is not visible before a value has been entered
            check_2.markerStart = 12
            check_3.markerStart = 12
            continueRoutine = False # go to next routine
     
    
    
    
    
    # keep track of which components have finished
    check_likertComponents = []
    for thisComponent in check_likertComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "check_likert" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from check_likert_code
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in check_likertComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "check_likert" ---
    for thisComponent in check_likertComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from check_likert_code
    win.mouseVisible = False
    # the Routine "check_likert" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "w" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wComponents = [text]
    for thisComponent in wComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "w" ---
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "w" ---
    for thisComponent in wComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'likerttest'

# get names of stimulus parameters
if likerttest.trialList in ([], [None], None):
    params = []
else:
    params = likerttest.trialList[0].keys()
# save data for this loop
likerttest.saveAsExcel(filename + '.xlsx', sheetName='likerttest',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "debriefing" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
debriefing_text.reset()
# keep track of which components have finished
debriefingComponents = [debriefing_text]
for thisComponent in debriefingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "debriefing" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debriefing_text* updates
    if debriefing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debriefing_text.frameNStart = frameN  # exact frame index
        debriefing_text.tStart = t  # local t and not account for scr refresh
        debriefing_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefing_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'debriefing_text.started')
        debriefing_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debriefingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "debriefing" ---
for thisComponent in debriefingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "debriefing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='comma')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
