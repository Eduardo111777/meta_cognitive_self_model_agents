# scripts/run_gridworld_experiment.py

import gymnasium as gym
import yaml
import os
import csv
import sys
import pandas as pd
from self_model_agents.agent import SelfModelAgent
from self_model_agents.self_model.simple_self_model import SimpleSelfModel
from self_model_agents.self_model.advanced_self_model import AdvancedSelfModel
from self_model_agents.policy.rl_policy import RLPolicy
from self_model_agents.policy.hybrid_policy import HybridPolicy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import compute_scientific_metrics from your utils/metrics.py
from self_model_agents.utils.metrics import compute_scientific_metrics

# === DummyPolicy for initial testing ===
class DummyPolicy:
    def select_action(self, observation):
        return env.action_space.sample()

# === Load config ===
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# === Create output directories ===
os.makedirs("outputs/logs", exist_ok=True)
os.makedirs("outputs/metrics", exist_ok=True)
os.makedirs("outputs/visualizations", exist_ok=True)
os.makedirs("outputs/scientific_metrics", exist_ok=True)  # <=== New folder

# === Initialize environment ===
env = gym.make(config["environment"])

# === Ask user which SelfModel to use ===
self_model_choice = input("Which SelfModel do you want to run? (simple / advanced): ").strip().lower()

if self_model_choice == "simple":
    self_model = SimpleSelfModel()
elif self_model_choice == "advanced":
    self_model = AdvancedSelfModel()
else:
    raise ValueError("Invalid SelfModel selected. Choose 'simple' or 'advanced'.")

# === Ask user which Policy to use ===
policy_choice = input("Which Policy do you want to run? (dummy / rl / hybrid): ").strip().lower()

if policy_choice == "dummy":
    policy = DummyPolicy()
elif policy_choice == "rl":
    print("\nUsing RLPolicy (PPO)...\n")
    policy = RLPolicy(env, total_timesteps=20000)
elif policy_choice == "hybrid":
    print("\nUsing HybridPolicy (RL + SelfModel)...\n")
    policy = HybridPolicy(env, total_timesteps=20000)  # <=== Corrected here
else:
    raise ValueError("Invalid Policy selected. Choose 'dummy', 'rl' or 'hybrid'.")

# === Initialize Agent ===
agent = SelfModelAgent(self_model, policy, env)

# === Training loop ===
num_steps = config["num_steps"]
log_interval = config["log_interval"]

# === Prepare CSV writer ===
metrics_path = f"outputs/metrics/gridworld_metrics_{policy_choice}_{self_model_choice}.csv"
metrics_file = open(metrics_path, mode="w", newline="")
csv_writer = csv.writer(metrics_file)
csv_writer.writerow(["step", "reward", "confidence_level", "fatigue_level", "current_mode"])

print(f"\n✅ Running experiment with {policy_choice.upper()} policy and {self_model_choice.upper()} SelfModel.\n")
print("Starting training loop...")

for step in range(1, num_steps + 1):
    reward, done = agent.step()

    # Log metrics
    state = agent.get_self_model_state()
    csv_writer.writerow([
        step,
        reward,
        state["confidence_level"],
        state["fatigue_level"],
        state["current_mode"]
    ])

    # Log progress
    if step % log_interval == 0:
        print(f"Step {step} | Reward: {reward:.2f} | Confidence: {state['confidence_level']:.2f} | Fatigue: {state['fatigue_level']:.2f} | Mode: {state['current_mode']}")

metrics_file.close()

print(f"\n✅ Training complete. Metrics saved to: {metrics_path}\n")

# === Compute and save scientific metrics ===
scientific_metrics = compute_scientific_metrics(metrics_path)

scientific_metrics_path = f"outputs/scientific_metrics/scientific_metrics_{policy_choice}_{self_model_choice}.csv"
scientific_metrics.to_csv(scientific_metrics_path, index=False)

print(f"\n✅ Scientific metrics saved to: {scientific_metrics_path}\n")




