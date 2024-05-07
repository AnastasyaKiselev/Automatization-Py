from StringUtils import StringUtils
import pytest

#Первая буква становится заглавной
@pytest.mark.parametrize('str, Str', [
    ('document', 'Document'),
    ("сыр", "Сыр"),
    ('Document', 'Document'),
    ('', '')
       ])
def test_capitalize(str, Str):
    res = StringUtils()
    result = res.capitilize(str)
    assert result == Str

#Удаляются пробелы перед текстом
@pytest.mark.parametrize('not_trimed, trimed', [
    ('   document', 'document'),
    ("  Сыр", "Сыр"),
    ('Nothing', 'Nothing'),
    ( '   123', '123'),
    ('', '')
       ])
def test_trim(not_trimed, trimed):
    res = StringUtils()
    result = res.trim(not_trimed)
    assert result == trimed
    
#Превращение текста в список по разделителю
@pytest.mark.parametrize('text, delimeter, list', [
    ('Members of our Beta Program get ', ' ', ['Members', 'of', 'our', 'Beta', 'Program', 'get','']),
    ('Members of our Beta Program get', ' ', ['Members', 'of', 'our', 'Beta', 'Program', 'get']),
    (" Сыр был у мыши", " ", ['','Сыр', 'был', 'у','мыши']),
    ('Nothing happened', ',', ['Nothing happened']),
    ('', ',', []),
    ])
def test_to_list_pos(text, delimeter, list):
    res = StringUtils()
    result = res.to_list(text, delimeter)
    assert result == list

@pytest.mark.xfail()  
@pytest.mark.parametrize('text, delimeter, list', [
    ('Members of our Beta Program get ', ' ', ['Members', 'of', 'our', 'Beta', 'Program', 'get']),
    ('Members of our Beta Program get', ' ', ['Members', 'of', 'our', 'get']),
    ("  Сыр был у мыши", " ", ['','Сыр', 'был', 'у','мыши']),
    ('Nothing happened', ',', ['Nothing', 'happened']),
    ('', ',', ['']),
    ])
def test_to_list_neg(text, delimeter, list):
    res = StringUtils()
    result = res.to_list(text, delimeter)
    assert result == list


#Поиск символа в строке: позитивный
@pytest.mark.parametrize('text, symbol, bool', [
    ("Elephant", 'p', True),
    ("Elephant and dog!", ' ', True),
    ("Elephant and dog!", '!', True),
    ("Elephant", 'e', True),
    ("Elephant and dog", 'and', True),
    ('', '', True)
    ])
def test_pos_contains(text, symbol, bool):
    res = StringUtils()
    bool = res.contains(text, symbol)
    assert bool
#Поиск символа в строке: негативный
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('text, symbol', [
    ("Elephant", 'f'),
    ("Elephant", 'u'),
    ("Elephant", ' '),
    ('', ' ')
    ])
def test_neg_contains(text, symbol):
    res = StringUtils()
    result = res.contains(text, symbol)
    assert result


#Удаление символа из строки
@pytest.mark.parametrize( "string, simbol, result", [
("Leto i more", ' i ', "Letomore"),
("Leto i more", 'Leto i mor', "e"),
('1234567890', '5', '123467890'),
])
def test_delete_pos_symbol(string, simbol, result):
    res = StringUtils()
    result = res.delete_symbol(string, simbol)
    assert result


@pytest.mark.xfail()
@pytest.mark.parametrize( "string, simbol, result", [
("Leto i more", 'u ', "ghjnxk"),
("Leto i more", '', "Leto i more"),
('1234567890', ' 5', '123467890')
])
def test_delete_neg_symbol(string, simbol, result):
    res = StringUtils()
    result = res.delete_symbol(string, simbol)
    assert result

#Проверка, начало строки с этой буквы или нет
@pytest.mark.parametrize( "string, simbol, result", [
("Leto", 'L', True),
("Leto", 'Le', True),
("Лето-красное", 'Л', True),
(" 13456", ' ', True),
("13456", '1', True),
("13456", '', True)
])
def test_starts_with_pos(string, simbol, result):
    res = StringUtils()
    result = res.starts_with(string, simbol)
    assert result

@pytest.mark.xfail()
@pytest.mark.parametrize( "string, simbol", [
('Leto', "hj"),
("Лето-красное", 'Кра'),
(" 13456", '1'),
("Leto", 'l')
])
def test_starts_with_neg(string, simbol):
    res = StringUtils()
    result = res.starts_with(string, simbol)
    assert result


#Проверка, конец строки заканчивается этим символом/символами или нет
@pytest.mark.parametrize( "string, simbol, result", [
("Leto!", '!', True),
("Leto", 'to', True),
("Лето-красное", 'ное', True),
(" 13456", '6', True),
("13456-*;", ';', True),
("13456", '', True)
])
def test_end_with_pos(string, simbol, result):
    res = StringUtils()
    result = res.end_with(string, simbol)
    assert result

@pytest.mark.xfail()
@pytest.mark.parametrize( "string, simbol", [
("Leto!", '! '),
("Leto", 'ot'),
("Лето-красное", 'НОЕ'),
(" 13456 ", ' 1'),
("13456-*;", ';*'),
])
def test_end_with_neg(string, simbol):
    res = StringUtils()
    result = res.end_with(string, simbol)
    assert result


#Проверка, пустая строка или нет
@pytest.mark.parametrize( "string, result", [
("", True),
("      ", True),
])
def test_is_empty_pos(string, result):
    res = StringUtils()
    result = res.is_empty(string)
    assert result

@pytest.mark.xfail()
@pytest.mark.parametrize( "string", ["Karakum", "Дельфин", "None", None])

def test_is_empty_neg(string):
    res = StringUtils()
    result = res.is_empty(string)
    assert result

#Превращение список в текст по разделителю
@pytest.mark.parametrize('text, delimeter, string', [
    (['Members', 'of', 'our', 'Beta', 'Program', 'get',''], ' ', 'Members of our Beta Program get '),
    (['Members', 'of', 'our', 'Beta', 'Program', 'get'], ' ', 'Members of our Beta Program get'),
    (['','Сыр', 'был', 'у','мыши'], ' ', " Сыр был у мыши"),
    (['Nothing happened'], ',', 'Nothing happened'),
    ([], ',', ''),
    (['lkj'], ',', 'lkj')
    ])
def test_list_to_string_pos(text, delimeter, string):
    res = StringUtils()
    result = res.list_to_string(text, delimeter)
    assert result == string

@pytest.mark.xfail()  
@pytest.mark.parametrize('text, delimeter, string', [
    (['Members', 'of', 'our', 'Beta', 'Program', 'get'], ' ', 'Members of our Beta Program get '),
    (['Members', 'of', 'our', 'get'], ' ', 'Members of our Beta Program get'),
    (['','Сыр', 'был', 'у','мыши'], ' ', "  Сыр был у мыши"),
    (['Nothing', 'happened'], '  ', 'Nothing happened'),
    (['lkj'], ',', '')
    ])
def test_list_to_string_neg(text, delimeter, string):
    res = StringUtils()
    result = res.list_to_string(text, delimeter)
    assert result == string