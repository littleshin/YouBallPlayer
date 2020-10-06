
class PlayerFunctions(object):
	"""docstring for PlayerFunctions"""
	def __init__(self, arg):
		super(PlayerFunctions, self).__init__()
		self.arg = arg
		
	def play():
		pass
	def pause():
		pass
	def single_frame():
		pass

	def time_bar_control():
		pass

	def tune_play_fps(self):
		pass	
	def crop(self):
		pass	
	def shift(self):
		pass	
	
	def overlap(self):
		pass	
	def swap(self):
		# swap two video by mouse-click up-or-down
		# purpose: as overlapping by "persistence of vision" 
		pass	
	def drawing_grids(self):
		# parrelelly draw on both image as ref of motion comparison
		pass	
	def tune_brightness(self):
		pass	
	def save_video(self):
		pass	
	def save_image(self):
		pass	

class PlayerCommunication(object):
	"""two side communication protocol: controller signals and player mouse-click return xy"""
	def __init__(self, arg):
		super(PlayerCommunication, self).__init__()
		self.arg = arg
		

class YouBallPlayer(object):
	"""docstring for YouBallPlayer"""
	def __init__(self, arg):
		super(YouBallPlayer, self).__init__()
		self.arg = arg
		
	def setup_window(self):
		pass

	def turn_on_controller(self):
		self.comm = PlayerCommunication()
		self.controller = PlayerController(self.comm)
		pass

	def main_loop(self):
		while True:
			self.update_comm_signal()
			if self.video_is_loaded()>0:
				self.apply_functions()
				self.show_a_frame()

if __name__ == '__main__':
    ybp = YouBallPlayer()
    ybp.setup_window()
    ybp.turn_on_controller()
    ybp.main_loop()

