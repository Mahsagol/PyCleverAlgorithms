#!/usr/bin/env python

"""
"""

def objective_function(v):
    return sum(map(lambda x : x**2, v))

def random_vector(minmax):
    import random
    return map(lambda x : x[0] + (x[1]-x[0]) * random.random(), minmax)

def create_particle(search_space, vel_space):
	particle = {}
  	particle['position'] = random_vector(search_space)
  	particle['cost'] = objective_function(particle['position'])
  	particle['b_position'] = particle['position'][:]
  	particle['b_cost'] = particle['cost']
  	particle['velocity'] = random_vector(vel_space)
  	return particle

def get_global_best(population, current_best=None):
  	population.sort(key=lambda x: x['cost']) 
  	best = population[0]
  	if current_best == None or best['cost'] <= current_best['cost'] : 
   		current_best = {}
    	current_best['position'] = best['position'][:]
    	current_best['cost'] = best['cost']
  	return current_best

def update_velocity(particle, gbest, max_v, c1, c2):
	pass

def update_position(part, bounds):
	pass

def update_best_position(particle):
	if particle['cost'] > particle['b_cost']:
		return
  	particle['b_cost'] = particle['cost']
  	particle['b_position'] = particle['position'][:]

def search(max_gens, search_space, vel_space, pop_size, max_vel, c1, c2):
	pass

def main():
	# problem configuration
  	problem_size = 2
  	search_space = [[-5,5]] * problem_size
  	# algorithm configuration
  	vel_space = [[-1,1]] * problem_size
  	max_gens = 100
  	pop_size = 50
  	max_vel = 100.0
  	c1, c2 = 2.0, 2.0
  	# execute the algorithm
  	best = search(max_gens, search_space, vel_space, pop_size, max_vel, c1, c2)
  	print 'Done. Best Solution: c=%f, v=%s' % (best['cost'], str(best['vector']))

if __name__ == "__main__":
    main()