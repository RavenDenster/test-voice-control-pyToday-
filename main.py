import speech_recognition
import os
import random

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'gretting': ['привет', 'приветствую'],
        'create_task': ['добавть задачу', 'создать задачу', 'заметка'],
        'play_music': ['включить музыку', 'дискотека']
    }
}

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

        return query
    except speech_recognition.UnknownValueError:
        return 'Damn... Не понял что ты сказал'

def gretting():
    return 'Привет, нищеброд!'

def create_task():
    print('Что добавим в список дел?')

    query = listen_command()
    with open('todo-list.txt', 'a', encoding='utf8') as file:
        file.write(f'- {query}\n')
    return f'Задача {query} добавлена в todo-list!'

def play_music():
    files = [os.path.join('music', x) for x in os.listdir('music')]
    random_file = random.choice(files)
    os.startfile(random_file)

    printi = random_file.split('\\')[-1]
    return f'Танцуем под {printi}'

def main():
    query = listen_command()

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())

if __name__ == '__main__':
    main()