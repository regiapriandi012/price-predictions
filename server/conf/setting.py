from configparser import ConfigParser

#directory di laptop @beroek
#def config(filename='C:/Users/Aceri3/PycharmProjects/PricePredictions/server/conf/database.ini', section='postgresql'):
#directory di laptop @mbagusi
#def config(filename='D:/project vscode/PricePredictions/server/conf/database.ini', section='postgresql'):
#directory di laptop @regi
def config(filename='/Users/regia/PycharmProjects/pythonProject/KECERDASANBUATAN/FINALL/server/conf/database.ini', section='postgresql'):
    # create a parser

    parser = ConfigParser()
    # read configServer file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db