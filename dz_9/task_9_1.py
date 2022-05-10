from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        count = 0
        while count != 3:
            print(TrafficLight.__color[count])
            if count == 0:
                sleep(3)
            elif count == 1:
                sleep(2)
            elif count == 2:
                sleep(3)
            count += 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
