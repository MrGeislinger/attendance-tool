# Attendance


## Setup

Include a `.streamlit/secrets.toml` (for https://streamlit.io/ under 'Secrets'
in settings for app)

Example:

```toml
[connections.studentinfo]
spreadsheet = "https://docs.google.com/spreadsheets/d/..."

type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "...@<project_id>.iam.gserviceaccount.com"
client_id = ".."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509...iam.gserviceaccount.com"
universe_domain = "googleapis.com"


[connections.checkin]
spreadsheet = "https://docs.google.com/spreadsheets/d/.../"
worksheet = "checkins"

# From JSON key file
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "...@<project_id>.iam.gserviceaccount.com"
client_id = "..."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/...%40<project_id>.iam.gserviceaccount.com"
universe_domain = "googleapis.com"

[connections.checkout]
spreadsheet = "..."
worksheet = "checkouts"

# From JSON key file
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "...@f<project_id>.iam.gserviceaccount.com"
client_id = "..."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/...%40<project_id>.iam.gserviceaccount.com"
universe_domain = "googleapis.com"

[connections.corrections]
spreadsheet = "..."
worksheet = "..."

# From JSON key file
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "...@f<project_id>.iam.gserviceaccount.com"
client_id = "..."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/...%40<project_id>.iam.gserviceaccount.com"
universe_domain = "googleapis.com"

[corrections]
form_url = "https://forms.gle/..."
spreadsheet_url = "https://docs.google.com/spreadsheets/d/..."
```