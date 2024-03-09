import configparser


def read_configurations(category,key):
    config = configparser.ConfigParser()
    config.read(r"C:\Users\devadn\PycharmProjects\SeleniumPytestHybridProject\configurations\config.ini")
    return config.get(category,key)
