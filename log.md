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
 
**Link to work:** [Text Processing Code](https://github.com/gayatrivenugopal/NLP/)