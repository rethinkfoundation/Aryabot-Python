from chatterbot import ChatBot

chatbot = ChatBot(
    'Aryabot',
    #trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    trainer='chatterbot.trainers.ListTrainer'
)

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")

chatbot.train([
    "Hi there!",
    "Hello",
    "Hello",
    "Hello",
    "Name",
    "Aryabot",
    "Who are you?",
    "I am Aryabot :)",
    "Father of Rethink",
    "Sijo Kuruvilla George",
    "Who is the father",
    "Sijo Kuruvilla George",
    "What is the address of rethink",
    "Rethink Technology Foundation, No.21/536A, AMS Building, CUSAT P.O, Thrikkakara North, Ernakulam, Kerala, India - 682022",
    "What is the address",
    "Rethink Technology Foundation, No.21/536A, AMS Building, CUSAT P.O, Thrikkakara North, Ernakulam, Kerala, India - 682022",
    "Where is office?",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "How to reach Rethink",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "Get to rethink",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "Get there",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "How to get there",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "Google maps link of Rethink",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "Google maps link",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "What is the wiki link",
    "Here you go : http://wiki.rethinkfoundation.in",
    "Rethink wiki",
    "Here you go : http://wiki.rethinkfoundation.in",
    "Rethink website",
    "Here you go : http://rethinkfoundation.in",
    "Website",
    "Here you go : http://rethinkfoundation.in",
    "Blog",
    "Here you go : http://blog.rethinkfoundation.in",
    "Rethink blog",
    "Here you go : http://blog.rethinkfoundation.in",
    "Opportunity",
    "Here you go : http://wiki.rethinkfoundation.in/opportunities",
    "Opportunities",
    "Here you go : http://wiki.rethinkfoundation.in/opportunities",
    "Who is the contact person",
    "You can send email to this email id http://volunteers@rethinkfoundation.in",
    "What are the projects?",
    "Here you go http://wiki.rethinkfoundation.in/Projects",
    "What is rethink foundation",
    "Rethink foundation is a non profit organization",
    "Team members",
    "Sijo, Arya, Aby",
    "Founders of rethink",
    "Sijo, Arya, Aby",
    "Founder of rethink",
    "Sijo, Arya, Aby",
    "Thank you",
    "You are welcome :)",
    "Thanks",
    "You are welcome",
    "Bye",
    "Bye :) Have a good day!",
    "Who is your creator?",
    "Zac!",
    "Who invented you?",
    "Zac!",
    "Who is the inventor",
    "Zac!",
    "How to join rethink",
    "Rethink is a non profit organisation and not an incubator / accelerator / coworking space. There is no process to join / register. Currently the space is provided to volunteers who are working on Rethink focused projects.",
    "What is Rethink",
    "Rethink is a non profit organisation and not an incubator / accelerator / coworking space. There is no process to join / register. Currently the space is provided to volunteers who are working on Rethink focused projects."
])

# Get a response to an input statement

inputData = ''
print ('Aryabot : Hello, I am Aryabot. You can ask me anything about Rethink :)')
while (inputData != "abort"):
    inputData = input("You : ")
    outputData = chatbot.get_response(inputData)
    print ("Aryabot : " + str(outputData))
