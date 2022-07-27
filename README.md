# python-notion

Notion API 써드파티 라이브러리입니다.

### 목차
- [사용예제](#사용예제)

### 사용예제
```py
from notion import Client

myApp = Client("api_key")
myApp.set_database("database_key")

for element in myApp.database.get_elements_text("Attribute"):
  print(element)
```

Attribute는 데이터베이스의 속성입니다. 다음 사진을 예로 들면 Name과 d가 속성입니다.
![Attribute.png](inkdrop://file:NnFAr8_Wf)
