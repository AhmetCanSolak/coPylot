import yaml


class MicroscopeConfig:
    def __init__(self, config_dict: dict):
        self.name = config_dict['name']
        self.config_dict = config_dict

    @property
    def nb_devices(self):
        return len(self.config_dict['hardware'])

    @staticmethod
    def read_config(config_path):
        with open(config_path, "r") as stream:
            try:
                response_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return MicroscopeConfig(response_dict)
