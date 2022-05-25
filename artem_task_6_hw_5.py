
our_set = {1, 2, 3, 4, "banana", 'bred', "milk"}
# Добавление в множества
our_set.add("Kartoplya")
# удаление элемента без выдачи ошибки
our_set.discard(4)
# тоже удаление но с возможной выдачей ошибки
our_set.remove("banana")
# удалинеие и вывод элемента который удалили за индексом по умолчанию (-1)
our_set.pop()

new_set = {1,2,3,4,5,"hometask", "pencil", "book"}
# сшитие двух множеств
print(our_set | new_set)
# Объединение двух множеств
union_sets = our_set.union(new_set)
# выводит разницу в множествах
diff_set = our_set.difference(new_set)
print(diff_set)
# выводит разные элементы которые есть у одного, но нет у другого
symm_diff = our_set.symmetric_difference(new_set)
print(symm_diff)
