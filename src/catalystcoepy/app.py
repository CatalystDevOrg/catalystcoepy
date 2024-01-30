"""
Catalyst Mobile 2.x Dev Stack Candidate (Python)
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class CatalystCOEPY(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        self.main_window = toga.MainWindow(title=self.formal_name)

        webview = toga.WebView()
        webview.url = "https://getcatalyst.eu.org"

        box = toga.Box(
        children=[
            toga.Box(
                children=[
                    #self.url_input,
                    #toga.Button(
                    #    "Go",
                    #    on_press=self.load_page,
                    #    style=Pack(width=50, padding_left=5),
                    #),
                ],
                style=Pack(
                    direction=COLUMN,
                ),
            ),
            webview,
        ],
        style=Pack(direction=COLUMN),
    )

        self.main_window.content = box
        self.main_window.show()


def main():
    return CatalystCOEPY()
