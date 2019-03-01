class Log:
    @staticmethod
    def log(val):
        if val == 'reset':
            file = open('output/log.txt', 'w',  encoding='utf-8')
            file.close()
        else:
            file = open('output/log.txt', 'a', encoding='utf-8')
            file.write(val + '\n')
            file.close()
