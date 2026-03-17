class UraConfig:
    skill_event_weight: list[int]
    reset_skill_event_weight_list: list[str]

    def __init__(self, config: dict):
        se = config.get("skillEventWeight", config.get("skill_event_weight"))
        rs = config.get("resetSkillEventWeightList", config.get("reset_skill_event_weight_list"))
        if se is None or rs is None:
            raise ValueError("Wrong configuration: must configure 'skillEventWeight'/'skill_event_weight' and 'resetSkillEventWeightList'/'reset_skill_event_weight_list'")
        self.skill_event_weight = se
        self.reset_skill_event_weight_list = rs
    
    def removeSkillFromList(self, skill: str):
        if skill in self.reset_skill_event_weight_list:
            self.reset_skill_event_weight_list.remove(skill)
            # If skill list is empty, reset weights
            # If the list is empty from the beginning, this branch won't trigger, and weights won't be reset
            if len(self.reset_skill_event_weight_list) == 0:
                self.skill_event_weight = [0, 0, 0]
    
    def getSkillEventWeight(self, date: int) -> int:
        if date <= 24:
            return self.skill_event_weight[0]
        elif date <= 48:
            return self.skill_event_weight[1]
        else:
            return self.skill_event_weight[2]

class ScenarioConfig:
    """ Configuration for all scenarios """
    ura_config: UraConfig = None

    def __init__(self, ura_config: UraConfig = None):
        self.ura_config = ura_config
