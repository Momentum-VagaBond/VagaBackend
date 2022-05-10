# **VagaBond**
## *connecting travelers with their folks at home*
---
to run this locally:
- install django

for trip subscribers to use this app, the contact of any trip must user the email that the traveler provided to register/log in.

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
	"user_id": 2,
	"first_name": "Fernando",
	"last_name": "de Soto",
	"username": "nomad",
	"last_login": null,
	"email": "email@wanderlust@travel.me",
	"bio": "User has yet to fill in their bio"
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
	"avatar": null,
	"bio": "User has yet to fill in their bio",
	"trips": [
		{
			"pk": 2,
			"title": "Party only trip",
			"location": "Paris",
			"begin": "2022-05-11T00:00:00Z",
			"end": "2022-05-12T00:00:00Z",
			"subscribers": [
				2
			],
			"user": "2",
			"username": "AJord91",
			"user_first_name": "Alex",
			"user_last_name": "Jordan"
		},
		{
			"pk": 3,
			"title": "Tx",
			"location": "Dallas TX",
			"begin": "2022-05-11T00:00:00Z",
			"end": "2022-05-12T00:00:00Z",
			"subscribers": [
				2
			],
			"user": "2",
			"username": "AJord91",
			"user_first_name": "Alex",
			"user_last_name": "Jordan"
		},
		{
			"pk": 4,
			"title": "Knox",
			"location": "Knox TN",
			"begin": "2022-05-11T00:00:00Z",
			"end": "2022-05-12T00:00:00Z",
			"subscribers": [
				2
			],
			"user": "2",
			"username": "AJord91",
			"user_first_name": "Alex",
			"user_last_name": "Jordan"
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
	"end":"2022-05-19T00:00:00.000Z",
	"subscribers": [*contact-pk*, *contact-pk*]
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
	"subscribers": [
		2,
		3
	]
	"user": "nomad",
	"username": "nomad",
	"user_first_name": "Willem",
	"user_last_name": "DeFoe"
}
```

### **list of all trips**

Request

> GET /api/trips/

** No JSON input**

Response

> 200 OK

```
[
	{
		"pk": 1,
		"title": "Party only trip",
		"location": "Paris",
		"begin": "2022-05-11T00:00:00Z",
		"end": "2022-05-12T00:00:00Z",
		"subscribers": [],
		"user": "River",
		"username": "River",
		"user_first_name": "River",
		"user_last_name": "Woodring-Starr"
	},
	{
		"pk": 2,
		"title": "My Fantastic Getaway",
		"location": "Maui",
		"begin": "2022-05-04T17:48:27Z",
		"end": "2022-05-17T17:48:30Z",
		"subscribers": [
			1
		],
		"user": "River",
		"username": "River",
		"user_first_name": "River",
		"user_last_name": "Woodring-Starr"
	},
	{
		"pk": 5,
		"title": "Getting some sun!",
		"location": "Oahu",
		"begin": "2022-05-08T00:00:00Z",
		"end": "2022-05-12T00:00:00Z",
		"subscribers": [
			2,
			3
		],
		"user": "River",
		"username": "River",
		"user_first_name": "River",
		"user_last_name": "Woodring-Starr"
	},
]
```

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
		"subscribers": [
			2
		],
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
		"subscribers": [
			2
		],
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
		"subscribers": [
			2
		],
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
		"subscribers": [
			2
		],
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
	"title": "Made it!"
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
	"title": "Made it!"
	"location": "Reykjavík City Airport",
	"latitude": 64.1323,
	"longitude": -21.94179,
	"details": "just landed safely! Waiting for the rental car...can't wait to check in to the hotel."
}
```
### **add an image to a log**
---
*be sure that you have a token entered under 'Bearer' with the prefix, 'Token'*

request 
> POST /api/logs/**log-pk**/images/

```
**Binary File**


Select picture to upload
```
```
**Header**

Content-Type           image/png
Content-Disposition    attachment;filename=**name of selected image**
```

Response
>201 Created

```
{
	"picture": "https://momentum-vagabond.s3.amazonaws.com/static/**filename.png**"
}
```

### **comment on a log**
---
*be sure that you have a token entered under 'Bearer' with the prefix, 'Token'*

Request
> POST /api/log/**log_pk**/comment/

JSON

{    
	  
    "comments":"hope the traffic doesnt make you miss the flight!"
}

Response
>201

```
{
	"username": "alex",
	"user_first_name": "alex",
	"user_last_name": "Jordan",
	"comments": "hope the traffic doesnt make you miss the flight!",
	"date_commented": "2022-05-09T00:45:36.678143Z"
}
```

## **view the log detail page from a trip**
---
*be sure that you have a token entered under 'Bearer' with the prefix, 'Token'*

Request
>GET /api/log/**log_pk/

** No JSON input **

response
>200 OK

```
{
	"pk": 1,
	"user": "Niles",
	"title": "Heading out to the beach!"
	"location": "Myrtle Beach, SC",
	"latitude": 32.09,
	"longitude": -32.9,
	"details": "On the road, cant wait to have some sun on these arms.",
	"start": false,
	"log_comments": [
		{
			"user": "AomameTheCat",
			"comments": "DO IT, NILES. COME JOIN ME IN THE SUN.",
			"date_commented": "2022-04-26T15:04:56.118193Z"
		},
		{
			"user": "Niles",
			"comments": "Ill be there soon!",
			"date_commented": "2022-04-27T20:21:21.489310Z"
		}
	]
}

```

### **view one trip of one user and that trip's respective logs**
---
*no authentication required*

Request
> GET /api/trips/**trip-pk/

** No JSON input **

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
	"subscribers": [
		1
	]
	"trip_logs": [
		{
			"pk": 1,
			"user": "emilyflo",
			"title": "All packed up!",
			"location": "Pittsburgh",
			"latitude": 23.0,
			"longitude": 32432.0,
			"details": "Ready to head for the airport!",
			"date_logged": "2022-05-22T01:27:08.491325Z",
			"images": []
		},
		{
			"pk": 2,
			"user": "emilyflo",
			"title": "Stuck in traffic",
			"location": "Somewhere on 376",
			"latitude": 342.0,
			"longitude": 23423.0,
			"details": "rush hour is standing between me and fresh air",
			"date_logged": "2022-05-22T01:27:09:271325Z",
			"images": []
		},
		{
			"pk": 9,
			"user": "emilyflo",
			"title": "Just went through TSA",
			"location": "Pittsburgh Airport",
			"latitude": 264.45,
			"longitude": 353.35,
			"details": "I'm getting antsy to get on this plane!",
			"images": []
		}
	]
}
```


### **add a contact for a user** 

Request

>POST /api/contacts/

JSON

```
{
“first_name”: “Emily”,
“last_name”: “Starr”,
“email”: “emilyflo.starr@gmail.com”
}
```
 Response

 ```
 {
		"user": "River",
		"first_name": "Emily",
		"last_name": "Starr",
		"email": "emilyflo.starr@gmail.com"
	}
```

### **view contacts to a logged in user**

Request

>GET

** No JSON input **

Response
```
{
		"user": "River",
		"first_name": "Emily",
		"last_name": "Starr",
		"email": "emilyflow.starr@gmail.com"
	
	   	"user": "River",
		"first_name": "Alex",
		"last_name": "Jordan",
		"email": "aljord91@gmail.com"
	
	}

```




