class CredentialsNotProvided(Exception):
    message = "You must pass either a valid token or a public/secret key set"


class CouldNotRetrieveToken(Exception):
    message = "Could not retrieve token from core API"