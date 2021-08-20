import pymongo


class ConnectionMongo:
    def connect_mongo(self):
        client = pymongo.MongoClient(
            host="localhost",
            port=27017,
            # retryWrites=False
        )
        print("aa")
        mydb = client['python15']
        if "python15" == mydb.name:
            print("数据库连接成功")
        else:
            print("数据库未连接成功")

        mycollection = mydb["customer_add"]
        if "customer_add" == mycollection.name:
            print("集合切换成功")
        else:
            print("集合切换失败")

        # 查询
        mydelete = {"customer_id": 1000000001}
        mycollection.delete_one(mydelete)
        if mycollection.find_one(mydelete) is None:
            print("删除成功")


if __name__ == '__main__':
    ConnectionMongo().connect_mongo()
