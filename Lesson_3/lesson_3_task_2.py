from smartphone import Smartphone

Sony= Smartphone("Sony", "A252", "9887889878")
Apple= Smartphone("Apple", "SE", "98123123123")
Xiaomi= Smartphone("Mi", "AA2", "911")
Samsung= Smartphone("Samsung", "Sam1", "32165475645")
Huawey= Smartphone("Huawey", "Hahaha", "+79845632147")
   
catalog = []

catalog.append(Sony)
catalog.append(Apple)
catalog.append(Xiaomi)
catalog.append(Samsung)
catalog.append(Huawey)   
#catalog.clear()

for i in catalog:
    print (i.mark, ' - ', i.model, '.' , i.number)
    


