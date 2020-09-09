import yaml


def yaml_to_list(file_path: str) -> dict:
    with open(file_path) as yaml_file:
        templates_list = yaml.safe_load(yaml_file)

        return templates_list


def list_to_yaml(templates_list: list, file_path: str):
    with open(file_path, 'w') as yaml_file:
        yaml.dump(templates_list, yaml_file, default_flow_style=False)
