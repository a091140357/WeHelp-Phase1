import csv, urllib.request, json

url_ch = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
url_en = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

with urllib.request.urlopen(url_ch) as web:
    hotel_ch = json.load(web)

with urllib.request.urlopen(url_en) as web:
    hotel_en = json.load(web)


num = 0
district_list = {}
district_rooms_list = {}

hotels_csv = []
districts_csv = []

for num in range(len(hotel_ch["list"])):
    hotel_id = hotel_ch["list"][num]["_id"]
    hotel_name_ch = hotel_ch["list"][num]["旅宿名稱"]
    hotel_address_ch = hotel_ch["list"][num]["地址"]
    hotel_phone = hotel_ch["list"][num]["電話或手機號碼"]
    hotel_rooms = hotel_ch["list"][num]["房間數"]

    #找到地址中 市、區 並加1 在提取該範圍字串出來
    district = hotel_address_ch[(hotel_address_ch.find("市") + 1):(hotel_address_ch.find("區") + 1)]

    if district in district_list:
        district_list[district] = district_list[district] + 1
        district_rooms_list[district] = district_rooms_list[district] + int(hotel_rooms)

    if district not in district_list:
        district_list[district] = 1
        district_rooms_list[district] = int(hotel_rooms)

    num_en = 0

    for num_en in range(len(hotel_en["list"])):
        if hotel_en["list"][num_en]["_id"] == hotel_id:
            hotel_name_en = hotel_en["list"][num_en]["hotel name"]
            hotel_address_en = hotel_en["list"][num_en]["address"]
            break
        num_en += 1
        
    hotels_csv.append([hotel_name_ch, hotel_name_en, hotel_address_ch, hotel_address_en, hotel_phone, hotel_rooms])

district_list_key = district_list.keys()
district_output = ""
for i in district_list_key:
    district_output = (f"{district_output}\n{i},{district_list[i]},{district_rooms_list[i]}")
    districts_csv.append([i, district_list[i], district_rooms_list[i]])

with open("hotels.csv", "w", newline = "", encoding = "utf-8")as f:
    writer = csv.writer(f)
    writer.writerows(hotels_csv)

with open("districts.csv", "w", newline = "", encoding = "utf-8")as f:
    writer = csv.writer(f)
    writer.writerows(districts_csv)