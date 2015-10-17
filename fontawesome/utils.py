import os
import yaml

PATH = os.path.join(os.path.dirname(__file__), 'icons.yml')


def get_icon_choices(only_ids=[], exclude_ids=[]):
    choices = [('', '----------')]

    with open(PATH) as f:
        icons = yaml.load(f)

    for icon in icons.get('icons'):
        id = icon.get('id')
        name = icon.get('name')
        choice = (id, name,)

        if only_ids and id in only_ids or \
                exclude_ids and id not in exclude_ids or \
                not any([only_ids, exclude_ids]):
            choices.append(choice)

    return choices
