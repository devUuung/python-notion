## 소개

Notion API 써드파티 라이브러리입니다. 이 프로젝트는 Notion의 데이터베이스 기능을 다른 관계형 데이터베이스처럼 사용할 수 있도록 구현하는 것이 목적입니다.

## 사용법

### DB 연결방법
```py
from notion.database import Database

db1 = Database(
        "databaseUrl",
        "apiKey",
        a=Database.CharField(pk = True),
        b=Database.CharField(null = False),
        c=Database.CharField(null = False)
    )
```

### 매개변수 정리
1. pk

primary-key인지 명시합니다.
(기본값 False)

2. null

값이 비워져있어도 되는지 명시합니다.
(기본값 True)

3. foreign

외래 db가 있는지 명시합니다.
(기본값 None)

### 외래키 연결법
```py
db1 = Database(
        "databaseUrl",
        "apiKey",
        a=Database.CharField(pk = True),
        b=Database.CharField(null = False),
        c=Database.CharField(null = False)
    )

db2 = Database(
        "databaseUrl",
        "apiKey",
        a=Database.CharField(pk = True, foreign=db1),
        b=Database.CharField(null = False),
        c=Database.CharField(null = False)
    )
```

foreign 매개변수를 활용해서 외래 db를 연결할 수 있습니다.
db2.insert를 할때, a의 값이 db1에 a에도 존재하는지 확인하는 절차를 거칩니다. 

## INSERT

### INSERT 코드 실행전
|a|b|c|
|-|-|-|
```py
from notion.database import Database

db1 = Database(
        "databaseUrl",
        "apiKey",
        a=Database.CharField(),
        b=Database.CharField(),
        c=Database.CharField()
    )

if db1.insert(a="hello", b="World", c="!"):
    print("Success!!")
```
### INSERT 코드 실행후
|a|b|c|
|-|-|-|
|hello|World|!|

## UPDATE

### UPDATE 코드 실행전
|a|b|c|
|-|-|-|
|hello|World|!|

```py
from notion.database import Database

db1 = Database(
        "databaseUrl",
        "apiKey",
        a=Database.CharField(),
        b=Database.CharField(),
        c=Database.CharField()
    )

if db1.update("a", "hello", a="Bye", b="world", c="?"):
    print("Success!!")
```

### UPDATE 코드 실행후
|a|b|c|
|-|-|-|
|Bye|world|?|

## DELETE

### DELETE 코드 실행전
|a|b|c|
|-|-|-|
|Bye|world|?|

```py
from notion.database import Database

db1 = Database(
        "databaseUrl",
        "apiKey",
        a=Database.CharField(),
        b=Database.CharField(),
        c=Database.CharField()
    )

if db1.delete("a", "Bye"):
    print("Success!!")
```

### DELETE 코드 실행후
|a|b|c|
|-|-|-|