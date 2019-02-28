
F = open('my_history.txt', 'r')
contents = F.read()
F.close()

def addphrase(phrase, trie):
	thing = trie['child']
	for x in range(len(phrase)):
		match = False
		for item in thing:
			if 'val' in item:
				if item['val'] == phrase[x]:
					item['count'] += 1
					location = thing.index(item)
					match = True
		if match:
			thing = thing[location]['child']
		else:
			dicttemp = {
			"val":phrase[x],
			'count':1,
			'child':[]
			}
			thing.append(dicttemp)
			thing = thing[len(thing)-1]['child']
	return trie

def autocomplete(phrase, trie):
 	if len(phrase) == 0:
 		resultlist = []
 		newlist = []	
 		for item in trie['child']:
 			resultlist.append([item['val'], item['count']])
 		ordered = sorted(resultlist, key = lambda x: int(x[1]))
 		ordered.reverse()
 		if len(ordered) < 5:
 			amount = len(ordered)
 		else:
 			amount = 5
 		for x in range(0,amount):
 			newlist.append(ordered[x][0])
 		return newlist
 	else:
 		checker = True
 		for item in trie['child']:
 			if 'val' in item:
	 			if item['val'] == phrase[0]:
	 				checker = False
	 				location = trie['child'].index(item)
	 	if checker:
	 		return "none found"
 		return autocomplete(phrase[1:], trie['child'][location])

def wordtrie(contents):
	trie = {
		'val' : "^",
		'count' :1,
		'child' :[]
	}
	contents = contents.split("\n")
	for x in range(len(contents)):
		contents[x] = contents[x].split(" ")
	for item in contents:
		trie = addphrase(item, trie)
	return trie

def lettertrie(contents):
	trie = {
		'val' : "^",
		'count' :1,
		'child' :[]
	}
	newwords = []
	contents = contents.split("\n")
	for x in range(len(contents)):
		contents[x] = contents[x].split(" ")
	for item in contents:
		for item2 in item:
			newwords.append(item2)
	for x in range(len(newwords)):
		newwords[x] = list(newwords[x])
	for item in newwords:
		trie = addphrase(item, trie)
	return trie

def interface():
	letters = lettertrie(contents)
	words = wordtrie(contents)
	x = True
	check2 = False
	while True:
		response = input("Choose Character or Word mode: Word mode predicts words, whereas Character mode predicts letters(so it takes letters for input and not words). Type W for word mode and C for Character mode ")
		if response == "C":
			actualtrie = letters
			x = True
		if response == "W":
			actualtrie  = words
			x = True
		else:
			print ("You can only type C or W")
			x = False
		while True:
			user = input("type to predict, exit() to exit, or change modes to change modes" + "\n")
			if user == "exit()":
				check2 = True
				break
			if user == "change modes":
				break
			if response == "C":
				user = list(user)
				print (autocomplete(user, actualtrie))
			if response == "W":
				user = user.split(" ")
				print (autocomplete(user, actualtrie))
		if check2:
			break

interface()


