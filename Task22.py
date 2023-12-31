# Задача 22: Даны два неупорядоченных набора целых чисел (
# может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
def ArrayInput():
    n = int(input("Введите количество элементов первого множества: "))
    m = int(input("Введите количество элементов первого множества: "))
    n_set = set()
    m_set = set()    
    print("Введите элементы первого множества.")
    for i in range(n):
        n_set.add(int(input(f"Введите {i + 1} элемент множества: ")))
    print("Введите элементы второго множества.")
    for i in range(m):
        m_set.add(int(input(f"Введите {i + 1} элемент множества: ")))
    return n_set, m_set

n_set, m_set = ArrayInput()
result_set = sorted(n_set.intersection(m_set))
print(result_set)