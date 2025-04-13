import matplotlib.pyplot as plt
import numpy as np

class ShapeDrawWindow:
    def __init__(self, controller, debug_mode, size=30):
        self.controller = controller
        self.dot_list =src.controller.get_model_info()
        self.debug_mode = debug_mode
        self.current_index = -1
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.size = size
        self.set_fullscreen()

        self.setup_window()

    @staticmethod
    def set_fullscreen():
        manager = plt.get_current_fig_manager()
        manager.window.state('zoomed')

    def setup_window(self):
        self.restore_window()
        if not self.debug_mode:
            self.create_image(len(self.dot_list) - 1)
        else:
            self.create_image(self.current_index)
            self.fig.canvas.mpl_connect('key_press_event', lambda event: self.on_key(event))

    def create_image(self, current_index):
        image = np.ones((self.size, self.size))

        for i in range(current_index + 1):
            dot = self.dot_list[i]
            if 0 <= dot[0] < self.size and 0 <= dot[1] < self.size:
                image[self.size-1 - dot[1], dot[0]] = 1 - dot[2]

        self.ax.clear()
        self.ax.imshow(image, cmap='gray', vmin=0, vmax=1, extent=(0, self.size, 0, self.size))
        self.restore_window()
        plt.draw()

    def restore_window(self):
        self.ax.set_title("Press space to draw the next pixel" if self.debug_mode else "All pixels displayed")
        self.ax.set_xlim(0, self.size)
        self.ax.set_ylim(0, self.size)
        self.ax.grid(True, which='both', color='black', linestyle='--', linewidth=0.5)
        self.ax.set_xticks(np.arange(0, self.size+1, 1))
        self.ax.set_yticks(np.arange(0, self.size+1, 1))
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.tick_params(axis='both', which='major', labelsize=6)

    def on_key(self, event):
        if event.key == ' ':
            if self.current_index < len(self.dot_list) - 1:
                self.current_index += 1
                self.create_image(self.current_index)
            else:
                self.ax.set_title("All pixels displayed")

    @staticmethod
    def show_shape():
        plt.tight_layout()
        plt.show()


