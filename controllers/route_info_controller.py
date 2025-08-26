from flask import Blueprint, jsonify

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def available_routes():
    """
    Returns a list of routes available in the API in JSON format.
    """

    routes = {
        "routes": {
            "/attempts/": ["POST", "GET"],
            "/attempts/<int:attempt_id>": ["GET"],
            "/attempts/all/": ["GET"],
            "/attempts/admin/remove/<int:attempt_id>/": ["DELETE"],
            "/register": ["POST"],
            "/delete": ["DELETE"],
            "/login": ["POST"],
            "/logout": ["GET"],
            "/climbs/": ["GET", "POST"],
            "/climbs/batch/": ["POST"],
            "/climbs/<int:climb_id>/": ["DELETE", "PATCH", "PUT"],
            "/companies/": ["GET", "POST"],
            "/companies/<int:company_id>": ["GET", "DELETE"],
            "/companies/<int:company_id>/": ["PATCH", "PUT"],
            "/gyms/": ["GET", "POST"],
            "/gyms/<int:gym_id>/": ["GET", "DELETE", "PATCH", "PUT"],
            "/gym-ratings/": ["GET", "POST"],
            "/gym-ratings/<int:rating_id>/": ["GET", "DELETE", "PATCH", "PUT"],
            "/gym-ratings/by-gym/<int:gym_id>/": ["GET"],
            "/gym-ratings/by-user/<int:user_id>/": ["GET"],
            "/gym-ratings/all/": ["GET"],
            "/gym-ratings/admin/<int:gym_rating_id>/": ["DELETE"],
            "/learn/skills/": ["GET", "POST"],
            "/learn/styles/": ["GET", "POST"],
            "/learn/about-api/": ["GET"],
            "/learn/skills/<int:skill_level_id>/": ["DELETE", "PATCH", "PUT"],
            "/learn/styles/<int:style_id>/": ["DELETE", "PATCH", "PUT"],
            "/users/": ["GET", "POST"],
            "/users/<int:user_id>/": ["DELETE"],
            "/users/profile/": ["GET"],
            "/users/admin/<int:user_id>/grant/": ["PATCH"],
            "/users/admin/<int:user_id>/revoke/": ["PATCH"],
            "/users/update-profile/": ["PATCH", "PUT"],
            "/": ["GET"]
            }
        }

    return jsonify(routes)