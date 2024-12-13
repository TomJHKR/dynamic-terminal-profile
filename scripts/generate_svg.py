import json


def generate_svg(data,size,commands_responses):
    """
    Generate an SVG terminal representation with dynamic content.

    Args:
        size (int): Width of the terminal in pixels.
        data (dict): Metadata like username, hostname, language, and contributions.
        commands_responses (list of tuples): A list of (command, response) pairs to display.

    Returns:
         str: The SVG string.
         """
    template = f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size/2}" style="background-color:transparent; border-radius:10px;">
        <svg y="0">
            <rect width="{size}" height="{size/20}" fill="#333333" />
            <rect width="{size/3.5}" height="{size/20}" fill="#1e1e1e" rx="{size/80}" y="{size/100}" x="{size/100}" />
            <svg width="{size/40}px" height="{size/40}px" x="{size/44.4}" y="{size/50}" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="#e1e1e1">
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
            <path d="M10.875 7l2.008 5h-.711l-2.008-5h.711zm-5.125.594c-.276 0-.526.041-.75.125a1.542 1.542 0 0 0-.578.375c-.162.166-.287.37-.375.61a2.364 2.364 0 0 0-.133.827c0 .287.04.547.117.781.078.235.196.433.352.594.156.162.346.29.57.383.224.094.48.138.766.133a2.63 2.63 0 0 0 .992-.195l.125.484a1.998 1.998 0 0 1-.492.148 4.381 4.381 0 0 1-.75.07 2.61 2.61 0 0 1-.914-.156 2.207 2.207 0 0 1-.742-.453 1.878 1.878 0 0 1-.485-.742 3.204 3.204 0 0 1-.18-1.023c0-.365.06-.698.18-1 .12-.302.287-.563.5-.782.214-.218.471-.388.774-.507a2.69 2.69 0 0 1 1-.18c.296 0 .536.023.718.07.183.047.315.094.399.14l-.149.493a1.85 1.85 0 0 0-.406-.14 2.386 2.386 0 0 0-.539-.055zM8 8h1v1H8V8zm0 2h1v1H8v-1z">
            </path>
            <path d="M15.5 1H.5l-.5.5v13l.5.5h15l.5-.5v-13l-.5-.5zM15 14H1V5h14v9zm0-10H1V2h14v2z"></path></g></svg>
            <svg width="{size/40}px" height="{size/40}px" x="{size/3.8}" y="{size/53.3}" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <rect width="24" height="24"></rect> <path d="M7 17L16.8995 7.10051" stroke="#e1e1e1" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M7 7.00001L16.8995 16.8995" stroke="#e1e1e1" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg> 
            <svg fill="#FFFFFF" height="{size/70}px" width="{size/70}px" y="{size/43}" x="{size/3.2}" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 455 455" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <polygon points="455,212.5 242.5,212.5 242.5,0 212.5,0 212.5,212.5 0,212.5 0,242.5 212.5,242.5 212.5,455 242.5,455 242.5,242.5 455,242.5 "></polygon> </g></svg> 
        </svg>
        <svg y="{size/20}">
         <rect width="{size}" height="{size/2 - size/20}" fill="#1e1e1e" />
        """

       # Add commands and responses dynamically
    y_offset = 160  # Start below the static content
    for command, response in commands_responses:
        template += f"""
            <text x="20" y="{y_offset}" font-family="'Fira Code', monospace" font-size="14" fill="#23d18b">
            TomJHKR@github
            </text>
            <text x="127" y="{y_offset}" font-family="'Fira Code', monospace" font-size="14" fill="#FFFFFF">
            :
            </text>
            <text x="135" y="{y_offset}" font-family="'Fira Code', monospace" font-size="14" fill="#3b8eea">
            ~
            </text>
            <text x="145" y="{y_offset}" font-family="'Fira Code', monospace" font-size="14" fill="#FFFFFF">
            $
            </text>
          <text x="155" y="{y_offset}" font-family="'Fira Code', monospace" font-size="14" fill="#FFFFFF">
              {command}
            </text>
            <text x="20" y="{y_offset + 30}" font-family="'Fira Code', monospace" font-size="14" fill="#FFFFFF">
                {response}
            </text>
        """
        y_offset += 60  # Add space for the next command-response pair

    template += """
            </rect>
        </svg>
    </svg>
    """
    with open("../assets/terminal.svg", "w") as file:
        file.write(template)

if __name__ == "__main__":
    with open("../data/test-stats.json") as file:
        data = json.load(file)
    commands_responses = [
    ("ls", "project1  project2  project3"),
    ("pwd", "/home/tomjkhr/projects"),
    ("cat readme.txt", "Welcome to my project!")
]
    generate_svg(data,800,commands_responses)


    """
                    <rect width="800" height="350" fill="#1e1e1e"/>
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
        """
