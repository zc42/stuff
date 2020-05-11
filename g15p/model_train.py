from model_train.mdl_train import train_model
from model_train.mdl_train_4_base_objctv import train_model_4_base_objective

if __name__ == '__main__':
    dir = './model_train/'
    train_model_4_base_objective(dir)
    train_model(dir)
