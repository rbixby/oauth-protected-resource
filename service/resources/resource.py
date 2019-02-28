from flask import current_app
from flask_restful import Resource
# from werkzeug.exceptions import BadRequest
# from service import logger


class ProtectedResource(Resource):

    def get_access_token(self, req, resp):
        # check the auth header first
        auth = req.headers['authorization']
        redis = current_app.config.get('redis', None)

        the_token = None

        # Look in Authorization header first
        # Will look in the other places later.
        if auth and auth.lower().startswith('bearer'):
            the_token = auth.split()[1]

        if redis is not None:
            if redis.sismember("AuthToken", the_token):
                req.access_token = the_token

    def post(self):
        # req = request.get_json()
        # logger.info('Received POST.')
        # token
        # req.
        pass
