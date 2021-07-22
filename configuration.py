import configparser





config = configparser.ConfigParser()
config.read('config.ini')
file_name = config['DEFAULT']['file_name']
file_type = config['DEFAULT']['file_type']
file = file_name+'.'+file_type

if file_type == 'json':
    import serializers.jsonserializer as s

elif file_type == 'pickle':
    import serializers.pickleserializer as s


elif file_type == 'csv':
    import serializers.csvserializer as s



else:
    print('Incorrect configuration file type. Create default type JSON' )
    import serializers.jsonserializer
    access = serializers.jsonserializer.access
    dumpfile = serializers.jsonserializer.dump

access = s.access
dumpfile = sdump
loadfile = s.loadfile

