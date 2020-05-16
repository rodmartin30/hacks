require 'oauth2'

callback = ""
app_id = ""

secret = ""
client = OAuth2::Client.new(app_id, secret, site: "libcurl.so/oauth/authorize")
client.auth_code.authorize_url(redirect_uri: callback)


code=ARGV[0]
access = client.auth_code.get_token( code, redirect_uri: callback)
access.get("/api/user").parsed

puts access.token 
