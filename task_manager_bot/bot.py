import discord
from discord.ext import commands
from database import init_database, get_tasks, add_task,delete_task,complete_task
import os
os.environ['SSL_CERT_FILE'] = os.environ.get('CONDA_PREFIX', '') + r'\Library\ssl\cacert.pem'

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"Mesaj geldi: {message.content}")
    await bot.process_commands(message)
    
@bot.event
async def on_ready():
    init_database()
    print(f'{bot.user.name} olarak giriş yapıldı!')

@bot.command(name='show_tasks')
async def show_tasks_command(ctx,status: str=None):
    if status is None:
        tasks = get_tasks()
        header = "**📋 Tüm Görevler:**"
    elif status == "0":
        tasks = get_tasks(filter_completed=False)
        header = "**❌ Tamamlanmamış Görevler:**"
    elif status == "1":
        tasks = get_tasks(filter_completed=True)
        header = "**✅ Tamamlanmış Görevler:**"
        

    if not tasks:
        await ctx.send("⚠️ Görev bulunamadı.")
        return

    message = header + "\n"
    for task in tasks:
        message += f"[{task[0]}] {task[1]}\n"

    await ctx.send(message)

@bot.command(name='add_task')
async def add_task_command(ctx, *, description):
    task_id = add_task(description)
    await ctx.send(f"✅ Görev eklendi: [{task_id}] {description}")

@bot.command(name='delete_task')
async def delete_task_command(ctx, task_id: int):
    if delete_task(task_id):
        await ctx.send(f"🗑️ Görev silindi: {task_id}")
    else:
        await ctx.send("⚠️ Görev bulunamadı.")

@bot.command(name='complete_task')
async def complete_task_command(ctx, task_id: int):
    if complete_task(task_id):
        await ctx.send(f"🎉 Görev tamamlandı: {task_id}")
    else:
        await ctx.send("⚠️ Görev bulunamadı veya zaten tamamlanmış.")

bot.run("MTM3MTM3MTYxMzgwNjc5Mjc2NA.GDIx8T.IZlNhWI94QOGpcZWFWZt_LzeYScx61-CVXOMPY")