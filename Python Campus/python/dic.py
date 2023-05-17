dic = {"first_name" : "Mariah" , "last_name" : "Carey", "birth_date" : "27.03.1970", "hobbies" : ["Sing", "Compose", "Act"]}
option = input("Enter option:")
if option == '1' :
	print(dic["last_name"])
if option == '2' :
	print(dic["birth_date"])
if option == '3' :
	print(len(dic["hobbies"]))	
if option == '4' :
	print(dic["hobbies"][-1])
if option == '5' :
	dic["hobbies"].append("Cooking")
	print(dic["hobbies"])
if option == '6' :
	day = dic["birth_date"][0:2]
	month = dic["birth_date"][3:5]
	year = dic["birth_date"][6:]
	birth_date_tuple = day, month, year
	print(birth_date_tuple)	
if option == '7' :
	dic["age"] = "50"
	print(dic["age"])
	