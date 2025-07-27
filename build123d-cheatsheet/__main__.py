import sys
from .abcq_tui import launch

if __name__ == "__main__":
    if not sys.argv[1:]:
        launch()
    else:
        shape = sys.argv[1]
        print(f"Running abcq_tui for shape: {shape}")
        launch(shape)