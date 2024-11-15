from CatG.core.object import ContainerObject

class GameSetting(ContainerObject):
    screen_width: int = 0
    screen_height: int = 0
    fullscreen: bool = False

    def get_screen_size(self) -> tuple[int, int]:
        return self.screen_width, self.screen_height

    # 히히 날먹
    def save_game_setting(self):
        return f"""
{{
  "$types": {{
    "GameSetting": "CatG.core.game.GameManager"
  }},
  "GameSetting": {{
    "screen_width": {self.screen_width},
    "screen_height": {self.screen_height},
    "fullscreen": {self.fullscreen},
  }}
}}
"""