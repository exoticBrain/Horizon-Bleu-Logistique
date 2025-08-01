import markdown

# Read the markdown file
with open('/home/ubuntu/delivery_logistics_report.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(markdown_content, extensions=['tables'])

# Read the existing HTML template
with open('/home/ubuntu/index.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

# Insert the converted content into the template
final_html = html_template.replace('</body>', f'{html_content}\n</body>')

# Write the final HTML file
with open('/home/ubuntu/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("HTML file created successfully!")

