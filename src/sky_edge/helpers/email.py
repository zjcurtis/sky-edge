from sky_edge.api.constituent import (
    CollectionOfEmails,
    Email,
    email_list_constituent_get,
)


def get_duplicate_emails(
    constituent_id: str, include_inactive: bool = False
) -> dict[str, list[Email]] | None:
    email_list_response = email_list_constituent_get(constituent_id)
    if isinstance(email_list_response, CollectionOfEmails):
        duplicate_dictionary = {}
        for email in email_list_response.value:
            if email.address in duplicate_dictionary:
                duplicate_dictionary[email.address].append(email)
            else:
                duplicate_dictionary[email.address] = [email]

        for k, v in duplicate_dictionary.items():
            if len(v) == 1:
                duplicate_dictionary.pop(k)

        return duplicate_dictionary
