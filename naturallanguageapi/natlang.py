from google.cloud import language

def text_analysis(text):

    client =  language.Client()

    document = client.document_from_text(text)

    sentiment_analysis = document.analyze_sentiment()

    sentiment = sentiment_analysis.sentiment

    entity_analysis = document.analyze_entities()

    entities = entity_analysis.entities

    return sentiment, entities

text = 'Python is the greatest programming language.'

sentiment, entities = text_analysis(text)

print(sentiment.score, sentiment.magnitude)

for entity in entities:

    print(entity.name, entity.type, entity.metadata, entity.salience)
