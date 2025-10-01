import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.files import File
from posts.models import SocialPost


class Command(BaseCommand):
    help = 'Load social posts from JSON file'

    def handle(self, *args, **kwargs):
        json_path = Path('data/posts.json')

        if not json_path.exists():
            self.stdout.write(self.style.ERROR('posts.json not found in data folder'))
            return

        with open(json_path, 'r') as f:
            posts_data = json.load(f)

        loaded_count = 0
        skipped_count = 0

        for post_data in posts_data:
            username = post_data['username']
            post_url = post_data['post_url']

            if SocialPost.objects.filter(username=username, post_url=post_url).exists():
                self.stdout.write(self.style.WARNING(f'Skipped (already exists): {username}'))
                skipped_count += 1
                continue

            image_path = Path('data') / post_data['screenshot']

            if not image_path.exists():
                self.stdout.write(self.style.WARNING(f'Image not found: {image_path}'))
                continue

            with open(image_path, 'rb') as img_file:
                social_post = SocialPost(
                    username=username,
                    platform=post_data['platform'],
                    post_url=post_url,
                    has_tagged_digitalocean=post_data.get('has_tagged_digitalocean', False),
                    has_starred_repo=post_data.get('has_starred_repo', False),
                )
                social_post.screenshot.save(
                    Path(post_data['screenshot']).name,
                    File(img_file),
                    save=True
                )

            self.stdout.write(self.style.SUCCESS(f'Loaded: {username}'))
            loaded_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {loaded_count} new posts'))
        if skipped_count > 0:
            self.stdout.write(self.style.WARNING(f'Skipped {skipped_count} existing posts'))
