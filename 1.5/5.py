class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data = data[:]

    def _get_str_print(self):
        return ' '.join(map(str, self.data))

    def _show_disable_graph(self):
        print('Отображение данных закрыто')

    def show_table(self):
        if self.is_show:
            print(self._get_str_print())
        else:
            self._show_disable_graph()

    def show_graph(self):
        if self.is_show:
            print(f'Графическое отображение данных: {self._get_str_print()}')
        else:
            self._show_disable_graph()

    def show_bar(self):
        if self.is_show:
            print(f'Столбчатая диаграмма: {self._get_str_print()}')
        else:
            self._show_disable_graph()

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
