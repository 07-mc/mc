import shutil,os,json
mc_path = input("mc>>>")
out = input("output>>>")
os.mkdir(out)
os.mkdir(out + "\\music")
os.mkdir(out + "\\record")
os.mkdir(out + "\\audio")
json_file = mc_path + "\\assets\\indexes\\" + os.listdir(mc_path + "\\assets\\indexes")[0]
o = open(json_file)
file_dict = json.load(o)
o.close()
dict = {"music":[],"record":[],"audio":[]}
id = 1
for key in file_dict["objects"]:
    if key.endswith(".ogg"):
        if key.startswith("minecraft/sounds/music/game/"):
            dict["music"].append([key,file_dict["objects"][key]["hash"],id])
        elif key.startswith("minecraft/sounds/records/"):
            dict["record"].append([key,file_dict["objects"][key]["hash"],id])
        else:
            dict["audio"].append([key,file_dict["objects"][key]["hash"],id])
        id += 1
o = open(out + "\\files.txt","w")
json.dump(dict,o)
o.close()
for key in dict:
    for file in dict[key]:
        if file[1][ : 2] in os.listdir(mc_path + "\\assets\\objects\\"):
            if file[1] in os.listdir(mc_path + "\\assets\\objects\\" + file[1][ : 2]):
                o1 = open(mc_path + "\\assets\\objects\\" + file[1][ : 2] + "\\" + file[1],"rb")
                o2 = open(out + "\\" + key + "\\#" + str(file[2]) + "-" + file[0].split("/")[-1],"wb")
                o2.write(o1.read())
                o1.close()
                o2.close()
