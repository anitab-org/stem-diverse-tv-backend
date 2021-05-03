from app.database.sqlalchemy_extension import db
from app.database.models.category_section import category_section


class CategoryModel(db.Model):
    # Specifying table
    __tablename__ = "category"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    # NOTE: won't have much categories (compared to videos), not need index at this point
    title = db.Column(db.Text(), unique=True, nullable=False)
    section = db.relationship(
        "SectionModel",
        secondary=category_section,
        backref=db.backref("category", lazy="dynamic"),
        cascade="all, delete",
        passive_deletes=True,
    )

    def __init__(self, title):
        self.title = title

    @classmethod
    def find_by_title(cls, title: str) -> "CategoryModel":
        return cls.query.filter_by(title=title.capitalize()).first()

    def save_to_db(self) -> None:
        """Add category to database"""
        self._add_and_commit()

    def add_sections(self, sections) -> None:
        """Add category section instance"""
        self.section.extend(sections)
        self._add_and_commit()

    def add_category_section(self, section) -> None:
        self.section.append(section)
        self._add_and_commit()

    def delete_from_db(self) -> None:
        """Deletes category from the database."""
        db.session.delete(self)
        db.session.commit()

    def _add_and_commit(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def json(self):
        return {"id": self.id, "title": self.title}
