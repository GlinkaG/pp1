import re
string = "To be, or not to be, that is the question"
ilosc = re.findall("[aeyiou]", string)

print(len(ilosc))