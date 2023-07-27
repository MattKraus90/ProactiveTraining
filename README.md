# RASA Chatbot


```
rasa train
```

```
rasa shell
```

Funktioniert noch nicht mit allen Namen und Mails, aber Max als Name und eine gmail Adresse funktionieren.

Bisher nur eine Konversation, Beispielablauf:

```
Your input ->  Hi
Please enter the full name of the recipient.
Your input ->  Max
Please enter the E-Mail address of the recipient.
Your input ->  sergejkrasnikov513@gmail.com                    
Email has been sent.
```

Demo Mail wird verschickt, an die angegebene Adresse

```
message = "Hello {}, This is a demo message".format(user_name)
```