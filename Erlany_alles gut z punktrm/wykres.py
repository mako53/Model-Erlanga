import matplotlib.pyplot as plt

def generate_graph(x, y, lines, graph,x2=None,y2=None):
    plt.figure(figsize=(10, 6))

    if graph == "Traffic":
        if isinstance(y[0], list):
            for i in range(len(y)):
                plt.plot(x, y[i], "o:", label=str(lines[i]) + " Block Rate")
        else:
            plt.plot(x, y, "o:", label=str(lines[0]) + " Block Rate")
        plt.title('Block Rate/Traffic Graph')
        plt.grid(True)
        plt.xlabel('Traffic')
        plt.ylabel('Lines')

    elif graph == "Lines":
        if isinstance(y[0], list):
            for i in range(len(y)):
                plt.plot(x, y[i], "o:", label=str(lines[i]) + " Block Rate")
        else:
            plt.plot(x, y, "o:", label=str(lines[0]) + " Block Rate")
        plt.title('Block Rate/Lines Graph')
        plt.grid(True)
        plt.xlabel('Lines')
        plt.ylabel('Traffic')

    if x2 is not None and y2 is not None:
        plt.scatter(x2, y2, color='red',zorder=5, label='Podany punkt')

    plt.legend()
    plt.show()

