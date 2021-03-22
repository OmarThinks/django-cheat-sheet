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














## 2) Attributes:

### 2-1) `fields` attribute:
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









### 2-2) `exclude` attribute:
<b>

```python
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['users']
```
</b>

All the names of the fielfds in the **`exclude`** will 
not be represented in this serialization.
## Since version 3.3.0, it is mandatory to provide one of the attributes `fields` or `exclude`.


















### 2-3) `read_only_fields` attribute:
<b>

```python
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
        read_only_fields = ['account_name']
```
</b>
These fields can not be modified.
















### 2-4) `extra_kwargs ` attribute:

This option is a dictionary, mapping field names to a dictionary of keyword arguments. For example:



<b>

```python
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
```

</b>











## 3) Overriding Fields:

You can **override default fields** by **explicitly declaring this 
field**.
<b>

```python
class AccountSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    groups = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Account
```
</b>
















## 4) Inspecting a model Sreializer:





<b>

```python
serializer = AccountSerializer()
print(repr(serializer))
```
</b>


<b>
Result:

```python
AccountSerializer():
    id = IntegerField(label='ID', read_only=True)
    name = CharField(allow_blank=True, max_length=100, required=False)
    owner = PrimaryKeyRelatedField(queryset=User.objects.all())
```
</b>



























