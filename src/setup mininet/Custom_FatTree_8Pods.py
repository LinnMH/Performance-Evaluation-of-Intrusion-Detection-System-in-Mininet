from mininet.topo import Topo

class FatTree(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Number of pods
        k = 8

        # Core switches
        cores = [self.addSwitch('c{}'.format(i + 1)) for i in range((k // 2) ** 2)]
        #notes from zakaria
        for x in range(len(cores)):
            print (cores[x])
            	
        # Aggregation switches
        aggs = [[self.addSwitch('a{}_{}'.format(pod, i + 1)) for i in range(k // 2)] for pod in range(k)]
        #notes from zakaria
        for x in range(len(aggs)):
          print(aggs[x])
	
        # Edge switches
        edges = [[self.addSwitch('e{}_{}'.format(pod, i + 1)) for i in range(k // 2)] for pod in range(k)]
        #notes from zakaria
        for x in range(len(edges)):
          print(edges[x])

        # Hosts
        hosts = [[self.addHost('h{}_{}'.format(pod, i + 1)) for i in range(((k**3) // 4) // k)] for pod in range(k)]
        #notes from zakaria
        for x in range(len(hosts)):
          print(hosts[x])

        # Connect Core switches to Aggregation switches
        for i, core in enumerate(cores):
            for j in range(k):
                self.addLink(core, aggs[j][i // (k // 2)])

        # Connect Aggregation switches to Edge switches
        for i in range(k):
          for edge in edges[i]:
            for agg in aggs[i]:
              self.addLink(agg, edge)              
                                                                          							
        # Connect Edge switches to Hosts       
        for i in range(k):
          for j in range(k // 2):
            for h in range(k // 2):
              self.addLink(edges[i][j], hosts[i][j * 4 + h])
                       

topos = {'fattree': (lambda: FatTree())}
