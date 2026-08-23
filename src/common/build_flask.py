from flask import Flask,jsonify, render_template, request, redirect, url_for, send_file
from flask import Request
from src.common.constants import  HTTP_STATUS_MESSAGES, GET, POST, DELETE
import os

directory = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(directory, os.listdir(directory))
directory = os.path.join(directory, 'src', 'frontend')
print(directory, os.listdir(directory))
app = Flask(__name__,static_folder=directory + '\\static', template_folder=directory + '\\templates')