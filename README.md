# DataScienceTermP
3학년 1학기 데이터과학 텀프로젝트 preprocessing

### 코드 수정해야 할 부분
+ 데이터 경로 전부 수정해야함!! 다 내 경로로 지정되어있음.
+ 파일도 따로 다운받아야 함 (.csv파일을 ignore 설정해둠)
+ ((데과팀플notion -> data preprocessing -> 이용한 데이터)에 올려두긴 함.)
+ [파일다운](https://woodean.notion.site/af2cb73295464d108f686d3d8dcd6653)

### 진행상황
1. **버스정류장** 데이터끼리 합치기 완료
2. **지하철역 주변 버스정류장** 데이터도 합쳐서 **특정 역 주변 버스 승하차 인원**은 전부 합쳐진 상태

### 할일
1. subway dataset에 **요일 feature 추가**
2. subway dataset에 **부역명 제거**해야함.
3. subway dataset과 busstop dataset 요일별 평균 승하차인원 구해서 새로 feature 추가하기
4. 날씨 dataset도 합쳐야함
5. normalization, tokenization 등 수행해야함.
