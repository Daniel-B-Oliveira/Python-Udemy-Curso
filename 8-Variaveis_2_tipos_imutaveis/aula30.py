"""
constante = "Variáveis" que não vão mudar
Muitas Condições no mesmo if (ruim)
        <- contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na entrada

# variável em caps é convencionalmente atribuida como imutável

RADAR_1 = 60  # velocidade máxima do radar
LOCAL_1 = 100  # local onde está o primerio radar
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and\
    local_carro <= (LOCAL_1 + RADAR_RANGE) 
carro_multado_radar_1 = velocidade_carro_passou_radar_1 and carro_passou_radar_1


if velocidade_carro_passou_radar_1:
    print('Carro passou o radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')
