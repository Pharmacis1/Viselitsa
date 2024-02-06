from human import HUMAN

WORD_BANK = {'Указатель',
             'Радуга',
'Мармелад',
'Поиск',
'Прятки',
'Сторож',
'Копейка',
'Леопард',
'Аттракцион',
'Дрессировка',
'Ошейник',
'Карамель',
'Водолаз',
'Защита',
'Батарея',
'Решётка',
'Квартира',
'Дельфинарий',
'Непогода',
'Вход',
'Полиция',
'Перекрёсток',
'Башня',
'вСтрелка',
'Градусник',
'Бутылка',
'Щипцы',
'Наволочка',
'Павлин',
'Карточка',
'Записка',
'Лестница',
'Переулок',
'Сенокос',
'Рассол',
'Закат',
'Сигнализация',
'Журнал',
'Заставка',
'Тиранозавр',
'Микрофон',
'Прохожий',
'Квитанция',
'Пауза',
'Новости',
}


def get_new_word():
    """Получить новое слово для игры."""
    new_word = ''
    while new_word == '':
        for word in WORD_BANK:
            new_word = word
    return new_word.upper()


def get_encrypted_word(word):
    """Получить зашифрованное слово."""
    encrypted_word = ''
    for i in range(len(word)):
        encrypted_word += '_'
    return encrypted_word


def check_letter_in_word(word, letter, counter):
    """Проверяет наличие буквы в слове.
    В случае, если буква есть, оставляет счётчик без изменений.
    Инчае - прибавляет к счётчику +1."""
    if letter in word:
        return counter
    else:
        return counter+1


def open_letter_in_word(word, encrypted_word, letter):
    """Открывает букву в зашифрованном слове."""
    new_encrypted_word = ''
    for i in range(len(word)):
        if letter == word[i]:
            new_encrypted_word += letter
        else:
            new_encrypted_word += encrypted_word[i]
    return new_encrypted_word


def start_new_game():
    """Запускаем новую игру."""
    counter = 7
    word = get_new_word()
    encrypted_word = get_encrypted_word(word)
    print('Я загадал слово! Начнём игру.')
    while counter >= 0 and ('_' in encrypted_word):
        print(HUMAN[counter])
        print(f'Загаданное слово: {encrypted_word}')
        letter = input('Введи букву: ').upper()
        if letter in word:
            encrypted_word = open_letter_in_word(word, encrypted_word, letter)
        else:
            counter -= 1
            print(f'Этой буквы в слове нет! Осталось попыток: {counter}')
    if '_' not in encrypted_word:
        print('Это великая победа! Вы спасли человечка!')
    else:
        print('Поражение. Мы его потеряли...')


if __name__ == '__main__':
    print('Добро пожаловать в Висилицу!')
    print('Если вы проиграете, то мы повесим несчастного человечка.')
    print('А если выиграете - то не повесим!')

    while True:
        comand = input('Нажмите "Д", чтобы начать играть,'
                       'и "В", чтобы выйти из игры: ').upper()
        if comand == 'Д':
            start_new_game()
        elif comand == 'В':
            break
        else:
            print('Такой команды нет')
