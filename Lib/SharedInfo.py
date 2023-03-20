class SharedInfo:
    window_main = None  # TODO
    widget_welcome = None
    widget_config = None
    widget_search = None
    widget_searching = None
    widget_save_file = None
    widget_warning_config_lack = None
    sys_config = {
        'vpn_port': "",
        'database_account': '',
        "database_pwd": '',
        'twitter_dev_account': '',
        'chatgpt_account': '',
        'offline_file_path': '',
        'result_save_path': ''
    }

    def show_main_window(self):
        self.window_main.show()

    def show_welcome_widget(self):
        self.widget_welcome.show()

    def show_config_widget(self):
        self.widget_config.show()
