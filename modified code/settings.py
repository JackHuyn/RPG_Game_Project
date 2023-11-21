
# game setup
WIDTH    = 1920
HEIGTH   = 1280
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'



monster_data = {
	'Demon': {'health': 2500,'exp':2000,'damage':100,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 5, 'resistance': 50, 'attack_radius': 100, 'notice_radius': 500},
	'Dragon': {'health': 50000,'exp':5000,'damage':200,'attack_type': ['claw','spell'],  'attack_sound':'../audio/attack/claw.wav','speed': 10, 'resistance': 100, 'attack_radius': 150, 'notice_radius': 1000},
	'Goblin': {'health': 500,'exp':50,'damage':100,'attack_type': 'blunt', 'attack_sound':'', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 300},
	'Minatour': {'health': 20000,'exp':1500,'damage':150,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 4, 'resistance': 30, 'attack_radius': 100, 'notice_radius': 250},
    'Orc': {'health': 10000,'exp':800,'damage':80,'attack_type': 'blunt', 'attack_sound':'../audio/attack/slash.wav', 'speed': 4, 'resistance': 20, 'attack_radius': 100, 'notice_radius': 400},
    'Slime': {'health': 200,'exp':20,'damage':5,'attack_type': 'blunt', 'attack_sound':'', 'speed': 1, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 250},
    'Nec': {'health': 1000,'exp':150,'damage':50,'attack_type': 'spell', 'attack_sound':'', 'speed': 2, 'resistance': 3, 'attack_radius': 150, 'notice_radius': 500},
    'Skeleton': {'health': 50,'exp':10,'damage':5,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 2, 'resistance': 1, 'attack_radius': 80, 'notice_radius': 250}}