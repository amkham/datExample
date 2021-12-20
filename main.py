import operator
import random


def printList(dataList):
    page_num = 0
    console_command = ""
    while console_command != "2":
        for i in range(20 * page_num, 20 * page_num + 20):
            if i >= len(dataList):
                print("end...")
                break
            else:
                print(str(i + 1) + ": " + str(dataList[i]))

        page_num = page_num + 1

        if len(dataList) <= 20:
            break
        print()
        print("/////////////////////INPUT NUM FOR COMMAND///////////////////")
        print("1: next 20 ")
        print("2: exit")
        print("/////////////////////////////////////////////////////////////")
        console_command = input()


def findBy(byValue):
    result = list(filter(lambda item: item['num_of_page'] == int(byValue), myList))
    print("Find " + str(len(result)) + " records")
    return result


def quicksortByYear(dataList):
    if len(dataList) <= 1:
        return dataList
    else:
        q = random.choice(dataList)
    l_nums = [n for n in dataList if n['year'] < q['year']]

    e_nums = [q] * dataList.count(q)
    b_nums = [n for n in dataList if n['year'] > q['year']]
    return quicksortByAuthor(l_nums) + e_nums + quicksortByAuthor(b_nums)


def quicksortByAuthor(dataList):
    if len(dataList) <= 1:
        return dataList
    else:
        q = random.choice(dataList)
    l_nums = [n for n in dataList if n['author'] < q['author']]

    e_nums = [q] * dataList.count(q)
    b_nums = [n for n in dataList if n['author'] > q['author']]
    return quicksortByAuthor(l_nums) + e_nums + quicksortByAuthor(b_nums)


def sortList(key1, key2):
    myList.sort(key=operator.itemgetter(key1))
    myList.sort(key=operator.itemgetter(key2))
    print("Sort finished!")


if __name__ == '__main__':
    myList = []
    i = 0
    with open(r"testBase1.dat", encoding='cp866') as file:
        if file:
            while len(myList) != 4000:
                record = dict.fromkeys(['author', 'title', 'publisher', 'year', 'num_of_page'])
                record['author'] = file.read(12).strip("\x00").strip(" ")
                record['title'] = file.read(32).strip("\x00").strip(" ")
                record['publisher'] = file.read(16).strip("\x00").strip(" ")
                buff = file.read(2)
                record['year'] = ord(buff[0]) + ord(buff[1])
                buff = file.read(2)
                record['num_of_page'] = ord(buff[0]) + ord(buff[1])
                myList.append(record)

    command = ""
    while command != "exit":
        print()
        print("/////////////////////INPUT NUM FOR COMMAND///////////////////")
        print("1: print data")
        print("2: sort data")
        print("3: search")
        print("/////////////////////////////////////////////////////////////")
        command = input()

        if command == "1":
            printList(myList)

        if command == "2":
            sortList('author', 'year')

        if command == "3":
            count = input("page count = ")
            printList(findBy(count))
