import math
from multiprocessing.dummy import Process
import time
from threading import Thread


class PiCalculator:


    def __init__(self, notebook=True):
        if notebook:
            from tqdm.notebook import tqdm
            self.tqdm = tqdm
        else:
            from tqdm import tqdm
            self.tqdm = tqdm

        self.threads = []
        self.processes = []


    def __calculate(self):
        '''ガウス＝ルジャンドルのアルゴリズムに従って、近似円周率を計算します
        '''

        a = {'n': 1, 'n+1': None}
        b = {'n': 1 / math.sqrt(2), 'n+1': None}
        t = {'n': 1 / 4, 'n+1': None}
        p = {'n': 1, 'n+1': None}

        for _ in range(1000):
            a['n+1'] = (a['n'] + b['n']) / 2
            b['n+1'] = math.sqrt(a['n'] * b['n'])
            t['n+1'] = t['n'] - p['n'] * (a['n'] - a['n+1'])**2
            p['n+1'] = 2 * p['n']
            a['n'] = a['n+1']
            b['n'] = b['n+1']
            t['n'] = t['n+1']
            p['n'] = p['n+1']

        pi = (a['n'] + b['n'])**2 / 4 / t['n']

        return pi


    def __calculate_3000(self):

        for _ in self.tqdm(range(3000)):
            pi = self.__calculate()

        return pi


    def calculate(self, num=7):

        start_time = time.time()

        for _ in range(num):
            pi = self.__calculate_3000()

        print('total time:', time.time() - start_time)
        print()

        return pi


    def calculate_with_threads(self, num=7):

        start_time = time.time()

        for _ in range(num):
            self.threads.append(
                Thread(target=self.__calculate_3000)
            )

        for t in self.threads:
            t.start()

        for t in self.threads:
            t.join()

        print('total time:', time.time() - start_time)
        print()

        return 


    def calculate_with_processes(self, num=7):

        start_time = time.time()

        for _ in range(num):
            self.processes.append(
                Process(target=self.__calculate_3000)
            )

        for p in self.processes:
            p.start()

        for p in self.processes:
            p.join()

        print('total time:', time.time() - start_time)
        print()

        return 