class TreeStore:
    def __init__(self, items):
        pass

    def get_all(self):
        pass

    def get_item(self):
        pass

    def get_children(self):
        pass

    def get_all_parents(self):
        pass


if __name__ == '__main__':
    ITEMS = [
        {'id': 1, 'parent': 'root'},
        {'id': 2, 'parent': 1, 'type': 'test'},
        {'id': 3, 'parent': 1, 'type': 'test'},
        {'id': 4, 'parent': 2, 'type': 'test'},
        {'id': 5, 'parent': 2, 'type': 'test'},
        {'id': 6, 'parent': 2, 'type': 'test'},
        {'id': 7, 'parent': 4, 'type': None},
        {'id': 8, 'parent': 4, 'type': None},
    ]
    ts = TreeStore(ITEMS)

    # print(ts.get_all())
    # [{'id':1,'parent':'root'},{'id':2,'parent':1,'type':'test'},
    # {'id':3,'parent':1,'type':'test'},{'id':4,'parent':2,'type':'test'},
    # {'id':5,'parent':2,'type':'test'},{'id':6,'parent':2,'type':'test'},
    # {'id':7,'parent':4,'type':None},{'id':8,'parent':4,'type':None}]

    # print(ts.get_item(7))
    # {'id':7,'parent':4,'type':None}

    # print(ts.get_children(4))
    # [{'id':7,'parent':4,'type':None},{'id':8,'parent':4,'type':None}]

    # print(ts.get_children(5))
    # []

    # print(ts.get_all_parents(7))
    # [{'id':4,'parent':2,'type':'test'},{'id':2,'parent':1,'type':'test'},
    # {'id':1,'parent':'root'}]
