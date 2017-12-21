from chain import Chain

c = Chain()

c.add("data in the first block")
c.add("data in the second block")

c.add("data in the third block")

c.show()
#c.chain[2].data = 'asdfsdf'
c[2].data = 'asdfsdf'
if c.broken():
    print("Error : chain is broken")
else:
    print("This chain is correct")


