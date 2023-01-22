class RunArray:
    def __init__(self):
        # runs are triples in the form (starting index, length, data)
        self.__runs = list()
        self.__total_length = 0

    def add_run(self, starting_index: int, length: int, data) -> None:
        self.__update_run_length(starting_index, length)
        new_run = (starting_index, length, data)
        self.__runs.append(new_run)

    def get(self, index: int):
        # going through the reversed list in order to reach overridden data first
        for run in reversed(self.__runs):
            starting_index = run[0]
            ending_index = run[0] + run[1]
            data = run[2]
            if starting_index <= index <= ending_index:
                return data
        raise IndexError("Index outside of range")

    def append_run(self, length: int, data) -> None:
        starting_index = self.__total_length
        new_run = (starting_index, length, data)
        self.__update_run_length(starting_index, length)
        self.__runs.append(new_run)

    def __update_run_length(self, starting_index: int, length: int) -> None:
        end_index = starting_index + length
        if end_index > self.__total_length:
            self.__total_length = end_index
