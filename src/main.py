from genetic_art import *
import os


POP_SIZE = 400
GENES_PER_INDIVIDUAL = 250
WIDTH = 256
HEIGHT = 256
NUM_GENERATIONS = 10000
MUTATION_RATE = 0.05

os.makedirs("../assets/results", exist_ok=True)

population = create_initial_population(POP_SIZE, GENES_PER_INDIVIDUAL, WIDTH, HEIGHT)

for generation in range(NUM_GENERATIONS):
    print(f"\n🔄 Generation {generation + 1}/{NUM_GENERATIONS}")
    best_individual = select_best_individuals(population, 1)[0]
    best_fitness = best_individual.fitness()
    print(f"🔥 Best fitness: {best_fitness}")
    
    if generation % 1000 == 0 or generation == NUM_GENERATIONS - 1:
        image = best_individual.to_image()
        image.save(f"../assets/results/gen_{generation:03d}.png")
    
    population = create_next_generation(population, POP_SIZE, MUTATION_RATE)


final_best = select_best_individuals(population, 1)[0]
image = final_best.to_image()
image.save("../assets/final_result.png")
print(f"\nDone ✅")
