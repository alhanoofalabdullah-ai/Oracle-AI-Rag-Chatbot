from app.logging_config import (
    configure_logging,
)

configure_logging()

import streamlit as st

from app.config import (
    get_settings,
)

from app.ui.components import (
    render_app,
)


def main() -> None:

    settings = get_settings()

    configuration_errors = (
        settings.validate_runtime()
    )

    if configuration_errors:

        st.warning(
            "Application configuration "
            "requires attention."
        )

        with st.expander(
            "Configuration Details"
        ):

            for error in (
                configuration_errors
            ):

                st.write(
                    f"- {error}"
                )

    render_app()


if __name__ == "__main__":

    main()
