## To initialize db follow following steps
    from project import app, db
    app.app_context().push()
    db.create_all()