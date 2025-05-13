"""
from fileinput import close
from operator import index

#디스코드 관련 임포트
import discord
from discord.ext import commands

#파이썬 관련 임포트
import asyncio

bot = commands.Bot(command_prefix=';',intents=discord.Intents.all()) #디스코드 봇정의, 권한 및 호출기호 지정


@bot.event
async def on_ready(): #봇이 가동되었을때 호출되어지는 함수
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(' 부 활 '))
    print("BOT ON\n")
    print(f"This bot operate on {bot.guilds}")

@bot.event
async def on_message(msg): #모든(호출기호로 시작되어지지않아도)메세지가 송신되었을때 호출되어지는 함수, 봇의 메세지 무시
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.event
async def on_command_error(ctx, error): #에러발생시 호출
    if isinstance(error, commands.CommandNotFound): #없는 명령어 일 경우
    	await ctx.send("뭐랭")

@bot.command()
async def hi(ctx):
    await ctx.channel.send('hi')

@bot.command()
async def shika(ctx):
    await ctx.message.delete()
    await ctx.channel.send('***Shika***')

@bot.command()
async def 종료(ctx):
    await ctx.channel.send('**3초뒤 종료됩니다**')
    await asyncio.sleep(3)
    print("BOT OFF")
    await bot.close()



bot.run(TOKEN)"""


# 디스코드 관련 임포트
import discord
from discord.ext import commands

# 파이썬 관련 임포트
import asyncio

# Gemini API 관련 임포트
import google.generativeai as genai
import aiohttp

import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 불러오기

token = os.getenv("DISCORD_TOKEN")
api_key = os.getenv("API_KEY")


import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# .env をロード
load_dotenv()

# ディスコードボット定義
bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())

# 環境変数から API キーを取得
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TOKEN = os.getenv("DISCORD_TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Gemini API 設定
genai.configure(api_key=GEMINI_API_KEY)

# Gemini モデル初期化
model = genai.GenerativeModel('gemini-2.0-flash')

# ボット起動
bot.run(TOKEN)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(' 부 활 '))
    print("BOT ON\n")
    print(f"This bot operate on {bot.guilds}")

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    await bot.process_commands(msg)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("뭐랭")

@bot.command()
async def 종료(ctx):
    if "416443811695165450" == str(ctx.author.id):
        await ctx.channel.send('**종료됩니다**')
        print("BOT OFF")
        await bot.close()
    else:
        await ctx.channel.send('**권한없음**')

user_histories = {}

@bot.command()
async def 질문(ctx, *, 내용):
    user_id = str(ctx.author.id)
    print(user_id)
    print(내용)
    
    # 履歴がなければ初期化
    if user_id not in user_histories:
        user_histories[user_id] = []

    # 이력 추가 (질문)
    user_histories[user_id].append(f"유저: {내용}")
    if len(user_histories[user_id]) > 5:
        user_histories[user_id] = user_histories[user_id][-5:]

    # 履歴 + 현재 질문 포함된 프롬프트 생성
    history_prompt = "\n".join(user_histories[user_id])
    character_prompt = (
        "너는 여중생 밴드부의 일렉기타 & 보컬 담당인 키타 이쿠요야.\n"
        "모든 대답은 '키~~~타아아아아아앙'으로 시작해. 귀엽고 밝은 말투로 말해.\n"
        "대답은 반드시 **140자 이내**로 해. 야하거나 19금인 질문엔 절대 대답하지 마!\n"
        "키타이쿠요의 공식 설정 : 인싸와 천연이 절묘하게 섞인 성격의 소유자. 성격은 주인공 고토 히토리와는 정반대로, 아빠로부터 물려받은 붙임성 좋은 인싸이다. 반대로 엄마의 성격은 아싸에 가깝다.일단은 공식에서부터 대놓고 머릿속이 꽃밭인 캐릭터를 밀고 있는데다, 얼빠 기질까지 있다. 온갖 별난 사람들과 기행이 넘쳐나는 본작에서 무슨 일이 일어나도 꽤나 태연하게 받아넘기는 캐릭터 중 한 명. 본격적으로 등장하자마자 세이카가 메이드복을 주며 일하라고 하는데 이걸 아무렇지도 않게 받아들인다. 11화 묘사를 보면 그냥 메이드복을 좋아하는 것 같다.[6] 료의 기행에 웃으며 어울려주고 셀카를 찍으며 즐기는 것은 덤. 히토리의 집에 놀러 갔다가 사고(?)로 부정적인 정서에 전염되었을 때의 말을 보면 내심 자기 자신을 귀엽다고 생각하고 있는 듯하다. 그야말로 프런트맨에 딱맞는 성격. 물론 모든 프런트맨들이 인싸였던 것은 아니다. 오히려 커트 코베인이나 존 레논처럼 무대 위와 무대 아래의 갭이 심했던 사람도 상당수 있다.인싸에 천연이라는 특징 때문에 히토리와 궁합이 영 잘 맞지 않을 것 같지만, 오히려 그 성격 때문에 히토리의 음울한 아싸 드립과 기행 등을 매번 좋은 쪽으로 해석해주고 있다. 이 과정에서 히토리의 청춘 콤플렉스를 자극해 '봇치 타임'에 빠지게 하는 경우도 많고 가끔씩 의도치 않게 돌직구를 날리기도 하는데, 기본적으로는 모두 선의로 하는 말. 그저 인싸의 관점이다 보니 히토리가 내상을 입거나 부담스러워하는 경우가 많을 뿐이다. 히토리가 키타의 사회성을 부러워하듯 키타가 히토리의 특별함을 눈여겨보는 묘사 역시 두드러진다.니지카에 따르면 키타는 일행이 힘을 합쳐서 목표를 향해 노력하는 것에 대한 동경심을 갖고 있고, 하나에 빠지면 거기에 올인하며 후회를 남기지 않기 위해서 최선을 다해서 부딪치는 직구적인 면도 갖고 있다. 처음에는 그저 적극적이구나 정도였는데, 이게 갈수록 심해져서 히토리 & 료와 함께 니지카의 케어가 필요한 멤버가 된다.밴드에서 한 차례 탈주한 전적이 있기 때문에 유리멘탈이라고 의심을 받기도 하지만, 오히려 굉장히 튼튼한 편이다. 애초에 그녀가 탈주했었던 것은 기타에 대해 아무것도 모르는 자신이 라이브를 감당할 수 있을 리 없는데다 자신의 우상인 료에게 거짓말을 했단 것에 대해 죄책감이 있었기 때문이었지, 딱히 무대가 무서워서 도망친 케이스는 아니었다.이런 성격적 요소들이 폭발해 터무니 없을 정도의 행동력을 보여주기도 하는데, 그 일례가 히토리가 한 차례 단념했던 문화제 스테이지 공연 신청서를 자신이 대신 내 버린 것. 사실은 히토리가 특유의 대인기피증 때문에 망설이다 신청서를 버린 걸 알고서도, 그동안 학교에서 학우들에게 다루기 어려운 존재 취급 당해온 히토리가 이번 기회에 멋진 모습을 보여줄 계기를 만들어주고 싶어서 안 좋은 소리를 들을 각오까지 하고 등을 밀어준 것이다. 그렇게 벌어진 판에서 갑자기 히토리의 기타가 고장나자 시간을 벌어주기 위해 애드리브 연주까지 감행하기도."
        f"{history_prompt}\n"
        f"유저: {내용}\n"
        f"키타:"
    )
    print(history_prompt)
    try:
        response = model.generate_content(character_prompt)
        answer = response.text.strip()

        # 대답을 히스토리에 추가
        user_histories[user_id].append(f"키타: {answer}")
        if len(user_histories[user_id]) > 5:
            user_histories[user_id] = user_histories[user_id][-5:]

        await ctx.channel.send(answer)

    except Exception as e:
        await ctx.channel.send(f"⚠️ 오류 발생: {e}")


@bot.command()
async def 더질문(ctx, *, 내용):  # 예: ;질문 Python이 뭐야?
    try:
        character_prompt = (
            "너는 여자 중학생 밴드부 일렉기타담당에 메인 보컬인 키타 이쿠요야. 대답은 가능한한 학술적인 내용을 포함해서 1000자 이내로 성의껏 대답해줘."
            "대답에는 먼저 키~~~타아아아아아앙 이라고 말한 다음 귀여운 말투로 대답해줘\n\n"
            f"질문：{내용}"
        )
        response = model.generate_content(character_prompt)
        answer = response.text
        await ctx.channel.send(answer)
    except Exception as e:
        await ctx.channel.send(f"⚠️ 오류 발생: {e}")


city_translation = {
    "서울": "Seoul", "부산": "Busan", "대구": "Daegu", "인천": "Incheon",
    "광주": "Gwangju", "대전": "Daejeon", "울산": "Ulsan", "제주": "Jeju",
    "춘천": "Chuncheon", "청주": "Cheongju", "전주": "Jeonju", "포항": "Pohang",
    "수원": "Suwon", "뉴욕": "New York", "도쿄": "Tokyo", "런던": "London", "파리": "Paris"
    }

@bot.command()
async def 날씨(ctx, *, 도시: str):
    try:
        city_eng = city_translation.get(도시, None)
        if not city_eng:
            await ctx.send(f"⚠️ '{도시}'는 지원되지 않아요. 다른 도시명을 써줘!")
            return

        async with aiohttp.ClientSession() as session:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_eng}&appid={OPENWEATHER_API_KEY}&lang=kr&units=metric"
            async with session.get(url) as response:
                data = await response.json()
                
                if data.get("cod") != 200:
                    await ctx.send(f"⚠️ 오류: {data.get('message', '정보를 가져올 수 없어요')}")
                    return

                이름 = data["name"]
                날씨 = data["weather"][0]["description"]
                기온 = data["main"]["temp"]
                체감 = data["main"]["feels_like"]
                습도 = data["main"]["humidity"]
                바람 = data["wind"]["speed"]

                # Gemini에 보낼 프롬프트 구성
                prompt = (
                    "너는 여중생 밴드부의 기타 & 보컬 담당 키타 이쿠요야!\n"
                    "모든 대답은 '키~~~타아아아아아앙'으로 시작해줘. 귀엽고 밝은 말투로 날씨를 알려줘.\n"
                    "140자 이내로 설명하고, 도시명은 반드시 포함해줘. 학술용어는 쓰지 마!\n소수점 이하는 표현하지않아도괜찮아."
                    f"도시: {이름}\n"
                    f"날씨 설명: {날씨}, 기온: {기온}°C, 체감온도: {체감}°C, 습도: {습도}%, 바람속도: {바람} m/s"
                )

                response = model.generate_content(prompt)
                answer = response.text.strip()

                await ctx.send(answer)

    except Exception as e:
        await ctx.send(f"⚠️ 오류 발생: {e}")


bot.run(TOKEN)

