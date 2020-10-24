# News Title Autocompletion and News Summarization with RNN and Transfer Learning  

## Contents
1. [Problem Definition](#Problem-Definition)

2. [How To Solve](#How-To-Solve)

3. [Datasets](#Datasets)

4. [Experiment Method](#Experiment-Method)

5. [Results](#Results)

6. [Reference](#Reference)

## Problem Definition  
본 프로젝트를 통해 2가지 기능을 구현하려고 한다.  
1) 유저가 검색어를 입력하면 그에 해당되는 기사 제목을 자동으로 완성하는 기능  
2) 후보 기사들의 본문을 딥러닝 기반의 알고리즘으로 요약해서 완성된 제목과 함께 보여주는 기능  

<img width="499" alt="스크린샷 2020-10-24 오후 6 40 25" src="https://user-images.githubusercontent.com/52681837/97078646-7d341400-1628-11eb-87c3-394c8bb7f616.png">

## How To Solve
1) 뉴스 제목 자동 완성 기능  
뉴스 데이터에 대하여 문자열 탐색 알고리즘을 수행하는 모듈이다.  
검토 후보는 Rabin-Karp Algorithm과 Knuth-Morris-Pratt(KMP) Algorithm, 그리고 Boyer-Moore Algorithm이었다.  
일반적으로 사람들이 뉴스를 검색할 때, 뉴스 제목의 제일 앞 단어가 아닌 핵심 단어를 중심으로 검색하기 때문에 문자열의 제일 앞부터 검토하는 것이 비효율적이라고 생각했다.  
따라서, 끝자리부터 빠르게 검색해서 문장의 중심으로 빠르게 넘어갈 수 있는 Boyer-Moore Algorithm을 채택하기로 했다.  

2) 뉴스 본문 요약 기능  


## Datasets  
데이터셋은 2개를 사용하였다.  
1) [BBC News Summary](https://www.kaggle.com/pariza/bbc-news-summary)  
뉴스 본문을 Input으로 주었을 때 요약된 뉴스를 Output으로 출력하는 알고리즘을 검증하기 위해 사용하였다.
2225개의 본문-요약 쌍이 데이터셋으로 제공되었다.  

++ 20.10.24.  
News Articles/sport/199.txt가 유니코드 인코딩이 되어 있지 않아 파일이 열리지 않는 버그를 찾았다.  
해당 txt 파일과 summaries 폴더 내 상응하는 txt 파일을 제거하고 실험을 진행하였다.  

2) [All the News](https://www.kaggle.com/snapcrack/all-the-news)  
서비스가 제공되는 플랫폼에서 데이터를 받아왔다고 가정했다. 뉴스 제목과 본문이 데이터셋에 들어있다.   
뉴스 제목 자동 완성 알고리즘 및 앞서 검증한 뉴스 본문 요약 알고리즘을 이 데이터셋이 적용하는 것을 목적으로 한다.

## Experiment Method

## Results

## Reference
