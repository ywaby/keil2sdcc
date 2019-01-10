import sys
from .c512sdcc import C51_2_SDCC
import argparse
import os
import glob


def main():
    parser = argparse.ArgumentParser(
        prog='keil2sdcc',
        description='convert keil c51 to sdcc',
        epilog='project at: https://www.github.ywaby.keil2sdcc'
    )
    parser.add_argument('-v', '--version',
                        help='print version',
                        action='version',
                        version='%(prog)s 0.0.2')
    parser.add_argument('-e', '--encode',
                        help='assign keil src encode',
                        default='utf8')
    parser.add_argument('-r', '--replace',
                        help='replace keil src with sdcc src',
                        action='store_true',
                        default=False)
    parser.add_argument('files',
                        help='keil srcs to convert;supprot glob',
                        nargs='*')
    parser.add_argument('-j', '--jobs',
                        type=int,
                        metavar='n',
                        default=1,
                        help='number of parallel jobs; '
                             'match CPU count if value is 0')
    args = parser.parse_args()

    if len(args.files) != 0:
        jobs_params = []
        for f_dir in args.files:
            for src in glob.glob(f_dir, recursive=True):
                if args.replace:
                    dist = src
                else:
                    root, ext = os.path.splitext(src)
                    dist = root + '.sdcc' + ext
                jobs_params.append((src, dist, args.encode))

        if args.jobs != 1:
            import multiprocessing
            if args.jobs == 0:
                args.jobs = multiprocessing.cpu_count()
            pool = multiprocessing.Pool(args.jobs)

            pool.map(_job_fix,jobs_params)
        else:
            for job_params in jobs_params:
                C51_2_SDCC(*job_params)

def _job_fix(params):
    C51_2_SDCC(*params)

if __name__ == '__main__':
    main()
