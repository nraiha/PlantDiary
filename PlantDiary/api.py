from flask import Blueprint
from flask_restful import Api

from .resources.plant_general import PlantGeneralCollection, PlantGeneral
from .resources.plant_item import PlantItem, PlantCollection
from .resources.diary import DiaryEntry, DiaryCollection

api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)

api.add_resource(PlantGeneralCollection, "/plantsgeneral/")
api.add_resource(PlantGeneral, "/plantsgeneral/<plant_id>/")
api.add_resource(PlantCollection, "/plants/")
api.add_resource(PlantItem, "/plant/<plant_name>/")
api.add_resource(DiaryCollection, "/plantdiary/")
api.add_resource(DiaryEntry, "/plantdiary/<entry_id>")


