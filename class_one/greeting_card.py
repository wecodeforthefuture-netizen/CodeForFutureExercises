import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ============================================================
#  BIBLE GREETING CARD
#  Change the variables below and run this file!
#  Your card will be saved as  my_card.png
#  Open that file in the Files panel to see it.
# ============================================================

# --- CHANGE THESE ---
name        = "Ay"
verse_text  = "The Lord is my shepherd; I shall not want."
verse_ref   = "Psalm 23:1"
message     = "May God bless you today and always!"
card_color  = "midnightblue"   # try: "darkgreen", "purple", "darkred", "navy"
# --------------------

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor(card_color)
ax.set_facecolor(card_color)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

border = patches.FancyBboxPatch((0.2, 0.2), 9.6, 5.6,
    boxstyle="round,pad=0.1",
    linewidth=3, edgecolor="gold", facecolor="none")
ax.add_patch(border)

ax.text(5, 5.1, "~ A Bible Greeting ~",
    ha='center', va='center', fontsize=13,
    color='gold', style='italic')

ax.text(5, 4.1, f'Dear {name},',
    ha='center', va='center', fontsize=16,
    color='white', fontweight='bold')

ax.text(5, 3.1, f'"{verse_text}"',
    ha='center', va='center', fontsize=12,
    color='lightyellow', style='italic',
    wrap=True, multialignment='center')

ax.text(5, 2.2, f'-- {verse_ref}',
    ha='center', va='center', fontsize=11,
    color='gold')

ax.text(5, 1.3, message,
    ha='center', va='center', fontsize=12,
    color='white', multialignment='center')

ax.text(5, 0.55, "* * *",
    ha='center', va='center', fontsize=14,
    color='gold')

plt.tight_layout()
plt.savefig("my_card.png", dpi=150, bbox_inches='tight',
            facecolor=card_color)
plt.close()

print("Your greeting card was saved as  my_card.png")
print("Open it in the Files panel on the left to see it!")
print("")
print(f"  Name:    {name}")
print(f"  Verse:   {verse_ref}")
print(f"  Color:   {card_color}")
