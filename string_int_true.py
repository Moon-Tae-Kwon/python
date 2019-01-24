#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 첫번째 줄 path 설정/ 두번째 줄의 경우 coding 중에 한글 표시가 주석형태로 기재 되기 떄문에 언어셋을 utf8 로 설정

import sys
#시스템 명령어를 사용하는 Python 기본 모듈 운영체제의 메모리 및 기본 명령어를 실행할수 있도록 해주는 모듈

def solution(s):
    return s.isdigit() and len(s) in (4, 6)
# and=그리고/len함수는 리스트의 크기를 알고 싶을 경우 사용/s 리스트 크기가 4와 6 사이에 있다.
print (solution("1234"))