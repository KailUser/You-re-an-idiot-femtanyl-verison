from PIL import Image
import tkinter as tk
from PIL import ImageTk
import time
import os, random


class AnimationWindow:
    def __init__(self, gif_path, output_dir):
        self.frames = self.convert_gif_to_frames(gif_path, output_dir)
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Femtanyl | You're an idiot Custom Version")
        self.root.geometry("200x200")

        self.window_height = self.root.winfo_screenheight()
        self.window_width = self.root.winfo_screenwidth()
        print(self.window_height, self.window_width)

    def run(self):
        while True:
            # Moving window in random direction
            if random.random() < 0.5:
                new_x = random.randint(0, self.window_width - 200)
            else:
                new_x = random.randint(0, self.window_width - 200) - 200
            if random.random() < 0.5:
                new_y = random.randint(0, self.window_height - 200)
            else:
                new_y = random.randint(0, self.window_height - 200) - 200
            print("DEBUG NEW X: {x} NEW Y: {y}".format(x=new_x, y=new_y))
            for i, frame in enumerate(self.frames):
                frame = frame.resize((200, 200))
                photo = ImageTk.PhotoImage(frame)
                label = tk.Label(self.root, image=photo)
                label.photo = photo
                label.pack()
                self.root.update()
                sleep_time = random.uniform(0.009, 0.05)
                print("DEBUG FRAME: {d} TIME: {t}".format(d=i, t=sleep_time))
                time.sleep(sleep_time)
                self.root.after(1000, label.destroy)

            self.root.geometry(f"+{new_x}+{new_y}")

    def convert_gif_to_frames(self, gif_path, output_dir):        
        with Image.open(gif_path) as gif:
            frames = []
            os.makedirs(output_dir, exist_ok=True)
            gif.seek(0)  # Make sure we start at the beginning
            image_counter = 0
            try:
                while True:
                    frame = gif.copy().convert('RGB')
                    frames.append(frame)
                    frame.save(f"{output_dir}/frame_{image_counter}.png", 'PNG', optimize=True, progressive=True)
                    gif.seek(gif.tell() + 1)  # Move to next frame
                    image_counter += 1
            except EOFError:
                pass
        return frames

gif_path = "1.gif"
output_dir = "_frames"
gif_path1 = "2.gif"
output_dir1 = "_frames1"

AnimationWindow(gif_path, output_dir).run() # Run first window
AnimationWindow(gif_path1, output_dir1).run() # Run second window ( First must be commented use # )

