import configparser

config = configparser.ConfigParser()
config.add_section("bot")
config.set("bot", "token", "6448501567:AAG88nPIzwF6-Xz4ZqIL_gr_cCWwL4ijqxw")
with open('config.ini', 'w') as config_file:
    config.write(config_file)
