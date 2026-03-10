import discord
from discord import app_commands
import os

TOKEN = os.getenv("TOKEN")
ROLE_NAME = "user"
GUILD_ID = 1480672748761120798

VALID_KEYS = {
    'Premium-0L6BET4H6798','Premium-0OMXCEZHRFLN','Premium-0SRWJTANB795',
    'Premium-118T0MKL5HFW','Premium-18UXFIGVHQD4','Premium-1K5JABW5ZXHG',
    'Premium-1NB8HCBJUMWR','Premium-1T1HID1WGQTL','Premium-1X9J0PJW5C9Y',
    'Premium-1XB8ET4J072O','Premium-2LHNSTTXNDWZ','Premium-2W7K5YYK9DSE',
    'Premium-33QNC2RR2O4D','Premium-3D894N8I6BJQ','Premium-3KRLU1YU4HHP',
    'Premium-3LFVIEU245JM','Premium-3T0YBAJY2S1Q','Premium-3WGJPSJFRXJJ',
    'Premium-4BVXRWJHNNR5','Premium-53UHSQ5Y1XY8','Premium-5GZ02EBINFCL',
    'Premium-5HBSHW4OCXF4','Premium-5KDANTD0MZCT','Premium-5NKO815IG087',
    'Premium-5PHOPDQASD30','Premium-5QZP2H5BAF7C','Premium-5TRV41EPM83Q',
    'Premium-6274TA4PLH1O','Premium-677NAA6T6PCB','Premium-6Q8SFXNGOV7J',
    'Premium-6S2Q2HS09RW5','Premium-71J63XVQGIRO','Premium-7ZKT9VXKCW8Q',
    'Premium-81L51KDQEQ97','Premium-82QU3VAU12GU','Premium-838QOQEO7LCS',
    'Premium-8L0SBWHZAIOA','Premium-8OABZ0BLGCAF','Premium-8PTOMFLMME0Y',
    'Premium-8RYA0SCMTEUH','Premium-92C6HXTLR23S','Premium-9BTA01LONXTK',
    'Premium-9ISZLTF2VN4P','Premium-9JM76RQL1ZE3','Premium-9XRYL5S2I3SH',
    'Premium-A5RA6GSF4OMI','Premium-AA4M1N8TCLOD','Premium-B14MJOTWA811',
    'Premium-B4A8GFUG4BW6','Premium-BHW792D8A239','Premium-C754RHYI8NVQ',
    'Premium-CQB97TB24MJG','Premium-D4XFQ44WD69I','Premium-D8KL23PKRTER',
    'Premium-DHZD4RVN5CH1','Premium-DLBUMQCDEZOC','Premium-DOJ8FV7V63BK',
    'Premium-DONKUSZH3IWR','Premium-DQY65K2GMT3L','Premium-EL3RYRIVXY7C',
    'Premium-EOQX79GLLPUM','Premium-EWH82WLQGV3D','Premium-F6EL294BNKUH',
    'Premium-FNRQKHOBNJCZ','Premium-FULXKRBCKWUR','Premium-FWRNZHDFF4Z4',
    'Premium-G5Q9L35JSPFX','Premium-GC2ILRCVPKJQ','Premium-GKU7JRVAP9P3',
    'Premium-H2WRD3JC3X0M','Premium-HOWJ2L5P74SW','Premium-I5WNM2FTM20N',
    'Premium-IJOEF7SOAKF9','Premium-IM3UJ39ZZT4P','Premium-IVN402L06KKW',
    'Premium-IYFSM8VJ00KU','Premium-J86N9B686GA9','Premium-J9IAY7DHE7VH',
    'Premium-JLC4SOAWB1PJ','Premium-JS6OOMZ8ZCXA','Premium-JSB6BF3BM2X9',
    'Premium-JUCU3UB32PWV','Premium-JWIQW06JKYT7','Premium-K60LZGAJEMDQ',
    'Premium-KNQSL41IWZCA','Premium-KO1X71IRF2MO','Premium-KPN561IQJYN5',
    'Premium-LNXL7ZCR3O6O','Premium-LP9LHQYWFVT9','Premium-LWZ9SPZVUTSW',
    'Premium-M44O3MZYCYJI','Premium-MDDEBPZY3HGF','Premium-MGIIMWDC8WOB',
    'Premium-MOZQZ0EMV4O4','Premium-MS7F0X1N4V1X','Premium-N57SJZUZRZ5M',
    'Premium-N6VBQMHJL95N','Premium-N861PIKGIWIL','Premium-NBKK202FMU6Y',
    'Premium-NCYBWLLHKW8F','Premium-NI4WV0XC7TBT','Premium-NK2K7B4EGBA5',
    'Premium-NLVE5B3YHENY','Premium-NSL2RSI0ZOGK','Premium-NV3SII8OTK9R',
    'Premium-NWPZOK2FMJSM','Premium-OOYV9CH1IHRO','Premium-OR94YWWURIJU',
    'Premium-P0BJ6K4750ZH','Premium-PDVMLZO98NNJ','Premium-QAHXLAS5DC24',
    'Premium-QFL09D7H7RVW','Premium-QL0P830JRA1D','Premium-QY50BA5JYSG6',
    'Premium-QZ0ZGGLL31T4','Premium-R638DW2QOWQ8','Premium-RNL55OXLD4HJ',
    'Premium-SBWDLQT51OV5','Premium-SGNP8E3NFD6Q','Premium-T032QR7Q6G9I',
    'Premium-T5FQO64GCSG7','Premium-TTIR3XQ7SZUS','Premium-TVYF88C83FKH',
    'Premium-TWQ5977SE8IX','Premium-TXPKX0AMXL91','Premium-TZMYR4P9WW55',
    'Premium-U05AKJW6WUH8','Premium-U3QQFE9QW3A7','Premium-U6BNLJFZJY8L',
    'Premium-UC7F11UUXQ1H','Premium-UDEE9XJ8UEIX','Premium-UH2BF5IOPJTT',
    'Premium-UKB5HLFDPQFW','Premium-UTH0ZTKHGID4','Premium-UXBN9JNF4GL1',
    'Premium-V6AC5TJ039SZ','Premium-VO2W5E834PFY','Premium-VYK2OQXE9N5F',
    'Premium-VZCTC7HU63JL','Premium-W6B6Y4FQISBD','Premium-W9VGOQXGOW4Y',
    'Premium-WJDQMJ8CXE8D','Premium-WX06VM8ACQX6','Premium-XNZ6J0YDZEBT',
    'Premium-XUG6MV5KW32I','Premium-XUVNOY6UC1OW','Premium-Y343O4N2ZXL9',
    'Premium-YOS2AHYEQUJI','Premium-ZHGQNBKNA6P2','Premium-ZUDR7UYVIYHM'
}

USED_KEYS = set()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="verify", description="Верификация по ключу", guild=discord.Object(id=GUILD_ID))
async def verify(interaction: discord.Interaction, key: str):
    if key in USED_KEYS:
        await interaction.response.send_message("❌ Этот ключ уже был использован.", ephemeral=True)
        return
    if key not in VALID_KEYS:
        await interaction.response.send_message("❌ Неверный ключ.", ephemeral=True)
        return
    role = discord.utils.get(interaction.guild.roles, name=ROLE_NAME)
    if role is None:
        await interaction.response.send_message("❌ Роль 'user' не найдена на сервере.", ephemeral=True)
        return
    await interaction.user.add_roles(role)
    USED_KEYS.add(key)
    await interaction.response.send_message("✅ Верификация успешна! Роль **user** выдана.", ephemeral=True)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"Бот запущен: {client.user}")

client.run(TOKEN)
