# Async API http server for Unison Telegram Bot database  

Author: Nikita Kulikov

Date: 12.2022

## About
### Description
This little http server provide remote controll for postgresql database for Unison Telegram Bot.

For **SENDING** information to database use **POST** request

For **GETTING** information from database use **GET** request

**url** = http://86.110.212.247:3333/

### Requirements
| **lib** | **version** |
| ------- | -------- |
| aiohttp | v. 3.8.3 |
| asyncpg | v. 0.27.0 |
| requests | v. 2.25.1 |

## Example of requests

### Status, Initiation of Tables and creating new user
___
Status
```
POST or GET:
url = http://86.110.212.247:3333/status

Rsponse if server is up:
<Response [200]>
{
    'status' : 'server is up'
}
```
Initiation of tables in database
```
POST or GET:
url = http://86.110.212.247:3333/ini

Rsponse if success:
<Response [200]>
{
    "status": "success"
}
```

Creating new user
```
POST or GET
url = http://86.110.212.247:3333/new_user

json = {
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Rsponse if success:
<Response [200]>
{
    "status": "success"
}
```

### Profile
____
**NAME** 

POST:
```
url = http://86.110.212.247:3333/name

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'name' : 'Никита'   # Must be string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```
GET:
```
url = http://86.110.212.247:3333/name

json = {
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'name' : 'Никита'  # string
}
```
**CITY**

POST:
```
url = http://86.110.212.247:3333/city

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'city' : 'Санкт-Петербург'  # string
}

Response if success:
<Response [200]>
{
    'name' : 'Никита' # string
}
```

GET:
```
url = http://86.110.212.247:3333/city

json = {
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'city' : 'Санкт-Петербург' # string
}
```
**GENDER**

POST:
```
url='http://86.110.212.247:3333/gender'

json ={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'gender' : 'Мужской'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/gender'

json ={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'gender' : 'Мужской'
}
```

**BIRTHDAY**

POST:
```
url='http://86.110.212.247:3333/birthday'

json={
     'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
     'birthday' : '07.08.1996'  # string wich contains date in format DD.MM.YYYY
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/birthday'

json={
    'id' : 1234567890
}

Response if success:
<Response [200]>
{
    'birthday': '1996-08-07'  # date string in format YYYY-MM-DD cause SQL saves date field like this
}
```

**REASON OF FINDING A PAIR**

POST:
```
url='http://86.110.212.247:3333/reason'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'reason' : 'Серьезные отношения'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/reason'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'reason' : 'Серьезные отношения'
}
```

**MATCH ID**

POST:
```
url='http://86.110.212.247:3333/match/id'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'match_id' : 0987654321  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/match/id'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'id' : 0987654321  # TelegramID (or id) . Must be int number or string.isdigit() == True
}
```

## SUBSCRIPTION

**Payment url**

POST:
```
url='http://86.110.212.247:3333/payment/url'

json = {
    'id' : 877505237,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'url' : 'test'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/payment/url'

json = {
    'id' : 877505237  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'url' : 'test.url'  # string
}
```

**Begin date**

POST:
```
url='http://86.110.212.247:3333/subscription/begin'

json={
     'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
     'date' : '07.12.2022'  # string wich contains date in format DD.MM.YYYY
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/subscription/begin'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'date': '2022-12-07'  # date string in format YYYY-MM-DD cause SQL saves date field like this
}
```

**End date**

POST:
```
url='http://86.110.212.247:3333/subscription/end'

json={
     'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
     'date' : '07.01.2023'  # string wich contains date in format DD.MM.YYYY
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/subscription/end'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'date': '2023-01-07'  # date string in format YYYY-MM-DD cause SQL saves date field like this
}
```