import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




class Betting_Simualtion:
    def __init__(self, starting_fund = 10000 , wager = 1000, wager_count = 1000, sample_size = 1000, win_prob = 0.49):
        self.starting_fund = starting_fund
        self.wager = wager
        self.wager_count = wager_count
        self.sample_size = sample_size
        self.win_prob = win_prob
    
    def roll(self):
        return random.random() < self.win_prob
    
    def simple_bettor(self):
        value = self.starting_fund
        for _ in range(self.wager_count):
            if value <= 0:
                return 0, True
            if self.roll():
                value += self.wager
            else:
                value -= self.wager
        return value, False
    
    def martingale_bettor(self):
        value = self.starting_fund
        wager = self.wager
        for _ in range(self.wager_count):
            if wager > value:
                return 0, True
            if self.roll():
                value += wager
                wager = self.wager
            else:
                value -= wager
                wager *= 2
        return value, False
             
    def simulate(self, strategy):
        results = []
        ruin_counts = 0
        for _ in range(self.sample_size):
            final_value, broke = strategy()
            results.append(final_value)
            if broke:
                ruin_counts += 1
        
        results = np.array(results)


        stats = {
            'final_mean': np.mean(results),
            'final_median': np.median(results),
            'final_std': np.std(results),
            'ruin_probability': ruin_counts / self.sample_size,
            'avg_log_growth': np.mean(np.log((results+1) / self.starting_fund))
        }

        return results, stats

    def plot_results(self, results, strategy_name):
        sns.histplot(results, bins=30, kde=True)
        plt.title(f'{strategy_name} Final Values Distribution')
        plt.xlabel('Final Value')
        plt.ylabel('Frequency')
        plt.show()


if __name__ == "__main__":
    sim = Betting_Simualtion()
    
    simple_results, simple_stats = sim.simulate(sim.simple_bettor)
    print("Simple Bettor Stats:", simple_stats)
    sim.plot_results(simple_results, "Simple Bettor")
    
    martingale_results, martingale_stats = sim.simulate(sim.martingale_bettor)
    print("Martingale Bettor Stats:", martingale_stats)
    sim.plot_results(martingale_results, "Martingale Bettor")

