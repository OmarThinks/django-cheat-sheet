# 2) Requests:



each endpoint will take `request` as a parameter.



## request attributes:



## `request.data`
This contains all the **parsed** data of the request
1. It includes **all parsed data: Files and not files**
2. You can use it to access `POST`, `PUT`, `PATCH` request data
3. Not just form data, also JSON data



## `request.query_params`
**Not for `GET` requst only**, but for all requests.  
You use this to get the quesry parameters of the request.

## `request.parsers`
To be explained later

---
---
---


## `request.user`
- Depends on auth policy
	- Success: Returns a `django.contrib.auth.models.User`
	- Failure: Returns a `django.contrib.auth.models.AnonymousUser`
 


## `request.auth`
- Depends on auth policy
	- Success: depends on auth policy
	- Failure: Returns the default value `None`




---
---
---

## `request.method`
Returns `GET`, `POST` or `PUT` .. ect.

