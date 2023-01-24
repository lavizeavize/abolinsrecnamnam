def izmaksas_receptei(recepte, cenas):
  summa=0
  for sastavdala, daudzums in recepte.items():
    summa += daudzums * cena[sastavdala]
    print("Pēc "+ str(sastavdala) +" " + str(daudzums) + " " + str(cena[sastavdala]) + "EUR " + " = " + str(round(summa,2)))
  return summa

def izmaksas_kopa(abolu_svars):
  recepte={"cukurs": 0.6, "kanelis": 0.08, "aboli": 2.0, "udens": 0.2}
  cenas={"cukurs": 0.75, "kanelis":30.0, "aboli": 0.0, "udens":0.0}
  print("Izmakas uz vienu kilogramu: " + str(round(izmaksas_receptei(recepte, cenas),2)) + "/" + str(recepte["aboli"]) + "=" + str(round(izmaksas_kg)))
  print("Ābolu svars ir " + str(abolu_svars) + " un izmaksas uz vienu kg ir " + str(round(izmaksas_kg,2)) + ", tad kopā ir " + str(abolu_svars) + "*" + str(round(izmaksas_kg,2)) + "=" + str(round(abolu_svars*izmaksas_kg)))
  izmaksas_kg = izmaksas_receptei ((recepte, cenas)/ recepte["aboli"])
  return abolu_svars * izmaksas_kg

aboli = 1.5
print("Uz {} kg abolu izmaksas bus {} EUR".format(aboli, izmaksas_kopa(aboli)))
#testins