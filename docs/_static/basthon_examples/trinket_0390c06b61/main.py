from pylab import *

organismer = ["Zooplankton", "Istidskreps", "Krøkle", "Lagesild", "Lake", "Brunørret"]
D5_mjøsa = [2.3, 11.8, 65.2, 161.9, 157.4, 2042]
D5_randsfjorden = [1.82, 0, 18.8, 0, 0, 46.78]

plot(organismer, D5_mjøsa, color = "Steelblue",
    label = "Mjøsa", linestyle = ":", marker = "s")
plot(organismer, D5_randsfjorden, color = "darkseagreen",
    label = "Randsfjorden", linestyle = "-", marker = "^")
xlabel("Organisme")
ylabel("ng siloksan per g fettvev (ng/g)")
ylim(0, 200)
legend()
show()