#Super 應用
class BaseCRUD:
  data = list(range(1,51))

  def read_data(self):
    return self.data

#繼承BaseCRUD的資料到子類別EvenCRUD
class EvenCRUD(BaseCRUD):
  def read_data(self):
    raw_data = super().read_data()
    return x
    list(filter(lambda x:x %2 ==0, raw_data))


print(EvenCRUD().read_data())