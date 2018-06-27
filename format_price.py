import argparse


def format_price(price):
    if isinstance(price, bool):
        return None
    try:
        price = round(float(price), 2)
        if float.is_integer(price):
            price = int(price)
    except (TypeError, ValueError):
        return None
    return '{:,}'.format(price).replace(',', ' ')


def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--price',
        type=int and float,
        help='set price',
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_command_line_args()
    output_price = format_price(args.price)
    print(output_price)
