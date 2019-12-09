import cartpole_dqn
import pylab
import datetime

def experiment_hidden_layers():
    episodes = {}
    scores = {}
    max_q_mean = {}
    experiments = [[1], [16], [32], [16,16], [32,32], [64,64]]
    for l in range(len(experiments)):
        hid_layers = experiments[l]
        episodes[l], scores[l], max_q_mean[l] = cartpole_dqn.experiment("hid_layers", hid_layers)
    plot_data(episodes, scores, max_q_mean, "hid_layers", experiments)


#Plots the different runs of the experiment in one plot
def plot_data(episodes, scores, max_q_mean, exp_type, experiments):
    colors = ['b', 'r', 'g', 'k', 'pink', 'purple']
    pylab.figure(0)
    for i in range(len(experiments)):
        pylab.plot(episodes[i], max_q_mean[i], colors[i], label=str(experiments[i]))
    pylab.xlabel("Episodes")
    pylab.ylabel("Average Q Value")
    pylab.legend()
    qvalues_fig = "qvalues_" + str(exp_type) + str(datetime.datetime.now()) + ".png"
    pylab.savefig(qvalues_fig)

    pylab.figure(1)
    for i in range(len(experiments)):
        pylab.plot(episodes[i], scores[i], colors[i], label=str(experiments[i]))
    pylab.xlabel("Episodes")
    pylab.legend()
    scores_fig = "scores_" + str(exp_type) + str(datetime.datetime.now()) +  ".png"
    pylab.savefig(scores_fig)

if __name__ == "__main__":
    experiment_hidden_layers()



