# Perfect Screen

A Django web application for Django Cameroon's Hacktoberfest 2025 celebration. Share your social media posts about Django Cameroon's Hacktoberfest participation and see them displayed on a beautiful gallery.

## About

Perfect Screen is a community-driven project where participants can submit screenshots of their social media posts about Django Cameroon's Hacktoberfest 2025. All submissions are displayed in an elegant gallery with Hacktoberfest's official branding.

## Features

- Display social media post screenshots in an elegant hero section with overlapping, inclined cards
- Paginated gallery view of community contributions
- Lazy loading for optimal performance
- Hacktoberfest 2025 official theme and colors
- Management command to load data from JSON
- Responsive design with TailwindCSS

## Requirements

- Python 3.11+
- uv package manager
- Django 5.2+
- Pillow

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DjangoCameroon/PerfectScreen.git
cd PerfectScreen
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Run migrations:
```bash
uv run python manage.py migrate
```

4. Load sample data:
```bash
uv run python manage.py load_posts
```

5. Run the development server:
```bash
uv run python manage.py runserver
```

6. Visit `http://localhost:8000` in your browser

## How to Participate

1. Post about Django Cameroon Hacktoberfest on Twitter or LinkedIn
2. Tag @DigitalOcean in your post
3. Include these hashtags: `#DjangoCameroonHack` `#Hacktoberfest` `#DjCMRHacktoberfest`
4. Star this repository on GitHub
5. Take a screenshot of your post
6. Follow the contribution guide to add your screenshot

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions on how to contribute your social media posts or code improvements.

### Quick Contribution Steps

1. Fork this repository
2. Add your screenshot to `data/images/`
3. Update `data/posts.json` with your information:
```json
{
  "username": "your_username",
  "platform": "Twitter",
  "screenshot": "images/your-username-twitter.png",
  "post_url": "https://twitter.com/your_username/status/123456789",
  "has_tagged_digitalocean": true,
  "has_starred_repo": true
}
```
4. Submit a Pull Request

## Project Structure

```
PerfectScreen/
├── data/
│   ├── images/          # Social media post screenshots
│   └── posts.json       # Post metadata
├── perfectscreen/       # Django project settings
├── posts/              # Main Django app
│   ├── management/
│   │   └── commands/
│   │       └── load_posts.py  # Load data from JSON
│   ├── models.py       # SocialPost model
│   ├── views.py        # View logic
│   └── templates/
│       └── posts/
│           └── home.html  # Main template
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE/
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Tech Stack

- **Framework**: Django 5.2.7
- **Package Manager**: uv
- **Frontend**: TailwindCSS CDN
- **Font**: Atkinson Hyperlegible
- **Image Processing**: Pillow

## Design

The project uses Hacktoberfest 2025's official branding:

### Colors
- Primary Background: `#1C1C3F` (Navy)
- Purple: `#5A5AB5`
- Lavender: `#C2C2FF`
- Dark Purple: `#403F7D`
- Periwinkle: `#A0A0FF`

### Typography
- Font Family: Atkinson Hyperlegible

## Management Commands

### Load Posts from JSON
```bash
uv run python manage.py load_posts
```

This command reads `data/posts.json` and loads all posts into the database.

## Development

### Creating Migrations
```bash
uv run python manage.py makemigrations
```

### Running Tests
```bash
uv run python manage.py test
```

### Creating Superuser
```bash
uv run python manage.py createsuperuser
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Community

- Organization: Django Cameroon
- Event: Hacktoberfest 2025
- Hashtags: `#DjangoCameroonHack` `#Hacktoberfest` `#DjCMRHacktoberfest`

## Acknowledgments

- Django Cameroon community
- Hacktoberfest organizers
- DigitalOcean
- All contributors

## Support

For questions or issues:
- Open an issue using the appropriate template
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- Reach out to the Django Cameroon community

---

Built with Django and open-source love by the Django Cameroon community
