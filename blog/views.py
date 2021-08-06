from django.shortcuts import render



posts = [
	{

		'author' : "Prajwal",
		'title' : 'BLog Post 1',
		'content' : 'First post content',
		'date_posted' : 'August 6th 2021'

	},
	{
	'author' : "Prajwal UN",
		'title' : 'BLog Post 2',
		'content' : 'Second post content',
		'date_posted' : 'August 7th 2021'
	}





]

def home(request):
	context = {
		'posts':posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'_About_'})


