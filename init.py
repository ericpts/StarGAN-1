#!/usr/bin/env python3
import os
import shutil
import subprocess
from random import randint, shuffle
from pathlib import Path
from typing import Iterator

datasets = ['apple2orange',
        'summer2winter_yosemite',
        'horse2zebra',
        'monet2photo',
        'cezanne2photo',
        'ukiyoe2photo',
        'vangogh2photo',
        'maps',
        'cityscapes',
        'facades',
        'iphone2dslr_flower',
        'ae_photos',
        'celeba']

def download():
    subprocess.run(['bash', 'download_dataset.sh'], check=True)

def images() -> Iterator[Path]:
    for d in datasets:
        dpath = Path('data') / d
        for img in dpath.glob('**/*.jpg'):
            yield img

def partition():
    comp = Path('data/comp')

    def force_make(path: Path):
        if path.exists():
            shutil.rmtree(str(path))
        path.mkdir()

    force_make(comp / 'colored')
    force_make(comp / 'black')

    def conv(src: str, dst: str):
        subprocess.run(['convert', src, '-colorspace', 'Gray', dst], check=True)

    for f in images():
        conv(str(f), str(comp / 'black' / f.name))
        shutil.copy(str(f), str(comp / 'colored'))


def main():
    download()
    partition()

if __name__ == '__main__':
    main()
