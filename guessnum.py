n=123
running=True
while running:
        g=int(raw_input('Enter a integer:'))
        if g==n :
            print 'Congratulations. You got it!'
            running=False
        elif g<n :
            print 'Try again. It\' a little lowwer.'
        else :
            print 'Try again. It\'s a little higher.'

else :    
        print 'Done'
