from PIL import Image, ImageDraw
import numpy as np

class Gene:
    def __init__(self, points, color):
        self.points = points
        self.color = color
    
    def mutate(self):
        pass


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
        target_image = Image.open("assets/mona_resized.png").convert("RGBA")
        target_array = np.array(target_image, dtype=np.int16)
        generated_array = np.array(self.to_image, dtype=np.int16)
        diff = target_array - generated_array
        mse = np.mean(np.square(diff))
        fitness_score = 1/(mse + 1e-8)
        return fitness_score
        
    def mutate(self):
        pass
    
    
triangle_points = [(50, 50), (200, 80), (100, 200)]
triangle_color = (255, 0, 0, 128)  
test_gene = Gene(triangle_points, triangle_color)


test_individual = Individual([test_gene])


img = test_individual.to_image()


img.show()