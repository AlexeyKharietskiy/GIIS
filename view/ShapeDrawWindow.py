import matplotlib.pyplot as plt
import numpy as np

class ShapeDrawWindow:
    def __init__(self, shape, debug_mode):
        self.shape = shape
        self.debug_mode = debug_mode
        self.current_index = -1
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.size = 30

        self.setup_window()

    def setup_window(self):
        """Настройка окна и сетки."""
        self.restore_window()

        if not self.debug_mode:
            self.create_image(len(self.shape.dot_list) - 1)
        else:
            self.fig.canvas.mpl_connect('key_press_event', lambda event: self.on_key(event))

    def create_image(self, current_index):
        """Создает и отображает изображение на основе текущего индекса."""
        image = np.ones((self.size, self.size))

        for i in range(current_index + 1):
            dot = self.shape.dot_list[i]
            if 0 <= dot.x < self.size and 0 <= dot.y < self.size:
                image[self.size-1 - dot.y, dot.x] = 1 - dot.intensity

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
        self.ax.tick_params(axis='both', which='major', labelsize=6)

    def on_key(self, event):
        if event.key == ' ':
            if self.current_index < len(self.shape.dot_list) - 1:
                self.current_index += 1
                self.create_image(self.current_index)
            else:
                print("All pixels have been drawn.")

    @staticmethod
    def show_shape():
        plt.tight_layout()
        plt.show()


