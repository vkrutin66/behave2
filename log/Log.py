class Log:
    @staticmethod
    def log(val):
        if val == 'reset':
            file = open('output/log.txt', 'w',  encoding='utf8')
            file.close()
        else:
            file = open('output/log.txt', 'a', encoding='utf8')
            file.write(val + '\n')
            file.close()
