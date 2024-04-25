from adress import Adress


class Mailing():
    cost1 = 0
    track1 = ''

    def __init__(self, to_adress, from_adress, cost, track):
        self.cost1 = cost
        self.track1 = track
        self.to_adress=to_adress
        self.from_adress=from_adress

    
    #def toAdress(self, to_adress):
     #   self.to_adress1 = to_adress

    #def fromAdress(self, from_adress):
     #   self.from_adress1 = from_adress
        
    #def get_to_adr(self, to):
      #  self.to= to
   # def get_from_adr(self, fromi):
       # self.fromi= fromi
    
    #def to_adr(self, to):
      #  return to
    
  #  def from_adr(self, fromi):
       # return fromi