ascii('ஐ')
"'\\u0b90'"

# chr() oftern defined with HEX entries.
chr(0x06a4)
'ڤ'
# chr() has a complimentary function ord()
chr(2960)
'ஐ'

# ord() - pass a single character, will return ASCII or unicode point for that.
ord('ஐ')
2960


#============= other type conversion functions =========
type()
int()
bin()
oct()
hex()
float()
complex()
str()
bool()