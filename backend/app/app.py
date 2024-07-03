import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required


app = Flask(__name__)
app.config = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app)


"""
USER ROUTES
"""
@app.route('/auth/register', methods=['POST'])
def register():
    ...


@app.route('/auth/login', methods=['POST'])
def login():
    ...


@app.route('/logout', methods=['POST'])
@jwt_required
def logout():
    ...


@app.route('/users/<user_id>', methods=['GET'])
@jwt_required
def get_user(user_id):
    ...


@app.route('/users/<user_id>', methods=['PUT'])
@jwt_required
def update_user(user_id):
    ...


@app.route('/users/<user_id>', methods=['DELETE'])
@jwt_required
def delete_user(user_id):
    ...


"""
CALENDAR ROUTES
"""
@app.route('/calendars', methods=['POST'])
@jwt_required
def create_calendar():
    ...


@app.route('/calendars/<calendar_id>', methods=['GET'])
@jwt_required
def get_calendar(calendar_id):
    ...


@app.route('/calendars/user/<user_id>', methods=['GET'])
@jwt_required
def get_user_calendars(user_id):
    ...


@app.route('calendars/<calendar_id>', methods=['PUT'])
@jwt_required
def update_calendar(calendar_id):
    ...


@app.route('/calendars/<calendar_id>', methods=['DELETE'])
@jwt_required
def delete_calendar(calendar_id):
    ...


"""
SHARED CALENDAR ROUTES
"""
@app.route('/shared-calendars', methods=['POST'])
@jwt_required
def share_calendar():
    ...


@app.route('/shared-calendars/shared-with/<user_id>', methods=['GET'])
@jwt_required
def get_shared_with_calendars(user_id):
    ...


@app.route('/shared-calendars/shared-by/<user_id>', methods=['GET'])
@jwt_required
def get_shared_by_calendars(user_id):
    ...


@app.route('/shared-calendars/<shared_calendar_id', methods=['DELETE'])
@jwt_required
def unshare_calendar(shared_calendar_id):
    ...


"""
EVENT ROUTES
"""
@app.route('/events', methods=['POST'])
@jwt_required
def create_event():
    ...


@app.route('/events/<event_id>', methods=['GET'])
@jwt_required
def get_events(event_id):
    ...


@app.route('/events/calendar/<calendar_id>', methods=['GET'])
@jwt_required
def get_calendar_events(calendar_id):
    ...


@app.route('/events/user/<user_id>', methods=['GET'])
@jwt_required
def get_user_events(user_id):
    ...


@app.route('/events/<event_id>', methods=['PUT'])
@jwt_required
def update_event(event_id):
    ...


@app.route('/events/<event_id>', methods=['DELETE'])
@jwt_required
def delete_event(event_id):
    ...


"""
APP PERMISSIONS ROUTES
"""
@app.route('/permissions', methods=['POST'])
@jwt_required
def create_permission():
    ...


@app.route('/permissions/<permission_id>', methods=['GET'])
@jwt_required
def get_permission_details(permission_id):
    ...


@app.route('/permissions/<permission_id>', methods=['DELETE'])
@jwt_required
def delete_permission(permission_id):
    ...