import os
import sqlite3
import time

# Migrations
def check_migration_level(conn: sqlite3.Connection):
    try:
        conn.execute("SELECT migration_level FROM meta")
    except Exception as error:
        print("Error while checking migration level:", error)
        if os.getenv("FORCE_MIGRATIONS"):
            migration_timer = 10
            while migration_timer != 0:
                migration_timer -= 1
                print("WARNING: Forcing migrations has been enabled, will start in", migration_timer, "seconds...")
                time.sleep(1)
            print("Starting migrations...")
            from0to1(conn)
        else:
            print("Migration forcing is disabled, continuing...")

# TODO: Since this is our only migration, we'll just start from here. Fix this soon to scan through the migration folder
def from0to1(conn: sqlite3.Connection):
    print("Migrating from 0 to 1...")
    try:
        qry = open('bluroma/db/migrations/20241125-initial.sql', 'r').read()
        conn.cursor().executescript(qry)
        conn.commit()
    except Exception as error:
        print("Error while upgrading from DB ver 0 to 1:", error)
        exit(1)
    print("Migrated to DB version 1")