class Log:
    @staticmethod
    def log(val):
        if val == 'reset':
            print('Reset')
            #file = open('output/log.txt', 'w',  encoding='utf-8')
            #file.close()
        else:
            print(val)
            #file = open('output/log.txt', 'a', encoding='utf-8')
            #file.write(val + '\n')
            #file.close()
