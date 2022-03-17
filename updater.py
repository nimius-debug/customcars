import requests
done=0
def install():
  f = open('building.jpg','wb')
  f.write(requests.get('https://raw.githubusercontent.com/bestbinaryboi/customcars/main/building.jpg').content)
  f.close()
  f = open('engine.wav','wb')
  f.write(requests.get('https://raw.githubusercontent.com/bestbinaryboi/customcars/main/engine.wav').content)
  f.close()
  f = open('version.txt','w')
  f.write(requests.get('https://raw.githubusercontent.com/bestbinaryboi/customcars/main/version.txt').text)
  f.close()
  f = open('customcarsmain.py','w')
  f.write(requests.get('https://raw.githubusercontent.com/bestbinaryboi/customcars/main/customcarsmain.py').text)
  f.close()
  f = open('customcarsthirdpersoncontroller.py','w')
  f.write(requests.get('https://raw.githubusercontent.com/bestbinaryboi/customcars/main/customcarsthirdpersoncontroller.py').text)
  f.close()
  f = open('tinker.obj','w')
  f.write(requests.get('https://raw.githubusercontent.com/bestbinaryboi/customcars/main/tinker.obj').text)
  f.close()
  done=1
