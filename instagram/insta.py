import json

import instaloader


def get_user(username: str):
    loader = instaloader.Instaloader()
    try:
        user = instaloader.Profile.from_username(loader.context, username)
    except instaloader.ProfileNotExistsException:
        return json.dumps({'error': 'Profile not found'}, indent=4)
    except Exception as e:
        return json.dumps({'error': f'Error fetching profile: {str(e)}'}, indent=4)

    data = {
        'user_id': user.userid,
        'username': username,
        'full_name': user.full_name,
        'bio': user.biography,
        'posts': [{'shortcode': post.shortcode, 'url': post.url} for post in user.get_posts()]
    }

    return json.dumps(data, indent=4)


if __name__ == '__main__':
    username = 'akbarali_hah'
    print(get_user(username))