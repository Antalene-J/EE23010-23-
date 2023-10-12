#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n = 2;  // Number of trials
    double p = 0.5;  // Probability of success
    int num_simulations = 10000;  // You can adjust the number of simulations as needed

    int success_count = 0;

    srand(time(NULL));  // Seed the random number generator

    for (int i = 0; i < num_simulations; i++) {
        // Simulate n trials with probability of success p
        int k = 0;
        for (int j = 0; j < n; j++) {
            double random_value = (double)rand() / RAND_MAX;  // Generate a random value between 0 and 1
            if (random_value < p) {
                k++;
            }
        }

        if (k <= 1) {
            success_count++;
        }
    }

    // Calculate the probability of k <= 1
    double probability = (double)success_count / num_simulations;

    printf("Probability of k <= 1: %f\n", probability);

    return 0;
}

