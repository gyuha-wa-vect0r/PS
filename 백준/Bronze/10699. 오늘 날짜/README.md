# [Bronze V] 오늘 날짜 - 10699 

[문제 링크](https://www.acmicpc.net/problem/10699) 

### 성능 요약

메모리: 38068 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력은 없다.</p>

### 출력 

 <p>서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.</p>

### MY MEMO

 <p> 날짜를 다룰 때에는 import datetime 을 이용한다. datetime 패키지 전체를 가지고 와서 쓰겠단 얘기다.</p>
 <p> datatime 패키지 내에는 datatime(날짜, 시간 저장), data(날짜만 저장), time(시간만 저장), timedelta(시간 구간만 저장) 클래스 등이 있다.</p>
 <p> datatime 클래스에는 year: 연도, month: 월, day: 일, hour: 시, minute: 분, second: 초, microsecond: 마이크로초 속성이 포함되어있다. 따라서 x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond -> (2020, 10, 2, 15, 27, 4, 517207) 로 출력된다.</p>
 <p>


