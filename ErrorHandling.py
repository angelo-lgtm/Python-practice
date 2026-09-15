import json, time

def fetch_user_profile(json_string):
		try:
				print("Parsing users...")
				data = json.loads(json_string)
		except json.JSONDecodeError:
				print("Invalid JSON received")
		else:
				#Runs only if the try block succeeds
				print("Users parsed successfully!")
				print(f"User's name: {data.get('name')}")
		finally:
				print("Cleaning up connections with the systems...")
				time.sleep(3) #Takes time in seconds
				print("Done")
				
fetch_user_profile('{"name": "Assencio","age": 30}')
fetch_user_profile('{"name": "Robert", "age":}')
				