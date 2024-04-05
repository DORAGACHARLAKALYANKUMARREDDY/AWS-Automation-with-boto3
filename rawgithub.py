link = "https://github.com/DORAGACHARLAKALYANKUMARREDDY/resume_pdf/blob/main/resume_tesing_git.pdf"

# note: this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex
# to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))