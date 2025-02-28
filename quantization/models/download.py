from huggingface_hub import snapshot_download

# Model repo on Hugging Face
model_name = "Qwen/Qwen2.5-1.5B"

# Download the entire model into the current directory
snapshot_download(repo_id=model_name, local_dir="Qwen2.5-1.5B", local_dir_use_symlinks=False)

print(f"Model {model_name} downloaded to ./Qwen2.5-1.5B")