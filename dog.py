class Dog():
  """Простая модель собаки"""
  def __init__(self, name, age, gen):
    self.name = name
    self.age = age
    self.gen = gen
    print('Собака')
  def sit(self):
    """Собака будет садиться по команде """
    print(self.name.title() + " сел")
  def gav(self):
    """Собака будет гавкать по команде """
    print(self.name.title() + " гавкнул")
  def jump(self):
    """Собака будет прыгать по команде"""
    print(self.name.title() + " прыгнул")
  def fall(self):
    """Собака будет падать по команде """
    print(self.name.title() + " упал")