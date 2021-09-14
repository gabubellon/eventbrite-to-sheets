import toml
from loguru import logger

import eventbrite
import google_sheets


def main():
    logger.info("Starting get attends from event")
    attends = eventbrite.get_event_attendees()
    attendes_array = []

    key_array = load_keys()
    for items in attends[:2]:
        attendes_array.append(
            [
                dict_nested_get(items, keys)
                for keys in [item.split(":") for item in key_array]
            ]
        )
    google_sheets.write_on_sheets(attendes_array)
    logger.info("All Attendes imported")


def load_keys():
    return toml.load("./eventbrite_fields.toml").get("attends")


def dict_nested_get(dic, keys):
    for key in keys:
        dic = dic.get(key)
    return dic


if __name__ == "__main__":
    main()
