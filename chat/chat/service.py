# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0  

from concurrent.futures import ThreadPoolExecutor

import os
import redis
import sys
import json
import uuid

from flask import make_response, jsonify, request
from chat import app, get_redis_client

def make_json_from_redis(objs):
  lst = [] 
  for obj in objs:
    lst.append(obj)
  return json.dumps(lst)

def get_all_messages(session_id):
    r = get_redis_client()
    idx = r.llen(session_id)
    if idx == 0:
        return 'empty list'
    log = r.lrange(session_id, 0, idx-1)
    if not log:
        return 'empty list'
    return make_json_from_redis(log)

@app.route('/start_session/<session_id>')
def start_session(session_id):
    r = get_redis_client()
    r.set('chat_live_session',session_id)
    return make_response(jsonify(session_id),200)

@app.route('/get_active_session')
def get_active_session():
    r = get_redis_client()
    return make_response(jsonify(r.get('chat_live_session')),200)

@app.route('/clear_session')
def clear_session():
    r = get_redis_client()
    sesh_name = r.get('chat_live_session')
    r.delete(sesh_name)
    return make_response('OK',200)

@app.route('/get_messages/<session_id>')
def get_messages(session_id):
    res = make_response(get_all_messages(session_id),200)
    return res

@app.route('/send_message/<session_id>', methods=['POST'])
def send_message(session_id):
    r = get_redis_client()
    m = instant_message.from_json(request.get_data(True))
    r.rpush(session_id,m.to_json())
    res = make_response(get_all_messages(session_id),200)
    return res 

class instant_message: 
    def __init__ (self, user_id, msg_txt):
        self.user_id = user_id
        self.msg_txt = msg_txt
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
