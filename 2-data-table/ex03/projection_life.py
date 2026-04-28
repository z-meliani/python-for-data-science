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
    x = abs(x)

    if x >= 1e6:
        return f'{int(x * 1e-6)}M'
    elif x >= 1e3:
        return f'{int(x * 1e-3)}k'
    else:
        return f'{int(x)}'


def main():

    # Load datasets
    file = {
        "income": "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
        "life": "life_expectancy_years.csv"
        }

    df_income = load(f"../data/{file['income']}")
    if df_income is None:
        return 1

    df_life = load(f"../data/{file['life']}")
    if df_life is None:
        return 1

    # Keep columns "country" an "1900"
    df_income = df_income.loc[..., ["country", "1900"]]
    df_life = df_life.loc[..., ["country", "1900"]]

    # Rename columns
    df_income = df_income.rename(columns={"1900": "income"})
    df_life = df_life.rename(columns={"1900": "life"})

    # Merge the DFs on 'country' column
    df = (df_income.merge(df_life, on='country', how='outer')
          .drop(columns='country'))

    # Plot the data
    ax = df.plot.scatter(x='income', y='life')

    ax.set_title('1900')
    ax.set_xlabel('Gross domestic product')
    ax.set_xscale('log')
    ax.set_ylabel('Life Expectancy')

    # Format x axis ticks
    ax.set_xticks([300, 1e3, 1e4])
    ax.xaxis.set_major_formatter(magnitude)

    # Display figure
    fig = ax.figure
    fig.savefig("income_life.jpg")
    # plt.show()


if __name__ == "__main__":
    main()
