import json


def load_candidates():
    with open("candidates.json", 'r', encoding='utf-8') as f:
        text = json.load(f)
        return text


def get_all():
    text = load_candidates()
    d = '<pre>'
    for i in text:
        d += f'''
        {i["name"]}\n
        {i["position"]}\n
        {i["skills"]}\n
        '''
    d += '</pre>'
    return d


def get_by_pk(pk):
    text = load_candidates()
    for i in text:
        if i["pk"] == pk:
            return i


def get_by_skill(skill_name):
    spisok = []
    text = load_candidates()
    for i in text:
        if skill_name.lower() in i["skills"].lower():
            spisok.append(i)
    return spisok

