# 모노 알파베틱 암호화 및 크래킹 - 정보보호 개론 실험실습 보고서

## 📋 프로젝트 개요

**과목명**: 정보보호 개론  
**과제물**: 암호문 만들기와 해독하기 (모노 알파베틱 암호)  
**개발언어**: Python  
**목표**: 모노 알파베틱 암호화 알고리즘을 구현하고, 복호화 및 크래킹 기법을 학습

---

## 🎯 실습 목표

1. **모노 알파베틱 암호 알고리즘 이해**: 치환 암호의 기본 원리를 이해하고 구현
2. **암호화 및 복호화**: 주어진 키값을 이용한 암호문 생성과 복호화
3. **암호 크래킹 기법 학습**: 무작위 대입법과 사전 대입법을 활용한 암호 해독
4. **성능 비교**: 서로 다른 크래킹 알고리즘의 수행 속도 비교

---

## 📚 모노 알파베틱 암호(Monoalphabetic Substitution Cipher)

### 개념
- 평문의 각 문자를 **고정된 규칙에 따라** 다른 문자로 치환하는 암호
- 키(Key)를 기반으로 **일대일 치환 규칙**을 생성
- 같은 평문 문자는 항상 같은 암호문 문자로 변환됨

### 작동 원리
1. **키 생성**: 입력된 키(key)를 이용하여 알파벳 순서를 재배열
2. **치환 테이블 생성**:
   - 원본 알파벳: a b c d e f g h i j k l m n o p q r s t u v w x y z
   - 암호 알파벳: (키를 기반으로 생성)
3. **암호화**: 평문의 각 문자를 치환 테이블에 따라 변환
4. **복호화**: 역방향 치환 테이블을 사용하여 암호문을 평문으로 복원

---

## 🔧 프로그램 구조

### 주요 함수

#### 1. `generate_cipher_alphabet(key)`
- **기능**: 키를 기반으로 암호 알파벳 생성
- **입력**: 암호화 키 (문자열)
- **출력**: 중복 제거된 정렬된 암호 알파벳 문자열

#### 2. `encrypt(plaintext, key)`
- **기능**: 평문을 주어진 키로 암호화
- **입력**: 평문, 암호화 키
- **출력**: 암호문
- **처리**: 공백 제거, 소문자 변환, 치환 수행

#### 3. `decrypt(ciphertext, key)`
- **기능**: 암호문을 주어진 키로 복호화
- **입력**: 암호문, 복호화 키
- **출력**: 평문
- **처리**: 역방향 치환 테이블 사용

#### 4. `crack_cipher_random(ciphertext, max_iterations=1000000)`
- **기능**: 무작위 대입법을 이용한 암호 크래킹
- **알고리즘**: 랜덤한 키를 생성하여 복호화 시도
- **효율성**: 낮음, 시간이 오래 걸림
- **용도**: 교육적 목적, 성능 비교

#### 5. `crack_cipher_dictionary(ciphertext, dictionary_file)`
- **기능**: 사전 대입법을 이용한 암호 크래킹
- **알고리즘**: 사전 파일의 각 단어를 키값으로 사용하여 복호화 시도
- **효율성**: 높음, 빠른 결과
- **용도**: 실제 암호 해독, 성능 최적화

---

## 📝 실습 1: 암호화 및 복호화

### 1-1. 암호화 실습

**주어진 데이터:**
- 암호화 키: `month`
- 평문: `monoalphabetic substitution`
- 공백 제거 후: `monoalphabeticsubstitution`

**실습 내용:**
```
암호화 키: month
평문: monoalphabetic substitution
공백 제거: monoalphabeticsubstitution
암호문: ???
```

**기대 결과:**
- 키 `month`를 이용하여 평문을 암호문으로 변환
- 같은 문자는 항상 같은 암호 문자로 치환되어야 함

### 1-2. 복호화 실습

**주어진 데이터:**
- 복호화 키: `value`
- 암호문: `telxsehvthvmgpsiwhn`

**실습 내용:**
```
복호화 키: value
암호문: telxsehvthvmgpsiwhn
평문: ???
```

**기대 결과:**
- 키 `value`를 이용하여 암호문을 평문으로 변환
- 원래의 의미 있는 영어 문장이 나와야 함

---

## 🔐 실습 2: 암호 크래킹

### 2-1. 크래킹 대상 암호문

```
kotcihndotmivhonucswthvaifcnsa
```

### 2-2. 크래킹 목표

1. **키 값 찾기**: 이 암호문을 암호화한 원래의 키는 무엇인가?
2. **평문 복원**: 원래의 평문은 무엇인가?
3. **알고리즘 선택**: 사전 파일을 이용하여 효율적으로 크래킹

### 2-3. 두 가지 크래킹 기법 비교

#### 무작위 대입법 (Random Brute Force)
```python
a = gettime()
# 암호해독 (무작위 키 시도)
plaintext = crack_cipher_random(ciphertext)
b = gettime()
proc_time = b - a
```

**특징:**
- 무작위로 키를 생성하여 시도
- 시간 복잡도: O(매우 높음)
- 평균 실행 시간: 수 분 ~ 수 시간
- 장점: 사전이 없어도 작동
- 단점: 비효율적, 시간 소요 큼

#### 사전 대입법 (Dictionary Attack)
```python
a = gettime()
# 암호해독 (사전 파일 사용)
plaintext = crack_cipher_dictionary(ciphertext, 'dictionary.txt')
b = gettime()
proc_time = b - a
```

**특징:**
- 사전 파일의 각 단어를 키로 사용
- 시간 복잡도: O(단어 수)
- 평균 실행 시간: 밀리초 ~ 초 단위
- 장점: 매우 빠름, 효율적
- 단점: 사전 파일 필요, 제한된 범위

### 2-4. 성능 비교 분석

| 항목 | 무작위 대입법 | 사전 대입법 |
|------|-------------|----------|
| 실행 속도 | 매우 느림 | 매우 빠름 |
| 성공률 | 높음 (충분한 시간 필요) | 중간~높음 (사전에 따라) |
| 메모리 사용 | 적음 | 중간 (사전 크기) |
| 실용성 | 낮음 | 높음 |
| 적용 분야 | 교육용 | 실무용 |

---

## 💻 사용 방법

### 1. 기본 암호화 및 복호화

```python
from ciper import encrypt, decrypt

# 암호화
plaintext = "monoalphabeticsubstitution"
key = "month"
ciphertext = encrypt(plaintext, key)
print(f"평문: {plaintext}")
print(f"암호문: {ciphertext}")

# 복호화
key_decrypt = "value"
ciphertext = "telxsehvthvmgpsiwhn"
plaintext = decrypt(ciphertext, key_decrypt)
print(f"암호문: {ciphertext}")
print(f"평문: {plaintext}")
```

### 2. 무작위 대입법을 이용한 크래킹

```python
from ciper import crack_cipher_random
import time

ciphertext = "kotcihndotmivhonucswthvaifcnsa"

a = time.time()
result = crack_cipher_random(ciphertext, max_iterations=100000)
b = time.time()

print(f"크래킹 결과: {result}")
print(f"소요 시간: {b - a:.2f}초")
```

### 3. 사전 대입법을 이용한 크래킹

```python
from ciper import crack_cipher_dictionary
import time

ciphertext = "kotcihndotmivhonucswthvaifcnsa"

a = time.time()
result = crack_cipher_dictionary(ciphertext, 'dictionary.txt')
b = time.time()

print(f"크래킹 결과: {result}")
print(f"소요 시간: {b - a:.4f}초")
```

---

## 📊 예상 실행 결과

### 실습 1 결과
```
[실습 1-1] 암호화
암호화 키: month
평문: monoalphabeticsubstitution
암호문: (생성된 암호문)

[실습 1-2] 복호화
복호화 키: value
암호문: telxsehvthvmgpsiwhn
평문: (복호화된 평문)
```

### 실습 2 결과
```
[실습 2] 암호 크래킹
대상 암호문: kotcihndotmivhonucswthvaifcnsa

무작위 대입법:
- 발견된 키: (키 값)
- 복호화된 평문: (평문)
- 소요 시간: (시간) 초

사전 대입법:
- 발견된 키: (키 값)
- 복호화된 평문: (평문)
- 소요 시간: (시간) 초

성능 비교:
- 무작위 대입법이 사전 대입법보다 약 (배수)배 느림
```

---

## 📁 파일 구조

```
monoalphabetic-cipher/
├── ciper.py                 # 모노 알파베틱 암호 구현 코드
├── dictionary.txt           # 사전 대입법에 사용할 단어 사전
├── test.py                  # 프로그램 테스트 코드 (선택사항)
└── README.md                # 이 문서
```

---

## 🔍 알고리즘 분석

### 모노 알파베틱 암호의 보안성

**강점:**
- 간단한 구현
- 계산량이 적음

**약점:**
- 빈도 분석에 취약 (영어의 경우 'e'가 가장 빈번)
- 작은 키 공간: 26! ≈ 4 × 10^26 (컴퓨터로도 브루트포스 가능)
- 패턴 분석으로 해독 가능

### 보안 개선 방법
1. **다중 알파벳 사용** (폴리알파베틱 암호)
2. **더 복잡한 치환 규칙**
3. **현대 암호화 알고리즘 사용** (AES, RSA 등)

---

## 📌 주의사항

1. **공백 처리**: 암호화 시 모든 공백은 제거됨
2. **대소문자**: 모든 입력은 소문자로 변환됨
3. **특수문자**: 알파벳만 처리하며, 숫자나 특수문자는 제거됨
4. **키 검증**: 키는 영문자만 포함해야 함

---

## 🎓 학습 포인트

1. **암호화의 기본 개념**: 치환 암호의 작동 원리
2. **알고리즘 구현**: 파이썬으로 암호화 알고리즘 구현
3. **성능 최적화**: 서로 다른 알고리즘의 효율성 비교
4. **보안 분석**: 암호의 강점과 약점 분석
5. **실무 기술**: 사전 대입법을 이용한 실제 암호 해독 기법

---

## 📞 참고사항

- **실험 일시**: 2026년 5월
- **제출 내용**: 실습 결과 및 성능 비교 분석 보고서
- **제출 형식**: 프로그램 코드 + 결과 분석 이메일 발송

---

**작성자**: 정보보호 개론 실습생  
**최종 수정**: 2026년 5월 19일
