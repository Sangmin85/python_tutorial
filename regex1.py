import re

data = """
park 800905-1049118 800905-1049118 800905-1049118
 kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(' '):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + '-' + '*******'
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

s = "1 2 3   4 5"
s.split(' ')

data = """
park 800905-1049118 800905-1049118 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

################################################

"""
 meta character: . ^ $ * + ? { } [ ] ( ) \ |
"""

"""
 ####################################################################
 #### 문자 클래스(character class)
 ####################################################################

 [] : 문자 클래스(character class), '[ 과 ] 사이의 매치'
 [abc] : 'a, b, c 중 한 개의 문자와 매치'
 ex) 패턴 [abc] 매치
    "a" : 'a'를 포함하여 매치
    "before" : 'b'를 포함하여 매치
    "dude" : 매치되지 않음

 ## '-'
 [a-c] : [abc] 와 동일
 [0-5] : [012345] 와 동일
 ex) [a-zA-Z] : 알파벳 모두
     [0-9] : 숫자 모두

 ## '^'
 [] 내에 ^ 가 있을 경우 : 반대(not)의 의미
 ex) [^0-9] : 숫자가 아닌 문자와 매치

 ## 자주 사용하는 문자 클래스([0-9], [a-zA-Z] 등)는 별도의 표기법을 사용가능
    - \d : 숫자와 매치, [0-9]과 동일
    - \D : 숫자가 아닌 것과 매치, [^0-9]과 동일
    - \s : whitespace 문자와 매치, [ \t\n\r\f\v]와 동일
    - \S : whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일
    - \w : 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9]와 동일
    - \W : 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9]와 동일

 ####################################################################
 #### Dot(.)
 ####################################################################

 '.' : 줄바꿈 문자 '\n'를 제외한 모든 문자와 매치됨을 의미
    (re.DOTALL이라는 옵션을 주면 \n 문자와도 매치)

 ex) a.b => "a + 모든문자 + b" (a와 b라는 문자 사이에 어떤 문자가 들어가도 모두 매치)
        - "aab" : 정규식과 매치
        - "a0b" : 정규식과 매치
        - "abc" : 매치 실패
"""
pat = re.compile("a.b")
print(pat.match("aab"))
print(pat.match("a0b"))
print(pat.match("abc"))
"""
 '[.]' : 문자'.' 그대로를 의미
        (re.DOTALL이라는 옵션을 주면 \n 문자와도 매치)

 ex) a[.]b : "a + Dot(.)문자 + b"
        - "a0b" : 매치 실패
"""
pat = re.compile("a[.]b")
print(pat.match("aab"))
print(pat.match("a.b"))
print(pat.match("a.c"))
"""
 ####################################################################
 #### 반복(*)
 ####################################################################
 '*' : '*' 바로 앞의 문자를 0부터 무한대로 반복할 수 있다는 의미

 ex) ca*t : "ct"    => 매치
            "cat"   => 매치
            "caaat" => 매치
"""
pat = re.compile("ca*t")
print(pat.match("ct"))
print(pat.match("cat"))
print(pat.match("caaat"))
"""
 ####################################################################
 #### 반복(+)
 ####################################################################
 '+' : '+' 바로 앞의 문자를 1개부터 무한대로 반복할 수 있다는 의미

 ex) ca+t : "ct"    => 매치 실패
            "cat"   => 매치
            "caaat" => 매치
"""
pat = re.compile("ca+t")
print(pat.match("ct"))
print(pat.match("cat"))
print(pat.match("caaat"))
"""
 ####################################################################
 #### 반복({m,n})
 ####################################################################
 {} : 반복 횟수를 고정
 {m, n} : 바로 앞 문자의 반복 횟수가 m 부터 n 까지 매치

 ex) {3}  : 반복 횟수가 3
     {3,} : 반복 횟수가 3번 이상
     {,3} : 반복 횟수가 0번부터 3번까지
     {1,} : + 와 동일
     {0,} : * 와 동일

     ca{2}t : "cat"   => 매치 실패
              "caat"  => 매치
              "caaat" => 매치 실패
              "cabat" => 매치 실패

     ca{2,5}t : "cat"   => 매치 실패
                "caat"  => 매치
                "caaat" => 매치
                "cabat" => 매치 실패
"""
pat = re.compile("ca{2}t")
print(pat.match("cat"))
print(pat.match("caat"))
print(pat.match("caaat"))
print(pat.match("cabat"))

pat = re.compile("ca{2,5}t")
print(pat.match("cat"))
print(pat.match("caat"))
print(pat.match("caaat"))
print(pat.match("cabat"))
"""
 ####################################################################
 #### 반복(?)
 ####################################################################
 ? : 반복 횟수가 0 또는 1,  {0, 1} 과 동일

 ex) ab?c : "abc" => 매치
            "ac"  => 매치
"""
pat = re.compile("ab?c")
print(pat.match("abc"))
print(pat.match("ac"))

"""
 ####################################################################
 #### re 모듈
 ####################################################################

 re.match()    : 문자열의 처음부터 정규식과 매치되는지 조사
 re.search()   : 문자열 전체를 검색하여 정규식과 매치되는지 조사
 re.findall()  : 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴
 re.finditer() : 정규식과 매치되는 모든 문자열(substring)을 iterator 객체로 리턴
"""
p = re.compile('[a-z]+')

"""
 match
"""
m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

"""
 search
"""
m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

"""
 findall
"""
result = p.findall("life is too short")
print(result)

"""
 finditer
"""
result = p.finditer("life is too short")
print(result)
for r in result: print(r)

"""
 #### Match object 메소드

 - group() : 매치된 문자열 리턴
 - start() : 매치된 문자열의 시작 위치를 리턴
 - end()   : 매치된 문자열의 끝 위치를 리턴
 - span()  : 매치된 문자열의 (시작, 끝) 위치를 튜플로 리턴
"""
m = p.match("python")
m.group()
m.start()
m.end()
m.span()

m = p.search("3 python")
m.group()
m.start()
m.end()
m.span()

"""
 #### 축약 형태 사용
"""
m = re.match('[a-z]+', "python")

"""
 ####################################################################
 #### re.compile 옵션
 ####################################################################

 DOTALL(S)     : Dot(.) 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 함
 IGNORECASE(I) : 대소문자에 관계없이 매치
 MULTILINE(M)  : 여러줄에 매치 (^, $ 메타문자와 관계)
 VERBOSE(X)    : verbose 모드 사용 (정규식을 읽기 쉽게 주석 등을 사용할 수 있음)

 S, I, M, X : 약어.  re.DOTALL 대신 re.S 로 사용 가능
"""

"""
 #### DOTALL(S)
"""
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL) # re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

"""
 #### DOTALL(S)
"""
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL) # re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

"""
 #### IGNORECASE(I)
"""
p = re.compile('[a-z]', re.I)
p.match('python')
p.match('Python')
p.match('PYTHON')

"""
 #### MULTILINE(M)

 '^' : 문자열의 처음을 의미
 '$' : 문자열의 끝을 의미

 ex) "^python" : 문자열이 python으로 시작
     "python$" : 문자열이 python으로 끝남
"""

data = """python one
life is too short
python two
you need python
python three
"""

p = re.compile("^python\s\w+")
print(p.findall(data))

p = re.compile("^python\s\w+", re.M)
print(p.findall(data))

"""
 #### VERBOSE(X)

 - re.VERBOSE 옵션을 사용하면 문자열에 사용된 whitespace는 실행 시 제거됨.
   (단, [] 안의 whitespace는 제외)
"""
charref = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

"""
 #### '\' 문제 해결

 - 정규식이 '\section'일 경우, '\s' 는 [ \t\n\r\f\v]ection 으로 해설될 수 있음
 - 이럴 경우, '\\section'으로 해야함.
 - r'\section' 으로 처리 가능
"""


