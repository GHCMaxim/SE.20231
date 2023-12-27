import os
from dotenv import load_dotenv

import logging


class Config:
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        access_token_expire_minutes: int,
    ) -> None:
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes


def init_config() -> Config:
    if not load_dotenv():
        logging.warning(
            "cannot find .env file. initializing default configuration with insecure secret key!"
        )

        return Config("cirno", "HS256", 30)
    else:
        secret_key = os.getenv("secret_key")
        if not secret_key:
            secret_key = "cirno"
            logging.warning(
                "secret key is not set. initializing default insecure secret key!"
            )
        algorithm = os.getenv("algorithm")
        if not algorithm:
            algorithm = "HS256"
            logging.warning(
                "algorithm is not set. initializing default value of HS256!"
            )
        access_token_expire_minutes = (
            int(value) if (value := os.getenv("access_token_expire_minutes")) else None
        )
        if not access_token_expire_minutes:
            access_token_expire_minutes = 30
            logging.warning(
                "access token expiration period is not set. initializing default value of 30 minutes!"
            )

        return Config(secret_key, algorithm, access_token_expire_minutes)


config = init_config()
