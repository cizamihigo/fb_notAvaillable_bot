from fbchat import Client, log
from fbchat.models import *
import credentials

class ChrisBot(Client) :
    def onMessage(self, author_id = None, message_object =None, thread_id = None, thread_type = ThreadType.USER, **kwargs):
        self.markAsSeen(author_id)

        log.info("Message {} from {} in {}".format(message_object,thread_id,thread_type))


        messagetxt = message_object.text
        print(messagetxt)

        reply = 'Hello AM not Availlable right now'

        if author_id != self.uid :
            self.send(Message(text= reply),thread_id= thread_id, thread_type = thread_type)
        self.markAsDelivered(author_id,thread_id)
Client = ChrisBot(credentials.email, credentials.password)
Client.listen()

