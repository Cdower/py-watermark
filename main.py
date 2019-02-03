import sys, argparse
from watermark import watermark

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Watermark one or more images.')
    parser.add_argument('--watermark-text', nargs=1,
        help="String of watermark text, in quotes")
    parser.add_argument('--output-dir', nargs=1, type=argparse.FileType('w'),
        default=sys.stdin, help="Output dir of watermarked image(s)")
    parser.add_argument('--infile', nargs='?', type=argparse.FileType('r'),
        default=sys.stdin, help="Image(s) to watermark")
    #
    #
    args = parser.parse_args()
    print(args)