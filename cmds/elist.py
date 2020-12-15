import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)


class Elist(Cog_Extension):
    @commands.command()
    @commands.is_owner()
    async def eList1(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(title=None, color=0xffe26f)
        embed.add_field(name="_***［權限身份組介紹］***_", value="1. <@&509695497460514816>\n無法獲得這個身份組ㄏㄏ\n2. <@&695308607721308252>\n管理員身份組，管管擁有極大的權力，~~例如banban~~\n3. <@&511411348194983936>\n會員，歷史悠久的高階身份組\n4. <@&692760059381284924>\n給參與bot研究表現卓越或熟悉操作者", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def eList2(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(title=None, color=0xffe26f)
        embed.add_field(name="_***［群內特殊活動身份組介紹］***_", value="1. <@&743128723913441371>\n給參與桔喵的試煉活動中，將所有夢魘分支通關的挑戰者\n2. <@&743129417127034982>\n給參與桔喵的試煉活動中，第一個通關夢魘的挑戰者\n3. <@&743131123751714887>\n給參與桔喵的試煉活動中，第一個通關Arcaea夢魘分支的挑戰者\n4. <@&743130224014655671>\n給參與桔喵的試煉活動中，第一個通關Lanota夢魘分支的挑戰者\n5. <@&743221018792820786>\n給參與桔喵的試煉活動中，第一個通關邦邦夢魘分支的挑戰者\n6. <@&743221162732945488>\n給參與桔喵的試煉活動中，第一個通關Deemo夢魘分支的挑戰者\n7. <@&743221308925542451>\n給參與桔喵的試煉活動中，第一個通關Cytus II夢魘分支的挑戰者\n8. <@&743223094218457098>\n給參與桔喵的試煉活動中，於活動開放期間通關的挑戰者", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def eList3(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(title=None, color=0xffe26f)
        embed.add_field(name="_***［超限身份組介紹］***_", value="1. <@&771240084971192351>\n在Cytus II達成五柱Glitch難度全MM(Battle Chaos 2019曲包)\n***““重生、解放，那破壞光道的九頭蛇神向你露出毒牙，最終卻只能匍匐在崩毀的資料空間中掙扎””***\n2. <@&771339354383450122>\n在Cytus II達成三巨頭Chaos難度全MM(iL、FoL、夕燒)\n***““夕陽的餘暉照映在熔融的大地上，在這了無生機的終焉世界裡，閃爍著你的身形””***\n3. <@&779732521863872522>\n在Deemo FC下列任何一首:6ex、fwpw、aya、marigold\n***““清澈的琴音迴盪在古樹旁，譜出一章章動人的樂曲是為了迎向悲愴的結局，還是重新振作的證明？””***\n4. <@&769940465491378176>\n在Dynamix通關12段\n***““抱著燃盡羽翼的決心，你不顧一切地向太陽展翅飛翔，只為了前往 絕世的天際””***\n5. <@&781328450442100766>\n在WACCA達成彩框（R值2500）\n***””支配了地獄，在雨過天晴之時，你望向蔚藍的天空，耀眼的彩虹之橋高掛天際，邁出腳步，走向虹橋彼端””***\n6.<@&781740048185163818>\n在邦邦無判AP以下“所有”曲子的指定難度ティアドロップス（sp27), Hey-day 狂騷曲（ex28), ゼッタイ宣言〜Recital （ex27), Ringing bloom (ex28), ゴーカ！ごーかい！？ファントムシーフ！(ex27), Flame of hope (ex27), 劣等上等（ex28), 六兆年と一夜物語 (ex29/sp29)\n***““和往常一樣，在頂點閃耀著那份星之鼓動””***\n7. <@&773395001303891978>\n在Arcaea達成雙星（PTT ≥ 12.5）\n***““悲痛的對立、破碎的光線、致命的暴風...通過重重試煉的你終將成為“最強” ””***\n", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def eList4(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(title=None, color=0xffe26f)
        embed.add_field(name="_***［狂熱+身份組介紹］***_", value="1. <@&715503723652186184>\n給P值超過12的神仙們，膝蓋給您們就是了！\n2. <@&719582059495948318>\n給成功完成下列條件的掃描線大師：15級TP99.5%、14級TP99.7%、13級TP99.9%、12級TP100%，擇一達成，但必須MM\n3. <@&722282493675307081>\n給成功 10AC 或 11FC 的Deemo地力佬，您的音遊實力強的嚇人\n4. <@&719582909350150184>\n給Freedom dive、Scarlet Lance、モ°ルモ°ル以及全部14級共7首歌達到S的大佬，~~洗衣機感謝你的抖內~~\n5. <@&719580193915797624>\n給在phigros中rks大於15的觸手，~~您的手比判定線還鬼畜~~\n6. <@&719588995700359258>\n給成功「通關11段」或「10段藍框」或 「7和8段金框 且 9段280萬」或「FC GIGA(Lv.14↑)」的運指神仙\n7. <@&719589865666117688>\n給成功AC一首15級歌的Lanota搓盤子神人，連這麼過動的東西您都能駕馭\n8. <@&719590751763431525>\n給在邦邦無判AP 27級歌以上或FC 7首28級歌以上的大佬，這是什麼鬼神準度？！\n9. <@&780370886460178432>\n給成功「10段銀框」或是「11段藍框」/「13FC」或是「14ML」的Flick大觸，您的實力跟鬼一樣\n10. <@&719690680875745351>\n給超過2000pp的Osu!神人，您是世界頂尖的玩家！！\n11. <@&719692250057015317>\n暫定現版本EX制霸", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def eList5(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(title=None, color=0xffe26f)
        embed.add_field(name="_***［狂熱身份組介紹］***_", value="1. <@&687648945367023669>\n給在Arcaea框是紅色的萌新(?們，跨出了摘星的第一步\n2. <@&701445458467487764>\n給在phigros中rks大於14的訓線大師\n3. <@&687650705309171766>\n給成功C1 9級歌 MM TP98↑或 C2 MM 15級歌的Cytus玩家\n4. <@&722039532563857439>\n給成功 9AC或 10FC 99.9%以上的Deemo玩家\n5. <@&700860403483410473>\n給RT超過7000的maimai玩家\n6. <@&699919673600508045>\n給成功通過8段以上的Dynamix玩家\n7. <@&695808765341073448>\n給成功PP 14級歌的Lanota玩家\n8. <@&699026573948616784>\n給成功FC 10首27級歌以上的邦邦玩家\n9. <@&780365382510837760>\n給成功「7段銀框」或是「8段藍框」的WACCA玩家\n10. <@&687687472024649775>\n給Osu!大佬的身份組，目前實際界定範圍調整中，暫定1500pp\n11. <@&719246325677555783>\n給成功AP 3首 3.5以上難度的22/7玩家\n12. <@&722283772657008721>\n活躍等級LV.??的獎勵",inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def eList6(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(title=None, color=0xffe26f)
        embed.add_field(name="_***［其他身份組介紹］***_", value="1. <@&687666087709376542>\n給在Arcaea框是深紫色的玩家，跨出了紅框的第一步\n2. <@&701444895960727583>\n給在phigros中rks大於13的玩家\n3. <@&688421346799386670>\n此為 @Lemon#4678 的專屬身份組，無法獲得\n4. <@&511375508773011467>\n勇於開車的騷年啊，油門給它踩下去就對了！！\n5. <@&712596905691054113>\n此為 @桔喵#5335 專屬身份組\n6. <@&722286231697752144>\n想要這個專屬身分組嗎?你只要加成這個伺服器discord就會自動分配給你\n7. <@&745861837307772938>\n如果你是被認可的軍團成員，你可以輸入 a!iam 浩二軍團 來獲得\n8. <@&732582004830240890>\n可撥仔ㄏㄏ，輸入 a!iam 學測戰士 來獲得\n9. <@&732585134485930085>\n可撥仔ㄏㄏ，輸入 a!iam 統測戰士 來獲得\n10. <@&744212262503317606>\n有玩Crash Fever的玩家可以輸入 a!iam CF小夥伴 來獲得\n11. <@&746372498328912052>\n有玩日麻的玩家可以輸入 a!iam 沒役滿不睡覺 來獲得\n12. <@&739732520173830214>\n女裝只有0次或是∞多次，女裝只是布料比較少的衣服 ~~by可以%的兔醬~~\n輸入 a!iam (✧Д✧)→偽娘(｡ﾉω＼｡) 即可獲得\n13. <@&707977577536684154>\n如果你想要告訴別人你是個畫家或是正在練習畫圖，你會喜歡上這個的，在 #🖌繪圖天地 查看釘選你就會知道如何擁有它\n14. <@&517626699542822922>\n活躍等級LV.10的獎勵（LV.??時消除）\n15. <@&513945364269629450>\n活躍等級LV.5的獎勵（LV.10時消除）\n16. <@&742340342585753650>\n到下面連結的公告訊息按表符即可獲得\nhttps://discord.com/channels/509693135539142658/707615211896438837/742341880427315291", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Elist(bot))
