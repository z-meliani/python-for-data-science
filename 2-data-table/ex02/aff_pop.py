from load_csv import load


def convert(x):
    """Convert a string with magnitude suffix into a numeric value."""

    magnitude = {"k": 1e3, "M": 1e6}

    try:

        if isinstance(x, str) and x[-1] in magnitude:
            return float(x[:-1]) * magnitude[x[-1]]
        else:
            float(x)

    except Exception as e:
        print(f"Error: {e}")
        return float('NaN')


def magnitude(x, pos):
    """Format a matplotlib axis values"""

    return f'{int(x*1e-6)}M'


def main():
    # Load the dataset
    df = load("../data/population_total.csv")
    if df is None:
        return 1

    # Keep data for France and Belgium an transpose the dataframe
    df = df.loc[df.country.isin(["France", "Belgium"])].T

    # Set country line as columns labels
    df = df.rename(columns=df.loc["country"]).drop(index="country")

    # Change index type from str to int
    df.index = df.index.astype(int)

    # Unsure that index is sortded
    df = df.sort_index()

    # Keep only values until 2050
    df = df.loc[:2050]

    # Convert str values to numeric ones
    df = df.map(convert)

    # Plot the data
    ax = df.plot()

    # Set title and labels
    ax.set_title("Population Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Populations")

    # Format y axis ticks
    ax.set_yticks([20e6, 40e6, 60e6])
    ax.yaxis.set_major_formatter(magnitude)

    # Display figure
    fig = ax.figure
    fig.savefig("population_total.jpg")
    # plt.show()


if __name__ == "__main__":
    main()
