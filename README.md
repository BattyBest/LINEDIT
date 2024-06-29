# LINEDIT
Vector Image Manipulation Program for the TI 84+ CE Graphical Calculator

# What's included
- LINEDIT.8xp

A program in TI-Basic that lets you draw
- LINEDIT Proccesor

A program in Python that turns outputs of LINEDIT.8xp into other formats

# Installation

1. Transfer LINEDIT.8xp & GDSTAND.8xp to your calculator using TI Connect CE or TiLP or any other program capable of transmitting .8xp files to the calculator.
2. Run GDSTAND in your calculator. Re-run this program anytime GDB9 is changed.
3. Install Python if not already installed.
4. Place the LINEDIT Proccesor anywhere convenient on your computer.
5. Done.

# Usage - LINEDIT
LINEDIT uses a data format that is now coined as the LINEDIT format. It involves a bunch of ordered pairs collapsed in a list, with an ordered pair with an x value of -1 representing a new stroke. Each stroke contains its ordered pairs from the previous ordered pair with -1 to the next. In each -1 ordered pair, the y value represents the color of the new stroke. To draw each stroke, a line segment from the current ordered pair to the next ordered pair is drawn unless the current or next ordered pair has a a value of -1, and then the next ordered pair is iterated to.

The following keys have the following functions:
- Arrow Keys - Move cursor.
- Numpad Keys - Set cursor speed to the respective number on the key, except 0, which does nothing.
- \[+/-\] - Doubles and halves the cursor speed respectively.
- \[ALPHA\] - Teleport cursor to a location
- \[2ND\] - Add a new ordered pair at cursors current location.
- \[Del\] - Remove newest ordered pair.
- \[Y=\] - Refresh screen.
- \[Window\] - Start a new stroke.
- \[Zoom\] - Change color of current stroke.
- \[Trace\] - Toggle whether to display cursor X,Y coordinates in the bottom-left of the screen.
- \[Graph\] - Zoom in or out and/or change the resolution of the image.
- \[Vars\] - Display the ordered points, if cursor is at an ordered point or points, then get the option to edit the point going from oldest to newest.
- \[Enter\] - Export current image. When clicked, the program will error, intentionally. To get the export, click on the goto option, then delete the junk surrounding the list definition.
- \[Stat\] - Display current list of ordered pairs. Will overflow off the screen if the list is too big.

Note: In some of the functions, freeform text can be inputted. An invalid input will cause the program to crash. To recover your work if the program crashes, set the variable Z to 3 times pi before re-launching the program. This will import the previous list over. It will not import the zoom.

# Usage - LINEDIT Proccesor
The LINEDIT Proccesor allows you to convert the list outputted from exporting to something else. It can convert to Line( function format, or to a python List of Tuples. It can also output the function needed to display images from LINEDIT format. The outputs are highly customizable in the settings section.

To use it, simply launch the .py file inside the folder and follow the instructions.
