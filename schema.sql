CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(500) NOT NULL,
    created_date TIMESTAMP NOT NULL
);

CREATE TABLE calendars (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    cal_description TEXT,
    user_id INT NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    created_date TIMESTAMP NOT NULL
);

CREATE TABLE shared_calendars (
    primary_user INT NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    shared_user INT NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    shared_permissions INT NOT NULL REFERENCES app_permissions (id) ON DELETE CASCADE,
    calendar_id INT NOT NULL REFERENCES calendars (id) ON DELETE CASCADE,
    created_date TIMESTAMP NOT NULL
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    event_description TEXT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    event_location VARCHAR(255),
    alert_time INTERVAL,
    created_date TIMESTAMP NOT NULL,
    calendar_id INT NOT NULL REFERENCES calendars (id) ON DELETE CASCADE,
    user_id INT NOT NULL REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE app_permissions (
    id SERIAL PRIMARY KEY,
    permission_name VARCHAR(50) NOT NULL
);
