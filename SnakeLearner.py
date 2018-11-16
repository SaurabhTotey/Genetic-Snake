import tensorflow

class DeepQNeuralNetworkAgent:

    def __init__(self):
        self.future_uncertainty_discount_rate = 0.9
        self.short_memory = []
        self.memory = []

        self.model = tensorflow.keras.models.Sequential()
        self.model.add(tensorflow.keras.layers.Dense(120, activation='relu'))
        self.model.add(tensorflow.keras.layers.Dropout(0.15))
        self.model.add(tensorflow.keras.layers.Dense(120, activation='relu'))
        self.model.add(tensorflow.keras.layers.Dropout(0.15))
        self.model.add(tensorflow.keras.layers.Dense(120, activation='relu'))
        self.model.add(tensorflow.keras.layers.Dropout(0.15))
        self.model.add(tensorflow.keras.layers.Dense(4, activation='softmax'))
        self.model.compile(loss='mse', optimizer=tensorflow.keras.optimizers.Adam(0.0005))

    def train(self, initial_state, taken_action, output_reward, is_done):
        self.model.fit([initial_state, taken_action], output_reward, verbose=0)
        self.memory.append((initial_state, taken_action, output_reward))
