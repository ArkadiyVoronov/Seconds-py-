import csv

# Script that accepts a CSV file at the input,
# uses the Google API to create a Html file "Tests Pass and not pass"

# file.CSV this is a table with three columns separated by commas.
# For example ("Test #34",45,23)
# In the first column, the name of the test. Text value, in quotation marks.
# Second column, number of asserts. Number.
# Third column, number of failed asserts. Number.

# final desired data formats:
# - Charts: [["Test Name",<NumberOfAsserts>,<NumberOfFailedAsserts>],...]

# read in the data from file

data_list = []
with open('TestAnalysisData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        data_list.append(row)
    # read in data using csv reader

column_chart_data = [["Test Name", "NumberOfAsserts"]]
table_data = [["Test Name", "NumberOfFailedAsserts"]]

# new list is initialized with headers
chart_data = [data_list[0]]
for row in data_list[1:]:
    num_asserts = int(row[1])
    num_failed_asserts = int(row[2])
    chart_data.append([row[0], num_asserts, num_failed_asserts])


# create the html for the chart
from string import Template
# first substitution is the header, the rest is the data
htmlString = Template("""
    <html><head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js">
    </script><script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart(){
      var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false);

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id = 'chart_div' style='width:800; height:600'><div>
</body>

</html>""")


chart_data_str = ''
for row in chart_data[1:]:
    # create the data string
    chart_data_str += '%s, \n'%row

# substitute the data into the template
completed_html = htmlString.substitute(labels=chart_data[0],
data=chart_data_str)

with open('Chart.html', 'w') as f:
    # write the html string you've create to a file
    f.write(completed_html)
