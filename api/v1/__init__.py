#!/usr/bin/python3
"""
API for AirBnB_clone_v3
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import
from api.v1.views import *
