class Settings():
  """存储所有的设置"""

  def __init__(self):
    """初始化游戏的设置"""
    # 屏幕设置 💻
    self.screen_width = 1200
    self.screen_height = 700
    self.bg_color = (230, 230, 230)

    # 飞船设置 ✈️
    # self.ship_speed_factor = 1.5
    self.ship_limit = 3

    # 子弹设置 🔫
    # self.bullet_speed_factor = 2
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullet_allowed = 10

    # 外星人设置 👽
    # self.alien_speed_factor = 1
    self.fleet_drop_speed = 30
    # self.fleet_direction = 1

    # 加速
    self.speedup_scale = 1.1
    self.score_scale = 1.5
    self.initilize_dynamic_settings()

  def initilize_dynamic_settings(self):
    self.ship_speed_factor = 1.5
    self.bullet_speed_factor = 3
    self.alien_speed_factor = 1
    self.fleet_direction = 1
    self.alien_points = 50

  def increase_speed(self):
    self.ship_speed_factor *= self.speedup_scale
    self.bullet_speed_factor *= self.speedup_scale
    self.alien_speed_factor *= self.speedup_scale

    self.alien_points = int(self.alien_speed_factor * self.alien_points)