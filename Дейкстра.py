import numpy
import math

i = math.inf

start = int(input("С какой вершины начинаем? ")) - 1
end = int(input("Какой вершиной заканчиваем? "))
minim = 0
node = start
n = 12
ostov = {node}  # Множество вершин, которые потом не надо будет рассматривать
rez = {node + 1: 0}  # Итоговый словарь

matrix = numpy.array([[0, 7, i, i, 9, 2, i, i, i, i, i, i],  # Матрица смежности
                      [7, 0, 5, 4, 8, 2, i, i, i, i, i, i],
                      [i, 5, 0, 2, 9, i, i, i, i, i, i, i],
                      [i, 4, 2, 0, 3, i, 8, 3, i, i, i, i],
                      [9, 8, 9, 3, 0, 3, 5, 1, 7, i, i, i],
                      [2, 2, i, i, 3, 0, i, 6, 1, i, i, i],
                      [i, i, i, 8, 5, i, 0, 6, i, 4, 4, i],
                      [i, i, i, 3, 1, 6, 6, 0, 2, 7, 8, 5],
                      [i, i, i, i, 7, 1, i, 2, 0, i, 6, 1],
                      [i, i, i, i, i, i, 4, 7, i, 0, 10, i],
                      [i, i, i, i, i, i, 4, 8, 6, 10, 0, 3],
                      [i, i, i, i, i, i, i, 5, 1, i, 3, 0]])

m = numpy.array([[i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i],
                 [i, i, i, i, i, i, i, i, i, i, i, i]])

for iter in range(n - 1):

    stroke = []
    column = []

    for j in range(n):
        if j not in ostov:
            column = m[:, j]
            stroke.append(min(min(column), matrix[node][j] + minim))
        else:
            stroke.append(i)

    m[node] = stroke
    minim = min(m[node])
    s = m[node]
    node = numpy.where(s == minim)[0][0]
    ostov.add(node)
    rez[node + 1] = int(minim)

    m[node] = stroke

print(f"Минимальный путь от вершины {start + 1} до вершины {end} равен {rez[end]}")