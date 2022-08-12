import os
import markdown

indexHtmlFileName = './_site/index.html'
mdFileName = './README.md'

tableStyle = """
<style>
table {
    border-collapse: collapse;
}
table, th, td {
   border: 1px solid black;
}
</style>
"""

try:
    os.remove(indexHtmlFileName)
except OSError:
    pass

indexHtml = open(indexHtmlFileName, 'a', encoding='utf-8')

# set html charset
indexHtml.write("""<meta http-equiv="Content-type" content="text/html; charset=utf-8" />""")
indexHtml.write(tableStyle)

md = open(mdFileName, 'r', encoding='utf-8')
indexHtml.write(markdown.markdown(md.read(), extensions=['tables', 'sane_lists'], output_format='html'))
md.close()

indexHtml.close()
