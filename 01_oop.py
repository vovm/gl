# realize an example of the pattern "Observer"
# by alarm fire system of some office


class Publisher:

    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def __str__(self):
        return self.name
    
    def register(self, new_subscriber):
        self.subscribers.append(new_subscriber)
        print('Added new subscriber - {}'.format(new_subscriber))
    
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(self, message)


class Subscriber:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def update(self, publisher, message):
        print('{}. From - {}'.format(message, publisher))


if __name__ == '__main__':
    publisher = Publisher('10 Red Avenue, Off 65')
    subscriber = Subscriber('Fire Department')
    publisher.register(subscriber)
    publisher.dispatch('Fire')
