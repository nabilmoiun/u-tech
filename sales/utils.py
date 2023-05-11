import io
import base64
from urllib.parse import quote

from xhtml2pdf import pisa
import matplotlib.pyplot as plt

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

def get_pie_chart_figure_uri(x_values, labels, title=""):
    plt.pie(x_values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    figuer = plt.gcf()
    buffer = io.BytesIO()
    figuer.savefig(buffer, format='png')
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = quote(string)
    plt.close()
    return uri


def get_line_chart_figure_uri(x_values, labels, x_label="", y_label="", title=""):
    plt.plot(x_values, labels)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    figuer = plt.gcf()
    buffer = io.BytesIO()
    figuer.savefig(buffer, format='png')
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = quote(string)
    plt.close()
    return uri


def generate_pdf(request, context={}):
    regions = []
    region_sales_count = []
    years = []
    year_sales_count = []

    for data in context.get('region_sales'):
        regions.append(data['region'])
        region_sales_count.append(data['id__count'])

    for data in context.get('year_sales'):
        years.append(data['order_date__year'])
        year_sales_count.append(data['id__count'])

    context['pie_chart'] = get_pie_chart_figure_uri(region_sales_count, labels=regions, title="Sales by region pie chart")
    context['line_chart'] = get_line_chart_figure_uri(years, labels=year_sales_count, title="Sales by year line chart")
    template = settings.BASE_DIR / "templates" / 'pdf.html'
    html = render_to_string(template, context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

    pisa.CreatePDF(html, dest=response)

    return response 