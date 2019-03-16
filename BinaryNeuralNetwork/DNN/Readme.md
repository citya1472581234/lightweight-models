# Binary Neural Network
* Deterministic
  * ![](https://i.imgur.com/6IVVC8U.png)
* stochastically
  * ![](https://i.imgur.com/FDYruhx.png)
* 雖然參數和激活值是二值化的，但是梯度不能用二值進行存儲
  * 梯度的變化很小
  * 梯度具有累加效果，即梯度都帶有一定的噪音，而噪音一般認為是服從正態分佈的，所以，多次累加梯度才能把噪音平均消耗掉。

* 直接對Deterministic求導數，會都是0，所以採用替代的方法
  * ![](https://i.imgur.com/5kMwrwd.png)
* 在具體的算法使用中，對於隱含層單元：
  * 直接使用決定式的二值化函數得到二值化的激活值
  * 對於權重，在進行參數更新時，要時時刻刻把超出[-1,1]的部分給裁剪了。即權重參數始終是[-1,1]之間的實數
  * 在使用參數是，要將參數進行二值化
* 儘管所有的層次的激活和參數都是二值化的，但第一層的輸入卻是連續值的，因為是像素。若要整個網絡都是二值化的，只需將輸入變化一下即可，用8位數字來表示一個像素，那麼輸入就是一個img_height×img_width×8的向量，而權重參數是一個img_height×img_width的全1向量
  * ![](https://i.imgur.com/UTQnjGC.png)
 
 