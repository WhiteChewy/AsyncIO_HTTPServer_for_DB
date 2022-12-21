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

### Example of requests

#### Status, Initiation of Tables and creating new user
Status
```
POST or GET:
url = http://86.110.212.247:3333/status

Answer if server is up:
{"status": "server is up"}
```
Initiation of tables in database
```
POST or GET:
url = http://86.110.212.247:3333/ini

Answer if success:
{"status": "success"}
```

Creating new user
```
```

#### Profile
Name:
```
POST:
url = http://86.110.212.247:3333
```