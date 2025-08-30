import re

def parse_file(s):
	html_str = ''
	parse_mode = ''
	with open("static/tfthe/" + s, "r") as file:
		while True:
			line = file.readline().strip('\n')
			print(line)
			match line:
				case 'CODEBLOCK':
					parse_mode = 'codeblock'

				case 'H1':
					parse_mode = 'h1'

				case 'H2':
					parse_mode = 'h2'

				case 'P':
					parse_mode = 'p'

				case 'IMG':
					parse_mode = 'img'

				case '{':
					match parse_mode:
						case 'codeblock':
							html_str += '<code class = "code-block">'
						case 'h1':
							html_str += '<h1>'
						case 'h2':
							html_str += '<h2>'
						case 'p':
							html_str += '<p>'
						case 'img':
							html_str += '<img src = \"'

				case '}':
					match parse_mode:
						case 'codeblock':
							html_str += '</code>'
						case 'h1':
							html_str += '</h1>'
						case 'h2':
							html_str += '</h2>'
						case 'p':
							html_str += '</p>'
						case 'img':
							html_str += '\">'
					parse_mode = ''

				case 'END':
					break
					
				case _:
					match parse_mode:
						case 'codeblock':
							html_str += line + "\n"
						case _:
							html_str += line
	return html_str
