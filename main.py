import sys, argparse
from watermark import watermark

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Watermark one or more images.')
    parser.add_argument('--watermark-text', nargs=1,
        help="String of watermark text, in quotes")
    parser.add_argument('--watermark-image', nargs=1, type=argparse.FileType('r'),
        help="Water Mark Image")
    parser.add_argument('--output-dir', nargs=1, default='./watermarked-images',
        help="Output dir of watermarked image(s)") #type=argparse.FileType('w'),
    parser.add_argument('--infile', nargs='?', help="Image(s) to watermark", required=True)
    #
    #
    args = parser.parse_args()
    #print(args)
    watermark_in = {
        "text": str().join(args.watermark_text),
        "image": args.watermark_image
    }
    watermark(images=args.infile, watermark=watermark_in, output_dir=args.output_dir[0])