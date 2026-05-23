import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Setup directories
PROJECT_ROOT = os.getcwd()
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
SVG_DIR = os.path.join(DATA_DIR, "svg")
os.makedirs(SVG_DIR, exist_ok=True)

CSV_PATH = os.path.join(DATA_DIR, "raw_life_insurance_statistics_2020_2026.csv")

def setup_font():
    """Setup Chinese font for matplotlib."""
    # Common Windows Chinese fonts
    fonts = ['Microsoft JhengHei', 'DFKai-SB', 'SimHei', 'Arial Unicode MS']
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    for font in fonts:
        if font in available_fonts:
            plt.rcParams['font.sans-serif'] = [font]
            break
    plt.rcParams['axes.unicode_minus'] = False # Fix minus sign issue

def plot_trends():
    if not os.path.exists(CSV_PATH):
        print(f"Error: CSV not found at {CSV_PATH}")
        return

    # Read data
    df = pd.read_csv(CSV_PATH, encoding='utf-8-sig')
    
    # Create a time label (Year + Quarter)
    df['時間'] = df['年度'].astype(str) + " " + df['季度']
    
    # Pivot to wide format
    df_pivot = df.pivot(index='時間', columns='項目', values='數值')
    df_pivot = df_pivot.sort_index()
    
    # Calculate "Other Payouts" to create a stack
    # Total Payout = Surrender + Others
    df_pivot['其他給付'] = df_pivot['保險給付總額'] - df_pivot['解約金']

    # --- Setup Style ---
    setup_font()
    STACK_COLORS = ["#FF5722", "#2196F3", "#4CAF50", "#FFC107"] # Red, Blue, Green, Yellow
    
    # Create Figure with Subplots (Matching TaiwanHouse multi-subplot style)
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(14, 12), sharex=True)

    # --- Subplot 1: Payout Composition (Stacked Area) ---
    labels = ["解約給付 (Surrender)", "其他保險給付 (Others)"]
    ax1.stackplot(df_pivot.index, 
                  df_pivot['解約金'] / 1000, 
                  df_pivot['其他給付'] / 1000, 
                  labels=labels, 
                  colors=[STACK_COLORS[0], STACK_COLORS[1]], 
                  alpha=0.85)
    
    ax1.set_title("壽險業總保險給付結構趨勢 (2020-2026 Q1)", loc="left", fontsize=16, fontweight="bold")
    ax1.set_ylabel("金額 (單位：十億元)")
    ax1.legend(loc="upper left")
    # Match TaiwanHouse grid style: #b0b0b0, dashed, alpha 0.5, width 0.8
    ax1.grid(True, linestyle='--', color='#b0b0b0', alpha=0.5, linewidth=0.8)

    # --- Subplot 2: Premium vs Payout (Lines with Fill) ---
    ax2.plot(df_pivot.index, df_pivot['總保費收入'] / 1000, color=STACK_COLORS[2], marker='s', linewidth=3, label='總保費收入')
    ax2.plot(df_pivot.index, df_pivot['保險給付總額'] / 1000, color=STACK_COLORS[0], marker='o', linewidth=3, label='總保險給付')
    
    # Fill the gap (Net Flow)
    ax2.fill_between(df_pivot.index, 
                     df_pivot['總保費收入'] / 1000, 
                     df_pivot['保險給付總額'] / 1000, 
                     where=(df_pivot['總保費收入'] >= df_pivot['保險給付總額']),
                     color='green', alpha=0.2, label='淨流入 (Net Inflow)', interpolate=True)
    ax2.fill_between(df_pivot.index, 
                     df_pivot['總保費收入'] / 1000, 
                     df_pivot['保險給付總額'] / 1000, 
                     where=(df_pivot['總保費收入'] < df_pivot['保險給付總額']),
                     color='red', alpha=0.2, label='淨流出 (Net Outflow)', interpolate=True)

    ax2.set_title("壽險業收支對比與流動性觀測 (2020-2026 Q1)", loc="left", fontsize=16, fontweight="bold")
    ax2.set_ylabel("金額 (單位：十億元)")
    ax2.legend(loc="upper left")
    # Match TaiwanHouse grid style
    ax2.grid(True, linestyle='--', color='#b0b0b0', alpha=0.5, linewidth=0.8)
    
    plt.xticks(rotation=45)
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])

    # Save as SVG
    output_path = os.path.join(SVG_DIR, "life_insurance_trend_stacked.svg")
    plt.savefig(output_path, format='svg')
    print(f"Successfully generated style-matched SVG: {output_path}")

    # --- Plot 2: Payout Structure Ratio ---
    plt.figure(figsize=(14, 8))
    setup_font()
    
    # Calculate Surrender ratio
    surrender_ratio = (df_pivot['解約金'] / df_pivot['保險給付總額']) * 100
    
    plt.fill_between(df_pivot.index, surrender_ratio, color='#FFC107', alpha=0.4, label='解約金佔總給付比例 (%)')
    plt.plot(df_pivot.index, surrender_ratio, color='#FF9800', marker='o', linewidth=3)
    
    plt.title("壽險業解約金佔總給付之佔比趨勢 (2020-2026 Q1)", loc="left", fontsize=16, fontweight="bold")
    plt.ylabel('佔比 (%)', fontsize=12)
    plt.ylim(0, 100)
    
    # Match TaiwanHouse grid style
    plt.grid(True, linestyle='--', color='#b0b0b0', alpha=0.5, linewidth=0.8)
    plt.xticks(rotation=45)
    
    # Annotate important points
    for i, val in enumerate(surrender_ratio):
        if i == len(surrender_ratio) - 1 or i == 0 or val > 65:
            plt.annotate(f'{val:.1f}%', (df_pivot.index[i], val), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, fontweight='bold')

    plt.tight_layout()
    output_ratio_path = os.path.join(SVG_DIR, "surrender_ratio_trend.svg")
    plt.savefig(output_ratio_path, format='svg')
    print(f"Successfully generated style-matched SVG: {output_ratio_path}")

if __name__ == "__main__":
    plot_trends()
