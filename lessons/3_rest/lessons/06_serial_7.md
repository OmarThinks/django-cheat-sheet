# 6-7) Serializers:

**Fields' Core Arguments**.

## 1) Why?
These argumnents can be used in any field.





## 2) What?



### **`read_only`**:
- **Default**: **`False`**
- Set this to **`True`** to ensure that the field is used when
 serializing a representation, but is not used when creating or
 updating an instance during deserialization.



### **`write_only`**:
- **Default**: **`False`**
- Set this to **`True`** to ensure that the field may be used when
 updating or creating an instance, but is not included when 
 serializing the representation.



### **`required`**:
- **Default**: **`True`**
- Setting this to **`False`** also allows the object attribute 
or dictionary key to be omitted from output when serializing 
the instance. If the key is not present it will simply not be 
included in the output representation.




### **`default`**:






### **`validators`**:
- A list of validator functions.



### **`error_messages`**:
- A dictionary of error codes to error messages.







