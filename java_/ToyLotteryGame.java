package java_;

public class ToyLotteryGame {
    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();

        toyStore.addToy(1, "Teddy Bear", 5, 20);
        toyStore.addToy(2, "Doll", 3, 15);
        toyStore.addToy(3, "Race Car", 7, 10);

        toyStore.updateToyWeight(1, 30); // Update weight of Teddy Bear

        toyStore.playToyLottery();
    }
}
