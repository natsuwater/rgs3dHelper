"""Qiita記事 「Python script を pip でインストール可能にする」 のサンプルプログラム."""

import argparse

import pyvista



def average() -> None:
    """entry point for vtk average tool"""
    parser = argparse.ArgumentParser(
        prog="lt", description="")
    parser.add_argument("-t", "--time-only",
                        help="Helper", action="store_true")
    args = vars(parser.parse_args())

    lt = LocalTime()
    is_full = True
    if args["time_only"]:
        is_full = False

    lt.show(is_full)


if __name__ == "__main__":
    average()
