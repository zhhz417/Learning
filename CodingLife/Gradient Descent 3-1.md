
----------
**Gradient Descent：** gradient = a vector
注意观察learning rate和loss的变化，eg. Learning rate more bigger – maybe loss bigger or smaller at beginning then not change.  Learning rate too small – maybe the loss will become smaller slowly. 观察前几次的loss是不是稳定下降。 

**Adaptive learning rate:** 通常来说，reduce the learning rate by some factor every few epochs, learning rate会随着loss的减小而减小，有利于收敛。Depends on the number of updates. 最好的是每一个参数都有不同的learning rate. 

**Adagrad：** 一个设置learning rate的方法 — divide the learning rate of each parameter by the root mean square of its previous dericatives.
	是一个基于时间的方法，即越往后更新的越小，收敛速度越慢，到后来可能是非常慢。
	Adagrad的计算公式里有分母和g（微分）的冲突，
	在有很多个参数的时候，不一定是gradient的值越大，离最低就越远，步子就越大
