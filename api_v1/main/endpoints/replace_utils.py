from api_v1.main.endpoints.replace.db import Replace


def text_replace(replace_object):
    replace = Replace.query.all()
    variables = {}
    for k in replace:
        variables[k.name] = k.value

    for i in replace_object:
        i.text = i.text.format(**variables)

    return replace_object
