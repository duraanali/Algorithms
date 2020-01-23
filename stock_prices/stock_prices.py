#!/usr/bin/python
import argparse


def find_max_profit(prices):

    current_min_price = 0
    max_profit_so_far = 0

    prices = [int(p) for i, p in enumerate(prices)]
    print("prizes", prices, )
    for i, p in enumerate(prices):
        print(i, p)
        if i == 0:
            current_min_price = p
            print("current_min_price:", current_min_price)
        elif i == 1:
            max_profit_so_far = p - current_min_price
            print("max_profit_so_far", max_profit_so_far)
            if p < current_min_price:
                current_min_price = p
        else:
            calcul = p - current_min_price
            if calcul > max_profit_so_far:
                max_profit_so_far = calcul
            if p < current_min_price:
                current_min_price = p
    return max_profit_so_far


print(find_max_profit([10, 5, 100, 10]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
