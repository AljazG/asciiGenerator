## The Grubko ascii image generator

A simple python script written to convert images into ascii art.

### Requirements

* Python 3.6 or higher
* The pillow package https://pillow.readthedocs.io/en/stable/
* Hacking gloves

### Usage

1. Make sure python and pip are installed
2. Run `pip install pillow`
3. Put desired photos in ./photos/
4. Run script: `python generateAscii.py`
5. Input the desired width of your ascii output (height will be scaled appropriately)
6. Input a number corresponding to desired ascii scheme (default is 1): 
* 1 -> 11 ascii characters
* 2 -> 70 ascii characters
7. Input if you would like to preserve the aspect ratio (default is 1):
* 1 -> doesn't preserve aspect ratio but it is more detailed
* 2 -> preserves the aspect ratio on the account of some detail loss
1. Celebrate as your ascii art awaits for you in "./generated_ascii/" ;)