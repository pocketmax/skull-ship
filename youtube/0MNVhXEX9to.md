# Steve Brunton - Reinforcement Learning: Machine Learning Meets Control Theory

https://www.youtube.com/watch?v=0MNVhXEX9to

## tags
ai,ml,rl,theory

RL: Framework for learning from experience

Label: Spread throughout environment and indicate “yes” you got a reward or “no” you didn’t
* regular supervised learning. 

Time delayed label: reward is delayed I.e. at the end of a mouse maze or when someone wins in chess
* Not linked to actions
* Used with Semi-Supervised Learning

Discount rate: 
Gamma constant: says how much you favor getting a reward now vs later

Figuring out what actions where good or bad is a very hard optimization problem

goal: optimize policy to maximize future rewards

MDP: Markov Decision Process


Optimization
* Differential Programming
* Monte Carlo
* Temporal Difference
* Bellman 1957
* Exploration vs Exploitation
* Policy Iteration
* Gradient Descent
* Evolutionary optimization, Simulated Annealing

Q-Learning: Q(s,a) = quality of state/action pair

Imitation Learning

## Direct terms
* Hindsight Replay
* Credit Assignment Problem
    * Central challenge in RL
    * Dense vs sparse rewards
    * Sample Efficiency


## Indirect terms (terms used as part of explanation of subject matter)
* Control Theory
* sample
    * Control law
    * Deterministic environment
    * probabilistic environment
    * Probabilistic policy
    * Deterministic policy
* Sample inefficiency
* Fully deterministic
* Stochastic
* Reward shaping: person adds intermediate rewords to help


## QnA
Why use pi symbol? What does that have to do with RL
Policy