"""
User Model
Purpose: Make interactions with users in the database easier
Usage:
...
"""
class User:
    def __init__(self, id, username, email, password_hash, created_date):
        self._id = id
        self._username = username
        self._email = email
        self._password_hash = password_hash
        self._created_date = created_date

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        self._id = new_id
        # update db id

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        self._username = new_username
        # update db username

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        self._email = new_email
        # update db email

    @property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, new_hash):
        self._password_hash = new_hash
        # update db password_hash

    @property
    def created_date(self):
        return self._created_date
    
    @created_date.setter
    def created_date(self, new_created_date):
        self._created_date = new_created_date

    @staticmethod
    def create_user():
        ...

    @staticmethod
    def get_user_by_id():
        ...

    @staticmethod
    def get_user_by_username():
        ...

    @staticmethod
    def get_user_by_email():
        ...

    @staticmethod
    def delete_user_by_id():
        ...

    @staticmethod
    def delete_user_by_username():
        ...

    @staticmethod
    def delete_user_by_email():
        ...


"""
Calendar Model
Purpose: Make interactions with calendars in the database easier
Usage:
...
"""
class Calendar:
    def __init__(self, id, title, description, user_id, created_date):
        self._id = id
        self._title = title
        self._description = description
        self._user_id = user_id
        self._created_date = created_date

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        self._id = new_id
        # update db id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        self._title = new_title
        # update db title

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, new_description):
        self._description = new_description
        # update db email

    @property
    def user_id(self):
        return self._password_hash
    
    @user_id.setter
    def user_id(self, new_user_id):
        self._user_id = new_user_id
        # update db password_hash

    @property
    def created_date(self):
        return self._created_date
    
    @created_date.setter
    def created_date(self, new_created_date):
        self._created_date = new_created_date

    @staticmethod
    def create_calendar():
        ...

    @staticmethod
    def get_calendar_by_id():
        ...

    @staticmethod
    def get_calendars_by_title():
        ...

    @staticmethod
    def get_calendars_by_user():
        ...

    @staticmethod
    def delete_calendar_by_id():
        ...


"""
Shared Calendar Model
Purpose: Make interactions with shared calendars in the database easier
Usage:
...
"""
class SharedCalendar:
    def __init__(self, id, primary_user, shared_user, shared_permissions, calendar_id, created_date):
        self._id = id
        self._primary_user = primary_user
        self._shared_user = shared_user
        self._shared_permissions = shared_permissions
        self._calendar_id = calendar_id
        self._created_date = created_date

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        self._id = new_id
        # update db id

    @property
    def primary_user(self):
        return self._primary_user
    
    @primary_user.setter
    def title(self, new_primary_user):
        self._primary_user = new_primary_user
        # update db title

    @property
    def shared_user(self):
        return self._shared_user
    
    @shared_user.setter
    def description(self, new_shared_user):
        self._shared_user = new_shared_user
        # update db email

    @property
    def shared_permissions(self):
        return self._shared_permissions
    
    @shared_permissions.setter
    def shared_permissions(self, new_permissions):
        self._shared_permissions = new_permissions
        # update db password_hash

    @property
    def calendar_id(self):
        return self._calendar_id
    
    @calendar_id.setter
    def calendar_id(self, new_calendar_id):
        self._calendar_id = new_calendar_id

    @property
    def created_date(self):
        return self._created_date
    
    @created_date.setter
    def created_date(self, new_created_date):
        self._created_date = new_created_date

    @staticmethod
    def share_calendar():
        ...

    @staticmethod
    def get_shared_with_calendars_by_user():
        ...

    @staticmethod
    def get_shared_by_calendars_by_user():
        ...

    @staticmethod
    def unshare_calendar():
        ...


"""
Event Model
Purpose: Make interactions with events in the database easier
Usage:
...
"""
class Event:
    def __init__(self, id, title, description, start_time, end_time, event_location, alert_time, created_date, calendar_id, user_id):
        self._id = id
        self._title = title
        self._description = description
        self._start_time = start_time
        self._end_time = end_time
        self._event_location = event_location
        self._alert_time = alert_time
        self._created_date = created_date
        self._calendar_id = calendar_id
        self._user_id = user_id

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        self._id = new_id
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        self._title = new_title
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, new_description):
        self._description = new_description
    
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, new_start_time):
        self._start_time = new_start_time
    
    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, new_end_time):
        self._end_time = new_end_time
    
    @property
    def event_location(self):
        return self._event_location
    
    @event_location.setter
    def event_location(self, new_event_location):
        self._event_location = new_event_location
    
    @property
    def alert_time(self):
        return self._alert_time
    
    @alert_time.setter
    def alert_time(self, new_alert_time):
        self._alert_time = new_alert_time
    
    @property
    def created_date(self):
        return self._created_date
    
    @created_date.setter
    def created_date(self, new_created_date):
        self._created_date = new_created_date
    
    @property
    def calendar_id(self):
        return self._calendar_id
    
    @calendar_id.setter
    def calendar_id(self, new_calendar_id):
        self._calendar_id = new_calendar_id
    
    @property
    def user_id(self):
        return self._user_id
    
    @staticmethod
    def create_event():
        ...
    
    @staticmethod
    def get_event_by_id():
        ...

    @staticmethod
    def get_events_by_title():
        ...

    @staticmethod
    def get_events_by_user():
        ...

    @staticmethod
    def get_events_by_calendar():
        ...

    @staticmethod
    def delete_event_by_id():
        ...


"""
App Permissions Model
Purpose: Make interactions with events in the database easier
Usage:
...
"""
class AppPermissions:
    def __init__(self, id, permission_name):
        self._id = id
        self._permission_name = permission_name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def permission_name(self):
        return self._permission_name
    
    @permission_name.setter
    def permission_name(self, new_permission_name):
        self._permission_name = new_permission_name

    @staticmethod
    def create_permission():
        ...

    @staticmethod
    def get_permission_name_by_id():
        ...

    @staticmethod
    def delete_permission():
        ...