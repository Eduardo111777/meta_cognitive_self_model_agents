# self_model/simple_self_model.py

from self_model_agents.self_model.base_self_model import BaseSelfModel

class SimpleSelfModel(BaseSelfModel):
    """
    Simple implementation of a SelfModel with basic meta-cognitive variables.
    """

    def __init__(self):
        self.confidence_level = 0.5  # Start with medium confidence
        self.fatigue_level = 0.0     # Start fully rested
        self.current_mode = "exploration"
        self.performance_history = []

    def update(self, reward, done):
        # Update performance history
        self.performance_history.append(reward)
        if len(self.performance_history) > 100:
            self.performance_history.pop(0)

        # Update confidence level
        avg_reward = sum(self.performance_history) / len(self.performance_history)
        self.confidence_level = max(0.0, min(1.0, avg_reward / 200))  # Example scaling

        # Update fatigue level
        self.fatigue_level = min(1.0, self.fatigue_level + 0.01)

        # Update current mode based on confidence and fatigue
        if self.confidence_level < 0.3:
            self.current_mode = "exploration"
        elif self.fatigue_level > 0.8:
            self.current_mode = "emergency"
        else:
            self.current_mode = "exploitation"

    def to_dict(self):
        return {
            "confidence_level": self.confidence_level,
            "fatigue_level": self.fatigue_level,
            "current_mode": self.current_mode,
            "performance_history": list(self.performance_history),
        }

    def reset(self):
        self.confidence_level = 0.5
        self.fatigue_level = 0.0
        self.current_mode = "exploration"
        self.performance_history = []
