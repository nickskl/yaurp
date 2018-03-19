from OpenSSL import SSL

context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_privatekey("./post.key")
#context.use_certificate("./post.crt")