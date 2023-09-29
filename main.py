from views.authentication import authentication_menu
import sentry_sdk

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
    division_by_zero = 1 / 0
    authentication_menu()
