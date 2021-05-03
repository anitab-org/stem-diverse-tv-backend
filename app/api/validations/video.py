from typing import Dict
from datetime import datetime
from app.utils.messages import SECTIONS_NOT_PROVIDED

REQUIRED_FIELDS_MAP = {
    "title": "title",
    "url": "url",
    "preview_url": "preview url",
    "date_published": "date of publishing",
    "source": "source",
    "channel": "channel",
    "duration": "duration",
}


def validate_video_creation_data(data: Dict[str, object]):
    structure_error = _validate_payload_structure(data)
    if structure_error:
        return structure_error
    date_format_error = _validate_date_format(data["date_published"])
    if date_format_error:
        return date_format_error


def validate_video_sections_data(data):
    if "sections" not in data:
        return SECTIONS_NOT_PROVIDED
    sections_list = data["sections"]
    if not all([isinstance(section, int) for section in sections_list]):
        return {"message": "Section id must be an integer."}


def _validate_payload_structure(data: Dict[str, object]):
    for field in REQUIRED_FIELDS_MAP:
        if field not in data:
            return {
                "message": f"{REQUIRED_FIELDS_MAP[field]} field must be provided."
            }, 400


def _validate_date_format(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError as e:
        return {
            "message": "Date format is not valid. Use the following format: ('YYYY-mm-dd')"
        }, 400
