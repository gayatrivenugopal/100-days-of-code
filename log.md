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


**Link to work:** [Text Processing Code](https://github.com/gayatrivenugopal/NLP/)