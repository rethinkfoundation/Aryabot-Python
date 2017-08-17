from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Aryabot',
    trainer='chatterbot.trainers.ListTrainer'
)

chatbot.train([
    "Hi there!",
    "Hello",
    "Father of Rethink",
    "Sijo Kuruvilla George",
    "What is the address of rethink",
    "AMS Building",
    "How to reach Rethink",
    "Here is the link to follow : www.google.com",
    "What is the wiki link",
    "Here you go : www.wiki.com",
    "What is the color of sky",
    "Yellow"
])

# Get a response to the input text 'How are you?'
response = chatbot.get_response('Can you tell me the address of rethink')

print(response)
