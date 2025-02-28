## steps
1. clipping ~ 15-20 min
2. generation -> quick as I only used 50 samples
3. training -> 1epoch batch size 4 ~2 minutes. Want ~3000+ samples, so conservatively 2-3 hours per train run for one epoch. more if more epochs needed (default=4).

## packaging
need transformers >=4.37.0 else qwen errors
downgrade peft to 0.8.0 to be compatible with ^
get rid of dispatch_batches arg when initialising accelerator,
looks like this is now auto detected from dataloader in constructor 

## Shell output
(sorry forgot to store others)
### Training
, 'train.py', '--local_rank=0', '--model_name_or_path', '/home/ubuntu/BitDistiller/quantization/models/Qwen2.5-1.5B/', '--data_path', '../data/datasets/qwen2.5-1.5b/mix_wiki_alpaca_48.json', '--model_max_length', '1024', '--output_dir', './ckpts/qwen2.5-1.5b/int2-g128/', '--logging_dir', './logs/qwen2.5-1.5b/int2-g128/', '--num_train_epochs', '1', '--bf16', 'True', '--seed', '42', '--per_device_train_batch_size', '4', '--per_device_eval_batch_size', '4', '--gradient_accumulation_steps', '1', '--gradient_checkpointing', 'True', '--evaluation_strategy', 'steps', '--eval_steps', '4', '--load_best_model_at_end', 'True', '--save_strategy', 'steps', '--save_steps', '4', '--save_total_limit', '15', '--learning_rate', '8e-6', '--lr_scheduler_type', 'constant', '--weight_decay', '0.', '--logging_steps', '1', '--report_to', 'tensorboard', '--deepspeed', 'config/zero.json', '--bits', '2', '--quant_type', 'int2-asym', '--q_group_size', '128', '--train_kd', 'True', '--kd_loss_type', 'cakld', '--max_train_samples', '999999', '--clip', '/home/ubuntu/BitDistiller/quantization/clip_cache/Qwen2.5-1.5B/int2-g128.pt']
[2025-02-28 15:13:19,314] [INFO] [real_accelerator.py:222:get_accelerator] Setting ds_accelerator to cuda (auto detect)
[2025-02-28 15:13:21,447] [INFO] [comm.py:658:init_distributed] cdb=None
[2025-02-28 15:13:21,447] [INFO] [comm.py:689:init_distributed] Initializing TorchBackend in DeepSpeed with backend nccl
loading /home/ubuntu/BitDistiller/quantization/models/Qwen2.5-1.5B/ model
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
Using 39 samples to train
Example Data
sources: 
  The R U Tuff Enuff album succeeded Reaction upon its release in July 1988 . Jackson was more involved with the production of th
targets: 
  e album than the previous one , and Jackson worked on several songs with the album .
Is the first sentence embedding the second one?

Pick from:
(a). no.
(b). yes.

(a).<|endoftext|>
Using 9 samples to evaluation
converting the model to qat, this may take a while...
Loading pre-computed Clipping results from /home/ubuntu/BitDistiller/quantization/clip_cache/Qwen2.5-1.5B/int2-g128.pt
Clipping init successfully!
loading Teacher Model...
Teacher Model loaded
Get the main Prob!
9it [00:00,  9.26it/s]
Get the coefficient: 0.4243715703487396
/home/ubuntu/BitDistiller/BitDistiller/lib/python3.9/site-packages/transformers/deepspeed.py:23: FutureWarning: transformers.deepspeed module is deprecated and will be removed in a future version. Please import deepspeed modules directly from transformers.integrations
  warnings.warn(
Using /home/ubuntu/.cache/torch_extensions/py39_cu124 as PyTorch extensions root...
Emitting ninja build file /home/ubuntu/.cache/torch_extensions/py39_cu124/cpu_adam/build.ninja...
Building extension module cpu_adam...
Allowing ninja to set a default number of workers... (overridable by setting the environment variable MAX_JOBS=N)
ninja: no work to do.
Loading extension module cpu_adam...
Time to load cpu_adam op: 2.92315936088562 seconds
[2025-02-28 15:14:03,823] [WARNING] [lr_schedules.py:683:get_lr] Attempting to get learning rate from scheduler before it has started
  0%|                                                                                                                           | 0/10 [00:00<?, ?it/s]`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`...
/home/ubuntu/BitDistiller/BitDistiller/lib/python3.9/site-packages/torch/_dynamo/eval_frame.py:745: UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. In version 2.5 we will raise an exception if use_reentrant is not passed. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
  return fn(*args, **kwargs)
{'loss': 2392.8262, 'learning_rate': 8e-06, 'epoch': 0.1}                                                                                              
{'loss': 1390.7155, 'learning_rate': 8e-06, 'epoch': 0.2}                                                                                              
{'loss': 2080.0435, 'learning_rate': 8e-06, 'epoch': 0.3}                                                                                              
{'loss': 2558.5049, 'learning_rate': 8e-06, 'epoch': 0.4}                                                                                              
{'eval_loss': 1864.392333984375, 'eval_runtime': 1.2191, 'eval_samples_per_second': 7.382, 'eval_steps_per_second': 2.461, 'epoch': 0.4}               
 40%|██████████████████████████████████████████████                                                                     | 4/10 [00:12<00:15,  2.61s/it/home/ubuntu/BitDistiller/BitDistiller/lib/python3.9/site-packages/torch/_dynamo/eval_frame.py:745: UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. In version 2.5 we will raise an exception if use_reentrant is not passed. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
  return fn(*args, **kwargs)
{'loss': 1194.2524, 'learning_rate': 8e-06, 'epoch': 0.5}                                                                                              
{'loss': 1768.8893, 'learning_rate': 8e-06, 'epoch': 0.6}                                                                                              
{'loss': 824.1122, 'learning_rate': 8e-06, 'epoch': 0.7}                                                                                               
{'loss': 1795.5801, 'learning_rate': 8e-06, 'epoch': 0.8}                                                                                              
{'eval_loss': 1298.67333984375, 'eval_runtime': 1.4327, 'eval_samples_per_second': 6.282, 'eval_steps_per_second': 2.094, 'epoch': 0.8}                
 80%|████████████████████████████████████████████████████████████████████████████████████████████                       | 8/10 [00:58<00:12,  6.33s/it/home/ubuntu/BitDistiller/BitDistiller/lib/python3.9/site-packages/torch/_dynamo/eval_frame.py:745: UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. In version 2.5 we will raise an exception if use_reentrant is not passed. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
  return fn(*args, **kwargs)
{'loss': 450.5551, 'learning_rate': 8e-06, 'epoch': 0.9}                                                                                               
{'loss': 454.5096, 'learning_rate': 8e-06, 'epoch': 1.0}                                                                                               
{'train_runtime': 116.1034, 'train_samples_per_second': 0.336, 'train_steps_per_second': 0.086, 'train_loss': 1490.9988739013672, 'epoch': 1.0}        
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [01:56<00:00, 11.61s/it]
[rank0]:[W228 15:16:12.771763217 ProcessGroupNCCL.cpp:1496] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
[2025-02-28 15:16:21,984] [INFO] [launch.py:351:main] Process 19637 exits successfully.
