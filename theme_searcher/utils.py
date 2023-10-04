import re


def phrase_unify(phrase: str) -> frozenset:
    """
    Принцип мешка слов
    Регистр букв не учитываем
    Знаки препинания игнорируем
    """
    return frozenset(re.findall(r'[\w-]+', phrase.lower()))
