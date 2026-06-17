import time

def verify_token(token):

if not token:
return False

created=int(token.split(".")[0])

return (
time.time()-created
)<3600
