## 소개

Notion API 써드파티 라이브러리입니다. 이 프로젝트는 Notion의 데이터베이스 기능을 다른 관계형 데이터베이스처럼 사용할 수 있도록 구현하는 것이 목적입니다.

## 사용법
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

### DELETE 코드 실행전

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