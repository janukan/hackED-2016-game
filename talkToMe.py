import requests
import uuid
from gfycat.client import GfycatClient
client = GfycatClient()
 
parameters = {"grant_type":"client_credentials","client_id":"2_bZfbte","client_secret":"EuSECvztvjiAxkCFNj3Mfqd5Gl0NGiVyXtET0S7N-12fY8fr4jdmMLxqyfK3gT8J"}
response = requests.get("https://api.gfycat.com/v1/oauth/token",params = parameters)
print(response)

r2 = requests.post("https://api.gfycat.com/v1/gfycats",params={"title":"hereiameh"})
key = "aeuoi12324135"
print(r2.json())

form = [('key', key),('acl', 'private'),('AWSAccessKeyId', 'AKIAIT4VU4B7G2LQYKZQ'),('success_action_status', 200),('signature', 'mk9t/U/wRN4/uU01mXfeTe2Kcoc='),('Content-Type', 'image/gif'),('policy',"eyAiZXhwaXJhdGlvbiI6ICIyMDIwLTEyLTAxVDEyOjAwOjAwLjAwMFoiLAogICAgICAgICAgICAiY29uZGl0aW9ucyI6IFsKICAgICAgICAgICAgeyJidWNrZXQiOiAiZ2lmYWZmZSJ9LAogICAgICAgICAgICBbInN0YXJ0cy13aXRoIiwgIiRrZXkiLCAiIl0sCiAgICAgICAgICAgIHsiYWNsIjogInByaXZhdGUifSwKCSAgICB7InN1Y2Nlc3NfYWN0aW9uX3N0YXR1cyI6ICIyMDAifSwKICAgICAgICAgICAgWyJzdGFydHMtd2l0aCIsICIkQ29udGVudC1UeXBlIiwgIiJdLAogICAgICAgICAgICBbImNvbnRlbnQtbGVuZ3RoLXJhbmdlIiwgMCwgNTI0Mjg4MDAwXQogICAgICAgICAgICBdCiAgICAgICAgICB9")]
data = form
files = {'file': open("image195.png", 'rb')}
r = requests.post("https://gifaffe.s3.amazonaws.com/", data=data, files=files)
print(r.json())
