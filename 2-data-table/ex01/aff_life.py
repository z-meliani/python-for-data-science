import matplotlib.pyplot as plt
from load_csv import load


def main():
    # Load the dataset
    df = load("../data/life_expectancy_years.csv")
    if df is None:
        return 1

    df_france = df.loc[df.country == "France"].drop(columns=["country"])

    # Convert columns to numpy arrays
    years = df_france.columns.to_numpy(dtype=int)
    life = df_france.to_numpy().T

    # Plot the data
    fig, ax = plt.subplots()

    ax.plot(years, life)
    ax.set_title("France Life expectancy Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Life expectancy")

    # Display figure
    fig.savefig("life_expectancy.jpg")
    # plt.show()


if __name__ == "__main__":
    main()
