import sentry_sdk

from views import MainMenu, AuthenticationMenu, SharedMenu

main_menu = MainMenu()
shared_menu = SharedMenu()
authentication_menu = AuthenticationMenu()

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

if __name__ == "__main__":
    menu_return_value, user = authentication_menu.authentication()
    
    while menu_return_value != "exit":
        
        if menu_return_value == "authentication":
            menu_return_value, user = authentication_menu.authentication()
        
        elif menu_return_value == "main" and user is not None:
            menu_return_value, user = main_menu.menu(user=user)
        
        elif menu_return_value == "dashboards" and user is not None:
            menu_return_value, user = shared_menu.dashboards(user=user)
        
        else:
            print("Error", menu_return_value)
            menu_return_value = authentication_menu.authentication()
            print("Error")
