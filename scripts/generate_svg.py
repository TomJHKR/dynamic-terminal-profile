import json

def generate_svg(data):
    template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400" style="background-color:#1e1e1e; border-radius:10px;">
        <rect width="800" height="400" fill="#282c34" rx="10" />
        <text x="20" y="40" font-family="monospace" font-size="18" fill="#00FF00">Terminal</text>
        <text x="20" y="80" font-family="monospace" font-size="14" fill="#FFFFFF">
            Most Used Language: {data['language']}
        </text>
        <text x="20" y="120" font-family="monospace" font-size="14" fill="#FFFFFF">
            Contributions: {data['contributions']}
        </text>
        <text x="20" y="160" font-family="monospace" font-size="14" fill="#00FF00">
            Repositories: {data['repos']}
        </text>
    </svg>"""
    with open("assets/terminal.svg", "w") as file:
        file.write(template)

if __name__ == "__main__":
    with open("data/stats.json") as file:
        data = json.load(file)
    generate_svg(data)

