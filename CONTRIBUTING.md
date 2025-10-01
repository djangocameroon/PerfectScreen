# Contributing to Perfect Screen

Thank you for your interest in contributing to Perfect Screen for Django Cameroon Hacktoberfest 2025!

## How to Contribute Your Social Media Post

### Prerequisites

1. Post about Django Cameroon Hacktoberfest on Twitter or LinkedIn
2. Tag @DigitalOcean in your post
3. Include these hashtags: `#DjangoCameroonHack` `#Hacktoberfest` `#DjCMRHacktoberfest`
4. Star this repository on GitHub

### Step-by-Step Guide

1. **Fork the Repository**
   - Click the "Fork" button at the top right of this repository

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/PerfectScreen.git
   cd PerfectScreen
   ```

3. **Create a New Branch**
   ```bash
   git checkout -b add-my-post
   ```

4. **Add Your Screenshot**
   - Take a screenshot of your social media post
   - Save it as `data/images/your-username-platform.png`
   - Example: `data/images/johndoe-twitter.png`

5. **Update the JSON File**
   - Open `data/posts.json`
   - Add your entry following this format:
   ```json
   {
     "username": "your_username",
     "platform": "Twitter",
     "screenshot": "images/your-username-platform.png",
     "post_url": "https://twitter.com/your_username/status/123456789",
     "has_tagged_digitalocean": true,
     "has_starred_repo": true
   }
   ```

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add social media post by @your_username"
   ```

7. **Push to Your Fork**
   ```bash
   git push origin add-my-post
   ```

8. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Fill in the PR template
   - Submit your PR

## Code Contribution Guidelines

### Code Style

- No emojis in code
- No comments in code
- Follow PEP 8 for Python code
- Use meaningful variable and function names

### Testing

Before submitting a PR for code changes:

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py load_posts
uv run python manage.py runserver
```

Visit `http://localhost:8000` to verify everything works.

## Pull Request Guidelines

- Use a clear and descriptive title
- Fill out the PR template completely
- Link any related issues
- Ensure your code follows the style guidelines
- Test your changes locally before submitting

## Reporting Issues

Use the appropriate issue template:
- Bug Report: For reporting bugs
- Feature Request: For suggesting new features
- Hacktoberfest: For Hacktoberfest-related questions
- Other: For general questions

## Community Guidelines

- Be respectful and inclusive
- Help others when possible
- Follow the code of conduct
- Have fun and learn!

## Questions?

If you have questions, please:
1. Check existing issues
2. Create a new issue using the "Other" template
3. Reach out to Django Cameroon community

Thank you for contributing to Perfect Screen!
