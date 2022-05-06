from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True, default=None)

    def to_json(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": True if self.completed_at else False
        }

    def update(self, request_body):
        self.title = request_body["title"]
        self.description = request_body["description"]

    @classmethod
    def create(cls, request_body):
        if "completed_at" not in request_body:
            request_body["completed_at"] = None
        new_task = cls(title=request_body["title"],
                       description=request_body["description"],
                       completed_at=request_body["completed_at"])

        return new_task
