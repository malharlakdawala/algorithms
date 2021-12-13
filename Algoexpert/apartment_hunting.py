from timer import timer


@timer
def appartment_hunting(blocks, reqs):
    store_dict = {}
    store_arr = []
    i = 0

    for block in blocks:
        for req in reqs:
            for block_item in blocks:
                if block_item[req] and req not in store_dict:
                    distance = abs(blocks.index(block_item) - blocks.index(block))
                    store_dict[req] = distance
        print("dictionary: ", store_dict)
        store_arr.append(store_dict)
        store_dict.clear()
    print("array: ", store_arr)


reqs = ["gym", "school", "store"]
blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]

appartment_hunting(blocks, reqs)
