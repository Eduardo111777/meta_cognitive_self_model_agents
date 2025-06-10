# scripts/visualize_self_model.py

import os
import pandas as pd
import matplotlib.pyplot as plt

# === Ask user which policy visualization they want ===
print("Which POLICY visualization do you want to generate? (dummy / rl / hybrid): ", end="")
policy_name = input().strip().lower()

# === Ask user which SelfModel visualization they want ===
print("Which SELF MODEL was used? (simple / advanced): ", end="")
self_model_name = input().strip().lower()

# === Validate inputs ===
valid_policies = ["dummy", "rl", "hybrid"]
valid_self_models = ["simple", "advanced"]

if policy_name not in valid_policies:
    raise ValueError(f"\n❌ Invalid policy: {policy_name}. Please choose one of: dummy / rl / hybrid.\n")

if self_model_name not in valid_self_models:
    raise ValueError(f"\n❌ Invalid SelfModel: {self_model_name}. Please choose one of: simple / advanced.\n")

# === Construct metrics file path ===
metrics_path = f"outputs/metrics/gridworld_metrics_{policy_name}_{self_model_name}.csv"

# === Check if file exists ===
if not os.path.isfile(metrics_path):
    raise FileNotFoundError(f"\n❌ Metrics file not found: {metrics_path}\nRun training first for this policy + self model.\n")

# === Create visualization output folder if it doesn't exist ===
os.makedirs("outputs/visualizations", exist_ok=True)

# === Load metrics from CSV ===
df = pd.read_csv(metrics_path)
print(f"\n✅ Loaded metrics from: {metrics_path}")
print(f"🎨 Generating visualization for POLICY: {policy_name.upper()} + SELF MODEL: {self_model_name.upper()}\n")

# === Load scientific metrics CSV ===
scientific_metrics_path = f"outputs/scientific_metrics/scientific_metrics_{policy_name}_{self_model_name}.csv"
if os.path.isfile(scientific_metrics_path):
    scientific_df = pd.read_csv(scientific_metrics_path)
    scientific_text = ""
    for col in scientific_df.columns:
        scientific_text += f"{col}: {scientific_df[col].values[0]:.4f}\n"

    print(f"\n✅ Loaded scientific metrics from: {scientific_metrics_path}\n")
else:
    scientific_text = "No scientific metrics found."
    print(f"\n⚠️ No scientific metrics file found at: {scientific_metrics_path}\n")

# === Plot configuration ===
plt.style.use("seaborn-v0_8")
fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Define smaller font size for Y-axis labels
ylabel_fontsize = 10

# Plot confidence level
axs[0].plot(df["step"], df["confidence_level"], color="blue")
axs[0].set_ylabel("Confidence Level", fontsize=ylabel_fontsize)
axs[0].set_title(f"Evolution of SelfModel Confidence ({policy_name.upper()} + {self_model_name.upper()})")

# Plot fatigue level
axs[1].plot(df["step"], df["fatigue_level"], color="orange")
axs[1].set_ylabel("Fatigue Level", fontsize=ylabel_fontsize)
axs[1].set_title(f"Evolution of Agent Fatigue ({policy_name.upper()} + {self_model_name.upper()})")

# Plot current mode (convert to numeric if necessary)
if df["current_mode"].dtype == object:
    axs[2].plot(df["step"], df["current_mode"].apply(lambda x: 1 if x == "exploitation" else 0), color="green")
    axs[2].set_ylabel("Current Mode\n(1 = exploitation, 0 = exploration)", fontsize=ylabel_fontsize)
else:
    axs[2].plot(df["step"], df["current_mode"], color="green")
    axs[2].set_ylabel("Current Mode", fontsize=ylabel_fontsize)

axs[2].set_xlabel("Step")
axs[2].set_title(f"Agent Mode over Time ({policy_name.upper()} + {self_model_name.upper()})")

# === Add scientific metrics as a text box in top right corner ===
fig.text(
    0.80, 0.85, scientific_text,  # x moved to 0.80 so it is fully in corner
    fontsize=11,
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
)

# === Final layout ===
plt.tight_layout()

# === Save figure ===
save_name = f"outputs/visualizations/self_model_evolution_{policy_name}_{self_model_name}.png"
plt.savefig(save_name)
print(f"\n✅ Visualization saved to: {save_name}\n")

# === Show plot ===
plt.show()
