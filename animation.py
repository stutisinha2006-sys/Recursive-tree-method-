import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ------------------------------------------------
# Recursion Tree Animation
# T(n) = 2T(n/2) + n
# ------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 7))

# Nodes at each level
levels = [
    [(0, 3, "T(n)")],

    [(-2, 2, "T(n/2)"),
     (2, 2, "T(n/2)")],

    [(-3, 1, "T(n/4)"),
     (-1, 1, "T(n/4)"),
     (1, 1, "T(n/4)"),
     (3, 1, "T(n/4)")],

    [(-3.5, 0, "T(1)"),
     (-2.5, 0, "T(1)"),
     (-1.5, 0, "T(1)"),
     (-0.5, 0, "T(1)"),
     (0.5, 0, "T(1)"),
     (1.5, 0, "T(1)"),
     (2.5, 0, "T(1)"),
     (3.5, 0, "T(1)")]
]

# Connections between nodes
edges = [
    # Level 0 -> Level 1
    ((0, 3), (-2, 2)),
    ((0, 3), (2, 2)),

    # Level 1 -> Level 2
    ((-2, 2), (-3, 1)),
    ((-2, 2), (-1, 1)),
    ((2, 2), (1, 1)),
    ((2, 2), (3, 1)),

    # Level 2 -> Level 3
    ((-3, 1), (-3.5, 0)),
    ((-3, 1), (-2.5, 0)),

    ((-1, 1), (-1.5, 0)),
    ((-1, 1), (-0.5, 0)),

    ((1, 1), (0.5, 0)),
    ((1, 1), (1.5, 0)),

    ((3, 1), (2.5, 0)),
    ((3, 1), (3.5, 0))
]


def draw_node(x, y, text):
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=11,
        bbox=dict(
            boxstyle="round,pad=0.4",
            facecolor="white",
            edgecolor="black"
        )
    )


def update(frame):

    ax.clear()

    ax.set_xlim(-5, 5)
    ax.set_ylim(-1.5, 4.5)
    ax.axis("off")

    ax.set_title(
        "Recursion Tree: T(n) = 2T(n/2) + n",
        fontsize=16,
        fontweight="bold"
    )

    # --------------------------------------------
    # Draw levels that should currently be visible
    # --------------------------------------------

    visible_levels = min(frame + 1, 4)

    for i in range(visible_levels):
        for x, y, text in levels[i]:
            draw_node(x, y, text)

    # --------------------------------------------
    # Draw connections
    # --------------------------------------------

    if frame >= 1:
        for edge in edges[:2]:
            (x1, y1), (x2, y2) = edge
            ax.plot([x1, x2], [y1, y2])

    if frame >= 2:
        for edge in edges[2:6]:
            (x1, y1), (x2, y2) = edge
            ax.plot([x1, x2], [y1, y2])

    if frame >= 3:
        for edge in edges[6:]:
            (x1, y1), (x2, y2) = edge
            ax.plot([x1, x2], [y1, y2])

    # --------------------------------------------
    # Step information
    # --------------------------------------------

    if frame == 0:

        ax.text(
            0,
            -0.8,
            "Start with the original problem",
            ha="center",
            fontsize=12
        )

    elif frame == 1:

        ax.text(
            0,
            -0.8,
            "Level 1: 2 nodes of size n/2",
            ha="center",
            fontsize=12
        )

        ax.text(
            0,
            -1.15,
            "Cost = 2(n/2) = n",
            ha="center",
            fontsize=12
        )

    elif frame == 2:

        ax.text(
            0,
            -0.8,
            "Level 2: 4 nodes of size n/4",
            ha="center",
            fontsize=12
        )

        ax.text(
            0,
            -1.15,
            "Cost = 4(n/4) = n",
            ha="center",
            fontsize=12
        )

    elif frame == 3:

        ax.text(
            0,
            -0.8,
            "Continue until the base case T(1)",
            ha="center",
            fontsize=12
        )

    elif frame == 4:

        ax.text(
            0,
            -0.65,
            "Cost at each level = n",
            ha="center",
            fontsize=13,
            fontweight="bold"
        )

        ax.text(
            0,
            -1.05,
            "Height of tree = log2(n)",
            ha="center",
            fontsize=13
        )

    elif frame == 5:

        ax.text(
            0,
            -0.55,
            "Total Cost = n x log2(n)",
            ha="center",
            fontsize=14
        )

        ax.text(
            0,
            -1.05,
            "Time Complexity = Theta(n log n)",
            ha="center",
            fontsize=15,
            fontweight="bold",
            bbox=dict(
                boxstyle="round,pad=0.4",
                facecolor="white",
                edgecolor="black"
            )
        )


# ------------------------------------------------
# Create animation
# ------------------------------------------------

animation = FuncAnimation(
    fig,
    update,
    frames=6,
    interval=1800,
    repeat=True
)

# Save animation as GIF
animation.save(
    "recursion_tree.gif",
    writer=PillowWriter(fps=0.6)
)

plt.close()

print("Animation created successfully!")
print("File: recursion_tree.gif")