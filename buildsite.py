print('Building Site')

top_html = open('templates/top.html').read()
middle_html = open('docs/blog.html').read()
bottom_html = open('templates/bottom.html').read()

combined_html = top_html + middle_html + bottom_html

open('blog.html', 'w+').write(combined_html)

top_html = open('templates/top.html').read()
middle_html = open('docs/projects.html').read()
bottom_html = open('templates/bottom.html').read()

combined_html = top_html + middle_html + bottom_html

open('projects.html', 'w+').write(combined_html)

top_html = open('templates/top.html').read()
middle_html = open('docs/contactme.html').read()
bottom_html = open('templates/bottom.html').read()

combined_html = top_html + middle_html + bottom_html

open('contactme.html', 'w+').write(combined_html)
