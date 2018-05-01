<p align="center"><img width="40%" src="png/logo.png" /></p>

--------------------------------------------------------------------------------
PyTorch implementation of [StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation](https://arxiv.org/abs/1711.09020). StarGAN can flexibly translate an input image to any desired target domain using only a single generator and a discriminator. The demo video for StarGAN can be found [here](https://www.youtube.com/watch?v=EYjdLppmERE).

<p align="center"><img width="100%" src="png/main.png" /></p>

## Authors

[Yunjey Choi](https://github.com/yunjey), [Minje Choi](https://github.com/mjc92), [Munyoung Kim](https://www.facebook.com/munyoung.kim.1291), [Jung-Woo Ha](https://www.facebook.com/jungwoo.ha.921), [Sung Kim](https://www.cse.ust.hk/~hunkim/), and [Jaegul Choo](https://sites.google.com/site/jaegulchoo/)
Korea Universitiy, Clova AI Research (NAVER), The College of New Jersey, HKUST
&nbsp;


## Results

#### Facial Attribute Transfer on CelebA
The images are generated by StarGAN trained on the CelebA dataset.
<p align="center"><img width="100%" src="png/result_celeb1.png" /></p>


&nbsp;

## Model Description

See original repo.

## Prerequisites
* [Python 3.5+](https://www.continuum.io/downloads)
* [PyTorch 0.2.0](http://pytorch.org/)
* [TensorFlow 1.3+](https://www.tensorflow.org/) (optional for tensorboard)

&nbsp;

## Getting Started

#### 1. Clone the repository
```bash
$ git clone https://github.com/ericpts/StarGAN.git
$ cd StarGAN/
```

#### 2. Download the dataset
```bash
$ python3 init.py
```

#### 3. Train StarGAN

```bash
$ python main.py --mode='train' --dataset='CelebA' --c_dim=5 --image_size=128 \
                 --sample_path='stargan_celebA/samples' --log_path='stargan_celebA/logs' \
                 --model_save_path='stargan_celebA/models' --result_path='stargan_celebA/results'
```

#### 4. Test StarGAN
##### (i) Facial attribute transfer on CelebA
```bash
$ python main.py --mode='test' --dataset='CelebA' --c_dim=5 --image_size=128 --test_model='20_1000' \
                 --sample_path='stargan_celebA/samples' --log_path='stargan_celebA/logs' \
                 --model_save_path='stargan_celebA/models' --result_path='stargan_celebA/results'
```

##### (ii) Facial expression synthesis on RaFD
```bash
$ python main.py --mode='test' --dataset='RaFD' --c_dim=8 --image_size=128 \
                 --test_model='200_200' --rafd_image_path='data/RaFD/test' \
                 --sample_path='stargan_rafd/samples' --log_path='stargan_rafd/logs' \
                 --model_save_path='stargan_rafd/models' --result_path='stargan_rafd/results'
```

##### (iii) Facial expression synthesis on CelebA
```bash
$ python main.py --mode='test' --dataset='Both' --image_size=256 --test_model='200000' \
                 --sample_path='stargan_both/samples' --log_path='stargan_both/logs' \
                 --model_save_path='stargan_both/models' --result_path='stargan_both/results'
```

&nbsp;

## Citation
If this work is useful for your research, please cite our [arXiv paper](https://arxiv.org/abs/1711.09020).
```
@article{choi2017stargan,
 title = {StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation},
 author = {Choi, Yunjey and Choi, Minje and Kim, Munyoung and Ha, Jung-Woo and Kim, Sunghun and Choo, Jaegul},
 journal= {arXiv preprint arXiv:1711.09020},
 Year = {2017}
}
```
&nbsp;

## Acknowledgement
This work was mainly done while the first author did a research internship at <b>Clova AI Research, NAVER (CLAIR)</b>. We also thank all the researchers at CLAIR, especially Donghyun Kwak, for insightful discussions.
