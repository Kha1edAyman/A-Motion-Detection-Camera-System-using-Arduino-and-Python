name = "Khaled"
age = 21
has_android_phone = "No"
print(name, age, has_android_phone)

person = dict(
    dict_name = name, 
    dict_age = age,
    dict_has_android_phone = has_android_phone ,
)
print(f"hello {person["dict_name"]} your age is : {person["dict_age"]} and you don't has android phone" )