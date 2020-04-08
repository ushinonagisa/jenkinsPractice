
did = "000080301234567"
if "00008030" in did and "00008030-" not in did:
    print("in")

didList = list(did)
didList
didList.insert(8,"-")
didList
a = "".join(didList)
a
