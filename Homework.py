"""This program prints a letter to a friend who they think the likely presidential candidate is."""

tuple1 = ('Hildegard','Hilary Clinton','Hilary Clinton','Brunhilda')
tuple2 = ('Cheech','Donald Trump','Donald Trump','Chong')
List = [tuple1,tuple2]
print (List)
print (('Dear %s ,\nI would like you to vote for %s because I think %s \n is best for this country \n Sincerely,\n %s') % ('Hildegard','Hilary Clinton','Hilary Clinton','Brunhilda'))
print (('Dear %s ,\nI would like you to vote for %s because I think %s \n is best for this country \n Sincerely,\n %s') % (tuple2))
