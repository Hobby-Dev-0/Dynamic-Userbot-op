from sample_config import Config
import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from exampleconfig import Var as Config
elif os.path.exists("config.py"):
    from config import Development as Config  # noqa


Var = Config
