import argparse #สำหรับรับ input จากภายนอก
import subprocess #สำหรับ รัน terminal command

#import flask # สำหรับ ทำ webapp และ webservice api

def print_other():
    print('something else')

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='test program to learn about argparse and subpocess')
    parser.add_argument(
        'm',
        type=int,
        help='value of M positional argument')

    parser.add_argument(
        '--x',
        type=int,
        help='value of x')

    parser.add_argument(
        '--yval',
        type=int,
        default=3,
        help='value of y')
    args = parser.parse_args()

    x = args.x
    y = args.yval
    print(f'M = {args.m}')
    print(f'calculate {x} x {y} = {x*y}')
    
    