from domain.HydroPower import HydroPower
from domain.SolarEnergy import SolarEnergy
from domain.BioGas import BioGas
from domain.ThermalEnergy import ThermalEnergy
from domain.WindPower import WindPower

from re import search


def type_generation(params):
    response = dict()
    for item in params:
        if item["name"].find("Hídrica") != -1:
            response["hydropower"] = HydroPower(
                item["name"], item["value"]).__dict__
        if item["name"].find("Térmica") != -1:
            response["thermal"] = ThermalEnergy(
                item["name"], item["value"]).__dict__
        if item["name"].find("Solar") != -1:
            response["solar"] = SolarEnergy(
                item["name"], item["value"]).__dict__
        if item["name"].find("Eólica") != -1:
            response["windpower"] = WindPower(
                item["name"], item["value"]).__dict__
        if item["name"].find("Biogás") != -1:
            response["biogas"] = BioGas(item["name"], item["value"]).__dict__

    return response
