# list of escape sequences in python
# \\	Backslash ()
# \'	Single quote (')
# \"	Double quote (")
# \a	ASCII Bell (BEL)
# \b	ASCII Backspace (BS)
# \f	ASCII Formfeed (FF)
# \n	ASCII Linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r ASCII	Carriage Return (CR)
# \t ASCII	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v	ASCII Vertical Tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

# Here is the example
while True:
	for i in ["/","-","|" "\\","|"]:
		print "%s\r" % i,

# What's happening...?


