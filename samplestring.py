

#sample string
sample_string="hello, world !"

#capitalize()
capitalize_string=sample_string . capitalize()
print ("capitalize():",capitalize_string)

#casefold()
casefolded_string=sample_string . casefold()
print ("casefold():",casefolded_string)

#center()
centered_string=sample_string . center(30,'*')
print ("center():",centered_string)

#count()
count_occurances=sample_string . count('1')
print ("count():",count_occurances)

#endswith()
ends_with=sample_string . endswith("!")
print ("endswith():",ends_with)

#encode()
encoded_string=sample_string . encode(encoding='utf-8')
print ("encode():",encoded_string)

#expandedtabs()
tab_expanded_string="hello\t world\t! ".expandtabs(4)
print ("expandedtabs():",tab_expanded_string)

#find()
position=sample_string . find ("llo")
print ("find():",position)

#format_map()
school={'name':'santhosh','age':17}
formated_map_string="i am (name),and : (age)" . format_map(school)
print ("format_map():",formated_map_string)

#index()
index_position=sample_string . index ('llo')
print ("index():",index_position)

sample_string="hello, world ! "

#isalnum()
is_alphanumeric=sample_string . isalnum()
print ("isalnum():",is_alphanumeric)

#isalpha()
is_alpha=sample_string . isalpha()
print ("isalpha():",is_alpha)

#isascii()
is_ascii=sample_string . isascii()
print ("isascii():",is_ascii)

#isdecimal()
is_decimal=sample_string . isdecimal()
print ("isdecimal():",is_decimal)

#isdigit()
is_digit=sample_string . isdigit()
print ("isdigit():",is_digit)

#isidentifier()
is_identifier=sample_string . isidentifier()
print ("isidentifier():",is_identifier)

#islower()
is_lower=sample_string . islower()
print ("islower():",is_lower)

#isnumeric()
is_numeric=sample_string . isnumeric()
print ("isnumeric():",is_numeric)

#isprintable()
is_printable=sample_string . isprintable()
print ("isprintable():",is_printable)

#isspace()
is_space=sample_string . isspace()
print ("isspace():",is_space)

#istitle()
is_title=sample_string . istitle()
print ("istitle():",is_title)

#isupper()
is_upper=sample_string . isupper()
print ("isupper():",is_upper)

#ljust()
left_justified_string=sample_string . ljust(25,'#')
print ("ljust():",left_justified_string)

#rjust
right_justified_string=sample_string . rjust(30,'!')
print ("rjust():",right_justified_string)

#join()
fruits=['apple','orange','papaya']
joined_string=",".join(fruits)
print("join():",joined_string)

#maketrans()
translate=sample_string . maketrans ("l" , "e")
translate_string=sample_string . translate (translate)
print ("translate():",translate_string)

#splitlines()
multiline_string="hello\n world\n ! "
print ("splitline():",multiline_string)

#partition()
partitioned_string=sample_string . partition (' . ')
print ("partition():",partitioned_string)

#lstrip()
trimmed_left_string="hello, world ! " . lstrip()
print ("lstrip():", trimmed_left_string)





