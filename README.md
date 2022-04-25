# **VagaBond**
## *connecting travelers with those closest to them from far away*
---
to run this locally:
- install django
---
## **endpoints**

### append the following endpoints to: https://momentum-vagabond.herokuapp.com/
---
### **register a user**
---
Request
> POST /auth/users/

JSON
```
{
    “email”: “email”,
	"username": "username",
	"password": "password"
}
```
Response

> 201 Created
```
{
	"email": "wanderlust@travel.me",
	"username": "nomad",
	"id": 1
}
```

### **log in**
---
Request
> POST /auth/token/login/

JSON
```
{
	"username": "nomad",
	"password": "nunya"
}
```
Response

> 200 OK
```
{
	"auth_token": "f8g0beeswax502notyours9f72m3"
}
```

### **log out**
---
*be sure that you have a token entered under 'Bearer' with the prefix, 'Token'*

Request

> POST /auth/token/logout/


**No JSON input**

Response

> 204 No Content
```
No body returned for response
```

### **start a new trip**
---
*be sure that you have a token entered under 'Bearer' with the prefix, 'Token'*

Request

> POST /api/trips/

```
{
	    "title": "I'm going on a Viking adventure!",
	    "location": "Iceland",
	    "duration": "2 weeks"
}
```

Response
> 201 Created

```
{
	"pk": 2,
	"title": "I'm going on a Viking adventure!",
	"location": "Iceland",
	"duration": "2 weeks",
	"user": "nomad",
	"username": "nomad",
	"user_first_name": "Willem",
	"user_last_name": "DeFoe"
}
```

### View a list of 'my trips'
---
*be sure that you have a token entered under 'Bearer' with the prefix, 'Token'*

Request

> GET /api/users/**user-pk**/mytrips

**No JSON input**

Response

> 200 OK

```
[
	{
		"pk": 2,
		"title": "I'm going on a Viking adventure!",
		"location": "Iceland",
		"duration": "2 weeks",
		"user": "emilyflo",
		"username": "emilyflo",
		"user_first_name": "",
		"user_last_name": ""
	},
	{
		"pk": 3,
		"title": "Gonna get some sun on my buns!",
		"location": "Bermuda",
		"duration": "1 week",
		"user": "emilyflo",
		"username": "emilyflo",
		"user_first_name": "",
		"user_last_name": ""
	},
	{
		"pk": 4,
		"title": "I want to visit as many coffee shops as possible",
		"location": "Seattle",
		"duration": "4 days",
		"user": "emilyflo",
		"username": "emilyflo",
		"user_first_name": "",
		"user_last_name": ""
	},
	{
		"pk": 5,
		"title": "Born to be wild",
		"location": "Juno, Alaska",
		"duration": "1 month",
		"user": "emilyflo",
		"username": "emilyflo",
		"user_first_name": "",
		"user_last_name": ""
	}
]
```

### log a travel entry
---
*be sure that you have a token entered under 'Bearer' with the prefix, 'Token'*

Request
> POST /api/users/**user-pk**/**trip-pk**/log/

JSON
```
{
	"user_id": 2,
	"trip": 2,
	"latitude": "64.13230",
	"longitude": "-21.94179",
	"location": "Reykjavík City Airport",
	"details": "just landed safely! Waiting for the rental car...can't wait to check in to the hotel."
}
```

Response
> 201 Created

```
{
	"pk": 33,
	"user": "emilyflo",
	"trip": 2,
	"location": "Reykjavík City Airport",
	"latitude": 64.1323,
	"longitude": -21.94179,
	"details": "just landed safely! Waiting for the rental car...can't wait to check in to the hotel."
}
```