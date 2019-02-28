class Log:
    @staticmethod
    def log(val):
        if val == 'reset':
            file = open('output/log.txt', 'w')
            file.close()
        else:
            file = open('output/log.txt', 'a')
            file.write(val + '\n')
            file.close()
