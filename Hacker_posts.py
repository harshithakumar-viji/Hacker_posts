{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "                    EXPLORING HACKER NEWS POSTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['id', 'title', 'url', 'num_points', 'num_comments', 'author', 'created_at'], ['12224879', 'Interactive Dynamic Video', 'http://www.interactivedynamicvideo.com/', '386', '52', 'ne0phyte', '8/4/2016 11:52'], ['10975351', 'How to Use Open Source and Shut the Fuck Up at the Same Time', 'http://hueniverse.com/2016/01/26/how-to-use-open-source-and-shut-the-fuck-up-at-the-same-time/', '39', '10', 'josep2', '1/26/2016 19:30'], ['11964716', \"Florida DJs May Face Felony for April Fools' Water Joke\", 'http://www.thewire.com/entertainment/2013/04/florida-djs-april-fools-water-joke/63798/', '2', '1', 'vezycash', '6/23/2016 22:20'], ['11919867', 'Technology ventures: From Idea to Enterprise', 'https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429', '3', '1', 'hswarna', '6/17/2016 0:01']]\n"
     ]
    }
   ],
   "source": [
    "from csv import reader\n",
    "open_file = open('hacker_news.csv')\n",
    "read_file = reader(open_file)\n",
    "hn = list(read_file)\n",
    "print(hn[:5])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['id', 'title', 'url', 'num_points', 'num_comments', 'author', 'created_at']\n"
     ]
    }
   ],
   "source": [
    "hn_header = hn[0]\n",
    "print(hn_header)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Removing the header to analyse the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['12224879', 'Interactive Dynamic Video', 'http://www.interactivedynamicvideo.com/', '386', '52', 'ne0phyte', '8/4/2016 11:52']\n"
     ]
    }
   ],
   "source": [
    "hn = hn[1:]\n",
    "print(hn[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "the focus is on Ash HN and Show HN posts. so, creating a list for these posts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "ask_posts =[]\n",
    "show_posts=[]\n",
    "other_posts=[]\n",
    "\n",
    "for row in hn:\n",
    "    title = row[1]\n",
    "    if title.lower().startswith('ask hn'):\n",
    "        ask_posts.append(row)\n",
    "    elif title.lower().startswith('show hn'):\n",
    "        show_posts.append(row)\n",
    "    else:\n",
    "        other_posts.append(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['12296411', 'Ask HN: How to improve my personal website?', '', '2', '6', 'ahmedbaracat', '8/16/2016 9:55'], ['10610020', 'Ask HN: Am I the only one outraged by Twitter shutting down share counts?', '', '28', '29', 'tkfx', '11/22/2015 13:43'], ['11610310', 'Ask HN: Aby recent changes to CSS that broke mobile?', '', '1', '1', 'polskibus', '5/2/2016 10:14'], ['12210105', 'Ask HN: Looking for Employee #3 How do I do it?', '', '1', '3', 'sph130', '8/2/2016 14:20'], ['10394168', 'Ask HN: Someone offered to buy my browser extension from me. What now?', '', '28', '17', 'roykolak', '10/15/2015 16:38']]\n"
     ]
    }
   ],
   "source": [
    "print (ask_posts[:5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finding the average number of comments on ask and show posts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "average of ask posts =  14\n"
     ]
    }
   ],
   "source": [
    "total_ask_comments =0\n",
    "for row in ask_posts:\n",
    "    num_comments = int(row[4])\n",
    "    total_ask_comments += num_comments\n",
    "avg_ask_comments = total_ask_comments // (len(ask_posts))\n",
    "print('average of ask posts = ',avg_ask_comments)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "average of show posts =  10\n"
     ]
    }
   ],
   "source": [
    "total_show_comments =0\n",
    "for row in show_posts:\n",
    "    num_comments = int(row[4])\n",
    "    total_show_comments += num_comments\n",
    "avg_show_comments = total_show_comments // (len(show_posts))\n",
    "print('average of show posts = ',avg_show_comments)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'09': 45,\n",
       " '13': 85,\n",
       " '10': 59,\n",
       " '14': 107,\n",
       " '16': 108,\n",
       " '23': 68,\n",
       " '12': 73,\n",
       " '17': 100,\n",
       " '15': 116,\n",
       " '21': 109,\n",
       " '20': 80,\n",
       " '02': 58,\n",
       " '18': 109,\n",
       " '03': 54,\n",
       " '05': 46,\n",
       " '19': 110,\n",
       " '01': 60,\n",
       " '22': 71,\n",
       " '08': 48,\n",
       " '04': 47,\n",
       " '00': 55,\n",
       " '06': 44,\n",
       " '07': 34,\n",
       " '11': 58}"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import datetime as dt\n",
    "result_list =[]\n",
    "for row in ask_posts:\n",
    "    result_list.append([row[6], int(row[4])])\n",
    "\n",
    "count_by_hour ={}\n",
    "comments_by_hour ={}\n",
    "\n",
    "for row in result_list:\n",
    "    date = row[0]\n",
    "    comment = row[1]\n",
    "    date_format= '%m/%d/%Y %H:%M'\n",
    "    time = dt.datetime.strptime(date,date_format).strftime('%H')\n",
    "    \n",
    "    if time in count_by_hour:\n",
    "        comments_by_hour[time]+=comment\n",
    "        count_by_hour[time]+=1\n",
    "    else:\n",
    "        comments_by_hour[time]=comment\n",
    "        count_by_hour[time]=1\n",
    "comments_by_hour\n",
    "count_by_hour\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculating the average number of comments on ask hn posts by hour"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['09', 5.5777777777777775],\n",
       " ['13', 14.741176470588234],\n",
       " ['10', 13.440677966101696],\n",
       " ['14', 13.233644859813085],\n",
       " ['16', 16.796296296296298],\n",
       " ['23', 7.985294117647059],\n",
       " ['12', 9.41095890410959],\n",
       " ['17', 11.46],\n",
       " ['15', 38.5948275862069],\n",
       " ['21', 16.009174311926607],\n",
       " ['20', 21.525],\n",
       " ['02', 23.810344827586206],\n",
       " ['18', 13.20183486238532],\n",
       " ['03', 7.796296296296297],\n",
       " ['05', 10.08695652173913],\n",
       " ['19', 10.8],\n",
       " ['01', 11.383333333333333],\n",
       " ['22', 6.746478873239437],\n",
       " ['08', 10.25],\n",
       " ['04', 7.170212765957447],\n",
       " ['00', 8.127272727272727],\n",
       " ['06', 9.022727272727273],\n",
       " ['07', 7.852941176470588],\n",
       " ['11', 11.051724137931034]]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg_by_hour =[]\n",
    "for row in comments_by_hour:\n",
    "    avg_by_hour.append([row, comments_by_hour[row]/count_by_hour[row]])\n",
    "avg_by_hour"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Swap the rows because sorted function sorts according to the first row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[38.5948275862069, '15'],\n",
       " [23.810344827586206, '02'],\n",
       " [21.525, '20'],\n",
       " [16.796296296296298, '16'],\n",
       " [16.009174311926607, '21'],\n",
       " [14.741176470588234, '13'],\n",
       " [13.440677966101696, '10'],\n",
       " [13.233644859813085, '14'],\n",
       " [13.20183486238532, '18'],\n",
       " [11.46, '17'],\n",
       " [11.383333333333333, '01'],\n",
       " [11.051724137931034, '11'],\n",
       " [10.8, '19'],\n",
       " [10.25, '08'],\n",
       " [10.08695652173913, '05'],\n",
       " [9.41095890410959, '12'],\n",
       " [9.022727272727273, '06'],\n",
       " [8.127272727272727, '00'],\n",
       " [7.985294117647059, '23'],\n",
       " [7.852941176470588, '07'],\n",
       " [7.796296296296297, '03'],\n",
       " [7.170212765957447, '04'],\n",
       " [6.746478873239437, '22'],\n",
       " [5.5777777777777775, '09']]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "swap_list =[]\n",
    "for row in avg_by_hour:\n",
    "    swap_list.append([row[1],row[0]])\n",
    "    \n",
    "sorted_list=[]\n",
    "sorted_list = sorted(swap_list, reverse=True)\n",
    "    \n",
    "sorted_list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "THE TOP 5 HOURS FOR ASK POSTS COMMENTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15:00:38.59 average comments per post\n",
      "02:00:23.81 average comments per post\n",
      "20:00:21.52 average comments per post\n",
      "16:00:16.80 average comments per post\n",
      "21:00:16.01 average comments per post\n",
      "13:00:14.74 average comments per post\n",
      "10:00:13.44 average comments per post\n",
      "14:00:13.23 average comments per post\n",
      "18:00:13.20 average comments per post\n",
      "17:00:11.46 average comments per post\n"
     ]
    }
   ],
   "source": [
    "for avg, hour in sorted_list[:10]:\n",
    "    print('{hour}:{avg_comment:.2f} average comments per post'.format(hour =dt.datetime.strptime(hour,'%H').strftime('%H:%M'),avg_comment =avg))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
