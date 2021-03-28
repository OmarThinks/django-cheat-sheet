import graphene

class HelloQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class Query(HelloQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    pass

schema = graphene.Schema(query=Query)