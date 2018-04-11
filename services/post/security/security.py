from OpenSSL import SSL

context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_privatekey("./post.key")
#context.use_certificate("./post.crt")


def check_current_user_id(current_user, expected_id):
    pass


def check_if_current_user_is_privileged(current_user):
    #TODO send request on USER service for the check
    pass