import tomllib
from pprint import pprint


def load_toml() -> dict:

    with open('config.toml', 'rb') as f:
        toml_data: dict = tomllib.load(f)
        return toml_data


if __name__ == "__main__":

    try:

        data: dict = load_toml()

    except Exception as ex:
        pprint(ex)

    else:
        pprint(data, sort_dicts=False)
