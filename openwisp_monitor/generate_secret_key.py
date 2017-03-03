from django.utils.crypto import get_random_string

def generate(length=50):
	chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	return get_random_string(length, chars)
