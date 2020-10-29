import logging
import time

class Crm_log:
    def __init__(self):
        # 创建logger对象
        self.logger = logging.getLogger('log')
    def set_message(self,message,level):
        global fh
        try:
            # 获取当前时间
            date_now = time.strftime('%Y-%m-%d', time.localtime())
            # 添加日志文件
            fh = logging.FileHandler('../../log_info/Crm_Auto_log_' + date_now + '.log','a','UTF-8')
            # 添加控制台
            ch = logging.StreamHandler()
            # 格式化日志信息
            fm = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
            # 对文件格式
            fh.setFormatter(fm)
            # 对控制台格式
            ch.setFormatter(fm)
            # 将文件句柄添加到log对象中去
            self.logger.addHandler(fh)
            # 将控制台句柄加入logger对象中去
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)
            # 输出info
            if level == 'debug':
                self.logger.debug(message)
            elif level == 'info':
                self.logger.info(message)
            elif level == 'error':
                self.logger.error(message)
            elif level == 'warning':
                self.logger.warning(message)
            # 移除文件句柄
            self.logger.removeHandler(fh)
            # 移除控制台对象
            self.logger.removeHandler(ch)
        except:
           print('file exception')
        finally:
            # 关闭文件
            fh.close()
# if __name__ == '__main__':
#     auto_log=Crm_log()
#     auto_log.set_message('message','info')