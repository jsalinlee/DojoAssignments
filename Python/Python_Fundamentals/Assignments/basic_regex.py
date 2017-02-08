import re
def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
 matches = []
 for word in words:
 	if re.search(regex,word):
 		matches.append(word)
 return matches
v = get_matching_words(r"v");
print v
double_s = get_matching_words(r"ss")
print double_s
end_e = get_matching_words(r"e\Z")
print end_e
b_char_b = get_matching_words(r"b.b")
print b_char_b
b_one_b = get_matching_words(r"b+.b")
print b_one_b
b_any_b = get_matching_words(r"b.*b")
print b_any_b
vowel = get_matching_words(r"a.*e.*i.*o.*u")
print vowel
reg_exp = get_matching_words(r"^[regular expression]*$")
print reg_exp
double = get_matching_words(r"([A-Za-z])\1")
print double
