package java_;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class ToyStore {
    private List<Toy> toys;
    private Random random;

    public ToyStore() {
        toys = new ArrayList<>();
        random = new Random();
    }

    public void addToy(int id, String name, int quantity, int weight) {
        Toy toy = new Toy(id, name, quantity, weight);
        toys.add(toy);
    }

    public void updateToyWeight(int id, int weight) {
        for (Toy toy : toys) {
            if (toy.getId() == id) {
                toy.setWeight(weight);
                return;
            }
        }
        System.out.println("Toy not found.");
    }

    public void playToyLottery() {
        int totalWeight = 0;
        for (Toy toy : toys) {
            totalWeight += toy.getWeight();
        }

        if (totalWeight == 0) {
            System.out.println("No toys available.");
            return;
        }

        int randomNumber = random.nextInt(totalWeight) + 1;
        int cumulativeWeight = 0;
        for (Toy toy : toys) {
            cumulativeWeight += toy.getWeight();
            if (randomNumber <= cumulativeWeight) {
                if (toy.getQuantity() > 0) {
                    toy.setQuantity(toy.getQuantity() - 1);
                    System.out.println("Congratulations! You won a " + toy.getName() + "!");
                } else {
                    System.out.println("Sorry, the toy is out of stock.");
                }
                return;
            }
        }
    }
}
