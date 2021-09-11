from loguru import logger

import eventbrite
import google_sheets


def main():
    logger.info("Starting get attends from event")
    attends = eventbrite.get_event_attendees()
    attendes_array = []

    for items in attends:
        attendes_array.append(
            [
                items.get("order_id"),
                items.get("profile").get("name"),
                items.get("profile").get("email"),
                items.get("ticket_class_name")
            ]
        )
    google_sheets.write_on_sheets(attendes_array)
    logger.info("Starting get attends frok event")

if __name__ == "__main__":
    main()
