import argparse
import pickle
from re import A
import warnings
warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser()    # step 1

# step 2
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument('-f', '--file', help = 'pass data in form of a file')   
group.add_argument('-l', '--line', help = 'pass data in form of a string in the terminal')   
args = parser.parse_args()     # step 3

with open('naive_classifier.bin', 'rb') as model_in:
    loaded_model = pickle.load(model_in)

if args.file:
    with open(args.file, 'r') as lyrics_file:
        lyrics = [lyrics_file.read()]

if args.line:
    lyrics = [args.line]

print(loaded_model.predict_proba(lyrics))