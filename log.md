# 100 Days Of Code - Log

### Day 1: August 10, 2018

**Today's Progress**: Extracted sentences from an existing coorpus of Hindi text and built my own. Also extracted the number of senses of a word from the Hindi WordNet

**Thoughts:** Happy to have used Spyder for the first time instead of Jupyter Notebook for this particular task as it was getting stuck for some reason.
A fair amount of time was spent in fixing errors and understanding how to call a function after a delay.

### Day 2: August 11, 2018

**Today's Progress**: Extracted the sense count of all the words in the files in a given directory and stored to a collection in Mongo DB.

**Thoughts:** The Hindi WordNet jar writes the senses to a file and the script reads from that file after 15 seconds. This delay, along with the size of the corpus is leading to an issue in the normal working of the system. An API that returns information about the word would have been useful. May have to modify the source code of HWN!

### Day 3: August 12, 2018

**Today's Progress**: Created a separate file for database functions. Stored properties of words that are encountered for the first time in the text, in the collection.

**Thoughts:** May have to modify the structure of the collection to facilitate flexible search.

### Day 4: August 13, 2018

**Today's Progress**: Tried to call a Java method from Python using Py4J.

**Thoughts:** Unable to call a user-defined function. Have to fix this before moving on to collections. Very important as this is the base of this application.

### Day 4: August 13, 2018

**Today's Progress**: Finally fixed the code. Did not need Py4J. Compiled the files and used the class files in Python using subprocess. Had to set the current working directory in the function.

**Thoughts:** Now I can go to sleep!

### Day 5: August 14, 2018

**Today's Progress**: Unable to find the stem of a word. Comments and files missing from the official HWN API.

**Thoughts:** Tried to find many workarounds; none worked. Will spend one more day and this and move on to the other tasks.

### Day 6: August 16, 2018

**Today's Progress**: Wrote debugging statements to find the issue. To be continued tomorrow...

**Thoughts:** It gets frustrating when we rely a lot on a third party tool, and it doesn't behave as expected.

### Day 7: August 17, 2018

**Today's Progress**: Finally found the issue. The word was not being passed in the correct format.

**Thoughts:** Spent a lot of time to find out that the program was behaving unexpectedly because of the way I was passing the word!

### Day 8: August 18, 2018

**Today's Progress**: Retreived the roots of a word.

**Thoughts:** One thing resolved, found another one. But that can be resolved as well. Will keep trying.

### Day 9: August 19, 2018

**Today's Progress**: Successfully passed the utf-8 string as an argument to the python file.

**Thoughts:** Unable to decode the byte representation back to the original string.

### Day 10: August 20, 2018

**Today's Progress**: Decided not to use jython after many experiments.

**Thoughts:** Wonder how long it would take to call a java method from py4j!

### Day 11: August 21, 2018

**Today's Progress**: Found the required documentation. Used py4j successfully to call a custom Java class method. Decided to use py4j to call other methods from other classes as well.

**Thoughts:** Many silly thoughtless mistakes led to a lot of bug resolving time but it was worth it. py4j turned out to be a saviour!

### Day 12: August 22, 2018

**Today's Progress**: Added sentences to the database. Standardized the format of the return values of all the functions.

**Thoughts:** Content with the fact that documentation and conventions are being followed as much as possible.

### Day 13: August 23, 2018

**Today's Progress**: Tried to POS tag a file, but got many errors in the existing code that was downloaded.

**Thoughts:** Hoping to get a working tagger from TDIL asap. Till then, will continue with the rest of the code.

### Day 14: August 24, 2018

**Today's Progress**: Updated values of existing words, found a bug - redundant documents are getting inserted with the updated values.

**Thoughts:** Will fix the bug tomorrow. It may have something to do with the ID of the document.
 
### Day 15: August 25, 2018

**Today's Progress**: Fixed the bug. It was an error in the program.

**Thoughts:** Glad to have found it without losing too much time. Next step, splitting words and retrieving their properties.
 
### Day 16: August 26, 2018

**Today's Progress**: Retrieved the number of characters, consonants, vowels and consonant conjuncts. Fixed a bug.

**Thoughts:** In a hurry, still managed to complete.

### Day 17: August 27, 2018

**Today's Progress**: Counting of syllables is in progress.

**Thoughts:** Need to consider many rules.
 
### Day 18: August 28, 2018

**Today's Progress**: Counted syllables.

**Thoughts:** Need to test thoroughly. Laborious process.

### Day 19: August 29, 2018

**Today's Progress**: Tested the syllables code. Modified the HWN Java file to count the number of hypernyms, hyponyms etc.

**Thoughts:** Will test this tomorrow.

### Day 20: August 30, 2018

**Today's Progress**: Fetched hypernyms, bugs detected in the Java code.

**Thoughts:** Can be fixed, no worries!

### Day 21: September 2, 2018

**Today's Progress**: Bug detected when counting properties of words with multiple senses.

**Thoughts:** Can be fixed. Took a break but continuing the challenge.

### Day 22: September 5, 2018

**Today's Progress**: Counted hypernyms, hyponyms and synonyms. Bug found while storing in the database.

**Thoughts:** Resuming work after a short break. Dedicating all the commits to a beloved student, Lalit Chandwani, who passed away on Monday. He was a passionate coder, teacher and learner.

### Day 23: September 6, 2018

**Today's Progress**: Fixed the bug, retrieved gloss.

**Thoughts:** Work is slow.

### Day 24: September 7, 2018

**Today's Progress**: Tried to use the morph analyzer from TDIL. Error found due to encoding format on Windows.

**Thoughts:** Will try to use live linux.

### Day 25: September 11, 2018

**Today's Progress**: Used CSS and created dropdown menus; had to use trial-and-error many times to align it with the existing elements on the page.

**Thoughts:** Not uploading this code on the GitHub page as it's not my personal project.

**Link to work:** NA

### Day 26: September 12, 2018

**Today's Progress**: Used geopy to read a geojson file.

**Thoughts:** Next step, decide which words to search on social media, and perform the search.

**Link to work:** https://github.com/gayatrivenugopal/GeoPy-Experiments

### Day 27: September 16, 2018

**Today's Progress**: Regression and classification programs using Python.

**Thoughts:** Not uploading this code on the GitHub page as it's part of a MOOC.

**Link to work:** NA

### Day 28: September 22, 2018

**Today's Progress**: Fetched the characteristics of the synonyms of all the synsets of a word in Hindi.

**Thoughts:** Glad that it did not take too much time.

### Day 29: September 24, 2018

**Today's Progress**: Used fasttext to classify imdb reviews.

**Thoughts:** Finally, something that I could understand.

### Day 30: September 25, 2018

**Today's Progress**: Cleaned a CSV file by removing the first column. Used word2vec.

**Thoughts:** Thankfully, it wasn't too difficult to understand.

**Link to work:** https://github.com/gayatrivenugopal/NLP