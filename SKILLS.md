---
name: auth-skill
description: Implement secure authentication flows for the Todo Full-Stack Web App using signup, signin, password hashing, JWT, and Better Auth integration.
---

# Authentication Skill

## Instructions

1. **User Flows**
   - Signup new users securely
   - Signin existing users
   - Password reset and update

2. **Security**
   - Hash passwords (never store plain text)
   - Issue and verify JWT tokens
   - Use HttpOnly cookies for sensitive tokens
   - Use environment variables for secrets and API keys
   - Implement rate limiting on auth endpoints

3. **Validation**
   - Sanitize and validate all user inputs
   - Enforce user isolation (only access own data)
   - Follow secure coding and clean code practices

## Best Practices
- Use industry-standard hashing algorithms (e.g., bcrypt)
- JWT expiry and refresh policies
- Validate tokens on every request
- Ensure secure integration with Better Auth

## When to Use
- Any signup, signin, password management, or auth provider integration
- Securing REST API endpoints that require authentication
