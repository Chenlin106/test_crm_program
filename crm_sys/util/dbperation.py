import pymysql
class MysqlConnection:
    def __init__(self,host='172.17.4.234',user='chenlin',password='123456',database='crm',port=3306,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                    port=self.port,
                                    charset=self.charset)
        # 创建游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    def close_connect(self):
        self.cur.close()
        self.conn.close()
    def select_message(self,sql,num=None):
        result = None
        try:
            self.connect()
            #执行sql
            self.cur.execute(sql)
            if str(num).isdigit():
                # fetchmany(?)取？条数据
                result = self.cur.fetchmany(num)
            else:
                # 通过游标的fetchall方法获取所有数据
                result = self.cur.fetchall()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.close_connect()
        print(result)
        return result
    def update_message(self,table_name,update_value,update_rule):
        try:
            #执行sql
            self.connect()
            sql = 'update {} set {} where {}'.format(table_name,update_value,update_rule)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.close_connect()
    def delete_message(self,table_name,delete_rule):
        try:
            self.connect()
            #执行sql
            sql = 'delete from {} where {}'.format(table_name,delete_rule)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.close_connect()
# if __name__ == '__main__':

    # my = MysqlConnection()
    # my.update_message('customer_info',"customer_name='曾海林'","customer_name='李然'")
    # my.delete_message('customer_info',"customer_name='李然'")
    # my.select_message("select * from customer_info where customer_name='曾海林'")