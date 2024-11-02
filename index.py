import requests
import html2text
import curses
import argparse

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

def render_text(stdscr, initial_url):
    # Clear the screen
    stdscr.clear()

    # Set the initial URL
    url = initial_url

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Current URL: {url}")  # Display the current URL
        stdscr.addstr(1, 0, "Press 'u' to change the URL.")
        stdscr.addstr(2, 0, "Fetching HTML...")

        # Fetch and render HTML
        html_content = fetch_html(url)
        text_content = html2text.html2text(html_content)

        # Clear the previous content before displaying new content
        stdscr.clear()  # Clear the screen again before displaying the text

        # Display the rendered text
        stdscr.addstr(0, 0, text_content)

        stdscr.addstr(curses.LINES - 1, 0, "Press 'q' to quit.")
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Handle 'u' to change the URL
        if key == ord('u') or key == ord('U'):  # Change the URL with 'u'
            stdscr.clear()
            stdscr.addstr(0, 0, "Enter new URL: ")
            curses.echo()  # Enable echoing of input
            new_url = stdscr.getstr().decode('utf-8')  # Get user input
            url = new_url if new_url else url  # Update URL if not empty
            curses.noecho()  # Disable echoing

        # Quit the application
        elif key == ord('q'):
            break

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Fetch and render HTML in the terminal.')
    parser.add_argument('url', type=str, nargs='?', default='https://example.com',
                        help='The URL to fetch HTML from (default: https://example.com)')
    args = parser.parse_args()

    # Initialize the curses application
    curses.wrapper(render_text, args.url)

if __name__ == "__main__":
    main()
