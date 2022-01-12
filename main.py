import visualizer
import webscraper


def main():
    webscraper.download_JHU()
    visualizer.visualize(country="Germany")


if __name__ == "__main__":
    main()
