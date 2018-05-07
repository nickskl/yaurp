from OpenSSL import SSL

context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_privatekey("./user.key")
#context.use_certificate("./user.crt")