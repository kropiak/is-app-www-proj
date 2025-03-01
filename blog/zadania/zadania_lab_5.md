# Rozwiązania zadań lab 5

## zadanie 2
```python
>>> Topic.objects.filter(name__startswith='S') 
<QuerySet [<Topic: Stary>]>
``` 

## zadanie 3
>>> Topic.objects.all().values('id','name')
<QuerySet [{'id': 2, 'name': 'Inny'}, {'id': 6, 'name': 'O życiu'}, {'id': 7, 'name': 'Różne'}, {'id': 8, 'name': 'Stary'}]>