from itertools import chain
from datetime import datetime



def logger(old_function):
    
    def new_function(*args, **kwargs):
  
        results = old_function(*args, **kwargs)
        sum_results = (sum(True for i in results))
        
        text = f'''
        Дата и время вызова функции - {datetime.now()}
        Функция -  {str(old_function.__name__)}
        Колличество элементов в списке - {str(sum_results)}
        '''
        
        with open('log_function.log', 'a') as file:
            file.write(text)
        
        return results
    
    return new_function




@logger
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
    
    def __iter__(self):
        self.flat_iter = chain.from_iterable(self.list_of_list)
        return self

    def __next__(self):
        return next(self.flat_iter)


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
