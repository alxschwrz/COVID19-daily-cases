import visualizer
import webscraper
import sys


def main():
    if len(sys.argv) > 1:
        country = str(sys.argv[1])
    else:
        country = "Germany"
    webscraper.download_JHU()
    visualizer.visualize(country=country)


if __name__ == "__main__":
    main()
