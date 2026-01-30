<<<<<<< HEAD
# 02-PJT-성호민



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://lab.ssafy.com/hmsung0908/02-pjt.git
git branch -M master
git push -uf origin master
```

## Integrate with your tools

- [ ] [Set up project integrations](https://lab.ssafy.com/hmsung0908/02-pjt/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/user/project/merge_requests/auto_merge/)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
=======
# SSAFY 15기 관통 프로젝트

<br/>


# 1. Project Overview (프로젝트 개요)
- 프로젝트 이름: 관통 PJT 02
- 프로젝트 설명: 넷플릭스 주가 데이터 분석

<br/>
<br/>


# 2. Team Members (팀원 및 팀 소개)
| 성하빈 |성호민 | 
|:------:|:------:|
| <img src="https://images.pet-friends.co.kr/v2/community/2025/11/16/f80f0c50-abed-431b-ad7c-63b1007b7eab.jpeg?f=webp"  width="150"> | <img src="https://images.mypetlife.co.kr/content/uploads/2022/12/08151554/AdobeStock_223053245-857x1024.jpeg"  width="150"> | 
| 5반 | 5반 |
| [GitHub](https://github.com/seonghabin) | [GitHub](https://github.com/hoomin0908) | 

<br/>
<br/>

# 3. Key Features (주요 기능)
- **데이터 수집**:
  - Kaggle 에서 Netflix 주가 데이터 다운로드

- **데이터 전처리**:
  - Netflix 주가 데이터 (NFLX.csv를 Pandas를 사용해 DataFrame 으로 읽음
  - 이 때 'Date', 'Open','High', 'Low', 'Close' 필드만 선택
  - 2021 년 이후 데이터 필터링

- **데이터 분석1**:
  - 2021년 이후 데이터에서 종가(Close)의 최대 최소 값을 추출

- **데이터 분석2**:
  - 2021년 이후 데이터를 월별로 그룹화하여 평균 종가를 계산 하여 시각화

- **데이터 시각화**:
  - 2022년 이후 데이터를 바탕으로 3 가지 지표를 하나의 그래프에 시각화

- **생성형 AI 활용**:
  - 생성형AI 에게 적절한 프롬프트를 설계하고 주가에 대한 예측 결과를 도출


<br/>
<br/>

# 4. Technology Stack (기술 스택)

|  |  |
|-----------------|-----------------|
| Jupyter Notebook    |<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/250px-Jupyter_logo.svg.png" alt="HTML5" width="100">| 
| Pandas    |   <img src="https://miro.medium.com/v2/resize:fit:1620/1*b3P4rdrVHMIHbhQXnwRVew.jpeg" alt="CSS3" width="100">|
| Numpy    |  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMrTWz33b86nfIrgaW9jE_t-7VCcqJtjL-pg&s" alt="Javascript" width="100"> | 
| Matplotlib    |  <img src="https://media.licdn.com/dms/image/v2/D4D12AQFq38cGkv_oHQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1679493396295?e=2147483647&v=beta&t=8hBosvau_9_t0Nt46DZ89TxWOgFZg_z47cMFn8o5cmM" alt="Notion" width="100">    |
| Git    |  <img src="https://github.com/user-attachments/assets/483abc38-ed4d-487c-b43a-3963b33430e6" alt="git" width="100">    |


<br/>

# 5. TIL (Today I Learned)
- **CSV 데이터를 분석용 데이터로 바꾸기**

❓ 문제

numpy로 불러온 데이터가 전부 문자열(str) 이라서 계산이 안 됐음

🚩해결
```python
df[['Close','High','Low','Open']] = df[['Close','High','Low','Open']].astype(float)
df['Date'] = pd.to_datetime(df['Date'])
```

✔ 숫자는 float, 날짜는 datetime으로 바꿔야 분석 가능

<br/>
<br/>

- **DataFrame은 딕셔너리가 아니다**
```python
df['Close']
```
<br/>

✔이 문법이 딕셔너리처럼 보여서 헷갈렸지만, 실제로는 행과 열을 가진 2차원 표 형태의 데이터 구조(DataFrame) 이다.

<br/>
<br/>

- **날짜 필터링 방법 차이**

| 상황 | 방법 |
|-----------------|-----------------|
| Date가 컬럼일 때	| df[df['Date'] >= '2022-01-01']|
| Date가 인덱스일 때	| df.loc['2022-01-01':]|

✔인덱스를 유지하고 싶어서 조건 필터링 방식 사용

<br/>
<br/>

- **matplotlib 시각화 핵심**

**그래프 크기 조절**
```python
plt.figure(figsize=(12,5))
```
**x축 글자 겹침 해결**
```python
plt.xticks(rotation=45)
plt.tight_layout()
```

❓y축이 이상했던 이유

🚩Close가 문자열이라 범주형 데이터처럼 처리됨
→ astype(float)로 변환해서 해결

<br/>
<br/>

- **생성형 AI 활용 분석 프롬프트 작성**

오늘의 마지막 단계는 단순 시각화를 넘어
AI가 데이터를 해석하도록 질문을 설계하는 것이었다.

우리가 만든 프롬프트 핵심 요소

**주가 추세 분석**

**급락 원인 해석**

**시장 심리 분석**

**단기 주가 예측**

**매수/매도 판단**

🚩 단순 코딩을 넘어 AI 기반 금융 분석 흐름까지 확장
>>>>>>> 6088950 (성호민)
