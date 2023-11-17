import configparser
from dataclasses import dataclass

config_name = "\\config.ini"


@dataclass
class DbConfig:
    host: str
    password: str
    username: str
    driver: str
    database: str
    db_name: str


@dataclass
class TgBot:
    token: str
    # admin_id: int
    # use_redis: bool


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path + config_name)

    tg_bot = config["tg_bot"]

    return Config(
        tg_bot=TgBot(
            token=tg_bot.get("token"),
            # admin_id=tg_bot.getint("admin_id"),
            # use_redis=tg_bot.getboolean("use_redis"),
        ),
        db=DbConfig(**config["database"]),
    )
