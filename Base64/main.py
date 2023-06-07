import base64

pwd="hello world"

fpwd=base64.b64encode(pwd.encode('utf-8'))
print(fpwd)

dpwd=base64.b64decode(fpwd.decode('utf-8'))
print(pwd)
