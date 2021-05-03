from app.database.models.section import SectionModel
from typing import List


class SectionDAO:
    @staticmethod
    def create_section(title: str) -> "SectionModel":
        """
        Create new section if the params fields are valid and section is not created before.
        :param title: "section title",
        :return:
        """
        section = SectionModel(title=title)
        section.save_to_db()
        return section

    @staticmethod
    def find_section_by_id(id: int) -> "SectionModel":
        """
        Find section that has the given id (if any).
        :param id: id of the section
        :return: SectionModel object (or None)
        """
        return SectionModel.query.get(id)

    @staticmethod
    def find_section_by_title(title: str) -> "SectionModel":
        """
        Find section that has the given title (if any).
        :param title: title of the section
        :return: SectionModel object (or None)
        """
        return SectionModel.query.filter_by(title=title).first()

    @staticmethod
    def find_sections_by_category(category_id: int) -> List["SectionModel"]:
        """
        Find sections for the given category.
        :param category_id: id of the category
        :return: List of SectionModel objects (or None)
        """
        return SectionModel.query.filter(SectionModel.category.contains(category_id))

    @staticmethod
    def find_sections_by_ids(ids: List[int]) -> List["SectionModel"]:
        """
        Search sections by list of ids
        :param ids: list of ids
        :return: List of SectionModel object which ids are provided
        """
        return SectionModel.query.filter(SectionModel.id.in_(ids))

    @staticmethod
    def find_all_sections():
        return SectionModel.query.all()

    @staticmethod
    def update_section(section, **kwargs):
        return section.update(**kwargs)

    @staticmethod
    def delete_section_by_id(id: int) -> bool:
        """
        Deletes section by id (if id is valid)
        :param id: id of the section
        :return:
        """
        section = SectionDAO.find_section_by_id(id)
        if not section:
            return False
        SectionDAO.delete_section(section)
        return True

    @staticmethod
    def delete_section(section):
        return section.delete_from_db()
