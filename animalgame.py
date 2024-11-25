class Animal:
    def __init__(self, name, characteristic_question, characteristic_answer, fun_facts):
        self.name = name
        self.characteristic_question = characteristic_question
        self.characteristic_answer = characteristic_answer
        self.fun_facts = fun_facts

    def ask_question(self):
        print(f"Here is your question about {self.name}:")
        print(self.characteristic_question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == self.characteristic_answer.lower():
            print("Correct! Great job!")
        else:
            print(f"Oops! The correct answer was: {self.characteristic_answer}")

    def display_fun_facts(self):
        print(f"\nHere are 5 fun facts about {self.name}:")
        for fact in self.fun_facts:
            print(f"- {fact}")


# Animal instances
cat = Animal(
    name="Cat",
    characteristic_question="What is the average number of hours a cat sleeps per day?",
    characteristic_answer="12",
    fun_facts=[
        "Cats have retractable claws.",
        "A group of cats is called a clowder.",
        "Cats can run up to 30 miles per hour.",
        "Domestic cats can jump up to six times their body length.",
        "Cats' purring is often a sign of contentment, but it can also be a healing mechanism."
    ]
)

dog = Animal(
    name="Dog",
    characteristic_question="Which breed of dog has the longest lifespan?",
    characteristic_answer="Chihuahua",
    fun_facts=[
        "Dogs have a sense of time and can predict future events, like when their owner will come home.",
        "A Greyhound can run at speeds of up to 45 miles per hour.",
        "Dogs have three eyelids.",
        "Dogs' noses are wet to help absorb scent chemicals.",
        "The Basenji dog is known for not barking, but instead yodeling."
    ]
)

dinosaurs = Animal(
    name="Dinosaurs",
    characteristic_question="What is the name of the largest dinosaur ever discovered?",
    characteristic_answer="Argentinosaurus",
    fun_facts=[
        "Dinosaurs first appeared during the Triassic period, around 230 million years ago.",
        "Some dinosaurs had feathers, not just reptiles.",
        "Tyrannosaurus rex had the strongest bite of any land animal.",
        "The longest dinosaur was the Argentinosaurus, reaching lengths of over 100 feet.",
        "Not all dinosaurs were massive; some were the size of a chicken."
    ]
)

dolphins = Animal(
    name="Dolphin",
    characteristic_question="Which species of dolphin is known for its ability to use tools?",
    characteristic_answer="Indo-Pacific bottlenose dolphin",
    fun_facts=[
        "Dolphins can recognize themselves in mirrors, showing signs of self-awareness.",
        "Dolphins have names for each other, using specific whistles.",
        "They sleep with one hemisphere of their brain at a time.",
        "Dolphins communicate using a series of clicks and whistles.",
        "Some dolphins use marine sponges as tools to protect their snouts while foraging."
    ]
)

sharks = Animal(
    name="Shark",
    characteristic_question="Which species of shark is known for having the most powerful bite force?",
    characteristic_answer="Great White Shark",
    fun_facts=[
        "Sharks have been around for over 400 million years.",
        "Some sharks can detect one drop of blood in 25 gallons of water.",
        "Great white sharks can grow up to 20 feet in length.",
        "Sharks never stop growing teeth; they shed up to 30,000 teeth a year.",
        "Sharks can live for decades, with some species reaching over 100 years old."
    ]
)

ants = Animal(
    name="Ant",
    characteristic_question="What is the fastest known species of ant?",
    characteristic_answer="Saharan silver ant",
    fun_facts=[
        "Ants can carry objects 50 times their body weight.",
        "Ants communicate using chemicals called pheromones.",
        "Some species of ants can live for up to 30 years.",
        "The army ant species has no permanent nest and moves in massive colonies.",
        "Ants are found on every continent except Antarctica."
    ]
)

# Animal selection
def select_animal():
    print("Please select an animal: ")
    animals = ["Cat", "Dog", "Dinosaurs", "Dolphins", "Sharks", "Ants"]
    for index, animal in enumerate(animals, 1):
        print(f"{index}. {animal}")
    
    choice = int(input("Enter the number corresponding to your choice: "))
    if choice == 1:
        return cat
    elif choice == 2:
        return dog
    elif choice == 3:
        return dinosaurs
    elif choice == 4:
        return dolphins
    elif choice == 5:
        return sharks
    elif choice == 6:
        return ants
    else:
        print("Invalid choice. Please choose a number between 1 and 6.")
        return select_animal()

def main():
    print("Welcome to the Animal Fun Facts Game!")
    selected_animal = select_animal()
    
    selected_animal.ask_question()
    selected_animal.display_fun_facts()

if __name__ == "__main__":
    main()
