# Blackjack Reinforcement Learning

## Teaching AI to play Blackjack using Reinforcement learning algorithms

---

### Effectivness of algorithms (milion epocs, milion games to test on)

| Algorithm                      | Win     | Draw   | Lose    |
|--------------------------------|---------|--------|---------|
| Deterministic                  | 42.95%  | 9.41%  | 47.63%  |
| Monte Carlo Exploring Starts   | 43.04%  | 9.38%  | 47.57%  |
| On Policy Monte Carlo          | 43.18%  | 8.76%  | 48.07%  |
| Sarsa                          | 42.81%  | 9.23%  | 47.95%  |
| Q-Learning                     | 42.86%  | 9.34%  | 47.79%  |

---

### Number of actions different than in deterministic algorithm (max = 200)

| Algorithm                      | Number
|--------------------------------|--------
| Deterministic                  | 0
| Monte Carlo Exploring Starts   | 3
| On Policy Monte Carlo          | 7
| Sarsa                          | 10
| Q-Learning                     | 10

---

### Time taken to train agent using 10000 epocs

| Algorithm                      | Time
|--------------------------------|--------
| Deterministic                  | 0s
| Monte Carlo Exploring Starts   | 7.15s
| On Policy Monte Carlo          | 6.48s
| Sarsa                          | 10.16s
| Q-Learning                     | 10.25s

# Detailed statistics

Actions, that are diffrent than in deterministic algorithm

## 1. Monte Carlo ES

Dealer sum: 2  
Player sum: 13  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  

Dealer sum: 11  
Player sum: 16  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Dealer sum: 11  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Number of differences:  3  
WIN = 43.0441%  
DRAW = 9.3818%  
LOSE = 47.5741%  

---

## 2. On-policy first-visit MC control

Dealer sum: 3  
Player sum: 12  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Dealer sum: 10  
Player sum: 15  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Dealer sum: 11  
Player sum: 15  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Dealer sum: 10  
Player sum: 16  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Dealer sum: 11  
Player sum: 16  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Dealer sum: 10  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Dealer sum: 11  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  
  
Number of differences:  7  
WIN = 43.1793%  
DRAW = 8.7557%  
LOSE = 48.065000000000005%  
  
---

## 3. Q-learning (off-policy TD control)

Dealer sum: 2  
Player sum: 13  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 11  
Player sum: 14  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  
  
Dealer sum: 2  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 3  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 4  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 5  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 6  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 8  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 10  
Player sum: 19  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 11  
Player sum: 19  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Number of differences:  10  
  
WIN = 42.8647%  
DRAW = 9.346599999999999%  
LOSE = 47.7887%  
  
---

## 4. Sarsa (on-policy TD control)

Dealer sum: 3  
Player sum: 12  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  
  
Dealer sum: 2  
Player sum: 13  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 11  
Player sum: 13  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  
  
Dealer sum: 6  
Player sum: 16  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 11  
Player sum: 16  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  

Dealer sum: 8  
Player sum: 17  
Player usable ace: False  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 4  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 5  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 6  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.STAND  
AGENT POLICY:  Action.HIT  
  
Dealer sum: 11  
Player sum: 18  
Player usable ace: True  
DETERMINISTIC POLICY:  Action.HIT  
AGENT POLICY:  Action.STAND  
  
Number of differences:  10  

WIN = 42.8189%  
DRAW = 9.231%  
LOSE = 47.9501%  

## Author

* **Wojciech Buczek**