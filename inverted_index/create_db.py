import json
import re
import os
from lxml import etree

labels = ['game','price','os','processor','ram','graphics','directX','storage', 'description']
def get_atributes_steam(path):
    parser = etree.HTMLParser()
    root = path
    
    XPATH_INFO_TITLE_STEAM = '//div[@class="sysreq_contents"]/div[1]/div[1]/ul/ul/li/strong/text()'
    XPATH_INFO_STEAM = '//div[@class="sysreq_contents"]/div[1]/div[1]/ul/ul/li/text()'
    XPATH_PRICE_STEAM = '//div[@class="discount_final_price"]/text()'
    XPATH_PRICE_STEAM2 = '//div[@class="game_purchase_action"]/div[1]/div[1]/text()'
    XPATH_NAME_STEAM = '//div[@class="apphub_AppName"]/text()'
    XPATH_DESC_STEAM = '//div[@class="game_description_snippet"]/text()'
    data = []

    tree = etree.parse(root, parser)
    RAW_NAME = tree.xpath(XPATH_NAME_STEAM)
    RAW_INFO_TITLE = tree.xpath(XPATH_INFO_TITLE_STEAM)
    RAW_INFO = tree.xpath(XPATH_INFO_STEAM)
    print(RAW_INFO)
    RAW_PRICE = tree.xpath(XPATH_PRICE_STEAM)
    RAW_DESC = tree.xpath(XPATH_DESC_STEAM)
    if(RAW_PRICE == []): RAW_PRICE = tree.xpath(XPATH_PRICE_STEAM2)

    FILTERED_INFO = get_list_info_steam(RAW_NAME, RAW_INFO_TITLE, RAW_INFO, RAW_PRICE, RAW_DESC)
    
    data.append(dict(zip(labels,FILTERED_INFO)))
        
    return data[0]

def get_list_info_steam(name, listReq, l, price, desc):
    info = []
    offset = 0
    for i in range(0, len(l)):
        if(i >= len(l)): break
        if(l[i] == ' '): 
            del l[i]
    if(name == []): info.append(None)
    else: info.append(name[0])
    if(price == []): info.append(None)
    else: 
        price = re.sub("[\t\n\r]+",'', price[0])
        price = re.sub("\w+\$", '', price)
        price = re.sub(" ", '', price)
        info.append(price)

    if('Requires a 64-bit processor and operating system' in l): offset = 1
    for j in range(2, len(labels)-1):
        printou = False
        for i in range(0,len(listReq)):
            if (listReq[i].lower() == (labels[j] + ":").lower()):
                if(i + offset >= len(l)): info.append("--")
                else: info.append(l[i + offset].lower())
                printou = True
        if(printou == False): info.append("--")
    if(desc != []): 
        desc = re.sub("[\t\n\r]+", '', desc[0])
        desc = re.sub('[\"]+', '\'', desc)
        desc = re.sub('[,.;]', '', desc)
        info.append(desc.lower())
    else: info.append("--")

    return info

def get_atributes_uplay(path):
    parser = etree.HTMLParser()
    root = path

    data_uplay = []

    XPATH_INFO_TITLE_UP = '//article[@class="minimum"]/ul/li/font/text()'
    XPATH_INFO_UP = '//article[@class="minimum"]/ul/li/text()'
    XPATH_PRICE_UP = '//span[@class="price-sales"]/text()'
    XPATH_NAME_UP = '//h1[@class="update-product-name"]/text()'

    tree = etree.parse(root, parser)
    RAW_NAME = tree.xpath(XPATH_NAME_UP)

    RAW_INFO_TITLE = tree.xpath(XPATH_INFO_TITLE_UP)
    RAW_INFO = tree.xpath(XPATH_INFO_UP)
    RAW_PRICE = tree.xpath(XPATH_PRICE_UP)
        
    FILTERED_INFO = get_list_info_uplay(RAW_NAME, RAW_INFO_TITLE, RAW_INFO, RAW_PRICE)
    data_uplay.append(dict(zip(labels,FILTERED_INFO)))
        
    return data_uplay[0]

def get_list_info_itch(name, listReq, price):
    info = []
    
    if(name == []): info.append(None)
    else: info.append(name[0])
    if(price == []): info.append("Free")
    else: info.append(price[0])
    
    for j in range(2, len(labels)):
        printou = False
        for i in range(0,len(listReq)):
            if(listReq == 'Recommended:' or listReq == 'Additional Notes:'): break
            
            express = re.search('(\w+\:)', listReq[i])
            if(express != None): 
                express = express.group(0)

            if (express.lower() == (labels[j] + ":").lower()):
                info.append(express.lower())
                printou = True
            
        if(printou == False): info.append("--")

    return info

def get_list_info_uplay(name, listReq, l, price):
    info = []
    offset = 0
    if(name == None): info.append(None)
    else:
        name = re.sub('[\"]+', '\'', name[0])
        name = re.sub('[,.;]', '', name)
        info.append(name.lower())

    if(price == None): info.append(None)
    else: info.append(price[0])
    if('Requires a 64-bit processor and operating system' in l): offset = 1
    for j in range(2, len(labels)):
        printou = False
        search = labels[j]
        if(search == "Storage"): search = "disk space"
        for i in range(0,len(listReq)):
            if (listReq[i].lower() == (labels[j] + ":").lower()):
                if(i + offset >= len(l)): info.append("--")
                #else: info.append(l[i + offset].lower())
                else: 
                    ins = l[i + offset].lower()
                    ins = re.sub('[,.;]', '', ins)
                    info.append(ins)
                printou = True
                print(listReq[i], labels[j])
        if(printou == False): info.append("--")
    print(info)
    return info

def get_atributes_itch(path):
    parser = etree.HTMLParser()
    root = path

    data_itch = []

    XPATH_INFO_ITCH = '//div[@id="left_col column"]/div[1]/ul/li/text()'
    XPATH_PRICE_ITCH = '//span[@class="buy_message"]/span[1]/text()'
    XPATH_NAME_ITCH = '//title/text()'

    tree = etree.parse(root, parser)
    RAW_NAME = tree.xpath(XPATH_NAME_ITCH)
    RAW_INFO = tree.xpath(XPATH_INFO_ITCH)
    RAW_PRICE = tree.xpath(XPATH_PRICE_ITCH)

    FILTERED_INFO = get_list_info_itch(RAW_NAME, RAW_INFO, RAW_PRICE)

    data_itch.append(dict(zip(labels,FILTERED_INFO)))
    
    return data_itch[0]

def save_files(filename, attrs, index):
    filename = filename.replace('.html', '')
    print(filename)
    with open('db/' + str(index), 'w', encoding='utf-8') as fp:
        json_text = json.dumps(attrs, ensure_ascii=False).encode('utf-8')
        fp.write(str(json_text)[2:])


def get_attrs_steam(file_path, index):
    file_attr = get_atributes_steam(file_path)
    save_files(filename, file_attr, index)

def get_attrs_uplay(file_path, index):
    file_attr = get_atributes_uplay(file_path)
    save_files(filename, file_attr, index)

def get_attrs_itch(file_path, index):
    file_attr = get_atributes_itch(file_path)
    save_files(filename, file_attr, index)

if __name__ == '__main__':
    pages_path = os.path.abspath('../pages')
    pages_path = pages_path + '/'
    index = 1
    for filename in os.listdir(pages_path):
        file_path = pages_path+filename
        # Search in steam pages
        if 'steam' in filename:
            print(filename)
            get_attrs_steam(file_path, index)
            index += 1
        if 'itch' in filename:
            print(filename)
            get_attrs_itch(file_path, index)
            index += 1
        if 'uplay' in filename:
            print(filename)
            get_attrs_uplay(file_path, index)
            index += 1