import gym

def demo():
    env = gym.make('CartPole-v0')
    env.reset()

    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample())

    env.close()

def demo2():
    env = gym.make('Ant-v2')

    for i in range(20):
        observe = env.reset()

        for t in range(10):
            env.render()
            print(observe)

            action = env.action_space.sample()
            observe, reward, done, info = env.step(action)

            if done:
                print("Episode finished after {} timestep".format(t + 1))
                break
    env.close()

def demo3():
    env = gym.make('Ant-v2')
    print(env.action_space)
    print(env.observation_space.high)
    print(env.observation_space.low)

if __name__ == "__main__":
    demo2()