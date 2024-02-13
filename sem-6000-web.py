#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, subprocess
from flask import Flask, request, Response, abort
from yattag import Doc


# learn known devices
devices = []
with open(os.path.expanduser("~/.known_sem6"), 'r') as f:
    for line in f.readlines():
        devices.append(line.strip().split(' ')[-1])

actions = [ 'on', 'off', 'toggle', 'status' ]


def run_command(command):
    """ execute the given command, return it's std-out and -err"""
    result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = result.stdout.decode('utf-8'); err = result.stderr.decode('utf-8')
    out = F"{command}{os.linesep}{out}"
    if err != '':
        out = F"{out}{os.linesep}{err}"
    return out


# flask application starts here
app = Flask(__name__)

@app.route('/sem/<path:device>/', methods=["GET", "POST"])
def handle_sem(device):
    """ run this when '/sem/<device>/?action=<action>' was accessed """
    # verfiy parameters
    if device not in devices:
        return abort(404, F"device '{device}' unknown")

    action = request.args.get('action')  # parse GET or POST arguments to identify 'action' parameter
    if request.environ['REQUEST_METHOD'] == 'POST':
        action = request.form['action']

    if action is None:
        action = 'status'

    if action not in actions:
        return abort(404, F"action '{action}' unknown")

    # start assembly of page
    doc, tag, text = Doc().tagtext()
    with tag('title'):
        text(device)

    # if request was anything than 'status' redirect back to status
    if action != 'status':
        doc.asis(F"<meta http-equiv=\"refresh\" content=\"1;{request.environ['PATH_INFO']}\">")

    # add buttons at the top of page
    with tag('form', method='get', action=request.environ['PATH_INFO']):
        with tag('table', border='0', style="text-align:center;"):
            for a in actions:
                with tag('td'):
                    with tag('input', type='submit', name='action', value=a):
                        pass

    # add section with output of command
    with tag('hr'):
        with tag('pre'):
            # assemble and run command
            text(run_command(F"./sem-6000.exp {device} --{action} --print"))
    with tag('hr'):
        pass

    # render and return page
    return Response(doc.getvalue(), mimetype='text/html;charset=UTF-8')


@app.route('/', methods=["GET"])
def handle_root():
    """ run this when '/' was accessed """
    # start assembly of page
    doc, tag, text = Doc().tagtext()
    with tag('h1'):
        text('known SEM-6000 devices')

    for device in devices:
        with tag('h2'):
            with tag('a', href=F"/sem/{device}/"): text(F"Device {device}")

    # render and return page
    return Response(doc.getvalue(), mimetype='text/html;charset=UTF-8')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)

