
# Brainwaves of dogs

config_eeg = {}
config_eeg['dataset'] = 'mnist'
config_eeg['verbose'] = True
config_eeg['save_every_epoch'] = 20
config_eeg['print_every'] = 50
config_eeg['work_dir'] = 'results_mnist'
config_eeg['plot_num_pics'] = 400
config_eeg['plot_num_cols'] = 20

config_eeg['input_normalize_sym'] = False
config_eeg['data_dir'] = 'mnist'

config_eeg['optimizer'] = 'adam' # adam, sgd
config_eeg['adam_beta1'] = 0.5
config_eeg['lr'] = 0.001
config_eeg['lr_adv'] = 0.0005
config_eeg['lr_schedule'] = 'manual' #manual, plateau, or a number
config_eeg['batch_size'] = 100
config_eeg['epoch_num'] = 100
config_eeg['init_std'] = 0.0099999
config_eeg['init_bias'] = 0.0
config_eeg['batch_norm'] = True
config_eeg['batch_norm_eps'] = 1e-05
config_eeg['batch_norm_decay'] = 0.9
config_eeg['conv_filters_dim'] = 4

config_eeg['e_pretrain'] = True
config_eeg['e_pretrain_sample_size'] = 1000
config_eeg['e_noise'] = 'add_noise'
config_eeg['e_num_filters'] = 1024
config_eeg['e_num_layers'] = 4
config_eeg['e_arch'] = 'dcgan' # mlp, dcgan, ali

config_eeg['g_num_filters'] = 1024
config_eeg['g_num_layers'] = 3
config_eeg['g_arch'] = 'dcgan_mod' # mlp, dcgan, dcgan_mod, ali

config_eeg['gan_p_trick'] = False
config_eeg['d_num_filters'] = 512
config_eeg['d_num_layers'] = 4

config_eeg['zdim'] = 8
config_eeg['pz'] = 'normal' # uniform, normal, sphere
config_eeg['cost'] = 'l2sq' #l2, l2sq, l1
config_eeg['pz_scale'] = 1.
config_eeg['z_test'] = 'mmd'
config_eeg['mmd_kernel'] = 'IMQ' # RBF, IMQ
config_eeg['lambda'] = 10.
config_eeg['lambda_schedule'] = 'constant'