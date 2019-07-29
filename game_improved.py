from playground import get_team_data, generate_dataframe, clean_up_df


def getTeamDf(team_id, year):
    df_header = get_team_data(team_id, year, header=True)
    df_row = [get_team_data(team_id, year)]
    return generate_dataframe(df_row, df_header)


def calculate_metric(team_df):
    team_df = clean_up_df(team_df)

    # scaling, im sure there's a better way to do this, later...
    pts = team_df['PTS'][0] / 120.0
    tov = team_df['TOV'][0] / 17.0
    efg = 2 * team_df['eFG%_0'][0] / 0.570  # key
    efg_opp = 2 * team_df['eFG%_1'][0] / 0.570  # key
    ftr = team_df['FTr'][0] / 0.315
    orb = team_df['ORB'][0] / 13.0
    drb = team_df['DRB'][0] / 40.0
    mov = 2 * team_df['MOV'][0] / 9.0   # key
    ast = team_df['AST'][0] / 30.0
    blk = team_df['BLK'][0] / 7.0
    ortg = 2 * team_df['ORtg'][0] / 116.0   # key
    drtg = team_df['DRtg'][0] / 116.0

    team_metric = 100*(pts - tov + efg - efg_opp + ftr + orb + drb + mov + ast + blk + ortg - drtg) / 9.0
    return team_metric


def get_team_metric(team_id, year):
    return calculate_metric(getTeamDf(team_id, year))


if __name__ == '__main__':

    team = input('team id: ')
    year = input('year: ')
    print(get_team_metric(team, year))




