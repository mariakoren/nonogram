import pygad, matplotlib as plt
import numpy as np
plt.style.use("default")


def nonogram_ga(nonogram, printing=True):
    gene_space = [0,1]
    
    nonogram_size = len(nonogram[0]) 
    num_genes = nonogram_size**2
    keep_parents = 2
    

    if (nonogram_size == 5):
        sol_per_pop = 120
        num_parents_mating = 60
        num_generations = 40
        parent_selection_type = "sss"
        crossover_type = "single_point"
        mutation_type = "random"
        mutation_percent_genes = 4
        
    elif (nonogram_size == 10):
        sol_per_pop = 300
        num_parents_mating = 100
        num_generations = 500
        parent_selection_type = "sss"
        crossover_type = "two_points"
        mutation_type = "random"
        mutation_percent_genes = 1
    
    elif (nonogram_size == 15):
        sol_per_pop = 300
        num_parents_mating = 150
        num_generations = 700
        parent_selection_type = "sss"
        crossover_type = "two_points"
        mutation_type = "random"
        mutation_percent_genes = 1
        
    else:
        print("Error: Nonogram size is not 5x5, 10x10 or 15x15!")
        return False
        

    def fitness_sequence(sequence, clues):
        fitness = 0
        seq_id = 0
        
        for clue in clues:
            
            #  Skip zeros in sequence
            while seq_id < len(sequence) and sequence[seq_id] == 0:
                seq_id += 1
                
            if seq_id == len(sequence):
                break
            
            # Count ones and check it matches to clue
            block_len = 0
            while seq_id < len(sequence) and sequence[seq_id] == 1:
                block_len += 1
                seq_id += 1
            
            if block_len == clue:
                # +1 point for each correct block
                fitness += 1
        
        if(seq_id < len(sequence)):
            # -1 point for each additional block
            fitness -= np.sum(sequence[seq_id:])
        
        return fitness

    # Main fitness function
    def fitness_func(model, solution, solution_idx):
        # Splits nonogram for columns and rows
        col_clues = np.array(nonogram[0], dtype=object)
        row_clues = np.array(nonogram[1], dtype=object)
        
        # Splits soluton to arrays of nonogram size
        grid = solution.reshape((len(row_clues), len(col_clues)))
        score = 0
        
        #  Checks each column solution
        for i in range(len(col_clues)):
            col_score = fitness_sequence(grid[:, i], col_clues[i])
            score += col_score
            
        # Checks each row solution
        for j in range(len(row_clues)):
            row_score = fitness_sequence(grid[j, :], row_clues[j])
            score += row_score
        return round(score,2)

        
    ga_instance = pygad.GA(fitness_func=fitness_func,
                           gene_space=gene_space,
                           num_genes=num_genes,
                           sol_per_pop=sol_per_pop,
                           num_parents_mating=num_parents_mating,
                           num_generations=num_generations,
                           keep_parents=keep_parents,
                           parent_selection_type=parent_selection_type,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes
                           )
    
    
    ga_instance.run()
    
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    
    # Function to validate the best solution, returns the precentage result.
    def accuracy_sol(nonogram, sol_fitness):
        col = np.concatenate( nonogram[0])
        row = np.concatenate(nonogram[1])
        clue_length = col.size + row.size
        return round(((sol_fitness*100)/clue_length),2)
    
    if (printing):
        # Nonogram
        print("Nonogram: ", nonogram)
        
        # Best solution 
        print("Best solution:")
        for i in range(0,len(nonogram[0])**2,len(nonogram[0])):
            print(solution[i:i+len(nonogram[0])])
            
        # Fitness score
        print("Solution score: ", solution_fitness)
        
        #  Accuracy 0-100%
        print("Accuracy: ", accuracy_sol(nonogram, solution_fitness),"%")
        
        # Shows plot - best scores in generations
        ga_instance.plot_fitness()
        
    return accuracy_sol(nonogram, solution_fitness)




nonogram_lvl1_1 = [
    [[1,1,1], [3], [5], [3], [1,1,1]],
    [[1,1,1], [3], [5], [3], [1,1,1]]
    ]
nonogram_lvl1_2 = [
    [[2], [1, 1], [1, 1], [1, 1], [2]],
    [[1,1], [1, 1,1], [1, 1], [1,1], [1]]
]

nonogram_lvl1_3 = [
    [[1], [2, 1], [5], [2, 1], [1]],
    [[1], [3], [5], [3], [1]]
]
nonogram_ga(nonogram_lvl1_3)