# Pygen
A silly Markov-chain text generator written in Python
## Installation
Markovify:
`pip install markovify`  
NLTK: `sudo pip install -U nltk`, uncomment the line `nltk.download(all)` on first run
## Configuration & Usage
Edit `config.ini` to change the output settings, enable Part of Speech (PoS) tagging, and change the corpus input.

###### Usage   
`python pygen.py`  
or   
`chmod +x pygen.py` to make it executable and then run with `./pygen.py`
## Example Outputs
##### Input: bible.txt
14:19 And the maid is in thee.  
49:1 Listen, O isles, unto me; and I will set thee over all the children of the LORD said unto him, Say on.  
8:30 As he saith unto him, Dost thou know that I drink the water.
##### Input: sherlock.txt
Two hours passed slowly away, and I volunteered to supply them.  
He denied strenuously having ever seen so thin a man.