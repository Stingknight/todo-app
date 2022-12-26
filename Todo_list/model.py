from Todo_list import db
from datetime import datetime

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(200),nullable=True)
    datetime_data=db.Column(db.DateTime,default=datetime.utcnow)