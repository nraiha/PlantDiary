from flask import Response, request, url_for
from flask_restful import Resource
from .. import db
from sqlalchemy.exc import IntegrityError
import json


class PlantItem(Resource):
    def get(self):
        pass

    def post(self):
        pass


class PlantCollection(Resource):
    def get(self):
        pass

    def post(self):
        pass
