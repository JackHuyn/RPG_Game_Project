def get_status(self, player):
		distance, direction = self.get_player_distance_direction(player)

		
		if distance <= self.attack_radius:
			if self.can_attack:
				if 'idle' in self.status:
					self.status = self.status.replace('_idle', '_attack')
				elif not 'attack' in self.status:
					self.status += '_attack'
			elif 'attack' in self.status:
				self.status = self.status.replace('_attack', '')
		elif distance <= self.notice_radius:
			print(direction) 
			# need new way to check for direction

			if direction.x < 0 and direction.y > 0:
				self.status = 'left'
				
			elif direction.x > 0 and direction.y < 0:
				self.status = 'right'
				
			elif direction.x > 0 and direction.y > 0:
				self.status = 'up'
				
			else:
				self.status = 'down'
				
		else:
			if not 'idle' in self.status:
				self.status += '_idle'
				
def import_graphics(self,name):
			monster_path = f'../graphics/monsters/{name}/'
			self.animations = {'up': [],'down': [],'left': [],'right': [],
				'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
				'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}

			for animation in self.animations.keys():
				full_path = monster_path + animation
				self.animations[animation] = import_folder(full_path)
				
def actions(self,player):
		if 'attack' in self.status:
			self.attack_time = pygame.time.get_ticks()
			self.damage_player(self.attack_damage,self.attack_type)
			self.attack_sound.play()
		elif not 'idle' in self.status and not 'attack' in self.status:
			self.direction = self.get_player_distance_direction(player)[1]
		else:
			self.direction = pygame.math.Vector2()

def animate(self):
    animation = self.animations[self.status]
    
    self.frame_index += self.animation_speed
    if self.frame_index >= len(animation):
        if 'attack' in self.status:
            self.can_attack = False
        self.frame_index = 0

    self.image = animation[int(self.frame_index)]
    self.rect = self.image.get_rect(center = self.hitbox.center)

    if not self.vulnerable:
        alpha = self.wave_value()
        self.image.set_alpha(alpha)
    else:
        self.image.set_alpha(255)