import matplotlib.pyplot as plt
import numpy as np
from game_improved import get_team_metric


# has to be equal/over 1980
def get_years(year, year_range=2):
    year_int = int(year)
    year_array = [year]

    #0,1,2
    for i in range(1, year_range+1):
        year_array.append(str(year_int+i))
        year_array.insert(0, str(year_int-i))
    return year_array


def pure_game_metric(team_id, year, year_range=2):
    years = get_years(year, year_range)
    yearly_pgms = []
    for year_i in years:
        pgm = get_team_metric(team_id, year_i)
        yearly_pgms.append([int(year_i), pgm])
        print("{} {}: {}".format(year_i, team_id, pgm))
    return yearly_pgms  # [[year(int), pgm], ...]


def get_x_y(tuple):
    x = list(map(lambda x_and_y: x_and_y[0], tuple))
    y = list(map(lambda x_and_y: x_and_y[1], tuple))
    return x, y


# team_tuple = [['GSW','2016'], ['GSW','2016'], ['GSW','2016'], ... ]
def plot_multiple_teams(team_tuples, same_range=False, year_range=2):
    multiple_teams_pgms = []

    # tuple = [team_id, year(str)]
    for tuple in team_tuples:
        multiple_teams_pgms.append([pure_game_metric(tuple[0], tuple[1], year_range), tuple])
        print()

    # team_pgms = [ [tuples of year(int) and corresponding pgm], [team_id, year(str)] ]
    for team_pgms in multiple_teams_pgms:
        x = []
        x, y = get_x_y(team_pgms[0])

        if same_range:
            x = np.arange(1,2*year_range+2)
        legend_years = "{} - {}".format(int(team_pgms[1][1])-year_range, int(team_pgms[1][1])+year_range)
        plt.plot(x, y, marker='o', markerfacecolor='purple', markersize=4, linewidth=2, label="{} {}".format(legend_years, team_pgms[1][0]))

    if same_range:
        plt.axis([0, 2*year_range+2, 0, 100])
    else:
        plt.axis([1980, 2020, 0, 100])

    plt.title("Teams' Pure Game Rating (PGR) Over {} Years".format(2*year_range+1))
    plt.legend()
    plt.show()


def interactive():

    presets = [ [['GSW','2016'], ['CHI','1996'], ['LAL','1987'], ['BOS','1986'], ['LAL','2002']],
                [['GSW', '2017'], ['CHI', '1996'], ['LAL', '1987']],
                [['CHI', '1996'], ['CLE', '2016']] ]

    teams_to_plot = []
    same_range_or_no = True

    preset_or_no = input('Enter a number 0-2 to use a preset. Enter any other key to do manual: ')
    try:
        preset_id = int(preset_or_no)
        teams_to_plot = presets[preset_id]
        range_years = 2
        print()
        print(teams_to_plot)
        print()
        plot_multiple_teams(teams_to_plot, same_range=same_range_or_no, year_range=range_years)

    except ValueError:

        range_years = int(input('Range of years (eg. 3 year range for 2015 => 2012 to 2018): '))

        same_range_or_no = input('Do you want to see the team ratings over their actual timeline? (Y or N): ')
        if same_range_or_no.lower() == 'y':
            same_range_or_no = False
        else:
            same_range_or_no = True

        team = ''
        year = '1979'

        while team.lower() != 'done':
            team = input("Enter a team ID (type 'done' to finish): ")
            if team.lower() != 'done' and team.lower() != '':
                while int(year) < 1980+range_years or int(year) >= 2020-range_years:
                    year = input("Enter a year for the range to be centered on: ")
                    if int(year) < 1980+range_years or int(year) >= 2020-range_years:
                        print('Advanced stats are available from 1980 to 2019. Choose a year where the range fits.')
                teams_to_plot.append([team, year])
                year = '1979'
        print()
        print(teams_to_plot)
        print()
        plot_multiple_teams(teams_to_plot, same_range=same_range_or_no, year_range=range_years)

if __name__ == '__main__':

    while input("Press any key to continue. Enter QUIT to exit: ").lower() != 'quit':
        interactive()

    # top_three_teams = [['GSW', '2017'], ['CHI', '1996'], ['LAL', '1987']]
    # interesting_teams = [['CHI', '1996'], ['CLE', '2016']]
    # plot_multiple_teams(top_three_teams, same_range=True, year_range=2)