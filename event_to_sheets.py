import eventbrite
import google_sheets


def main():
    at = eventbrite.get_event_attendees()
    attendes_array = []

    for items in at[:100]:
        attendes_array.append(
            [
                items.get("order_id"),
                items.get("profile").get("name"),
                items.get("profile").get("email"),
            ]
        )
    google_sheets.write_on_sheets(attendes_array)


if __name__ == "__main__":
    main()
