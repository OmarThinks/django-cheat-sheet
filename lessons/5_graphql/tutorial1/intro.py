from graphene import ObjectType, String, Schema

class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)




# we can query for our field (with the default argument)
query_string = '{ hello }'
result = schema.execute(query_string)
print("1) ",result)
# 1)  {'data': {'hello': 'Hello stranger!'}}
print("2) ",result.data)
# 2)  {'hello': 'Hello stranger!'}
print("3) ",result.data['hello'])
# 3)  Hello stranger!

# or passing the argument in the query
query_with_argument = '{ hello(name: "GraphQL") }'
result = schema.execute(query_with_argument)
print("4) ",result.data['hello'])
# 4)  Hello GraphQL!

# Testing the goodbye
query_goodbye = '{ goodbye }'
result = schema.execute(query_goodbye)
print("5) ",result.data["goodbye"])
# 5)  See ya!


