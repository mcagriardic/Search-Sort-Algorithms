"""
Create a script which pulls a column of data from a sql database,
counts number of occurrences of each value in the sql column,
saves number of occurrences per value in the sql column to a csv file,
emails the csv file as an attachments to author of program.
"""

import pyodbc
import pandas
import csv

import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import Encoders


def sql_get_request():
    """
    Establishes a connection to sql server database FI_EMEA
    Pull the column with language information for each completed workitem in
    the FICME Fixed Income workflow
    Password information removed for safety
    :return: returns a list of tuples [(language, ), (language, )]
    """
    conn = pyodbc.connect(driver='SQL Server Native Client 11.0',
                              server='nysqlgdtoaagl01', database='FI_EMEA',
                              UID='Confidential',
                              PWD='Confidential',
                              MultiSubnetFailover='Yes')
    cursor = conn.cursor()

    sql_query = """
                SELECT Language
                FROM [FI_EMEA].[dbo].[JRWL_Prod]
                WHERE Task_Type = 'Complete'
                """

    fetched_data = cursor.execute(sql_query)
    language_data = fetched_data.fetchall()
    conn.close()
    return language_data

def count_language_in_dict(language_data):
    """
    Takes list of tuples and counts how many times each language is present for
    the total number of completed workitems.
    :param language_data: a list of tuples [(language, ), (language, )] where
    language is available in the first tuple location for every list variable.
    Second tuple location is always empty, and ignored below.
    :return: returns a dict which contains a key, and one value per key.
    The key is the language and the val is the count of number of times the
    language is present in list. eg dict = {'English': 200, 'German': 50}
    """
    language_dict = {}

    for lng in language_data:
        if lng[0] in language_dict.keys():
            language_dict[lng[0]] += 1
        else:
            language_dict.update({lng[0]: 1})

    return language_dict


def save_to_csv(language_dict):
    """
    This function saves the language dict as a csv file with two columns,
    Volume (val) and Language (key)
    :param language_dict: dict = {'English': 200, 'German': 50}
    :return: no return
    """
    with open('F:/Git/Solutions/top_languages.csv', 'wb') as fp:
        w = csv.writer(fp, dialect='excel')
        w.writerow(['Language', 'Volume'])
        for key, val in language_dict.iteritems():
             w.writerow([key, val])


def dev_email():
    """
    This function sends an email with the csv generated from the
    language_dict. Sender is me, recipient is me
    :return: no return
    """
    email_recipients = ['marnesen@bloomberg.net'] # list of recipients

    msg = MIMEMultipart("alternative")
    msg['From'] = 'marnesen@bloomberg.net'
    msg['To'] = ", ".join(email_recipients)
    msg['Subject'] = """Language use in JRWL"""

    html1 = """
            <html>
              <head>
              </head>
              <body>
              <font face = "Calibri" size = "3">
                    <p>Attached is a list of languages and their volume of use<br>
                </font><br />
                </p>
              </body>
            </html>
                """
    part_html = MIMEText(html1, "html")
    msg.attach(part_html)
    #attachment information
    attachment = MIMEBase('application', "octet-stream")
    attachment.set_payload(open("F:/Git/Solutions/top_languages.csv", "rb").read())
    Encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment; filename="top_languages.csv"')
    msg.attach(attachment)

    try:
        server = smtplib.SMTP('relay.bloomberg.com')
        server.sendmail(msg['From'], email_recipients, msg.as_string())
        server.quit()
    except Exception as ex:
        raise ex


if __name__ == '__main__':
    language_data = sql_get_request()
    language_dict = count_language_in_dict(language_data)
    save_to_csv(language_dict)
    dev_email()