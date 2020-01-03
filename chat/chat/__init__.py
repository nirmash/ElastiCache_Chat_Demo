# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0  

import redis
import os
from flask import Flask, Markup, request, render_template

app = Flask(__name__)

hostname = os.getenv('REDIS_MASTER_HOST') # Change this value
port = os.getenv('REDIS_MASTER_PORT') # Default Redis port

def get_redis_client():
    return redis.Redis(host=hostname, port=port, db=0, decode_responses=True)

import chat.service

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')
