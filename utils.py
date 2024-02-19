import os, datetime, splitfolders
from pathlib import Path
from torch.utils.data import DataLoader
from dataloader import PolypDatasetLoader


def folder_creation(dest_dir, args):
    os.makedirs(dest_dir, exist_ok=True)
    time = datetime.now().strftime("%H_%M_%S")
    dest_dir = dest_dir + time + "_" + args.name + "/"
    os.makedirs(dest_dir, exist_ok=True)


def splitting_data(args):
    loc = Path(__file__).resolve().parent.parent
    save_loc = os.path.join(loc, "split_data")
    print(save_loc)
    splitfolders.ratio(args.data_dir, output=save_loc, seed=7, ratio=(.85, .15), group_prefix=None, move=False)
    return save_loc


def get_dataloader(save_loc, args):
    train_dataset = PolypDatasetLoader(save_loc + "/train/" + args.image_dir + "/", save_loc + "/train/" + args.mask_dir + "/")
    train_dataloader = DataLoader(train_dataset, shuffle=True, drop_last=False, batch_size=args.batch_size)

    val_dataset = PolypDatasetLoader(save_loc + "/val/" + args.image_dir + "/", save_loc + "/val/" + args.mask_dir + "/")
    val_dataloader = DataLoader(val_dataset, shuffle=True, drop_last=False, batch_size=args.batch_size)
    return train_dataloader, val_dataloader