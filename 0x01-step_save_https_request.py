# Objective:
#   - Register answer http request on a file

# --> Recall first step
# --> Register on a file called reponse.html

def backup_file(html):
    """
    name: backup_file
    Description: This function write(saves) the answer to http request in a file called reponse.html.
    Args:
        html (string): It's variable that content html response of http request. This
        variable is obtained by `html = answer.tex`
    """
    f = open("reponse.html", "w")
    f.write(html)
    f.close()