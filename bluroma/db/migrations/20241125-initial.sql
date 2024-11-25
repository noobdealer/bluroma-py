CREATE TABLE meta (migration_level INTEGER PRIMARY KEY, migration_name TEXT, migration_date DATETIME);
CREATE TABLE user_sessions (session_id TEXT PRIMARY KEY, session_did TEXT, session_handle TEXT, session_display_name TEXT);
INSERT INTO meta VALUES (1, 'initial', '2024-11-25 12:00:00');