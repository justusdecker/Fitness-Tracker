from src.databases.items import Item
from src.databases.data_access import Base, engine
Base.metadata.create_all(engine)
from os import listdir
from yaml import safe_load
ITM_PATH = './src/databases/build/'
for new_item in listdir(ITM_PATH):
    with open(ITM_PATH + new_item, encoding='utf-8') as f:
        data = safe_load(f)
        print(data)
        Item.create(**data)