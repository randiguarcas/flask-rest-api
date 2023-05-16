from slugify import slugify
from domain.Plant import Plant


def get_plants(data):
    response = []

    for item in data:
        if "name" in item:
            response.append(
                Plant(item["name"],
                      item["color"],
                      item["nactual"],
                      item["cotamax"],
                      item["vert"],
                      item["cons"],
                      item["mwactual"],
                      item["genactual"],
                      item["agente"],
                      item["contrato"]).__dict__
            )

    return response
