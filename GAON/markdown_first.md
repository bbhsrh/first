# 안녕하시렵니까


> 일반 테스트 형식 구문을 사용하는 마크업 언어의 일종인 마크다운 사용법이 참 쉽고 간결
> 빠르게 문서정리 가능
> 단, 모든 HTML 마크업 대체X
>
> HTML Markup(마크업) <-> Markdown(마크다운)
> 
> * 마크업: 문서에서 특정내용이 어떤 역할을 하는지 표시
> * 마크다운: 번거로운 마크업의 태그를 더 간단히 기호로 표시

---

## 1. 문법
### 1.1 Header
> 헤더는 제목을 표현할 때 사용.\
> 단순히 글자크기 ㄴㄴ\
> 의미적인 중요도!

# h1 태그
## h2 태그
### h3 태그
#### h4 태그
##### h5 태그
###### h6 태그

### 1.2 List
> 목록 나열에 사용
* 순서가 있는 목록
1. 순서있는 상위 목록
2. 순서있는 상위 목록
    1. 순서있는 하위 목록
    2. 순서있는 하위 목록
        1. 순서있는 하위 목록
        2. 순서있는 하위 목록
* 순서 없는
    * 순서 없 하
        * 순서 없 하하
        

### 1.3 Code Block
> 코드블럭은 작성한 코드를 정리, 강조할때 사용
> 이것도 인라인과 블럭으로 나눠서 사용 가능

+ inline : 백틱을 이용해 사용\
    `console.log('hello')`
    
* block : 백틱을 세번 이용
    ```javascript
    console.log('hello')
    ```
    
### 1.4 Image
> 로컬 이미지 삽입 또는 링크활용 삽입가능

* `![]()`로 작성`()`안에 이미지 주소
![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/1200px-Markdown-mark.svg.png)

### 1.5 Table
> 표를 작성
* `|`파이프 사이에 컬럼

|이름|학과|먹고싶은 과자|
|:--:|:--:|:-------:|
|박가온|정보통계학과|스윙칩|

### 1.7 기타

인용문 : `>`

수평선 : `---`

강조 : `*이탤릭*`, `**볼드**`, `~~취소~~`



# Markdown syntax guide

## Headers

# This is a Heading h1
## This is a Heading h2 
###### This is a Heading h6

## Emphasis

*This text will be italic*  
_This will also be italic_

**This text will be bold**  
__This will also be bold__

_You **can** combine them_

## Lists

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b

### Ordered

1. Item 1
1. Item 2
1. Item 3
  1. Item 3a
  1. Item 3b

## Images

![This is a alt text.](/image/sample.png "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.


---
---

## GIT
코드관리, 협업, 배포

## CLI (Command Line Interface)
커맨드(명령어)를 통해 작동하는 인터페이스
<-> GUI(Graphic User Interface)

1. pwd(print working directory)
   - 현재 폴더의 경로
2. ls(list)
   - 현재 폴더 내 내용물
3. cd [폴더명] (change directory)
    - 폴더 변경
4. mkdir [폴더명] (make directory)
    - 폴더 생성
5. rm [파일명] (remove)
    - 파일 삭제
6. rm -r [폴더명] (remove) (recursively:재귀적)
    - 폴더 삭제
7. touch [파일명]
    - 파일 생성
8. cp [파일명] [위치] (copy)
9. mv [파일/폴더] [파일/폴더] (move)
    - 파일이동, 이름변경


## Github
