import re

"""
 meta character: . ^ $ * + ? { } [ ] ( ) \ |
"""

"""
 ####################################################################
 #### 문자열 소모가 없는(zero-width assertions) 메타 문자
 ####################################################################
"""

"""
 #### '|' : or 과 같은 의미
"""
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

"""
 #### '^' : 문자열의 맨 처음과 일치
"""
print(re.match('^life', 'life is too short'))
print(re.search('^life', 'my life'))

"""
 #### '$' : 문자열의 맨 끝과 일치
"""
print(re.search('short$', 'life is too short'))
print(re.search('short$', 'life is too short, you need python'))

"""
 #### '\^', '\$' 또는 [^], [$] : 문자열 중의 '^' 또는 '$'를 찾고자 할 경우 사용
"""

"""
 #### '\A' : 문자열의 처음과 매치
    - re.MULTILINE 옵션(X) : '^' 과 동일
    - re.MULTILINE 옵션(O) : 라인과 상관없이 전체 문자열의 처음과 매치
                             '^' 는 라인별 문자열의 처음과 매치
"""

"""
 #### '\Z' : 문자열의 끝과 매치
    - re.MULTILINE 옵션(X) : '$' 과 동일
    - re.MULTILINE 옵션(O) : 라인과 상관없이 전체 문자열의 끝과 매치
                             '$' 는 라인별 문자열의 끝과 매치
"""

"""
 #### '\b' : 단어 구분자(word boudary)
    - 주의점: 일반 문자열에서 '\b'는 backspace이므로, 정규식 문자열 작성 시에
              r'\b' 처럼 r 을 붙여야 함.
"""
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

print(p.search('one subclass is'))  # class 앞뒤로 공백이 없음
                                    # whitespace 로 구분된 단어가 아님
print(p.search('the declassified algorithm'))

"""
 #### '\B' : whitespace로 구분된 단어가 아닐 경우를 매치
"""
print(re.search(r'\Bclass\B', 'no class at all'))
print(re.search(r'\Bclass\B', 'the declassified algorithm'))
print(re.search(r'\Bclass\B', 'one subclass is'))


"""
 ####################################################################
 #### Grouping : 문자열의 반복 매치
 ####################################################################
"""
m = re.search('(ABC)+', 'ABCABCABC ok?')
print(m)
print(m.group())
m.group(0)
m.group(1)

re.search(r"\w+\s+\d+[-]\d+[-]\d+", "park 010-1234-1234")

m = re.search(r"(\w+)\s+\d+[-]\d+[-]\d+", "park 010-1234-1234")
m.group(0)  # group[0]: 매치된 전체 문자열
m.group(1)  # group[1]: 첫 번째 그룹에 해당되는 문자열

m = re.search(r"(\w+)\s+(\d+[-]\d+[-]\d+)", "park 010-1234-1234")
m.group(0)  # group[0]: 매치된 전체 문자열
m.group(1)  # group[1]: 1 번째 그룹에 해당되는 문자열
m.group(2)  # group[2]: 2 번째 그룹에 해당되는 문자열

m = re.search(r"(\w+)\s+((\d+)[-]\d+[-]\d+)", "park 010-1234-1234")
m.group(0)  # group[0]: 매치된 전체 문자열
m.group(1)  # group[1]: 1 번째 그룹에 해당되는 문자열
m.group(2)  # group[2]: 2 번째 그룹에 해당되는 문자열
m.group(3)  # group[3]: 3 번째 그룹에 해당되는 문자열
            # 그룹의 순서는 () 중첩 우선순위에 따름

"""
 ####################################################################
 #### Grouping 문자열 재참조
 ####################################################################
"""
m = re.search(r'(\b\w+)\s+\1', 'Paris is the the spring')
m.group()   # (group1) + ' ' + group1과 동일한 단어

"""
 ####################################################################
 #### Grouping 문자열에 이름 붙이기
 ####################################################################
    - (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
       ~~~~~~~~ : (\w+) -> (?P<name>\w+)
    - (?P<name>그룹명) : 정규표현식의 확장 구문
"""
m = re.search(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)", "park 010-1234-1234")
m.group("name")
m = re.search(r"(?P<name>\w+)\s+(?P<tel>(?P<telexc>\d+)[-]\d+[-]\d+)", "park 010-1234-1234")
m.group("name")
m.group("tel")
m.group("telexc")

m = re.search(r'(?P<word>\b\w+)\s+(?P=word)', 'Paris in the the spring')
m.group()

"""
 ####################################################################
 #### 전방 탐색(Lookahead Assertions) 확장구문
 ####################################################################
    - Positive 전방 탐색 ( (?=...) ): 해당 정규식과 매치(O), 문자열 소모 없음
    - Negative 전방 탐색 ( (?!...) ): 해당 정규식과 매치(X), 문자열 소모 없음
"""
m = re.search(".+:", "http://google.com")
m.group()

"""
    - 'http:' 에서 ':'를 제외하고 출력하고 싶을 경우 ?
"""
m = re.search(".+(?=:)", "http://google.com")
m.group()

"""
    - '.*[.].*$' : 파일명 + '.' + 확장자 정규식
"""
m = re.search(".*[.].*$", "foo.bar")
m.group()

"""
    - bat 확장자 파일은 제외 ?
"""
m = re.search(".*[.](?!bat$).*$", "foo.bat")
print(m)

"""
    - bat 또는 exe 확장자 파일은 제외 ?
"""
m = re.search(".*[.](?!bat$|exe$).*$", "foo.exe")
print(m)

"""
 ####################################################################
 #### 문자열 바꾸기
 ####################################################################
"""
p = re.compile('(blue|white|red)')
p.sub('color', 'blue socks and red shoes')

p = re.compile('(blue|white|red)')
p.sub('color', 'blue socks and red shoes', count=1)  # 처음 한 번만 변경

"""
    - subn : sub과 동일. 단, 결과와 발생 횟수를 포함한 tuple을 리턴
"""
p = re.compile('(blue|white|red)')
p.subn('color', 'blue socks and red shoes')

"""
 #### sub 사용 시 참조 구문 사용
"""
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
    # 이름+전화번호 -> 전화번호+이름으로 변경

"""
 #### sub 메소드의 입력 인수로 함수 넣기
"""
def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
hex(65490)
hex(49152)

"""
 ####################################################################
 #### Greedy vs Non-Greedy
 ####################################################################
    - Non-Greedy : 가능한 한 가장 최소한의 반복 수행
"""
s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())

print(re.match('<.*?>', s).group())

