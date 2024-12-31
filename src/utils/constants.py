from pathlib import Path


# [Main]
PROJECT_DIR = Path("..").absolute().resolve()

# Project fs
DATA_DIR = PROJECT_DIR.joinpath('data')
IMG_DIR: Path = DATA_DIR.joinpath('img')
TRANSLATE_DIR: Path = DATA_DIR.joinpath('translate')

RECIPE_URLS: Path = DATA_DIR.joinpath("recipe_urls.csv")
RECIPES: Path = DATA_DIR.joinpath("recipes.csv")
TRANSLATED_RECIPES: Path = DATA_DIR.joinpath("translated_recipes.csv")

# Proxy
PROXY_PATH = PROJECT_DIR.joinpath('temp').joinpath('proxy_list.csv').resolve()

# [Logs]
LOG_DIR = PROJECT_DIR.joinpath('logs').joinpath('main').resolve()

# [Misc]
EMPTY = ['none', 'nan', '', ' ', '\n', '\t', '\r']
