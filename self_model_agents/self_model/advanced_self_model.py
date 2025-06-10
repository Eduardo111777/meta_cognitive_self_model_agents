# self_model_agents/self_model/advanced_self_model.py

class AdvancedSelfModel:
    def __init__(self):
        # Initialize self model state
        self.confidence_level = 0.5
        self.fatigue_level = 0.0
        self.current_mode = "exploration"

        # Parameters for updating state
        self.confidence_increase = 0.01
        self.confidence_decrease = 0.02
        self.fatigue_increase = 0.005
        self.fatigue_decrease = 0.01
        self.confidence_threshold = 0.7
        self.fatigue_threshold = 0.7

    def update(self, reward, done=None):
        # Update confidence level based on reward
        if reward > 0:
            self.confidence_level += self.confidence_increase
        else:
            self.confidence_level -= self.confidence_decrease

        # Clamp confidence level between 0 and 1
        self.confidence_level = max(0.0, min(1.0, self.confidence_level))

        # Update fatigue level based on current mode
        if self.current_mode == "exploitation":
            self.fatigue_level += self.fatigue_increase
        else:
            self.fatigue_level -= self.fatigue_decrease

        # Clamp fatigue level between 0 and 1
        self.fatigue_level = max(0.0, min(1.0, self.fatigue_level))

        # Update current mode based on thresholds
        if self.confidence_level >= self.confidence_threshold and self.fatigue_level < self.fatigue_threshold:
            self.current_mode = "exploitation"
        else:
            self.current_mode = "exploration"

    def get_state(self):
        # Return current state of the self model
        return {
            "confidence_level": self.confidence_level,
            "fatigue_level": self.fatigue_level,
            "current_mode": self.current_mode
        }
    def to_dict(self):
        return self.get_state()
