function Population(target, m, num) {
  this.generations = 0;
  this.finished = false;
  this.target = target;
  this.mutationRate = m;
  this.best = "";
  this.matingPool = [];
  this.perfectScore = 1.0;
  
  this.population = [];
  for (var i = 0; i < num; i++) {
    this.population[i] = new DNA(this.target.length);
  }
  this.isFinished = function() {
    return this.finished;
  }
  
  this.getBest = function() {
    var worldRecord = 0.0;
    var index = 0;
    for (var i = 0; i < this.population.length; i++) {
      if (this.population[i].fitness > worldRecord) {
        index = i;
        worldRecord = this.population[i].fitness;
      }
    }
    if (worldRecord == this.perfectScore) this.finished = true;
    return this.population[index].getPhrase();
    
  }
  
  this.calcFitness = function() {
    for (var i = 0; i < this.population.length; i++) {
      this.population[i].calcFitness(target);
    }
  }
  
  this.createMatingPool = function() {
    this.matingPool = [];
    var maxFitness = 0;
    for (var i = 0; i < this.population.length; i++) {
      if (this.population[i].fitness > maxFitness) {
        maxFitness = this.population[i].fitness;
      }
    }
    
    for (var i = 0; i < this.population.length; i++) {
      var fitness = map(this.population[i].fitness, 0, maxFitness, 0, 1);
      var n = floor(fitness * 100);
      for (var j = 0; j < n; j++) {
        this.matingPool.push(this.population[i]);
      }
    }
    
  }
  
  this.reproduction = function() {
    
    for (var i = 0; i < this.population.length; i++) {
      var a = floor(random(this.matingPool.length));
      var b = floor(random(this.matingPool.length));
      var partnerA = this.matingPool[a];
      var partnerB = this.matingPool[b];
      var child = partnerA.crossover(partnerB);
      child.mutate(this.mutationRate);
      this.population[i] = child;
    }
    this.generations++;
    
  }
  
  
  
}