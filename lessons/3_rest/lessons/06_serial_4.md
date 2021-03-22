# 6-3) Serializers: Part 4:

**ModelSerializer**.





## 1) ModelSerializer:

Looks exactly like the `Serializer` class, except:

1. **automatically generate** a set of **fields** for you, 
based on the model
2. **automatically generate validators** for the serializer, 
such as **`unique_together`** validators
3. **Includes** simple **default implementations** of 
**`.create()`** and **`.update()`**
<b>

```python
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
```
</b>

- By default, all the model fields on the class will be mapped to a corresponding serializer fields























## 2) `fields` attribute:
This attribute lets you tell which fields names of the model 
will you use in this serializer.  
It is a list of strings, each value is a field name.


<b>

```python
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
        # fields = "__all__"
```

</b>
In case of using 

<b>

```python
fields = "__all__"
```

</b>
This means that you have chosen all the fields of this model.


























































































