from flask_restful import Resource
from domain import HydroPower
from domain.use_cases.type_generation import type_generation
from domain.use_cases.get_plants import get_plants
from domain.use_cases.get_generation_plant import get_generation_plants
from controller.datasource import Datasource


class TypeGenerationController(Resource):
    def get(self):
        data = Datasource.get_data()
        print(data)
        return type_generation(data["pie"])


class PlantsController(Resource):
    def get(self):
        data = Datasource.get_plants()

        return get_plants(data["plant"])

class PlantsGeneratorsController(Resource):
    def get(self, name):
        data = Datasource.get_data()

        return get_generation_plants(data["unit"], name)
