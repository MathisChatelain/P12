import sentry_sdk

from views import MainMenu, AuthenticationMenu, SharedMenu, ActionMenu

main_menu = MainMenu()
shared_menu = SharedMenu()
authentication_menu = AuthenticationMenu()
action_menu = ActionMenu()

sentry_sdk.init(
    dsn="https://98c783f8159e4964f864f2ddfeb24129@o4505963636391936.ingest.sentry.io/4505963639144448",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

menu_options = {
    "authentication": authentication_menu.authentication,
    "main": main_menu.menu,
    "dashboards": shared_menu.dashboards,
    "action_menu": action_menu.menu,
    "manager_menu": action_menu.manager_menu,
}

if __name__ == "__main__":
    menu_return_value, user = authentication_menu.authentication()

    while menu_return_value != "exit":
        if user is not None:
            menu_function = menu_options.get(menu_return_value)
            if menu_function:
                menu_return_value, user = menu_function(user=user)

        else:
            print("Error", menu_return_value)
            menu_return_value = authentication_menu.authentication()
            print("Error")
