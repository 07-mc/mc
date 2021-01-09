try:
    import os,json
    mc_path = input("mc:")
    json_file = mc_path + "\\indexes\\" + os.listdir(mc_path + "\\indexes")[0]
    o = open(json_file)
    file_dict = json.load(o)
    o.close()
    print(file_dict)
except:
    pass
