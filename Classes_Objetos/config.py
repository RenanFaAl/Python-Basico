#setattr(object, attribute_name, value) , igual ao getattr
class Configuration:
    pass

setting_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Seta atributos usando chaves-valor do dicionário dinamicamente
for attr_name, attr_value, in setting_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.max_retries)# 5