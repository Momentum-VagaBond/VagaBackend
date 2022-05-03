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
	"password": "password",
	"first_name": "Your-first-name",
	"last_name": "your_last=name",
}
```
Response

> 201 Created
```
{
	"email": "wanderlust@travel.me",
	"username": "nomad",
	"id": 1,
	"first_name": "Fernando",
	"last_name": "de Soto"
}
```

### **log in**
---
Request
> POST /auth-token-login/

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

### **view logged in user's profile**
*be sure that you have a token under 'Bearer' with the prefix, 'Token'*

REQUEST

> GET  /api/auth/me

**No JSON input**

RESPONSE

> 200 OK
```
{
	"id": 2,
	"username": "alex",
	"first_name": "alexFirst",
	"last_name": "Last",
	"avatar": null,
	"bio": "User has yet to fill in their bio",
	"trips": [
		{
			"pk": 2,
			"title": "Party only trip",
			"location": "Paris",
			"begin": "2022-05-11T00:00:00Z",
			"end": "2022-05-12T00:00:00Z",
			"user": "alex",
			"username": "alex",
			"user_first_name": "alexFirst",
			"user_last_name": "Last"
		},
		{
			"pk": 3,
			"title": "Tx",
			"location": "Dallas TX",
			"begin": "2022-05-11T00:00:00Z",
			"end": "2022-05-12T00:00:00Z",
			"user": "alex",
			"username": "alex",
			"user_first_name": "alexFirst",
			"user_last_name": "Last"
		},
		{
			"pk": 4,
			"title": "Knox",
			"location": "Knox TN",
			"begin": "2022-05-11T00:00:00Z",
			"end": "2022-05-12T00:00:00Z",
			"user": "alex",
			"username": "alex",
			"user_first_name": "alexFirst",
			"user_last_name": "Last"
		}
	]
}
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
	"begin":"2022-05-11T00:00:00.000Z",
	"end":"2022-05-19T00:00:00.000Z"
}
```

Response
> 201 Created

```
{
	"pk": 2,
	"title": "I'm going on a Viking adventure!",
	"location": "Iceland",
	"begin": "2022-06-21 00:00:00-00",
	"end": "2022-07-01 00:00:00-00",
	"user": "nomad",
	"username": "nomad",
	"user_first_name": "Willem",
	"user_last_name": "DeFoe"
}
```

### **list of all trips**


### **View a list of logged in user's trips**
---
*be sure that you have a token entered under 'Bearer' with the prefix, 'Token'*

Request

> GET /api/mytrips/

**No JSON input**

Response

> 200 OK

```
[
	{
		"pk": 2,
		"title": "I'm going on a Viking adventure!",
		"location": "Iceland",
		"begin": "2022-05-22T00:00:00Z",
		"end": "2022-05-31T00:00:00Z",
		"user": "emilyflo",
		"username": "emilyflo",
		"user_first_name": "",
		"user_last_name": ""
	},
	{
		"pk": 3,
		"title": "Gonna get some sun on my buns!",
		"location": "Bermuda",
		"begin": "2022-02-15T00:00:00Z",
		"end": "2022-02-29T00:00:00Z",
		"user": "emilyflo",
		"username": "emilyflo",
		"user_first_name": "",
		"user_last_name": ""
	},
	{
		"pk": 4,
		"title": "I want to visit as many coffee shops as possible",
		"location": "Seattle",
		"begin": "2022-06-03T00:00:00Z",
		"end": "2022-06-09T00:00:00Z",
		"user": "emilyflo",
		"username": "emilyflo",
		"user_first_name": "",
		"user_last_name": ""
	},
	{
		"pk": 5,
		"title": "Born to be wild",
		"location": "Juno, Alaska",
		"begin": "2022-07-16T00:00:00Z",
		"end": "2022-07-24T00:00:00Z",
		"user": "emilyflo",
		"username": "emilyflo",
		"user_first_name": "",
		"user_last_name": ""
	}
]
```

### **log a travel entry**
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

### **view one trip of one user and that trip's respective logs**
---
*no authentication required*

Request
> GET /api/trips/**trip-pk/

JSON
```
-----
```

Response
> 200 OK
```
{
	"pk": 1,
	"title": "I need some ME time",
	"location": "Banff, Alberta, Canada",
	"begin": "2022-05-22T00:00:00Z",
	"end": "2022-05-29T00:00:00Z",
	"user": "emilyflo",
	"username": "emilyflo",
	"user_first_name": "Emily",
	"user_last_name": "Starr",
	"trip_logs": [
		{
			"pk": 1,
			"user": "emilyflo",
			"location": "location 1 Canada trip",
			"latitude": 23.0,
			"longitude": 32432.0,
			"details": "this is the details section of Canada trip, log 1",
			"start": false
		},
		{
			"pk": 2,
			"user": "emilyflo",
			"location": "location 2",
			"latitude": 342.0,
			"longitude": 23423.0,
			"details": "details for location 2, canada trip, emily",
			"start": false
		},
		{
			"pk": 9,
			"user": "emilyflo",
			"location": "Pittsburgh Airport",
			"latitude": 264.45,
			"longitude": 353.35,
			"details": "I'm getting antsy to get on this plane!",
			"start": false
		}
	]
}
```

### **add comment to log entry**

Request

> POST

JSON

Response

```
```

### **add comment to log entry**

Request

> POST

JSON

Response

```
```
