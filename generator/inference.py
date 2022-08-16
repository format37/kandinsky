import torch
from rudalle.pipelines import generate_images, show
from rudalle import get_rudalle_model, get_tokenizer, get_vae
from rudalle.utils import seed_everything
import os
import system

device = 'cuda'
tokenizer = get_tokenizer()
vae = get_vae(dwt=False).to(device)

print('loading model...')

# dalle = get_rudalle_model('Kandinsky', fp16=True, device=device, use_auth_token=KANDINSKY_TOKEN)
dalle = get_rudalle_model('Kandinsky', fp16=True, device=device, local_files_only=True, cache_dir='/app/model/rudalle')

print('model leaded')

# receive text from parameters
text = ' '.join(system.argv[1:])
# seed_everything(42)
top_k, top_p = 768, 0.99
pil_images, _ = generate_images(text, tokenizer, dalle, vae, top_k=top_k, images_num=1, bs=3, top_p=top_p)

path = 'data/generated/'
# save images to disk
for i, pil_image in enumerate(pil_images):
    pil_image.save(path + '{}.png'.format(i))

print('Images saved to disk')
