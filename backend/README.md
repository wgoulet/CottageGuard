Cottage Guard Backend App

This app is a webservice that acts as a backend for the web front end app as well as acts as the backend service for calls from API clients on Raspberry PI devices.

The backend authenticates/authorizes all API calls using OIDC/OAuth2.0. The web front end app is responsible for obtaining access/ID tokens from the IdP (Okta) using authorization code with PKCE while API clients on Raspberry PI devices will use client authentication.

The front end web app and the API clients will be linked to Okta via 2 Okta applications; CottageGuardFE (configured with auth code + PKCE) and CottageGuardBE (configured with client credential auth). The CottageGuard BE app will verify access/ID tokens using the Starlette OAuth middleware. The Backend web app has no corresponding application in Okta; it will simply verify that the tokens are valid.