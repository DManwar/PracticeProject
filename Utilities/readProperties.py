import configparser
config =configparser.RawConfigParser()
config.read("C:\Users\RAMJI\PycharmProjects\PracticeProject\Configuration\config.ini")

class Readconfig():
    @staticmethod
    def getApplicationURL(self):
        url=config.get('common info ','baseURL')
        return url
    @staticmethod
    def getUseremail():
        username = config.get('common info',"useremail")
        return username
    @staticmethod
    def getPassword():
        password= config.get('common info ','password')
        return password