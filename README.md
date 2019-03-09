# BasicAutocomplete
A basic script to do autocomplete based on a text file

# The Data
I was given a dataset of search history off which to base my autocomplete script. It was in the form of a text file, with each line being a search query.

# Creating Tries
I created two tries, one for letters and one for words, in which following a path on the trie would create a search query. Nodes in the trie also contained a count for how many times a child word was used after its parent words. First, I split my data into nested lists of words and characters. I created a function to add a phrase (in the form of a list of words or letters) to the trie by adding a given word or character to a given level of the trie, then calling the function recursivley on the next word or character and deeper branch of the trie. The tries were made by iterating over each word or phrase in the nested list and calling the function on that phrase.

# Autocompletion
In order to create autocompletion, I created a function to predict the next word or character based off given words or characters. It would follow the phrase down the trie until it reached the last word or character, then return the five children of that node with the highest count. If no matches were found, it would return "none found."

# Interface
After creating functions and tries to autocomplete, I had to create an interface. The interface would first ask if the user would like to use word or character prediction mode, which would use the word trie or character trie, respectivley. The user would then input a phrase, and the autocomplete function would be called to predict the next character or word. The interface would end when the user typed "exit()." Otherwise, it would repeat.

Made while working with Hello World Studio
