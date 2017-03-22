import pymysql
import config


class MysqlHepler:
    def __init__(self):
        config.devPassward=input("请输入开发环境数据库密码:")
        self.db = pymysql.connect(config.devUrl, config.devUserName, config.devPassward, config.database_name,
                                  charset="utf8")
        self.cursor = self.db.cursor()

    # 查询表整个表
    def get_table_data(self, table_name):
        sql = "select * from " + table_name
        table_data_list = self.cursor.fetchall()
        return table_data_list

    # 根据sql语句查询一个
    def get_one_by_sql(self, sql):
        self.cursor.execute(sql)
        one = self.cursor.fetchone()
        return one

    # 根据sql查询所有
    def get_all_by_sql(self, sql):
        self.cursor.execute(sql)
        all = self.cursor.fetchall()
        return all

    #
    # 更新 例如: update_sql = "update bs_car_series set en_name = '%s' where id = %d" % (en_name, id)
    def update_db(self, sql):
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("成功")
        except:
            print("失败")
            self.db.rollback()

    # 获取数据库中所有的表
    def getTables(self):
        tableList = []  # 列表List
        sql = "show tables"
        self.cursor.execute(sql)
        tls = self.cursor._rows
        for item in tls:
            tableList.append(item[0])  # item 是元祖 tuple 里面只包含一个元素即表名，取第一个
        return tableList

    # 查询数据库中所有表的字段名 返回字典
    def getAllTableColumnName(self):
        tableComlumsDic = {}  # 字典，{'表名称':[..字段列表...]}
        tableList = self.getTables()  # 查询所有表名称,返回列表List
        for item in tableList:
            columnList = []
            sql = "select * from " + item
            self.cursor.execute(sql)
            columnsDescrip = self.cursor.description  # (('id', 3, None, 11, 11, 0, False), ('slug', 253, None, 128, 128, 0, True), ('name', 253, None, 512, 512, 0, True), ('name_en', 253, None, 512, 512, 0, True))
            for colName in columnsDescrip:
                columnList.append(colName[0])
            tableComlumsDic[item] = columnList
        return tableComlumsDic











