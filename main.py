# -*- coding: utf-8 -*-

from core import run_timMRD


def main(args):
    tis_name = args.tis_name
    pla_name = args.pla_name
    methyl_file = args.methyl_file
    baseline_file = args.baseline_file
    output_dir = args.output_dir
    r_home = args.r_home
    run_timMRD(tis_name, pla_name, methyl_file, baseline_file, output_dir, r_home)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--tis_name", action="store", required=True)
    parser.add_argument("--pla_name", action="store", required=True)
    parser.add_argument("--methyl_file", action="store", required=True)
    parser.add_argument("--baseline_file", action="store", required=True)
    parser.add_argument("--output_dir", action="store", required=True)
    parser.add_argument("--r_home", action="store", required=True)

    args = parser.parse_args()
    main(args)
