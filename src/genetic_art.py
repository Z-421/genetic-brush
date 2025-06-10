from PIL import Image, ImageDraw
import numpy as np
import random

class Gene:
    def __init__(self, points, color):
        self.points = points
        self.color = color
    
    def mutate(self, mutation_rate = 0.1,max_width=256, max_height=256):
        new_points = []
        for (x, y) in self.points:
            if random.random() < mutation_rate:
                dx = random.randint(-10, 10)
                dy = random.randint(-10, 10)
                x = max(0, min(x + dx, max_width - 1))
                y = max(0, min(y + dy, max_height - 1))
            new_points.append((x, y))
        self.points = new_points


class Individual:
    def __init__(self, list_gene):
        self.list_gene = list_gene
    
    def to_image(self):
        width = 256
        height = 256
        image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image, "RGBA")
        for gene in self.list_gene:
            draw.polygon(gene.points, fill=gene.color)
        return image
    
    def fitness(self):
        target_image = Image.open("../assets/mona_resized.png").convert("RGBA")
        target_array = np.array(target_image, dtype=np.int16)
        generated_array = np.array(self.to_image(), dtype=np.int16)
        diff = np.abs(target_array - generated_array)
        mse = np.mean(diff)
        fitness_score = 1/(mse + 1)
        return fitness_score
        
    def mutate(self, mutation_rate = 0.1):
        for gene in self.list_gene:
            gene.mutate(mutation_rate)