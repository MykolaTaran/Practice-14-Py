import matplotlib.pyplot as plt

# Зчитування вмісту файла TF22_2
try:
    with open('TF22_2.txt', 'r') as file:
        content = file.read()
        words = content.split('\n')
except IOError:
    print("Помилка відкриття/читання файлу TF22_2.txt")

# Побудова кругової діаграми
if words:
    labels = words
    sizes = [1] * len(words)  # Число 1 для кожного слова (ви можете використовувати відсотки або інші значення)

    # Розфарбовка секторів діаграми в різні кольори
    colors = plt.cm.Paired(range(len(labels)))

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.axis('equal')  # Забезпечення круглої форми діаграми

    plt.title('Слова найбільшої довжини з символом "а"')
    plt.show()
else:
    print('Слова найбільшої довжини з символом "а" відсутні.')