from slugify import slugify


class Plant:
    def __init__(self, name, color, nactual,
                 cotamax,
                 vert,
                 cons,
                 mwactual,
                 genactual,
                 agente,
                 contrato):
        self.name = name
        self.color = color
        self.nactual = nactual
        self.cotamax = cotamax
        self.vert = vert
        self.cons = cons
        self.mwactual = mwactual
        self.genactual = genactual
        self.agent = agente
        self.contract = contrato
        self.slug = slugify(name)
