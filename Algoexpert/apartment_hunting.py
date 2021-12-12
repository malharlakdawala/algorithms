from timer import timer


@timer
def appartment_hunting(block, reqs):

    for block in blocks:
        for req in reqs:
            if block[req]:
                pass

#



reqs = ["gym", "school", "store"]
blocks = [
  {
    "gym": false,
    "school": true,
    "store": false
  },
  {
    "gym": true,
    "school": false,
    "store": false
  },
  {
    "gym": true,
    "school": true,
    "store": false
  },
  {
    "gym": false,
    "school": true,
    "store": false
  },
  {
    "gym": false,
    "school": true,
    "store": true
  }
]


#appartment_hunting(blocks,reqs)
