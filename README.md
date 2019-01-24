## python

# 천천히.. 확실하게..

* 프로그램이 동작하는 과정을 이해 시켜주는 사이트
http://pythontutor.com

---

* len() 함수는 리스트에 들어있는 원수 개수/리스트 크기를 알려줌
```
len([1, 2, 3, 4, 5])
5
len(a_list)
13
```
* isdigit() 함수는 '문자열이 숫자로 구성되어 있는가' 라는 것을 확인해 주는 메소드일 뿐이다.
```
"123".isdigit()
True
"-123".isdigit()
False
"1a23".isdigit()
False
```
* append()는 object를 맨 뒤에 추가합니다.
```
x = [1, 2, 3]
x.append([4, 5])
print (x)
x = [1, 2, 3, [4, 5]]
```
* extend()는 iterable 객체(리스트, 튜플, 딕셔너리 등)의 엘레멘트를 list에 appending시킵니다.
```
x = [1, 2, 3]
x.extend([4, 5])
print (x)
x = [1, 2, 3, 4, 5]
```
* continue를 만나면 그 아래의 코드를 수행하지 않고 while 문의 조건을 판단하는 곳으로 점프하게 됩니다.
```
num = 0
while num < 10:
    num += 1
    if num == 5:
            continue
    print(num)
```

---

* [중복되는 리스트 제거 (같은숫자제거)](same_number.py)
* [문자열 다루기 1](string_int_true.py)