import torch
import torch.nn as nn


class FaceMatchingAI(nn.Module):
    def __init__(self, input_dim, output_dim, d_model, nhead, num_encoder_layers, num_decoder_layers):
        super(AttentionTransformer, self).__init__()
        torch.set_default_tensor_type('torch.cuda.FloatTensor')
        self.embedding = nn.Linear(input_dim, d_model)
        self.encoder = nn.TransformerEncoder(nn.TransformerEncoderLayer(d_model, nhead), num_encoder_layers)
        self.decoder = nn.TransformerDecoder(nn.TransformerDecoderLayer(d_model, nhead), num_decoder_layers)
        self.fc = nn.Linear(d_model, output_dim)

    def forward(self, src, tgt=None):
        embedded = self.embedding(src)
        memory = self.encoder(embedded)
        
        #Square Mask
        tgt_mask = None
        if (tgt != None):
            tgt_seq_len = tgt.size(0)
            tgt_mask = torch.triu(torch.ones(tgt_seq_len, tgt_seq_len), diagonal=1).bool().to(tgt.device)
   
        output = self.decoder(memory=memory, tgt=tgt, tgt_mask=tgt_mask)
        output = self.fc(output)
        return output
