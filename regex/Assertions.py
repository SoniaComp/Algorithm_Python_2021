Regex_Pattern = r'o(?=oo)'

Regex_Pattern = r'(.)(?!\1)'

Regex_Pattern = r'(?<=[13579])[0-9]'

Regex_Pattern = r'(?<![aeiouAEIOU]).'
# . 메타문자는 \n을 제외한 모든 문자와 매치된다.
# ※ 만약 앞에서 살펴본 문자 클래스([]) 내에 Dot(.) 메타 문자가 사용된다면 이것은 "모든 문자"라는 의미가 아닌 문자 . 그대로를 의미한다. 혼동하지 않도록 주의하자.