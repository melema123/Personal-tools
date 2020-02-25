import untangle

xmlobj = untangle.parse('ascii87.xml')
isodata = "0210F23000002E800400000000000400000006111111002000000000000100022400000000009611515137XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1200000000000100000076ABCDE0010402001646C0000000819000000000C00000008190013111111111111"
bitmap = isodata[4:32]
result = ""
availablefields=""
bcd = "1"+str(bin(int(bitmap, 16)))[2:]
print("===============================================================================================")
print("If the results are not correct, correct ascii87.xml to reflect message format.\
    \nCheck the available fields below (Ignore field 0) and correct others") 
print("================================================================================================")

for i, x in enumerate(bcd):
    if x == "1":
        availablefields += " " + str(i)
        for child in xmlobj.fieldformater.isofield:
            if str(i) == child["id"]:
                if child["size"] == "0":
                    result += "\n" + child["id"] + " = " + isodata[0:int(child["length"])]
                    isodata = isodata[int(child["length"]):]
                else:
                    strlen = int(isodata[0:int(child["size"])]) + int(child["size"])
                    result += "\n" + child["id"] + " = " + isodata[int(child["size"]):strlen]
                    isodata = isodata[strlen:]

print("Available fields: ", availablefields) # Prints available fields
print("===============================================================================================")

print(result) # Prints formated iso data
print("===============================================================================================")

