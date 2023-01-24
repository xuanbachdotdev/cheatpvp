import requests

i = int(712950) 
while True: 
  requests.get( f'http://211.253.26.47:8092/ELDORADO_M/PvP/put_score_to_server_pvp.php?ETC=&SCORE={i}&dbName=&LEVEL=10&HOST_ID=EM229886&USER_NAME=XuanBachDe')
  i += 250
