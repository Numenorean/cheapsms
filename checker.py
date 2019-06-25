import logging
info = 'Abuse by _Skill_'
logging.basicConfig(level=logging.INFO)
logging.info(info)

import api, itertools

class Checker(object):
    def __init__(self):
        pass


    def login(self, a):
        result = api.getNumber()
        ids.append(result)


    def main(self, threads, col):
        from multiprocessing.dummy import Pool
        self.threads = threads
        pool = Pool(self.threads)
        global ids
        ids = []
        a = []
        for i in range(int(col)):
            a.append(i)
        pool.map(self.login, a)
        api.setStatuses(ids)
        #for _ in pool.imap_unordered(self.login, zip(self.acc_array, self.proxies)):
         #   pass



if __name__ == '__main__':
    import time, os
    while True:
        try:
            print('Баланс: '+api.getBalance())
            threads = int(input('Количество потоков --> '))
            col = input('Сколько --> ')
            Checker().main(threads, col)
        except KeyboardInterrupt:
            logging.info('Остановлено')
            os._exit(1)
        #except:
         #   logging.error('Что-то пошло не так')
