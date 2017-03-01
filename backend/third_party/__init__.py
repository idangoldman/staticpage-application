from mailchimp3 import MailChimp

def mailchimp_subscribe( email, username, api_key, list_id ):
    client = MailChimp( username, api_key )

    # TODO: rewrite this crap.
    try:
        payload = {
            'email_address': email,
            'status': 'subscribed'
        }

        client.lists.members.create( list_id, payload )
    except Exception as e:
        # TODO: Check if user exist and return true otherwise false
        return True

    return True
