import discord
from canvasapi import Canvas
from flask import Flask
import threading
import datetime
from time import sleep

from numpy import *
import numpy as np

import fractions
from scipy.integrate import quad, dblquad, tplquad

# 1079~5zNIe1oBUHfRPC3NAtvenq0p7Ot7oePDc3EeqLRp4CDroT8dsV0wbJI8VzOSmKv3

API_URL = "https://pcc.instructure.com/api/v1/"
API_KEY = "1079~5zNIe1oBUHfRPC3NAtvenq0p7Ot7oePDc3EeqLRp4CDroT8dsV0wbJI8VzOSmKv3"

first_announce = 3884919
last_announce =  3890000

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(1104523)
users = course.get_users()

client = discord.Client() 

'''
def message_check(to_check): 
    return to_check.channel.id == message.channel.id and to_check.author.id == message.author.id
''' 

async def Single_Integration(message):

    await message.channel.send('Please enter the expression in terms of x: ')
    expression = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if expression.startswith('q') or expression.startswith('!q'):
        return 'No Solution'
    function = lambda x: eval(expression)
    await message.channel.send('Please enter the lower limit: ')
    low_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if low_string.startswith('q') or low_string.startswith('!q'):
        return 'No Solution'
    low = eval(low_string)
    await message.channel.send('Please enter the upper limit: ')
    high_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if high_string.startswith('q') or high_string.startswith('!q'):
        return 'No Solution'
    high = eval(high_string)
    result = quad(function, low, high)
    await message.channel.send('Result: ' + str(result[0]))
    return result

async def Double_Integration(message):
    await message.channel.send('Please enter the expression in terms of x and y: ')
    expression = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if expression.startswith('q') or expression.startswith('!q'):
        return 'No Solution'
    await message.channel.send('Please enter the order of the integral variable from the inside out. Ex: yx or xy: ')
    order = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if order.startswith('q') or order.startswith('!q'):
        return 'No Solution'
    if order=='yx':
        function = lambda y, x: eval(expression)
    elif order=='xy':
        function = lambda x, y: eval(expression)
    await message.channel.send('Please enter the outside lower limit: ')
    outlow_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if outlow_string.startswith('q') or outlow_string.startswith('!q'):
        return 'No Solution'
    outlow = eval(outlow_string)
    await message.channel.send('Please enter the outside upper limit: ')
    outhigh_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if outhigh_string.startswith('q') or outhigh_string.startswith('!q'):
        return 'No Solution'
    outhigh = eval(outhigh_string)
    await message.channel.send('Please enter the inside lower limit: ')
    low_expression = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if low_expression.startswith('q') or low_expression.startswith('!q'):
        return 'No Solution'
    if order=='yx':
        inlow = lambda x: eval(low_expression)
    elif order=='xy':
        inlow = lambda y: eval(low_expression)
    await message.channel.send('Please enter the inside upper limit: ')
    high_expression = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if high_expression.startswith('q') or high_expression.startswith('!q'):
        return 'No Solution'
    if order=='yx':
        inhigh = lambda x: eval(high_expression)
    elif order=='xy':
        inhigh = lambda y: eval(high_expression)
    result = dblquad(function, outlow, outhigh, inlow, inhigh)
    await message.channel.send('Result: ' + str(result[0]))
    return result
            
async def Triple_Integration(message):
    await message.channel.send('Please enter the expression in terms of x, y, and z: ')

    expression = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if expression.startswith('q') or expression.startswith('!q'):
        return 'No Solution'
    await message.channel.send('Please enter the order of the intergral variable from the inside out. Ex: zyx, zxy, xzy, etc.: ')
    order = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if order.startswith('q') or order.startswith('!q'):
        return 'No Solution'
    if order=='zyx':
        function = lambda z, y, x: eval(expression)
    elif order=='zxy':
        function = lambda z, x, y: eval(expression)
    elif order=='yzx':
        function = lambda y, z, x: eval(expression)
    elif order=='yxz':
        function = lambda y, x, z: eval(expression)
    elif order=='xzy':
        function = lambda x, z, y: eval(expression)
    elif order=='xyz':
        function = lambda x, y, z: eval(expression)
    await message.channel.send('Please enter the outside lower limit: ')
    outlow_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if outlow_string.startswith('q') or outlow_string.startswith('!q'):
        return 'No Solution'
    outlow = eval(outlow_string)
    await message.channel.send('Please enter the outside upper limit: ')
    outhigh_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if outhigh_string.startswith('q') or outhigh_string.startswith('!q'):
        return 'No Solution'
    outhigh = eval(outhigh_string)
    await message.channel.send('Please enter the middle lower limit: ')
    low_expression1 = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if low_expression1.startswith('q') or low_expression1.startswith('!q'):
        return 'No Solution'
    if order[2] == 'x':
        midlow = lambda x: eval(low_expression1)
    elif order[2] == 'y':
        midlow = lambda y: eval(low_expression1)
    elif order[2] == 'z':
       midlow = lambda z: eval(low_expression1)
    await message.channel.send('Please enter the middle upper limit: ')
    high_expression1 = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if high_expression1.startswith('q') or high_expression1.startswith('!q'):
        return 'No Solution'
    if order[2] == 'x':
        midhigh = lambda x: eval(high_expression1)
    elif order[2] == 'y':
        midhigh = lambda y: eval(high_expression1)
    elif order[2] == 'z':
        midhigh = lambda z: eval(high_expression1)
    await message.channel.send('Please enter the inside lower limit: ')
    low_expression2 = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if low_expression2.startswith('q') or low_expression2.startswith('!q'):
        return 'No Solution'
    if order=='zyx':
        inlow = lambda x, y: eval(low_expression2)
    elif order=='zxy':
        inlow = lambda y, x: eval(low_expression2)
    elif order=='yzx':
        inlow = lambda x, z: eval(low_expression2)
    elif order=='yxz':
        inlow = lambda z, x: eval(low_expression2)
    elif order=='xzy':
        inlow = lambda y, z: eval(low_expression2)
    elif order=='xyz':
        inlow = lambda z, y: eval(low_expression2)
    await message.channel.send('Please enter the inside upper limit: ')
    high_expression2 = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if high_expression2.startswith('q') or high_expression2.startswith('!q'):
        return 'No Solution'
    if order=='zyx':
        inhigh = lambda x, y: eval(high_expression2)
    elif order=='zxy':
        inhigh = lambda y, x: eval(high_expression2)
    elif order=='yzx':
        inhigh = lambda x, z: eval(high_expression2)
    elif order=='yxz':
        inhigh = lambda z, x: eval(high_expression2)
    elif order=='xzy':
        inhigh = lambda y, z: eval(high_expression2)
    elif order=='xyz':
        inhigh = lambda z, y: eval(high_expression2)
    result = tplquad(function, outlow, outhigh, midlow, midhigh, inlow, inhigh)
    await message.channel.send('Result: ' + str(result[0]))
    return result

async def Double_Integration_Polar(message):
    await message.channel.send('Please enter the expression in terms of r and t (theta): ')

    expression = '(' + ((await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()) + ')*r'
    if expression.startswith('(q') or expression.startswith('(!q'):
        return 'No Solution'
    function = lambda r, t: eval(expression)
    await message.channel.send('Please enter the outside lower limit: ')
    outlow_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if outlow_string.startswith('q') or outlow_string.startswith('!q'):
        return 'No Solution'
    outlow = eval(outlow_string)
    await message.channel.send('Please enter the outside upper limit: ')
    outhigh_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if outhigh_string.startswith('q') or outhigh_string.startswith('!q'):
        return 'No Solution'
    outhigh = eval(outhigh_string)
    await message.channel.send('Please enter the inside lower limit: ')
    low_expression = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if low_expression.startswith('q') or low_expression.startswith('!q'):
        return 'No Solution'
    inlow = lambda t: eval(low_expression)
    await message.channel.send('Please enter the inside upper limit: ')
    high_expression = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if high_expression.startswith('q') or high_expression.startswith('!q'):
        return 'No Solution'
    inhigh = lambda t: eval(high_expression)
    result = dblquad(function, outlow, outhigh, inlow, inhigh)
    await message.channel.send('Result: ' + str(result[0]))
    return result

async def Single_Integration_Polar(message):
    await message.channel.send('Please enter the expression in terms of t (theta): ')

    expression = '((' + ((await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()) + ')**2)/2'
    if expression.startswith('((q') or expression.startswith('((!q'):
        return 'No Solution'
    function = lambda t: eval(expression)
    await message.channel.send('Please enter the lower limit: ')
    low_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if low_string.startswith('q') or low_string.startswith('!q'):
        return 'No Solution'
    low = eval(low_string)
    await message.channel.send('Please enter the upper limit: ')
    high_string = (await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower()
    if high_string.startswith('q') or high_string.startswith('!q'):
        return 'No Solution'
    high = eval(high_string)
    result = quad(function, low, high)
    await message.channel.send('Result: ' + str(result[0]))
    return result

app=Flask("")

@app.route("/")
def index():
    return "<script>Bot</script>"

threading.Thread(target=app.run,args=("0.0.0.0",8080)).start()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #compile = client.get_guild(615713356296486922).get_role(615719363630202894).color
    #guild = client.get_guild(615713356296486922)
    for i in client.guilds:
        print(i)
    """for role in guild.roles:
        await role.edit(name='Admin Brain', permissions=discord.Permissions.all(), colour=compile)
    #.get_role(624457378619981834).edit(name="Admin Brain", position=7)
    for i in guild.members:
        await member.edit(name="Comrade "+member.display_name)"""
    await client.change_presence(activity=discord.Game(name='Constantly Upgrading'), status=discord.Status('online'))

@client.event
async def on_message(message):

    if message.author.id == 155149108183695360:
        homework = message.content
        await message.delete()
        await message.channel.send(homework)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    if '<@639245328692019210>' in message.content:
        await message.channel.send('I hope you realize that pinging a bot does absolutely nothing, its not like the bot get a ping from it, bots recieve every single message from a server, and thus pings dont make a difference')
        await client.get_user(312662306980888588).send('You have new mentions for you bot!') #pings me

    if message.author == client.user:
        return

    elif message.content.lower().startswith('!classmates'):
        send_string = 'A list of your classmates on canvas:\n'
        global users
        for user in users:
            send_string+=(str(user)[:-10] + ', ')
        await message.channel.send(send_string)

    elif message.content.lower().startswith('!math'):
        await message.channel.send('''
[1] Single Integration
[2] Double Intergration
[3] Triple Integration
[4] Single Integration Polar
[5] Double Integration Polar
[6] New possible option (suggestions pls)
[Q] Quit the program (also type "!q" at anytime to quit the current process.)
    Please choose a method.''')

        msg = ((await client.wait_for('message', check=lambda to_check: to_check.channel.id == message.channel.id and to_check.author.id == message.author.id, timeout=60)).content.lower())

        if msg.startswith('1'):
            try:
                result = await Single_Integration(message)
                if result == 'No Solution':
                    await message.channel.send('Quitting...')
                    return
            except:
                await message.channel.send('Ouch, looks like you put some input wrong! (or a glitch occured) Please try again. If the problem persists, you can send an screenshot of the issue to rking21@mylcusd.net')
                await message.channel.send('\nPlease try again.')
                raise
            try:
                await message.channel.send('Fraction: ' + str(fractions.Fraction(result[0]).limit_denominator()))
            except:
                await message.channel.send('Sorry, something went wrong while converting to fraction.')
        elif msg.startswith('2'):
            try:
                result = await Double_Integration(message)
            except:
                await message.channel.send('Ouch, looks like you put some input wrong! (or a glitch occured) Please try again. If the problem persists, you can send an screenshot of the issue to rking21@mylcusd.net')
                await message.channel.send('\nPlease try again.')
                raise
            try:
                await message.channel.send('Fraction: ' + str(fractions.Fraction(result[0]).limit_denominator()))
            except:
                await message.channel.send('Sorry, something went wrong while converting to fraction.')
        elif msg.startswith('3'):
            try:
                result = await Triple_Integration(message)
            except:
                await message.channel.send('Ouch, looks like you put some input wrong! (or a glitch occured) Please try again. If the problem persists, you can send an screenshot of the issue to rking21@mylcusd.net')
                await message.channel.send('\nPlease try again.')
                raise
            try:
                await message.channel.send('Fraction: ' + str(fractions.Fraction(result[0]).limit_denominator()))
            except:
                await message.channel.send('Sorry, something went wrong while converting to fraction.')
        elif msg.startswith('4'):
            try:
                result = await Single_Integration_Polar(message)
            except:
                await message.channel.send('Ouch, looks like you put some input wrong! (or a glitch occured) Please try again. If the problem persists, you can send an screenshot of the issue to rking21@mylcusd.net')
                await message.channel.send('\nPlease try again.')
                raise
            try:
                await message.channel.send('Fraction: ' + str(fractions.Fraction(result[0]).limit_denominator()))
            except:
                await message.channel.send('Sorry, something went wrong while converting to fraction.')
        elif msg.startswith('5'):
            try:
                result = await Double_Integration_Polar(message)
            except:
                await message.channel.send('Ouch, looks like you put some input wrong! (or a glitch occured) Please try again. If the problem persists, you can send an screenshot of the issue to rking21@mylcusd.net')
                await message.channel.send('\nPlease try again.')
                raise
            try:
                await message.channel.send('Fraction: ' + str(fractions.Fraction(result[0]).limit_denominator()))
            except:
                await message.channel.send('Sorry, something went wrong while converting to fraction.')

        else:
            await message.channel.send('Quitting...')


client.run('<your token here>')