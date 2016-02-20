# exercise 8: printing, printing
formatter = "%r %r %r %r" 		#%r give the raw programmer version of variable
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
#print formatter % (
	#"I had this thing.",
	#"That you could type up right.",
	#"But it didn's sing.",
	#"So I said goodnight."
#) 

# Use single quote
print formatter % (
	'I had this thing.',
	'That you could type up right.',
	'But it didn't sing.',
	'So I said goodnight.'
) 
