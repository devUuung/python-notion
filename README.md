### 목차

- [소개](#소개)
- [사용예제](#사용예제)

### 소개

Notion API 써드파티 라이브러리입니다. 이 프로젝트는 Notion의 데이터베이스 기능을 다른 관계형 데이터베이스처럼 사용할 수 있도록 구현하는 것이 목적입니다.

### 사용예제

```py
from notion import Client

myApp = Client("api_key")
myApp.set_database("database_key")

for element in myApp.database.get_elements_text("Attribute"):
  print(element)
```
