# -*- coding: utf-8-*-

from google.cloud import translate


def translate_text(text, target = 'en'):

    translate_client = translate.Client()

    result = translate_client.translate(text, target_language=target)

    print ('Text: ', result['input'])

    print ('Translation: ', result['translatedText'])

    print ('Detected Source Language', result['detectedSourceLanguage'])


text = '''
Je cherche le téléphone.
'''

translate_text(text)
