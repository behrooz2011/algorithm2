""" ["hi", "guys"] ==> ["hi", "guys"] """
def encode(arr):
    res = ""
    for x in arr:
        helper = ""
        helper = "5#" + x
        res += helper
    print(res.split("5#")[1:])
    return res
print(encode(["hello", "world"]))