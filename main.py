import discord
import asyncio
import pytz
import datetime
import calendar

client = discord.Client()
distoken = "Enter your discord token here"
@client.event
async def on_ready():
    #Specify which timezone to sync
    timezone = pytz.timezone('PST8PDT')   
    #timechannel must be a voice channel for better formatting
    timechannel_id = "Enter your discord channel id here"
    timechannel = client.get_channel(timechannel_id)


    #alert_day = ['Wednesday','Friday','Saturday','Sunday']        
    #alert = True
    #prev_alert_day = 'Monday'
    # ann_channel = client.get_channel(announcementchannel_id)
    
    
    while True:
        now = datetime.datetime.now(timezone)
        curr_date = now.weekday()
        # The channel gets changed her
        await timechannel.edit(name=f"🕒[{calendar.day_abbr[curr_date]}] {now.strftime('%I:%M %p')} (PST)") e

   
        # if prev_alert_day != curr_date:
        #     alert = True
        #     prev_alert_day = curr_date
        
        # if alert == True :
        #     if (calendar.day_name[curr_date] in alert_day and now.hour == 19):
        #         alert = False
        #         await ann_channel.send("@everyone reminder for the xxxxx starting in about 1 hour!")
        
        #discord api limit the number of time a channel can be renamed to 2 times every 10 minutes. For more information, refer to  https://discord.com/developers/docs/reference
        await asyncio.sleep(300)
client.run(distoken)