# Deepracer

## TODO
* Reach out to community asking where to start with my skills
* Understand Inference
* Whos fastest at time trial

## Hyper parameters

* gradient descent batch size
TODO: REWORD!
`The number of recent vehicle experiences sampled at random from an experience buffer and used for updating the underlying deep-learning neural network weights. Random sampling helps reduce correlations inherent in the input data. Use a larger batch size to promote more stable and smooth updates to the neural network weights, but be aware of the possibility that the training may be longer or slower. The batch is a subset of an experience buffer that is composed of images captured by the camera mounted on the AWS DeepRacer vehicle and actions taken by the vehicle.`

* number of epochs
TODO: REWORD!
`The number of passes through the training data to update the neural network weights during gradient descent. The training data corresponds to random samples from the experience buffer. Use a larger number of epochs to promote more stable updates, but expect a slower training. When the batch size is small, you can use a smaller number of epochs.`

* learning rate
TODO: REWORD!
`During each update, a portion of the new weight can be from the gradient-descent (or ascent) contribution and the rest from the existing weight value. The learning rate controls how much a gradient-descent (or ascent) update contributes to the network weights. Use a higher learning rate to include more gradient-descent contributions for faster training, but be aware of the possibility that the expected reward may not converge if the learning rate is too large.`

* entropy
TODO: REWORD!
`The degree of uncertainty used to determine when to add randomness to the policy distribution. The added uncertainty helps the AWS DeepRacer vehicle explore the action space more broadly. A larger entropy value encourages the vehicle to explore the action space more thoroughly.`

* discount factor
TODO: REWORD!
`The discount factor determines how much of future rewards are discounted in calculating the reward at a given state as the averaged reward over all the future states. The discount factor of 0 means the current state is independent of future steps, whereas the discount factor 1 means that contributions from all of the future steps are included. With the discount factor of 0.9, the expected reward at a given step includes rewards from an order of 10 future steps. With the discount factor of 0.999, the expected reward includes rewards from an order of 1000 future steps.`

* loss type
TODO: REWORD!
`The type of the objective function to update the network weights. A good training algorithm should make incremental changes to the vehicle’s strategy so that it gradually transitions from taking random actions to taking strategic actions to increase reward. But if it makes too big a change then the training becomes unstable and the agent ends up not learning. The Huber and Mean squared error loss types behave similarly for small updates. But as the updates become larger, the Huber loss takes smaller increments compared to the Mean squared error loss. When you have convergence problems, use the Huber loss type. When convergence is good and you want to train faster, use the Mean squared error loss type.`

* number of experience episodes between each policy-updating iteration
TODO: REWORD!
`The size of the experience buffer used to draw training data from for learning policy network weights. An episode is a period in which the vehicle starts from a given starting point and ends up completing the track or going off the track. Different episodes can have different lengths. For simple reinforcement-learning problems, a small experience buffer may be sufficient and learning will be fast. For more complex problems which have more local maxima, a larger experience buffer is necessary to provide more uncorrelated data points. In this case, training will be slower but more stable. The recommended values are 10, 20 and 40.`

* SAC alpha (α) value
`Most algorithms’ objective functions focus only on maximizing total reward. SAC’s objective function maximizes both entropy (randomness) and total reward. This encourages your agent to keep exploring while it looks for rewards, which helps it become a life-long learner and prevents over fitting. The alpha value weights the importance of entropy. A higher α value encourages the agent to take actions that are more random.`


## Reward graph
* Average reward (Training)
* Average percentrage (Training)
* Average percentage completion (Evaluating)


## Tasks

## Terms
* Types of RL
    * Value based
    * Policy based
    * Model based
* Types of reinforcement
    * Primary
    * Secondary
    * Positive
    * Negative
* Environment: the world in which the agent lives in and interacts with
* Agent
* Action Space: Set of all valid possible actions an agent can perform
* Discrete vs Continuous action space
* Action space type
* Iteration
* Episode: group of actions and states agent performed from a start state to an end state
* Value function
* Reward
* Reward function: 
* Model
* Training Algos for hyper parameters
    * SAC
        * https://spinningup.openai.com/en/latest/algorithms/sac.html
    * PPO
        * https://openai.com/blog/openai-baselines-ppo/
* Policy Network: trained NN. Predicts next action based on video input
* Empirical
* Hyperparameters
* Learning rate: controls how many new experiences are counted in learning at each step. faster training with bigger rate, higher quality with lower rate
* Policy Iteration aka policy-updating iteration aka epoch: passes through randomly sampled training data to update the NN weights during gradient ascent
* Gradient ascent
* Evaluation sim trace CSV columns
    * Yaw
    * Steer
    * Throttle
    * Action
    * Done
    * All wheels on track
    * Progress
    * Closest waypoint
    * Track Len
    * tstamp
    * Episode status
    * Pause duration


## General Features


## QnA
* Can I export the model in sagemaker?
* other then the time limit, what else would stop training?
* what does the reward graph mean?
* Epoch vs Episode?
* Does it do any training during the evaluation phase?


￼￼
