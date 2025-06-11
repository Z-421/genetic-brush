from PIL import Image, ImageDraw
import numpy as np
import random

class Gene:
    def __init__(self, points, colors):
        self.points = points
        self.colors = colors
    
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
        
        new_colors = []
        for color in self.colors:
            if random.random() < mutation_rate:
                delta = random.randint(-20, 20)
                new_val = max(0, min(color + delta, 255))
            else:
                new_val = color
            new_colors.append(new_val)
        self.colors = tuple(new_colors)


class Individual:
    def __init__(self, list_gene):
        self.list_gene = list_gene
    
    def to_image(self):
        width = 256
        height = 256
        image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image, "RGBA")
        for gene in self.list_gene:
            draw.polygon(gene.points, fill=gene.colors)
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
            if random.random() < 0.2:
                gene.mutate(mutation_rate)


def create_random_gene(width, height):
    points = [(random.randint(0,width), random.randint(0,height)) for _ in range(3)]
    colors = (
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,150)
    )
    
    return Gene(points, colors)

def create_random_individual(genes_per_individual, width, height):
    return Individual([create_random_gene(width, height) for _ in range(genes_per_individual)])

def create_initial_population(population_size, genes_per_individual, width, height):
    population = []

    for _ in range(population_size):
        individual = create_random_individual(genes_per_individual, width, height)
        population.append(individual)
    
    return population

def select_best_individuals(population, n_best):
    best_scores = []
    for x in population:
        score = Individual.fitness(x)
        best_scores.append((x,score))
    
    sorted_list = sorted(best_scores, key=lambda x: x[1], reverse=True)
    best_individuals = [individual for individual, score in sorted_list[:n_best]]
    return best_individuals
    

def crossover(parent1, parent2):
    if len(parent1.list_gene) == len(parent2.list_gene):
        n_genes = len(parent1.list_gene)
        new_genes = []
        for i in range(n_genes):
            if random.random() < 0.5:
                copied_points = [(x, y) for (x, y) in parent1.list_gene[i].points]
                copied_colors = tuple(parent1.list_gene[i].colors)

            else:
                copied_points = [(x, y) for (x, y) in parent2.list_gene[i].points]
                copied_colors = tuple(parent2.list_gene[i].colors)
            
            new_gene = Gene(copied_points, copied_colors)
            new_genes.append(new_gene)
        return Individual(new_genes)

def create_next_generation(population, num_offspring, mutation_rate):
    n_best = max(2, int(len(population) * 0.1))
    elites = select_best_individuals(population, n_best)
    children = []
    num_children = len(population) - len(elites)
    while len(children) < num_children:
        parent1, parent2 = random.sample(elites,2)
        child = crossover(parent1, parent2)
        child.mutate(mutation_rate)
        children.append(child)
    8
    return elites + children
