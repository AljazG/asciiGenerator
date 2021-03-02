## The Grubko ascii img generator

A dank ass python script designed to convert your legal anime lolli photos into more legal and clean ascii grills

### Requirements

* Python 3.6 or higher
* The pillow package https://pillow.readthedocs.io/en/stable/
* Hacking gloves

### Usage

1. make sure python and pip are installed
2. run `pip install pillow`
3. put desired photos in ./photos/
4. run script: `python generateAscii.py`
5. input the desired width of your ascii output (height will be scaled appropriately)
6. input a number corresponding to desired ascii scheme (default is 1): 
* 1 -> 11 ascii characters
* 2 -> 70 ascii characters
7. input if you would like to preserve the aspect ratio (default is 1):
* 1 -> doesn't preserve aspect ratio but it is more detailed
* 2 -> preserves the aspect ratio on the account of some detail loss
8. celebrate as your transformed ascii anime girls are waiting for you in "./generated_ascii/"