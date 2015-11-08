#!/usr/bin/env python
# Pygen: Python Markov Text Generator
# Use input corpus text to generate output text (see configuration file for options)
import markovify
import nltk
import re
import sys
import time
import ConfigParser

# Get configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

path = config.get('DEFAULT', 'corpus_path')
numLines = config.getint('DEFAULT', 'number_of_lines_to_generate')
posFlag = config.getboolean('DEFAULT', 'use_PoS')
charLim = config.getint('DEFAULT', 'character_limit')
useCharLim = config.getboolean('DEFAULT', 'obey_character_limit')

# Extended class that uses Part-of-Speech tagging for (allegedly) more coherent sentences
# WARNING: Slow runtime!
###################################################################
class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
###################################################################
# If first time running, uncomment this:
# nltk.download('all')


# Get raw text as string.
with open(path) as f:
    text = f.read()
o = open("output.txt", "w+")

# Build the model based on arguments
start = time.time()

if posFlag == True:
	text_model = POSifiedText(text)
else:
	text_model = markovify.Text(text)

# Log
end = time.time()
elapsed = end - start
runtime = "============================\nMARKOVIFIED IN " + str(elapsed)[:5] + " SECONDS\nCORPUS: "+path+"\n============================"
print runtime
o.write(runtime)
o.write("\n")


if useCharLim == False:
    # Print five randomly-generated sentences
    for i in range(5):
        output = text_model.make_sentence()
        print output
        o.write(output + " ")

else:
    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(numLines):
        output = text_model.make_short_sentence(charLim)
        print output
        o.write(output + " ")
o.close()
f.close()


