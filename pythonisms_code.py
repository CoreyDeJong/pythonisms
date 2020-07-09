from functools import wraps


class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): # [a,b,c] => [a] -> [b] -> [c] -> None
                self.insert(item)


    def __iter__(self):

        def value_generator():

            current = self.head

            while current:

                yield current.value

                current = current.next

        return value_generator()

    def __str__(self):

        output = ""

        for value in self:
            output += f"[ {value} ] -> "

        return output + "None"

    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):

        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError


    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_


#####################################################################################

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val_from_undecorated_function = func(*args, **kwargs)

        emphasized = return_val_from_undecorated_function.upper() + "!!!"

        return emphasized

    return wrapper

def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Sure, that sounds like fun to "{orig_val}"'

    return wrapper


@emphasize
@sarcastic_decorator
def proclaim(txt):
    return txt

@sarcastic_decorator
@emphasize
def restaurant_suggestion(food):
    return food





###### Decorator ###########
# if __name__ == "__main__":
#     # print(proclaim('spam is better than eggs'))
#     # print(proclaim("Want to go for a walk?"))

#     print(restaurant_suggestion('Mexican'))




###### Linked List #############
# if __name__ == "__main__":

#     foods = LinkedList(["apple","banana","cucumber"])

#     first_food = foods[0]

#     for food in foods:
#         print(food)

#     def gen():
#         i = 0
#         while True:
#             yield i
#             i += 1


#     num_gtr = gen()

#     for i in range(100):
#         print(next(num_gtr))

    # print(num_gtr)

    # try:
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    #     print(next(num_gtr))
    # except StopIteration:
    #     print('all done')




