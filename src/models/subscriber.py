from datetime import datetime
from src import db


class Subscriber(db.Model):
    __tablename__ = 'subscribers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    total_cats = db.Column(db.Integer, nullable=False)
    cat_knowledge_level = db.Column(db.Integer, nullable=False)
    puppy_subscribed = db.Column(db.Boolean, nullable=False)
    br_state = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'total_cats': self.total_cats,
            'cat_knowledge_level': self.cat_knowledge_level,
            'puppy_subscribed': self.puppy_subscribed,
            'br_state': self.br_state,
            'created_at': self.created_at
        }
