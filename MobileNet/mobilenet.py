# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:07:57 2018

@author: USER
"""
import torch.nn as nn

class MobileNet(nn.Module):
    def __init__(self):
        super(MobileNet, self).__init__()

        def conv_bn(inp, oup, stride):
            return nn.Sequential(
                nn.Conv2d(inp, oup, 3, stride, 1, bias=False),
                nn.BatchNorm2d(oup),
                nn.ReLU(inplace=True)
            )

        def conv_dw(inp, oup, stride):
            return nn.Sequential(
                nn.Conv2d(inp, inp, 3, stride, 1, groups=inp, bias=False),
                # separable conv 
                nn.BatchNorm2d(inp),
                nn.ReLU(inplace=True),
    
                nn.Conv2d(inp, oup, 1, 1, 0, bias=False),
                nn.BatchNorm2d(oup),
                nn.ReLU(inplace=True),
            )

        self.model = nn.Sequential(
            conv_bn(  3,  32, 2), 
            conv_dw( 32,  32, 1),
            conv_bn( 32, 64, 1),
            conv_dw(64, 64, 2),
            conv_bn(64, 128, 1),
            conv_dw(128, 128, 1),
            conv_bn(128, 128, 1),
            conv_dw(128, 128, 2),
            conv_bn(128, 256, 1),
            conv_dw(256, 256, 1),
            conv_bn(256, 256, 1),
            conv_dw(256, 512, 1),
            conv_bn(512, 512, 1),
            
            conv_dw(512, 512, 1),
            conv_bn(512, 512, 1),
            conv_dw(512, 512, 1),
            conv_bn(512, 512, 1),
            conv_dw(512, 512, 1),
            conv_bn(512, 512, 1),
            conv_dw(512, 512, 1),
            conv_bn(512, 512, 1),
            conv_dw(512, 512, 1),
            conv_bn(512, 512, 1),
            
            conv_dw(512, 512, 1),
            conv_bn(512, 1024, 1),
            
            
            
            
            
            nn.AvgPool2d(4),
            
        )
        self.fc = nn.Linear(1024, 10)

    def forward(self, x):
        x = self.model(x)
        x = x.view(-1, 1024)
        x = self.fc(x)
        return x