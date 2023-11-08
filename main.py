import subprocess
import json 

subprocess.run(["aws", "--version"])
response = subprocess.run(["aws", "iam", "list-users"], capture_output= True)
print(response)
print(type(response))
print(dir(response))
print(response.stdout)

my_json = response.stdout.decode('utf8')
json_data = json.loads(my_json)
print(json_data)