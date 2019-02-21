from service.resources.resource import ProtectedResource

RESOURCES = [
    ('/resource', ProtectedResource)
]


def add_resources(api):
    for route, resource in RESOURCES:
        api.add_resource(resource, route)
