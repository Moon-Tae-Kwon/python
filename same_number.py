#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 첫번째 줄 path 설정/ 두번째 줄의 경우 coding 중에 한글 표시가 주석형태로 기재 되기 떄문에 언어셋을 utf8 로 설정

import sys
#시스템 명령어를 사용하는 Python 기본 모듈 운영체제의 메모리 및 기본 명령어를 실행할수 있도록 해주는 모듈

same_number = [1, 1, 3, 3, 0, 1, 1]
# 리스트화를 진행한 숫자 [] <- 리스트화
print(type(same_number)) # list 타입 확인.

number = [] #중복이 제외된 숫자 list를 담을 리스트 사전에 생성
for i in same_number: #for 문을 이용한 변수(i)와 제시되는 숫자를 반복
    if number[-1:] == [i]: continue # if 문을 통한 비교값 nomber 리스트에서 슬라이싱을 활용한 비교되는 리스트 를 맨뒤 에 삽입된 숫자와 비교 continue문은 결과를 만족할 경우에는 다시 처음으로, break 와 반대로 사용 됩니다.
    number.append(i) # 위의 continue 부분으로 인해서 리스트에서 슬라이싱한 -1 을 계속 비교하여 중복으로 나열되지 않은 숫자만 결국 .append 를 이용하여 리스트에 넣습니다.
print (number)

#같은 숫자가 중복되면 제외하는 함수
def same_number(del_number):
    a = []
    for i in del_number:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

print (same_number("1133011"))