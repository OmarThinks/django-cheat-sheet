import graphene

class HelloQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class MainQuery(HelloQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    # This is the query of the server
    # It inherets from all the queries
    # To form the query that the server will handle
    pass

schema = graphene.Schema(query=MainQuery)
