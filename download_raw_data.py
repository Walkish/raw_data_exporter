import gdown
from config import get_raw_data_conf

if __name__ == "__main__":
    config = get_raw_data_conf()
    for keys in config:
        for url in config[keys]["urls"]:
            gdown.download(
                url=url,
                output=config[keys]["path"],
                quiet=False,
                fuzzy=True,
            )
