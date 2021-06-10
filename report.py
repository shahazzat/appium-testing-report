from jinja2 import Environment, FileSystemLoader
import webbrowser
import time

##################################################
## This is report module and responsible to generate report.
##################################################
__author__ = "Shahazzat Hossain"
__copyright__ = "Copyright 2021, Project"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Shahazzat Hossain"
__email__ = "shahazzat@gmail.com"
__status__ = "POC"


class TestReport:

    def __init__(self):
        # Load templates file from templtes folder
        self.env = Environment(loader=FileSystemLoader('./report'), trim_blocks=True, lstrip_blocks=True)
        self.template = self.env.get_template('index.html')
        self.rendered_filename = "report_"+time.strftime("%Y%m%d-%H%M%S")+".html"
        self.rendered_file_path = "./report/" + self.rendered_filename
        self.template_vars = {
            "total_number_of_test": '',
            "passed": '',
            "failed": '',
            "not_executed": '',
            "result_table": ''
        }

    def generate_html(self, *args):
        self.prepare_summary(args[1])
        self.prepare_result_table(args[0])
        print("Test result: ")
        print(self.template_vars)
        output_text = self.template.render(self.template_vars)

        with open(self.rendered_file_path, "w") as result_file:
            result_file.write(output_text)

        # open a public URL, in this case, the webbrowser docs
        # url = "http://docs.python.org/library/webbrowser.html"
        # webbrowser.open(url, new=new)

        # open an HTML file on my own (Windows) computer
        url = "file://D:/AppiumProject/vrit/report/"+self.rendered_filename
        webbrowser.open(url)

    def prepare_summary(self, summary):
        # print(summary)
        self.template_vars["total_number_of_test"] = summary["total_number_of_test"]
        self.template_vars["passed"] = summary["passed"]
        self.template_vars["failed"] = summary["failed"]
        self.template_vars["not_executed"] = summary["not_executed"]

    def prepare_result_table(self, test_result):
        html_table = ""

        for test in test_result:
            html_table += '<tr role="row">'
            html_table += '<td>'+test["title"]+'</td>'
            html_table += '<td>'+test["type"]+'</td>'
            html_table += '<td>'+test["status"]+'</td>'
            html_table += '</tr>'

        self.template_vars["result_table"] = html_table
