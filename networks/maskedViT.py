""""
    Refs: https://github.com/facebookresearch/mae/blob/main/models_mae.py


"""
from timm.models.vision_transformer import PatchEmbed, Block
import torch
import torch.nn as nn

from utils.pos_embed import get_2d_sincos_pos_embed

class MaskedViT(nn.Module):
    def __init__(self, img_size = 224, patch_size = 16, in_chans = 3
                 , embed_dim =1024, depth = 24, num_heads=16
                 , decoder_embed_dim=512, decoder_depth=8, decoder_num_heads = 16
                 , mlp_ratio=4, norm_layer = nn.LayerNorm, norm_pix_loss = False ):
        super().__init__()

    def _init_weight(self)

    def forward_encoder(self, x, mask_ratio):
        pass

    def forward_decoder(self, x, ids_restore):
        pass


    

    