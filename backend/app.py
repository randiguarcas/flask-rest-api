from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from controller.bridge_controller import TypeGenerationController, PlantsController, PlantsGeneratorsController

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

api.add_resource(TypeGenerationController, '/api/generation-types')
api.add_resource(PlantsController, '/api/plants')
api.add_resource(PlantsGeneratorsController, '/api/plants/<name>/generation-types')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5200)