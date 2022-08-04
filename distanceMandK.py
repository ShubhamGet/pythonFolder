class Distance():
  def __init__(self, kilo, mitter):
    self.kilo = kilo
    self.mitter = mitter

  def add(k1, k2):
    t3 = Distance(0,0)
    if k1.kilo+k2.mitter > 60:
      t3.kilo = (k1.kilo+k2.kilo)//60
    t3.kilo = t3.kilo+k1.kilo+k2.kilo
    t3.mitter = (k1.mitter + k2.mitter) % 60
    return t3

  def displayKilo(self):
    print("Distance is",self.kilo,"kilo and",self.mitter,"mitter.")

  def displayMitter(self):
    print((self.kilo*60)+self.mitter)

a = Distance(2,40)
b = Distance(1,30)
c = Distance.add(a,b)
c.displayKilo()
c.displayMitter()