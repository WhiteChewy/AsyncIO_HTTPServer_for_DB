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


## PHOTOS

**Profile photo TelegramID of image**

POST:
```
url='http://86.110.212.247:3333/photo/profile_id'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'photo_id' : 'photo tgid'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/profile_id'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'photo_id' : 'photo tgid'  # string
}
```

**Profile photo base64 string**

WARNING JSON don't know bytes format so u need to convert bytes string to string to send it to database. And string to bytes if u need to get it from database.

POST:
```
url='http://86.110.212.247:3333/photo/profile_b64'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'b64' : 'bSTRING'  # string wich starts with b
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/profile_b64'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'b64' : 'bSTRING'  # string wich starts with b
}
```


**First side photo tgID of image**

POST:
```
url='http://86.110.212.247:3333/photo/side/first_id'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'photo_id' : 'photo tgid'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/side/first_id'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'photo_id' : 'photo tgid'  # string
}
```


**First side photo base64 string**

WARNING JSON don't know bytes format so u need to convert bytes string to string to send it to database. And string to bytes if u need to get it from database.

POST:
```
url='http://86.110.212.247:3333/photo/side/first_b64'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'b64' : 'bSTRING'  # string wich starts with b
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/side/first_b64'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'b64' : 'bSTRING'  # string wich starts with b
}
```


**Second side photo tgID of image**

POST:
```
url='http://86.110.212.247:3333/photo/side/second_id'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'photo_id' : 'photo tgid'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/side/second_id'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'photo_id' : 'photo tgid'  # string
}
```


**Second side photo base64 string**

WARNING JSON don't know bytes format so u need to convert bytes string to string to send it to database. And string to bytes if u need to get it from database.

POST:
```
url='http://86.110.212.247:3333/photo/side/second_b64'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'b64' : 'bSTRING'  # string wich starts with b
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/side/second_b64'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'b64' : 'bSTRING'  # string wich starts with b
}
```


**Third side photo tgID of image**

POST:
```
url='http://86.110.212.247:3333/photo/side/third_id'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'photo_id' : 'photo tgid'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/side/third_id'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'photo_id' : 'photo tgid'  # string
}
```


**Third side photo base64 string**

WARNING JSON don't know bytes format so u need to convert bytes string to string to send it to database. And string to bytes if u need to get it from database.

POST:
```
url='http://86.110.212.247:3333/photo/side/third_b64'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'b64' : 'bSTRING'  # string wich starts with b
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/side/third_b64'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'b64' : 'bSTRING'  # string wich starts with b
}
```


**First photo for algorithm base64 string**

WARNING JSON don't know bytes format so u need to convert bytes string to string to send it to database. And string to bytes if u need to get it from database.

POST:
```
url='http://86.110.212.247:3333/photo/ex/first_photo_b64'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'b64' : 'bSTRING'  # string wich starts with b
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/ex/first_photo_b64'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'b64' : 'bSTRING'  # string wich starts with b
}
```


**Second photo for algorithm base64 string**

WARNING JSON don't know bytes format so u need to convert bytes string to string to send it to database. And string to bytes if u need to get it from database.

POST:
```
url='http://86.110.212.247:3333/photo/ex/second_photo_b64'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'b64' : 'bSTRING'  # string wich starts with b
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/ex/second_photo_b64'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'b64' : 'bSTRING'  # string wich starts with b
}
```


**Third photo for algorithm base64 string**

WARNING JSON don't know bytes format so u need to convert bytes string to string to send it to database. And string to bytes if u need to get it from database.

POST:
```
url='http://86.110.212.247:3333/photo/ex/third_photo_b64'

json={
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'b64' : 'bSTRING'  # string wich starts with b
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url='http://86.110.212.247:3333/photo/ex/third_photo_b64'

json={
    'id' : 1234567890  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'b64' : 'bSTRING'  # string wich starts with b
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


## TAGS

Tags - is different flags that used by bot

**Matching pause**

Shows if user stoped finding of match through database

POST:
```
url = http://86.110.212.247:3333/match/paused

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'pause' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/match/paused

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'paused' : True/False  # bool
}
```


**Was Meeting**

Shows if there was meeting between users

POST:
```
url = http://86.110.212.247:3333/meeting/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/meeting/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'was_meeting' : True/False  # bool
}
```

**Waiting Payment**

Shows if user waiting while payment will be confirmed

POST:
```
url = http://86.110.212.247:3333/payment/waiting

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/payment/waiting

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'waiting' : True/False  # bool
}
```


**Waiting help**

Shows if user waiting while moderation help him

POST:
```
url = http://86.110.212.247:3333/help/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'statuse' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/help/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'waiting_help' : True/False  # bool
}
```

**First Time**

Shows if user using service first time

POST:
```
url = http://86.110.212.247:3333/first_time

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/first_time

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'first_time' : True/False  # bool
}
```

**Communication Complain**

Shows if user ask moderation for help while has dialog with his match or complain about it.

POST:
```
url = http://86.110.212.247:3333/communication/complain/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/communication/complain/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'complain' : True/False  # bool
}
```

**Moderated**

Shows if user profile pass moderation.

POST:
```
url = http://86.110.212.247:3333/moderation/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/moderation/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'moderated' : True/False  # bool
}
```

**First time moderated**

Shows if user first time trying to pass moderation

POST:
```
url = http://86.110.212.247:3333/moderation/first_time

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/moderation/first_time

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'first_time' : True/False  # bool
}
```

**Photo moderated**

Shows if user photos pass moderation

POST:
```
url = http://86.110.212.247:3333/moderation/photo_ok

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/moderation/photo_ok

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'photo_ok' : True/False  # bool
}
```

**Info moderated**

Shows if user profile information pass moderation

POST:
```
url = http://86.110.212.247:3333/moderation/info_ok

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/moderation/info_ok

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'info_ok' : True/False  # bool
}
```

**Error flag**

Using by bot to send only one message about trying to upload media group.

POST:
```
url = http://86.110.212.247:3333/error

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/error

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'error' : True/False  # bool
}
```

**Match flag**

Shows if service find a match for user.

POST:
```
url = http://86.110.212.247:3333/match/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'status' : True/False  # bool
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/match/status

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'has_match' : True/False  # bool
}
```


## ALGORITHM

**Alogrithm steps**

Contains how many steps of educating the algorithm left

POST:
```
url = http://86.110.212.247:3333/education/steps

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'steps' : 30  # Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/education/steps

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'step' : 30  # int
}
```

**Likes**

Contains how many likes left

POST:
```
url = http://86.110.212.247:3333/education/likes

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'likes' : 7  # Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/education/likes

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'likes' : 7  # int
}
```

**Superlikes**

Contains how many superlikes left

POST:
```
url = http://86.110.212.247:3333/education/superlikes

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'superlikes' : 5  # Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/education/superlikes

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'superlikes' : 5  # int
}
```

## UNMATCHING

Contains callback info

**Reason to stop communication**

POST:
```
url = http://86.110.212.247:3333/communication/reason_to_stop

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'reason' : 'Не понравилось общение'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/communication/reason_to_stop

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'reason_to_stop' : 'Не понравилось общение'  # int
}
```

**Meeting reaction**

Reaction for meeting

POST:
```
url = http://86.110.212.247:3333/meeting/reaction

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'reaction' : 'Все отлично'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/meeting/reaction

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'reaction' : 'Все отлично'  # int
}
```

**Why meeting was bad**

Contains info about why user don't like meeting.

POST:
```
url = http://86.110.212.247:3333/meeting/why_bad

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
    'reason' : 'Еда была не вкусной'  # string
}

Response if success:
<Response [200]>
{
    'status' : 'success'
}
```

GET:
```
url = http://86.110.212.247:3333/meeting/why_bad

json = {
    'id' : 1234567890,  # TelegramID (or id) . Must be int number or string.isdigit() == True
}

Response if success:
<Response [200]>
{
    'reason' : 'Еда была не вкусной'  # int
}
```