from app import create_app, db
from sqlalchemy import inspect
app = create_app()

with app.app_context():
    db.create_all()
    print("Base de datos creada correctamente.")
    inspector = inspect(db.engine)
    print(inspector.get_table_names())
