#!/bin/bash
# https://github.com/junyanz/CycleGAN/blob/master/datasets/download_dataset.sh

DATASETS=(\
    apple2orange\
    summer2winter_yosemite\
    horse2zebra\
    monet2photo\
    cezanne2photo\
    ukiyoe2photo\
    vangogh2photo\
    maps\
    cityscapes\
    facades\
    iphone2dslr_flower\
    ae_photos\
    )

function get() {
    URL=$1
    ZIP_FILE=$2
    TARGET_DIR=$3

    mkdir -p $TARGET_DIR
    wget -c $URL -O $ZIP_FILE
    unzip -j -u $ZIP_FILE -d ./data/$TARGET_DIR
}

# Download normal datasets.
for d in ${DATASETS[@]}; do
    get https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/$d.zip ./data/archives/$d.zip ./data/$d/
done

# Download CelebA.
get https://www.dropbox.com/s/3e5cmqgplchz85o/CelebA_nocrop.zip?dl=0 ./data/archives/celeba.zip ./data/celeba
