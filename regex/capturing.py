Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'	# Do not delete 'r'.

Regex_Pattern = r'(ok){3}'	# Do not delete 'r'.

Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
