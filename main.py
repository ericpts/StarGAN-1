import os
import argparse
from solver import Solver
from data_loader import get_loader
from torch.backends import cudnn
from datetime import datetime
from pathlib import Path


def str2bool(v):
    return v.lower() in ('true')

def main(config):
    # For fast training
    cudnn.benchmark = True

    # Create directories if not exist
    if not os.path.exists(config.log_path):
        os.makedirs(config.log_path)
    if not os.path.exists(config.model_save_path):
        os.makedirs(config.model_save_path)
    if not os.path.exists(config.sample_path):
        os.makedirs(config.sample_path)
    if not os.path.exists(config.result_path):
        os.makedirs(config.result_path)

    # Data loader
    data_loader = get_loader(
            Path(config.image_path),
            config.crop_size,
            config.image_size,
            config.batch_size,
            config.mode)

    # Solver
    solver = Solver(data_loader, config)

    if config.mode == 'train':
        solver.train()
    elif config.mode == 'test':
        solver.test()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Model hyper-parameters
    parser.add_argument('--c_dim', type=int, default=1)
    parser.add_argument('--crop_size', type=int, default=256)
    parser.add_argument('--image_size', type=int, default=256)
    parser.add_argument('--g_conv_dim', type=int, default=64)
    parser.add_argument('--d_conv_dim', type=int, default=64)
    parser.add_argument('--g_repeat_num', type=int, default=6)
    parser.add_argument('--d_repeat_num', type=int, default=6)
    parser.add_argument('--g_lr', type=float, default=0.0001)
    parser.add_argument('--d_lr', type=float, default=0.0001)
    parser.add_argument('--lambda_cls', type=float, default=1)
    parser.add_argument('--lambda_rec', type=float, default=10)
    parser.add_argument('--lambda_gp', type=float, default=10)
    parser.add_argument('--d_train_repeat', type=int, default=5)

    # Training settings
    parser.add_argument('--num_epochs', type=int, default=40)
    parser.add_argument('--num_epochs_decay', type=int, default=5)
    parser.add_argument('--num_iters', type=int, default=200000)
    parser.add_argument('--num_iters_decay', type=int, default=10000)
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--num_workers', type=int, default=1)
    parser.add_argument('--beta1', type=float, default=0.5)
    parser.add_argument('--beta2', type=float, default=0.999)

    # pre-trained models
    parser.add_argument('--pretrained_model', type=str, default=None)
    parser.add_argument('--pretrained_model_path', type=str, default='./stargan/models/')

    # Test settings
    parser.add_argument('--test_model', type=str, default='20_1000')

    # Misc
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'test'])
    parser.add_argument('--use_tensorboard', type=str2bool, default=True)

    # Path
    parser.add_argument('--image_path', type=str, default='./data/comp/')

    main_log_path = './stargan/comp'
    log_path = '{}/logs'.format(main_log_path)
    sample_path = '{}/samples'.format(main_log_path)
    result_path = '{}/results'.format(main_log_path)
    model_save_path = '{}/models'.format(main_log_path)

    parser.add_argument('--main_log_path', type=str, default=main_log_path)
    parser.add_argument('--log_path', type=str, default=log_path)
    parser.add_argument('--model_save_path', type=str, default=model_save_path)
    parser.add_argument('--sample_path', type=str, default=sample_path)
    parser.add_argument('--result_path', type=str, default=result_path)

    # Step size
    parser.add_argument('--log_step', type=int, default=50)
    parser.add_argument('--sample_step', type=int, default=50)
    parser.add_argument('--model_save_step', type=int, default=100)

    config = parser.parse_args()
    print(config)
    main(config)
