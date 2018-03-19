from OpenSSL import SSL

context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey("./post.key")
#context.use_certificate("./post.crt")