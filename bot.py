import praw
import random
import datetime
import time


# FIXME:
# copy your generate_comment functions from the week_07 lab here

def generate_comment_0():
    names = ['Joe Biden', 'Joseph Biden', 'Joe', 'Joey']
    random.choice(names)
    names= random.choice(names)
    countries = ['Russia', 'China', 'North Korea', 'Iran']
    random.choice(countries)
    countries = random.choice(countries)
    industries = ['Economics', 'Healthcare', 'Climate Change', 'Politics']
    random.choice(industries)
    industries = random.choice(industries)
    characteristics = ['person', 'man', 'human', 'leader']
    random.choice(characteristics)
    characteristics = random.choice(characteristics)
    nicknames = ['dude', 'guy', 'candidate', 'politician']
    random.choice(nicknames)
    nicknames = random.choice(nicknames)

    text= names + " is the best " + nicknames + ". He is strong on " + countries + ". He understands " + industries  + ". And most importantly, he is a good " + characteristics
    return text

#print('text=', generate_comment_0())


def generate_comment_1():
    start = ['What!', 'Hey!', 'Yo!', 'Hahaha!']
    random.choice(start)
    start= random.choice(start)
    adjective = ['perfect', 'interesting', 'dynamic', 'beautiful']
    random.choice(adjective)
    adjective = random.choice(adjective)
    attention = ['Yo', 'Hey', 'Aye', 'Okay']
    random.choice(attention)
    attention = random.choice(attention)
    heroes = ['superman and batman', 'the justice league', 'the avengers', 'starsky and hutch']
    random.choice(heroes)
    heroes = random.choice(heroes)
    promise = ['promise it.', 'swear it.', 'tell you.', 'feel it.']
    random.choice(promise)
    promise = random.choice(promise)    
     
    text = start + ' Kamala Harris and Joe Biden are ' + adjective + '. ' + attention + ' listen up. Together, they are like ' + heroes + '. I ' + promise
    return text

#print('text=', generate_comment_1())


def generate_comment_2():
    debate = ['debate', 'speech', 'talk', 'townhall']
    random.choice(debate)
    debate= random.choice(debate)
    concise = ['concise', 'direct', 'strategic', 'clear']
    random.choice(concise)
    concise = random.choice(concise)
    points = ['points', 'arguments', 'perspectives', 'insights']
    random.choice(points)
    points = random.choice(points)
    think = ['think', 'know', 'believe', 'hope']
    random.choice(think)
    think = random.choice(think)
    win = ['win', 'triumph', 'be victorious', 'celebrate']
    random.choice(win)
    win = random.choice(win)    
    
    text = 'Biden delivered a good ' + debate + '. He was ' + concise + '. He also had really good ' + points + '. I ' + think + ' he should ' + win + ' for sure.'
    return text

#print('text=', generate_comment_2())


def generate_comment_3():
    names = ['Donald Trump', 'Trump', 'Donald', 'The Donald']
    random.choice(names)
    names= random.choice(names)
    countries = ['Russia.', 'China.', 'North Korea.', 'Iran.']
    random.choice(countries)
    countries = random.choice(countries)
    industries = ['Economics.', 'Healthcare.', 'Climate Change.', 'Politics.']
    random.choice(industries)
    industries = random.choice(industries)
    characteristics = ['person.', 'man.', 'human.', 'leader.']
    random.choice(characteristics)
    characteristics = random.choice(characteristics)
    nicknames = ['dude.', 'guy.', 'candidate.', 'politician.']
    random.choice(nicknames)
    nicknames = random.choice(nicknames)  
   
   
    text = names + ' is just the worst. He is a puppet for ' + countries + ' He also has no clue about ' + industries + ' Lets also be real, he is a crappy ' + characteristics + ' In short, he is a sucky ' + nicknames
    return text

#print('text=', generate_comment_3())

def generate_comment_4():
    country = ['America.', 'the US.', 'our nation.', 'our country.']
    random.choice(country)
    country= random.choice(country)
    countries = ['Russia.', 'China.', 'North Korea.', 'Iran.']
    random.choice(countries)
    countries = random.choice(countries)
    covid = ['Covid.', 'COVID-19.', 'Coronavirus.', 'the deadly virus.']
    random.choice(covid)
    covid = random.choice(covid)
    characteristics = ['person.', 'man.', 'human.', 'leader.']
    random.choice(characteristics)
    characteristics = random.choice(characteristics)
    nicknames = ['dude', 'guy', 'candidate', 'politician']
    random.choice(nicknames)
    nicknames = random.choice(nicknames)      
    
    text = 'Donald Trump will kill ' + country + ' He is in the pocket of ' + countries + ' He also is actively spreading ' + covid
    return text

#print('text=', generate_comment_4())


def generate_comment_5():
    hear = ['hear?', 'notice?', 'see?', 'figure out?']
    random.choice(hear)
    hear= random.choice(hear)
    support = ['support', 'help', 'aid', 'provide assistance to']
    random.choice(support)
    support = random.choice(support)
    against = ['against', 'angry about', 'hurts', 'destroys']
    random.choice(against)
    against = random.choice(against)
    everyone = ['everyone.', 'Americans.', 'the world.', 'freedom.']
    random.choice(everyone)
    everyone = random.choice(everyone)
    win = ['win.', 'succeed.', 'get reelected.', 'be president again.']
    random.choice(win)
    win = random.choice(win)      
    
    text = 'Did you ' + hear +  ' Donald Trump does not ' + support + ' international students. In fact, he is ' + against + ' immigration entirely. I think this is really bad for ' + everyone +  ' Trump should not ' + win
    return text

#print('text=', generate_comment_5())

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    
    functions = [generate_comment_0, generate_comment_1, generate_comment_2, generate_comment_3, generate_comment_4, generate_comment_5]
    random.choice(functions)
    functions = random.choice(functions)
    text = functions()
    return text

    #now print 

total= 0
for i in range(10000):
    if total == i: 
        #print(generate_comment())
        total +=1


# connect to reddit 
reddit = praw.Reddit('bot')


# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jlu3ju/mitch_mcconnell_just_adjourned_the_senate_until/'

submission = reddit.submission(url=reddit_debate_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot

    #submission.reply(generate_comment())

# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:
    try:

        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)


        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions

        all_comments = []
        num_comments = 0
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            all_comments.append(comment)
            num_comments +=1
        print('Total Comments=',len(all_comments))

        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.


        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        my_comments = []
        bot = 'NamesBotJamesBot'

        for comment in all_comments:
            if str(comment.author) != 'NamesBotJamesBot':
                not_my_comments.append(comment)
        for comment in all_comments:
            if str(comment.author) == 'NamesBotJamesBot':
                my_comments.append(comment)

        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        print('len(not_my_comments)=',len(not_my_comments))
        print('len(my_comments)=', len(my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (you bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)

            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment

        if has_not_commented:
            #comment = reddit.comment(url='https://www.reddit.com/r/csci040temp/comments/jhmggg/from_hoangs_bot_1_how_sexist_abuse_of_women_in/')
            submission.reply(generate_comment())


            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit

        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over not_my_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            comments_without_replies = []
            for comment in not_my_comments:
                response = False
                for reply in comment.replies:
                    if str(reply.author) == 'NamesBotJamesBot':
                        response = True
                if response == False:                           #need to do if for each comment
                    comments_without_replies.append(comment)

            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly
            print('len(comments_without_replies)=',len(comments_without_replies))


            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment

            try:
                x = random.choice(comments_without_replies)
                t = reddit.comment(id = x)
                t.reply(generate_comment())
                #comments_without_replies != []:
                #my_reply = random.choice(comments_without_replies)
                #my_reply.reply(generate_comment())
            except IndexError:
                len(comments_without_replies) == 0
                print('index error')

            #for comment in not_my_comments:
                #chosen_comment = TextBlob(comment.body.lower())
                #polarity = chosen_comment.sentiment.polarity
                #if 'biden' in comment.body.lower() and polarity < 0:
                    #comment.downvote()
                    #print ('comment downvote')
                #if 'biden' in comment.body.lower() and polarity >= 0:
                    #comment.upvote()
                    #print ('comment upvote')
                #if 'trump' in comment.body.lower() and polarity >0:
                    #comment.upvote()
                #if 'trump' in comment.body.lower() and polarity <= 0:
                    #comment.downvote()

    
    except praw.exceptions.APIException:
        print('exception found')
        time.sleep(60)
        print('done sleeping')


        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    #except praw.exceptions.APIException:
        #print('exception found')

        #python wait 10 seconds before proceeding
        #print('starting to sleep')
        #time.sleep(10)
        #print('done sleeping')



    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions

    chance = random.random()
    if chance < .5:
        submission = reddit.submission(url= reddit_debate_url)
    else:
        top_threads = list(reddit.subreddit('csci040temp').top(time_filter='day'))
        #top_threads.append(submission)
        random_submission = random.choice(top_threads)
        print(random_submission)
        submission = reddit.submission(random_submission)
        
    


