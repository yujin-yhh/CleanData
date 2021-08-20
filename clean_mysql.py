"""
connect to database
"""

import pymysql.cursors

# Connect to the database
import yaml


class ConnectionMysql:
    def connect_mysql(self):
        # 读取yaml文件获取数据源
        with open("datasorce.yaml") as f:
            # 获取mysql的连接信息
            datasrc = yaml.safe_load(f)

        connection = pymysql.connect(host=datasrc["mysql"]["host"],
                                     port=datasrc["mysql"]["port"],
                                     user=datasrc["mysql"]["username"],
                                     # 因为密码是12345，转换成了数字12345，次数将类型转换为字符串
                                     password=str(datasrc["mysql"]["password"]),
                                     database='python15',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection:
            # with connection.cursor() as cursor:
            #     # Create a new record
            #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
            #
            # # connection is not autocommit by default. So you must commit to save
            # # your changes.
            # connection.commit()

            # with connection.cursor() as cursor:
            #     # Read a single record
            #     sql = f'select * from customer {datasrc["customer_ids"]["id"]}'
            #     cursor.execute(sql)
            #     result = cursor.fetchall()
            #     print(result)

            #  删除操作
            with connection.cursor() as cursor:
                # 如果有多个ID，循环
                print(datasrc["customer_ids"])
                for item in datasrc["customer_ids"]:
                    sql = f'delete from customer where customer_id={item}'
                    print(sql)
                    cursor.execute(sql)
                #  提交
                connection.commit()


if __name__ == '__main__':
    ConnectionMysql().connect_mysql()
