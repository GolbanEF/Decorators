from fileOpen import get_shop_list_by_dishes


def main():
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    get_shop_list_by_dishes(['Фахитос'], 6)


if __name__ == '__main__':
    main()