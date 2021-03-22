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






























































































