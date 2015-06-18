Read this [article](http://segmentfault.com/a/1190000000400091) to understand why testing is useful.

My Advice is.
you are going to create many procedures or functions,
you should write test for each of them.

Let's say, you want to write a function to calculate the sum of two number

you may just write
```python
  def add2Numbers(fn, sn):
    return fn + sn;
```
and then use this function.

Now You May Change Your Steps:

1.  you just write down the function name and then return 0
```python
  def add2Numbers(fn, sn):
    return 0;
```

2.  write a test case ( the article shows you a way to use unittest module to write testing code )
the core of the test case may be:
```python
  def test_add2Numbers(self):
    self.assertEqual(add2Numbers(1, 2), 3, 'test add2Numbers(1+2) fail')
    self.assertEqual(add2Numbers(1, -1), 0, 'test add2Numbers(1+(-1)) fail')
    self.assertEqual(add2Numbers("1", "1"), None, 'test add string -> should not return a number')
```
Note: your function add2Numbers should take 2 numbers as parameter, but what if the parameters are string, this may cause a bug.

3.  just run test code, fix your function add2Number to make all test code pass.

This looks stupid, but it does help you debug code, imagine that you've finish a complex function, and call it : doComplexWork(), but the result is not as expected.
You need to debug, but it's not easy to debug when problems occur: you need to run code step by step, and watch over every related variable, check if it acts well.
But if you write testing codes before you use the function, and make the function work well under any circumstances you can imagine ( not too absurd ), DOESN'T this sound great ?

[Another Reference](http://blog.csdn.net/five3/article/details/7104466)
