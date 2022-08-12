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
  padding-left:5px;
  padding-right:5px;
}
.main-content {
  padding-left:13px;
  padding-right:13px;
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
indexHtml.write("""<div class="main-content">\n""")

md = open(mdFileName, 'r', encoding='utf-8')
indexHtml.write(markdown.markdown(md.read(), extensions=['tables', 'sane_lists'], output_format='html'))
md.close()

indexHtml.write("""\n</div>""")
indexHtml.close()
