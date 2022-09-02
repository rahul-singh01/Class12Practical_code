choice='y'
want='yes'
while choice[0]=='y' or choice[0]=='Y':
	z=0
	while z==0:#for set if we not enter ant no.
		want=input('Do you want to play Simple mode or Advance mode\n')
		if want:
			z=1
		else:
			print('Please Enter Something Relevant')

	while want[0]=='s' or want[0]=='S':
		a=10
		import random
		n=random.randint(1,a)
		print('''Welcome in guess the number game!!!:)
		Rule:1.Please, Only try a whole no.
			2.You have only 3 chance \U0001F609''')
		guess=None
		i=0
		l=3
		while guess!=n:
			i+=1
			if i==1:
				print('Lets try your first chance :-)')
			guess=int(input('Try a no:'))
			if guess>n:
				print('Too high \U0001F605')
				if i!=3:
					print('Make another guess')
			if guess<n:
				print('Too low \U0001F605')
				if i!=3:
					print('Make another guess')
			if i==2 and guess!=n:
				print(f'WARNING!!! You have only {l - i} life remainging \U0001F915')
			if i==3 and guess!=n:
				print(':(You lose the game, but I am sure you will win next time...\U0001F61E')
			want='no'
			if i==3 and guess!=n:
				choice=input(('Do you want to play again[Yes/No]  \U0001F914\n'))
			if i==3 and guess!=n:
				break
		while guess==n:
			if i==1:
				print('CONGRATULATIONS, You WON the game; At your first try!!! \U0001F918')
			if i==2:
				print('CONGRATULATIONS, You WON the game \U0001F601')
			if i==3:
				print('CONGRATULATIONS, You WON the game; At your last chance!!! \U0001F601')
			choice=input(('Do you want to play again[Yes/No]  \U0001F914\n'))
			want='no'
			if i<=3:
				break
			
	
	while want[0]=='a' or want[0]=='A':
		print('hello')
		a=int(input('Enter the range where you want, the no. to be choosen\n'))
		import random
		n=random.randint(1,a)
		print('''Welcome in guess the number game!!!:)
		Rule:1.Please, Only try a whole no.''')
		guess=None
		i=0
		l=int(input('How many lives do you want:'))
		while guess!=n:
			i+=1
			if i==1:
				print('Lets try your first chance :-)')
			guess=int(input('Try a no:'))
			if guess>n:
				print('Too high \U0001F605')
				if i!=l:
					print('Make another guess')
			if guess<n:
				print('Too low \U0001F605')
				if i!=l:
					print('Make another guess')
			if i>1 and i<l and guess!=n:
				print(f'WARNING!!! You have only {l - i} life remainging \U0001F915')
			want='no'
			if i==l and guess!=n:
				print(':(You lose the game, but I am sure you will win next time...\U0001F61E')
			if i==l and guess!=n:
				choice=input(print('Do you want to play again? Y/N  \U0001F914\n'))
			if i==l and guess!=n:
				break
		while guess==n:
			if i==1:
				print('CONGRATULATIONS, You WON the game; At your first try!!! \U0001F918')
			if i<l and i!=1:
				print('CONGRATULATIONS, You WON the game \U0001F601')
			want='no'
			choice=input(('Do you want to play again[Yes/No] \U0001F914\n'))
			if guess==n:
				break


print('THANKS for playing\U0001F601\U0001F601')