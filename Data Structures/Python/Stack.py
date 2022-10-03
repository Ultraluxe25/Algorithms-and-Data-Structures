class Stack:
    def __init__(self):
        self.collection = []

    def put(self, element):
        self.collection.insert(0, element)

    def take_away(self):
        try:
            return self.collection.pop(0)
        except IndexError:
            print("Stack is already empty")

    def show_stack(self):
        print(self.collection)

    def check_empty(self):
        check = '' if len(self.collection) == 0 else 'not '
        print(f"Stack is {check}empty")


st = Stack()
st.take_away()  # -> Stack is already empty
st.show_stack()  # -> []

st.put(3)
st.put(8)
st.put(4)
st.show_stack()  # -> [4, 8, 3]
st.take_away()
st.show_stack()  # -> [8, 3]

st.check_empty()  # -> Stack is not empty
