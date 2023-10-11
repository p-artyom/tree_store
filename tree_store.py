from itertools import groupby

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


def parent(item):
    return item['parent']


class TreeStore:
    def __init__(self, items):
        self.__items = {item['id']: item for item in items}
        self.__parent = {
            key: [item['id'] for item in group_items]
            for key, group_items in groupby(self.__items.values(), parent)
        }

    def get_all(self):
        return list(self.__items.values())

    def get_item(self, find_id):
        return self.__items.get(find_id)

    def get_children(self, find_id):
        return list(
            [
                self.get_item(parent_id)
                for parent_id in self.__parent.get(find_id, [])
            ]
        )

    def get_all_parents(self, find_id):
        parent_id = self.get_item(find_id).get('parent')
        parent = self.get_item(parent_id)
        if parent is not None:
            return [parent] + self.get_all_parents(parent['id'])
        return []


if __name__ == '__main__':
    ts = TreeStore(ITEMS)

    assert ts.get_all() == [
        {'id': 1, 'parent': 'root'},
        {'id': 2, 'parent': 1, 'type': 'test'},
        {'id': 3, 'parent': 1, 'type': 'test'},
        {'id': 4, 'parent': 2, 'type': 'test'},
        {'id': 5, 'parent': 2, 'type': 'test'},
        {'id': 6, 'parent': 2, 'type': 'test'},
        {'id': 7, 'parent': 4, 'type': None},
        {'id': 8, 'parent': 4, 'type': None},
    ], 'Метод get_all() возвращает некорректное значение!'

    assert ts.get_item(7) == {
        'id': 7,
        'parent': 4,
        'type': None,
    }, 'Метод get_item() возвращает некорректное значение!'

    assert ts.get_children(4) == [
        {'id': 7, 'parent': 4, 'type': None},
        {'id': 8, 'parent': 4, 'type': None},
    ], 'Метод get_children() возвращает некорректное значение!'

    assert (
        ts.get_children(5) == []
    ), 'Метод get_children() возвращает некорректное значение!'

    assert ts.get_all_parents(7) == [
        {'id': 4, 'parent': 2, 'type': 'test'},
        {'id': 2, 'parent': 1, 'type': 'test'},
        {'id': 1, 'parent': 'root'},
    ], 'Метод get_all_parents() возвращает некорректное значение!'
