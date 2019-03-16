# SuffleNet

* 主要使用 channel shuffle、pointwise group convolutions和depthwise separable convolution，和MobileNet主要差異在於 channel shuffle，
  因為不做shuffle可能會造成學出來的特徵只侷限在channel的一部分，還有對於 pointwise convolutions 做group運算減少參數量。
  
  ![](https://github.com/citya1472581234/MobileNet/blob/master/1.jpg?raw=true)