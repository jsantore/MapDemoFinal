import openpyxl
from us_state_abbrev import us_state_abbrev
import plotly.graph_objects

def get_data_rows(file_name):
    Excel_file = openpyxl.load_workbook(file_name)
    what_ever_we_want = Excel_file.active
    return what_ever_we_want.rows


def process_data(all_data):
    state_names_list = []
    unemployment_rate_list =[]
    for state_row in all_data:
        name = state_row[0].value
        if name in us_state_abbrev:
            state_abbrev = us_state_abbrev[name]
            state_names_list.append(state_abbrev)
            rate = state_row[1].value
            unemployment_rate_list.append(rate)
    return state_names_list, unemployment_rate_list


def display_data(state_list, unemployment_list):
    our_beautiful_map = plotly.graph_objects.Figure(
        data=plotly.graph_objects.Choropleth(
            locations=state_list,
            z =unemployment_list,
             locationmode ="USA-states",
            colorscale ="thermal",
            colorbar_title ="Unemployment Rate"
        )
    )
    our_beautiful_map.update_layout(
        title_text="US Unemplyoement Sept 2020",
        geo_scope="usa"
    )
    our_beautiful_map.show()


def main():
    all_data = get_data_rows("lanrderr-unemployment.xlsx")
    state_list, unemployment_list = process_data(all_data)
    display_data(state_list, unemployment_list)

main()