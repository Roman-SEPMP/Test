class FT:
   def __init__(self, n):
      self.n = n
      self.fw = [0] * (n + 1)
   def build(self, a):
      for i,val in enumerate(a,start=1):
       self.upd(i, val)
   def upd(self, i, x):
      while i <= self.n:
       self.fw[i] += x
       i += i & -i
   def presum(self, i):
      s = 0
      while i > 0:
        s += self.fw[i]
        i -= i & -i
        return s
   def rsum(self, l, r):
       return self.presum(r) - self.presum(l-1)
a=list(map(int, input().split()))
ft=FT(len(a))
ft.build(a)
print(ft.presum(4))
print(ft.rsum(2,4))