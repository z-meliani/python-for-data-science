from load_csv import load


def main():

    try:
        print(load("../data/life_expectancy_years.csv"))
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    main()
