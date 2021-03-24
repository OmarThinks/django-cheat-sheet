# 11) Pagination:


# 1) Setting Default Pagination:
<b>

`settings.py`
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
```
</b>
You can also specify the pagination in the view, like this:
<b>

```python
pagination_class = ...
```
</b>


# 2) Types:





## 2-1) PageNumberPagination:
This pagination style accepts a single number page number in the request query parameters.
<b>

`settings.py`
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
```
Request:
```bash
GET https://api.example.org/accounts/?page=4
```
Response:
```bash
HTTP 200 OK
{
    "count": 1023
    "next": "https://api.example.org/accounts/?page=5",
    "previous": "https://api.example.org/accounts/?page=3",
    "results": [
       …
    ]
}
```
</b>









## 2-2) LimitOffsetPagination:
This pagination style accepts a single number page number in the request query parameters.
<b>

`settings.py`
```python
GET https://api.example.org/accounts/?limit=100&offset=400
```
</b>































