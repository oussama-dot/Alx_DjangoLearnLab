# HTTPS Deployment Instructions

This Django app is configured to enforce HTTPS.

## Web Server Configuration

### If using Nginx:

- Install Certbot for Let's Encrypt
- Generate certificate:
  ```bash
  sudo certbot --nginx
  ```
