def dim_4(self):
    self.nodes = []
    for l in [0, 1]:
        if l == 0:
            for k in [0, 1]:
                if k == 0:
                    for j in [0, 1]:
                        if j == 0:
                            for i in [0, 1]:
                                self.nodes.append([i, j, k, l])
                        else:
                            for i in [1, 0]:
                                self.nodes.append([i, j, k, l])

            else:

                for i in [0, 1]:
                    if i == 0:
                        for j in [1, 0]:
                            self.nodes.append([i, j, k, l])
                    else:
                        for j in [0, 1]:
                            self.nodes.append([i, j, k, l])

        else:
            for j in [1, 0]:
                if j == 1:
                    for k in [1, 0]:
                        if k== 1:
                            for i in [1, 0]:
                                self.nodes.append([i, j, k, l])
                        else:
                            for i in [0, 1]:
                                self.nodes.append([i, j, k, l])
                else:
                    for i in [1, 0]:
                        if i== 1:
                            for k in [0, 1]:
                                self.nodes.append([i, j, k, l])
                        else:
                            for k in [1, 0]:
                                self.nodes.append([i, j, k, l])
