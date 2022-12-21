# -*- coding: utf-8 -*-
from aiohttp import web
import json
import requests
import asyncpg
import datetime
from db_config import DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME

#
async def set_match(request: requests.Request) -> web.Response:
    r'''
    Set match status for user in DB.
    json in request must be:
    { 
        'status': True/False (or 'True'/'False'),
        'id' : int number or string with isdigit() == True
    }
    '''
    try:
        match_status = await request.json()
        if type(match_status['status']) == str: 
                if match_status['status'].lower() == 'false': match_status['status'] = False
                else: match_status['status'] = True
        if type(match_status['id']) == str and match_status['id'].isdigit():
            match_status['id'] = int(match_status['id'])
        
        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET match_flag=$1 WHERE user_id=$2', match_status['status'], match_status['id'])
        await connection.close()

        response_obj = { 'status' : 'success' }
        return web.Response(text=json.dumps(response_obj), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_match_id(request: requests.Request) -> web.Response:
    r'''
    Get match id from database
    json in request must be:
    {
        'id' : int number or string with isdigit() == True
    }
    '''
    try:
        request_dict = await request.json()
        user_id = request_dict['id']
        if type(user_id) == str and user_id.isdigit():
            user_id = int(user_id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT match_id FROM users WHERE user_id=$1', user_id)
        await connection.close()
        
        response_obj = { 
            'status' : 'success',
            'id' : row['match_id'] 
            }
        return web.Response(text=json.dumps(response_obj), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_name(request: requests.Request) -> web.Response:
    r'''
    Get name from database
    json in request must be:
    {
        'id' : int number or string with str.isdigit() == True
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT name FROM users WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = { 
            'status' : 'success',
            'name' : row['name']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_city(request: requests.Request) -> web.Response:
    r"""
    Get city from database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT city FROM users WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = { 
            'status' : 'success',
            'city' : row['city']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_gender(request: requests.Request) -> web.Response:
    r"""
    Get gender from database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT gender FROM users WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = { 
            'status' : 'success',
            'gender' : row['gender']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_birthday(request: requests.Request) -> web.Response:
    r"""
    Get birthday from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT birthday FROM users WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = { 
            'status' : 'success',
            'birthday' : str(row['birthday'])  # need this cause json can't serialize date type object
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_reason(request: requests.Request) -> web.Response:
    r"""
    Get reason from database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT reason FROM users WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = { 
            'status' : 'success',
            'reason' : row['reason']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_profile_photo_id(request: requests.Request) -> web.Response:
    r"""
    Get profile photo id from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT profile_photo_id FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = { 
            'status' : 'success',
            'photo_id' : row['profile_photo_id']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_subscribtion_end_date(request: requests.Request) -> web.Response:
    r"""
    Get end date of subscribtion from database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT end_date FROM subscribtion WHERE user_id=$1', id)
        await connection.close()
        
        end_date = row['end_date']

        response_obj = {
            'date' : end_date
        }
        
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)


async def get_subscribtion_begin_date(request: requests.Request) -> web.Response:
    r"""
    Get begin date of subscribtion from database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT begin_date FROM subscribtion WHERE user_id=$1', id)
        await connection.close()
        
        begin_date = row['begin_date']

        response_obj = {
            'date' : begin_date
        }
        
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_pause_status(request: requests.Request) -> web.Response:
    r"""
    Get pause status from database as bool object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT matching_pause FROM tags WHERE user_id=$1', id)
        await connection.close()
                
        response_obj = { 
            'status' : 'success',
            'paused' : row['matching_pause']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_reason_to_stop_communication(request: requests.Request) -> web.Response:
    r"""
    Get users reason to stop communication from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT reason_to_stop_communication FROM unmatching WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = { 
            'status' : 'success',
            'reason_to_stop' : row['reason_to_stop_communication']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_meeting_status(request: requests.Request) -> web.Response:
    r"""
    Get status of meeting from database as bool object
    it shows was there meeting between user and match
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT was_meeting FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'was_meeting' : row['was_meeting']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_meeting_reaction(request: requests.Request) -> web.Response:
    r"""
    Get meeting reaction from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT meeting_reaction FROM unmatching WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'meeting_reaction' : row['meeting_reaction']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_reason_why_meeting_bad(request: requests.Request) -> web.Response:
    r"""
    Get reason why meeting was bad from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT why_meeting_bad FROM unmatching WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'why_bad' : row['why_meeting_bad']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_payment_url(request: requests.Request) -> web.Response:
    r"""
    Get payment url from database as str object
    it shows was there meeting between user and match
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT payment_url FROM subscribtion WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'url' : row['payment_url']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_waiting_payment_status(request: requests.Request) -> web.Response:
    r"""
    Get status of user waiting confirm payment url from database as bool object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT waiting_payment FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'is_waiting' : row['waiting_payment']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_matching_status(request: requests.Request) -> web.Response:
    r"""
    Get status of finding match for user from database as bool object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT match_flag FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'has_match' : row['match_flag']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_help_status(request: requests.Request) -> web.Response:
    r"""
    Get status of user waiting help from moderation from database as bool object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT waiting_help FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'is_waiting_help' : row['waiting_help']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_first_time_status(request: requests.Request) -> web.Response:
    r"""
    Get status of first time user using service from database as bool object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT first_time FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'is_first_time' : row['first_time']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_complain_status(request: requests.Request) -> web.Response:
    r"""
    Get status of user complaining to communication from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT communication_complain FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'is_complain' : row['communication_complain']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_fisrt_side_photo_id(request: requests.Request) -> web.Response:
    r"""
    Get first side photo id from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT first_side_photo_id FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'photo_id' : row['first_side_photo_id']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_second_side_photo_id(request: requests.Request) -> web.Response:
    r"""
    Get second side photo id from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT second_side_photo_id FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'photo_id' : row['second_side_photo_id']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_third_side_photo_id(request: requests.Request) -> web.Response:
    r"""
    Get second side photo id from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT third_side_photo_id FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'photo_id' : row['third_side_photo_id']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_moderation_status(request: requests.Request) -> web.Response:
    r"""
    Get moderation status from database as bool object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT moderated FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'moderated' : row['moderated']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_first_time_moderated_status(request: requests.Request) -> web.Response:
    r"""
    Get status of first time moderated tag from database as bool object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT first_time_moderated FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'is_first_time' : row['first_time_moderated']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_photo_moderation_status(request: requests.Request) -> web.Response:
    r"""
    Get status photo moderation from database as str object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT photo_moderated FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'photo_ok' : row['photo_moderated']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_info_moderation_status(request: requests.Request) -> web.Response:
    r"""
    Get status of checking info from database like bool object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT info_moderated FROM users WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'info_ok' : row['info_moderated']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_alogorithm_steps(request: requests.Request) -> web.Response:
    r"""
    Get algorithm steps from database like int object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT algorithm_steps FROM algorithm WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'step' : row['algorithm_steps']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_likes(request: requests.Request) -> web.Response:
    r"""
    Get number of likes from database like int object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT likes FROM algorithm WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'likes' : row['likes']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_super_likes(request: requests.Request) -> web.Response:
    r"""
    Get number of superlikes from database like int object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT superlikes FROM algorithm WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'superlikes' : row['superlikes']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_profile_photo_b64(request: requests.Request) -> web.Response:
    r"""
    Get profile photo base64 data from database like bytes string object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT b64_profile FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'b64' : row['b64_profile']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_first_side_photo_b64(request: requests.Request) -> web.Response:
    r"""
    Get first side photo base64 data from database like bytes string object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT b64_first_side FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'b64' : row['b64_first_side']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_second_side_photo_b64(request: requests.Request) -> web.Response:
    r"""
    Get second side photo base64 data from database like bytes string object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT b64_second_side FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'b64' : row['b64_second_side']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_third_side_photo_b64(request: requests.Request) -> web.Response:
    r"""
    Get third side photo base64 data from database like bytes string object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT b64_third_side FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'b64' : row['b64_third_side']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_first_ex_photo_b64(request: requests.Request) -> web.Response:
    r"""
    Get first ex girlfriend/boyfriend photo base64 data from database like bytes string object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT b64_first_ex_photo FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'b64' : row['b64_first_ex_photo']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_second_ex_photo_b64(request: requests.Request) -> web.Response:
    r"""
    Get second ex girlfriend/boyfriend photo base64 data from database like bytes string object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT b64_second_ex_photo FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'b64' : row['b64_second_ex_photo']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_third_ex_photo_b64(request: requests.Request) -> web.Response:
    r"""
    Get third ex girlfriend/boyfriend photo base64 data from database like bytes string object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT b64_third_ex_photo FROM photos WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'b64' : row['b64_third_ex_photo']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def get_error_status(request: requests.Request) -> web.Response:
    r"""
    Get error status for checking mediagroups from database like bytes string object
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    """
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        row = await connection.fetchrow('SELECT error_flag FROM tags WHERE user_id=$1', id)
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            'error_status' : row['error_flag']
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def table_initiation() -> web.Response:
    r"""
    Tables initiation
    """
    try:
        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('''
CREATE TABLE IF NOT EXISTS users(
				user_id bigint PRIMARY KEY,
                name text,
                city text,
                gender text,
                birthday date,
                reason text,
                match_id bigint
				);
	
CREATE TABLE IF NOT EXISTS photos(
				id SERIAL PRIMARY KEY,
				user_id bigint UNIQUE,
				profile_photo_id text,
				b64_profile text,
				first_side_photo_id text,
				b64_first_side text,
                second_side_photo_id text,
				b64_second_side text,
                third_side_photo_id text,
                b64_third_side text,
                b64_first_ex_photo text,
                b64_second_ex_photo text,
                b64_third_ex_photo text,
				FOREIGN KEY (user_id) REFERENCES users (user_id) 
				ON DELETE CASCADE 
				ON UPDATE CASCADE
				);

CREATE TABLE IF NOT EXISTS algorithm(
				id SERIAL PRIMARY KEY,
				user_id bigint UNIQUE,
				algorithm_steps int,
                likes int,
                superlikes int,
				FOREIGN KEY (user_id) REFERENCES users (user_id) 
				ON DELETE CASCADE
				ON UPDATE CASCADE
				);

CREATE TABLE IF NOT EXISTS subscribtion(
				id SERIAL PRIMARY KEY,
				user_id bigint UNIQUE,
				payment_url text,
				begin_date date,
				end_date date,
				FOREIGN KEY (user_id) REFERENCES users (user_id) 
				ON DELETE CASCADE
				ON UPDATE CASCADE
				);

CREATE TABLE IF NOT EXISTS tags(
				id SERIAL PRIMARY KEY,
				user_id bigint UNIQUE,
				matching_pause bool,
				was_meeting bool,
				waiting_payment bool,
				waiting_help bool,
				first_time bool,
				communication_complain bool,
				moderated bool,
				first_time_moderated bool,
				photo_moderated bool,
				info_moderated bool,
				error_flag bool,
				match_flag bool,
				FOREIGN KEY (user_id) REFERENCES users (user_id) 
				ON DELETE CASCADE
				ON UPDATE CASCADE
				);

CREATE TABLE IF NOT EXISTS unmatching(
				id SERIAL PRIMARY KEY,
				user_id bigint UNIQUE,
				reason_to_stop_communication text,
				meeting_reaction text,
				why_meeting_bad text,
				FOREIGN KEY (user_id) REFERENCES users (user_id)  
				ON DELETE CASCADE
				ON UPDATE CASCADE
				);
        ''')
        await connection.close()
        
        response_obj = {
            'status' : 'success',
            }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def create_new_user(request: requests.Request) -> web.Response:
    r'''
    creating new user in database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        
        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('''
        INSERT INTO users(user_id, name, city,
                        gender, birthday, reason,
                        match_id)
                        VALUES ($1, $2, $3,
                        $4, $5, $6,
                        $7) ON CONFLICT (user_id) DO NOTHING;
        ''', # users
            #1  2   3
            id, '', '',
            # 4   5   6
            '', None, '',
            #7
            0)
        
        await connection.execute('''
        INSERT INTO subscribtion(user_id, payment_url, begin_date,
                                end_date)
                                VALUES ($1, $2, $3,
                                $4) ON CONFLICT (user_id) DO NOTHING;
        ''',#8  9    10
            id, '', None,
            #11
            None)
        
        await connection.execute('''
        INSERT INTO photos(user_id, profile_photo_id, b64_profile,
                            first_side_photo_id, b64_first_side, second_side_photo_id,
                            b64_second_side, third_side_photo_id, b64_third_side,
                            b64_first_ex_photo, b64_second_ex_photo, b64_third_ex_photo)
                            VALUES ($1, $2, $3,
                                    $4, $5, $6,
                                    $7, $8, $9,
                                    $10, $11, $12
                                    ) ON CONFLICT (user_id) DO NOTHING;
        ''',# 1  2   3
             id, '', '',
            # 4   5   6
             '', '', '',
            # 7   8   9
             '', '', '',
            # 10 11  12
             '', '', '')
        
        await connection.execute('''
        INSERT INTO tags(user_id, matching_pause, was_meeting,
                        waiting_payment, waiting_help, first_time,
                        communication_complain, moderated, first_time_moderated,
                        photo_moderated, info_moderated, error_flag,
                        match_flag) VALUES ($1, $2, $3,
                                            $4, $5, $6,
                                            $7, $8, $9,
                                            $10, $11, $12,
                                            $13) ON CONFLICT (user_id) DO NOTHING;
        ''',# 1    2      3
             id, False, False,
            # 4      5     6
            False, False, True,
            # 7      8      9
            False, False, False,
            # 10    11     12
            False, False, False,
            # 13
            False)
        
        await connection.execute('''
        INSERT INTO unmatching(user_id, reason_to_stop_communication, meeting_reaction,
                            why_meeting_bad) VALUES ($1, $2, $3,
                                                    $4) ON CONFLICT (user_id) DO NOTHING;
        ''',# 1   2    3
              id, '', '',
            # 4
              '')

        await connection.execute('''
        INSERT INTO algorithm(user_id, algorithm_steps, likes,
                             superlikes) VALUES ($1, $2, $3,
                                                $4) ON CONFLICT (user_id) DO NOTHING;

         ''',# 1  2   3
              id, 30, 7,
            # 4
              5)
    
        await connection.close()
        
        response_obj = {
            'status' : 'success',
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_name(request: requests.Request) -> web.Response:
    r'''
    Post request to set name of user to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'name' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        name = request_dict['name']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE users SET name=$1 WHERE user_id=$2', name, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_city(request: requests.Request) -> web.Response:
    r'''
    Post request to set city of user to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'city' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        city = request_dict['city']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE users SET city=$1 WHERE user_id=$2', city, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_gender(request: requests.Request) -> web.Response:
    r'''
    Post request to set gender of user to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'gender' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        gender = request_dict['gender']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE users SET gender=$1 WHERE user_id=$2', gender, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_birthday(request: requests.Request) -> web.Response:
    r'''
    Post request to set gender of user to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'birthday' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        birthday = request_dict['birthday']
        birthday = datetime.datetime.strptime(birthday, "%d.%m.%Y").date()

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE users SET birthday=$1 WHERE user_id=$2', birthday, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_reason(request: requests.Request) ->web.Response:
    r'''
    Post request to set reason of finding match of user to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'reason' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        reason = request_dict['reason']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE users SET reason=$1 WHERE user_id=$2', reason, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_profile_photo_id(request: requests.Request) -> web.Response:
    r'''
    Post request to set profile photo id to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'photo_id' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_id = request_dict['photo_id']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET profile_photo_id=$1 WHERE user_id=$2', photo_id, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_subscribtion_begin_date(request: requests.Request) -> web.Response:
    r'''
    Post request to set begin of subscribtion date in data base
    json in request must be like
    {
        'id' : int number or string where str.isdigit() == True
        'date' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        date = request_dict['date']
        date = datetime.datetime.strptime(date, "%d.%m.%Y").date()

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE subscribtion SET begin_date=$1 WHERE user_id=$2', date, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)

    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_subscribtion_end_date(request: requests.Request) -> web.Response:
    r'''
    Post request to set end of subscribtion date in data base
    json in request must be like
    {
        'id' : int number or string where str.isdigit() == True
        'date' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        date = request_dict['date']
        date = datetime.datetime.strptime(date, "%d.%m.%Y").date()
        
        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE subscribtion SET end_date=$1 WHERE user_id=$2', date, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)

    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_matching_pause_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set matching pause status to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'pause' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        pause = request_dict['pause']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET matching_pause=$1 WHERE user_id=$2', pause, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_reason_to_stop_communication(request: requests.Request) -> web.Response:
    r'''
    Post request to set reason to stop communicating to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'reason' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        reason = request_dict['reason']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE unmatching SET reason_to_stop_communication=$1 WHERE user_id=$2', reason, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_meeting_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set status is there was meeting to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET was_meeting=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_meeting_reaction(request: requests.Request) -> web.Response:
    r'''
    Post request to set meeting reaction to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'reaction' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        reaction = request_dict['reaction']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE unmatching SET meeting_reaction=$1 WHERE user_id=$2', reaction, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_reason_why_meeting_bad(request: requests.Request) -> web.Response:
    r'''
    Post request to set reason why meeting was bad to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'reason' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        reason = request_dict['reason']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE unmatching SET why_meeting_bad=$1 WHERE user_id=$2', reason, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_payment_url(request: requests.Request) -> web.Response:
    r'''
    Post request to set payment url to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'url' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        url = request_dict['url']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE subscribtion SET payment_url=$1 WHERE user_id=$2', url, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_waiting_payment_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set waiting payment status to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET waiting_payment=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_waiting_for_help_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set status of waiting for help to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET waiting_help=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_first_time_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set first time status to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET first_time=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_complain_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set communication complain to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET communication_complain=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_match_id(request: requests.Request) -> web.Response:
    r'''
    Post request to set match id to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'match_id' : int number or string where str.isdigit() == True
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        match_id = request_dict['match_id']
        if type(match_id) == str and match_id.isdigit():
            match_id = int(match_id)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE users SET match_id=$1 WHERE user_id=$2', match_id, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_first_side_photo_id(request: requests.Request) -> web.Response:
    r'''
    Post request to set first side photo id to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'photo_id' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_id = request_dict['photo_id']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET first_side_photo_id=$1 WHERE user_id=$2', photo_id, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_second_side_photo_id(request: requests.Request) -> web.Response:
    r'''
    Post request to set second side photo id to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'photo_id' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_id = request_dict['photo_id']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET second_side_photo_id=$1 WHERE user_id=$2', photo_id, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_third_side_photo_id(request: requests.Request) -> web.Response:
    r'''
    Post request to set third side photo id to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'photo_id' : string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_id = request_dict['photo_id']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET third_side_photo_id=$1 WHERE user_id=$2', photo_id, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_moderated_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set status of moderation to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET moderated=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_first_time_moderated_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set first time moderated profile to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET first_time_moderated=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_photo_moderation_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set does photo of profile pass moderation to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET photo_moderated=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_info_moderation_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set info moderation status to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET info_moderated=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_alogorithm_steps(request: requests.Request) -> web.Response:
    r'''
    Post request to set algorithm steps number to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'steps' : int number or string where str.isdigit() == True
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        steps = request_dict['steps']
        if type(steps) == str and steps.isdigit():
            steps = int(steps)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE algorithm SET algorithm_steps=$1 WHERE user_id=$2', steps, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_likes(request: requests.Request) -> web.Response:
    r'''
    Post request to set likes number to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'likes' : int number or string where str.isdigit() == True
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        likes = request_dict['likes']
        if type(likes) == str and likes.isdigit():
            likes = int(likes)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE algorithm SET likes=$1 WHERE user_id=$2', likes, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_superlikes(request: requests.Request) -> web.Response:
    r'''
    Post request to set superlikes number to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'superlikes' : int number or string where str.isdigit() == True
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        superlikes = request_dict['superlikes']
        if type(superlikes) == str and superlikes.isdigit():
            superlikes = int(superlikes)

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE algorithm SET superlikes=$1 WHERE user_id=$2', superlikes, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_profile_photo_b64(request: requests.Request) -> web.Response:
    r'''
    Post request to set photo in base64 format to database
    b64_string must be bytes converted to string.
    For example:
    import base64
    str = 'test'
    string_b64 = base64.b64encode(str)

    superlikes = str(string_b64)  # target string becourse postgresql dont know bytes type

    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'b64' : bytes string converted to string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_b64 = request_dict['b64']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET b64_profile=$1 WHERE user_id=$2', photo_b64, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_first_side_photo_b64(request: requests.Request) -> web.Response:
    r'''
    Post request to set first side photo in base64 format to database
    b64_string must be bytes converted to string.
    For example:
    import base64
    str = 'test'
    string_b64 = base64.b64encode(str)

    superlikes = str(string_b64)  # target string becourse postgresql dont know bytes type

    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'b64' : bytes string converted to string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_b64 = request_dict['b64']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET b64_first_side=$1 WHERE user_id=$2', photo_b64, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_second_side_photo_b64(request: requests.Request) -> web.Response:
    r'''
    Post request to set second side photo in base64 format to database
    b64_string must be bytes converted to string.
    For example:
    import base64
    str = 'test'
    string_b64 = base64.b64encode(str)

    superlikes = str(string_b64)  # target string becourse postgresql dont know bytes type

    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'b64' : bytes string converted to string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_b64 = request_dict['b64']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET b64_second_side=$1 WHERE user_id=$2', photo_b64, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_third_side_photo_b64(request: requests.Request) -> web.Response:
    r'''
    Post request to set third side photo in base64 format to database
    b64_string must be bytes converted to string.
    For example:
    import base64
    str = 'test'
    string_b64 = base64.b64encode(str)

    superlikes = str(string_b64)  # target string becourse postgresql dont know bytes type

    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'b64' : bytes string converted to string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_b64 = request_dict['b64']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE users SET b64_3rd=$1 WHERE user_id=$2', photo_b64, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_first_ex_photo_b64(request: requests.Request) -> web.Response:
    r'''
    Post request to set first photo for correction of NN in base64 format to database
    b64_string must be bytes converted to string.
    For example:
    import base64
    str = 'test'
    string_b64 = base64.b64encode(str)

    superlikes = str(string_b64)  # target string becourse postgresql dont know bytes type

    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'b64' : bytes string converted to string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_b64 = request_dict['b64']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET b64_first_ex_photo=$1 WHERE user_id=$2', photo_b64, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_second_ex_photo_b64(request: requests.Request) -> web.Response:
    r'''
    Post request to set photo in base64 format to database
    b64_string must be bytes converted to string.
    For example:
    import base64
    str = 'test'
    string_b64 = base64.b64encode(str)

    superlikes = str(string_b64)  # target string becourse postgresql dont know bytes type

    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'b64' : bytes string converted to string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_b64 = request_dict['b64']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET b64_second_ex_photo=$1 WHERE user_id=$2', photo_b64, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_third_ex_photo_b64(request: requests.Request) -> web.Response:
    r'''
    Post request to set photo in base64 format to database
    b64_string must be bytes converted to string.
    For example:
    import base64
    str = 'test'
    string_b64 = base64.b64encode(str)

    superlikes = str(string_b64)  # target string becourse postgresql dont know bytes type

    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'b64' : bytes string converted to string
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        photo_b64 = request_dict['b64']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE photos SET b64_third_ex_photo=$1 WHERE user_id=$2', photo_b64, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)

#
async def set_error_status(request: requests.Request) -> web.Response:
    r'''
    Post request to set info moderation status to database
    json in request must be:
    {
        'id': int number or string where str.isdigit() == True
        'status' : bool
    }
    '''
    try:
        request_dict = await request.json()
        id = request_dict['id']
        if type(id) == str and id.isdigit():
            id = int(id)
        status = request_dict['status']

        connection = await asyncpg.connect('%s://%s:%s@%s/%s' % (DB, DB_USER, DB_PASSWORD, DB_ADRESS, DB_NAME))
        await connection.execute('UPDATE tags SET error_flag=$1 WHERE user_id=$2', status, id)
        await connection.close()

        response_obj = {
            'status' : 'success'
        }
        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=200)
    
    except KeyError as e:
        response_obj = {
            'status' : 'failed',
            'key' : str(e)
        }

        return web.Response(text=json.dumps(response_obj, ensure_ascii=False), status=400)
    
    except Exception as e:
        response_obj = {
            'status' : 'failed',
            'reason' : str(e)
            }
        
        return web.Response(text=json.dumps(response_obj), status=500)


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/new_user', create_new_user)
    app.router.add_post('/new_user', create_new_user)
    app.router.add_post('/ini', table_initiation)
    app.router.add_get('/ini', table_initiation)
    app.router.add_get('/match/id', get_match_id)
    app.router.add_post('/match/id', set_match_id)
    app.router.add_get('/name', get_name)
    app.router.add_post('/name', set_name)
    app.router.add_get('/city', get_city)
    app.router.add_post('/city', set_city)
    app.router.add_get('/gender', get_gender)
    app.router.add_post('/gender', set_gender)
    app.router.add_get('/birthday', get_birthday)
    app.router.add_post('/birthday', set_birthday)
    app.router.add_get('/reason', get_reason)
    app.router.add_post('/reason', set_reason)
    app.router.add_get('/subscribtion/begin', get_subscribtion_begin_date)
    app.router.add_post('/subscribtion/begin', set_subscribtion_begin_date)
    app.router.add_get('/subscribtion/end', get_subscribtion_end_date)
    app.router.add_post('/subscribtion/end', set_subscribtion_end_date)
    app.router.add_get('/match/paused', get_pause_status)
    app.router.add_post('/match/paused', set_matching_pause_status)
    app.router.add_get('/communication/reason_to_stop', get_reason_to_stop_communication)
    app.router.add_post('/communication/reason_to_stop', set_reason_to_stop_communication)
    app.router.add_get('/meeting/status', get_meeting_status)
    app.router.add_post('/meeting/status', set_meeting_status)
    app.router.add_get('/meeting/reaction', get_meeting_reaction)
    app.router.add_post('/meeting/reaction', set_meeting_reaction)
    app.router.add_get('/meeting/why_bad', get_reason_why_meeting_bad)
    app.router.add_post('/meeting/why_bad', set_reason_why_meeting_bad)
    app.router.add_get('/payment/url', get_payment_url)
    app.router.add_post('/payment/url', set_payment_url)
    app.router.add_get('/payment/waiting', get_waiting_payment_status)
    app.router.add_post('/payment/waiting', set_waiting_payment_status)
    app.router.add_get('/match/status', get_matching_status)
    app.router.add_post('/match/status', set_match)
    app.router.add_get('/help/status', get_help_status)
    app.router.add_post('/help/status', set_waiting_for_help_status)
    app.router.add_get('/first_time', get_first_time_status)
    app.router.add_post('/first_time', set_first_time_status)
    app.router.add_get('/communication/complain/status', get_complain_status)
    app.router.add_post('/communication/complain/status', set_complain_status)
    app.router.add_get('/photo/profile_id', get_profile_photo_id)
    app.router.add_post('/photo/profile_id', set_profile_photo_id)
    app.router.add_get('/photo/side/first_id', get_fisrt_side_photo_id)
    app.router.add_post('/photo/side/first_id', set_first_side_photo_id)
    app.router.add_get('/photo/side/second_id', get_second_side_photo_id)
    app.router.add_post('/photo/side/second_id', set_second_side_photo_id)
    app.router.add_get('/photo/side/third_id', get_third_side_photo_id)
    app.router.add_post('/photo/side/third_id', set_third_side_photo_id)
    app.router.add_get('/photo/profile_b64', get_profile_photo_b64)
    app.router.add_post('/photo/profile_b64', set_profile_photo_b64)
    app.router.add_get('/photo/side/first_b64', get_first_side_photo_b64)
    app.router.add_post('/photo/side/first_b64', set_first_side_photo_b64)
    app.router.add_get('/photo/side/second_b64', get_second_side_photo_b64)
    app.router.add_post('/photo/side/second_b64', set_second_side_photo_b64)
    app.router.add_get('/photo/side/third_b64', get_third_side_photo_b64)
    app.router.add_post('/photo/side/third_b64', set_third_side_photo_b64)
    app.router.add_get('/photo/ex/first_photo_b64', get_first_ex_photo_b64)
    app.router.add_post('/photo/ex/first_photo_b64', set_first_ex_photo_b64)
    app.router.add_get('/photo/ex/second_photo_b64', get_second_ex_photo_b64)
    app.router.add_post('/photo/ex/second_photo_b64', set_second_ex_photo_b64)
    app.router.add_get('/photo/ex/third_photo_b64', get_third_ex_photo_b64)
    app.router.add_post('/photo/ex/third_photo_b64', set_third_ex_photo_b64)
    app.router.add_get('/moderation/status', get_moderation_status)
    app.router.add_post('/moderation/status', set_moderated_status)
    app.router.add_get('/moderation/first_time', get_first_time_moderated_status)
    app.router.add_post('/moderation/first_time', set_first_time_moderated_status)
    app.router.add_get('/moderation/photo_ok', get_photo_moderation_status)
    app.router.add_post('/moderation/photo_ok', set_photo_moderation_status)
    app.router.add_get('/moderation/info_ok', get_info_moderation_status)
    app.router.add_post('/moderation/info_ok', set_info_moderation_status)
    app.router.add_get('/education/steps', get_alogorithm_steps)
    app.router.add_post('/education/steps', set_alogorithm_steps)
    app.router.add_get('/education/likes', get_likes)
    app.router.add_post('/education/likes', set_likes)
    app.router.add_get('/education/superlikes', get_super_likes)
    app.router.add_post('/education/superlikes', set_superlikes)
    app.router.add_get('/error', get_error_status)
    app.router.add_post('/error', set_error_status)

    web.run_app(app, port=3333)
