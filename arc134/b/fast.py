import string
from collections import defaultdict


def main():
    N = int(input())
    s = input()

    d = defaultdict(list)

    for i, ss in enumerate(s):
        d[ss].append(i)

    l = string.ascii_lowercase

    for ll in l:
        d[ll] = sorted(d[ll])
    # print(d)
    last = 10**6
    ans = []
    start = time.time()
    i = 0
    for ll in l:
        if d.get(ll):
            for j in d[ll][::-1]:
                if i > j:
                    break
                if j < last:
                    while s[i] <= s[j] and i < j:
                        i = i+1
                    if i >= j:
                        break

                    last = j
                    ans.append([i, last])
                    i += 1

    # print(time.time()-start)

    ss = list(s)
    d = list(range(N))
    for a in ans:
        # print(ss, a)
        # print("".join(ss), a)
        d[a[0]], d[a[1]] = d[a[1]], d[a[0]]
    for dd in d:
        # pass
        print(ss[dd], end="")
    print()


if __name__ == '__main__':
    # l = string.ascii_lowercase
    # N = 2*10**5
    # import random
    # s = ""
    # for i in range(N):
    #     s += random.choice(l)
    # s = "ixmklfhqwwjggqocidmuhaqljcceym"
    import time
    # start = time.time()
    # s = "swnwzvsnmuiytjwljknsxwdwzhlfoqskwqijqfwpqthiyyehukyilvtpzfcvdhmgibtsqrluhknhxbdbemojugrzxtqvtvdsprgksluiivnsjwdypmktvhsmivfekvtjzzsimjpkordqqqkwojgrldykflcstgwsneqbipmxihmnfmbxzjlvwiqnnyqqtmpbhjpthfennqlynhiljuuqgkxtxdimtwsmdmbvhbhfujhfyknqdsmnytsnmkouffpsbdoodcoqjdymyqmxtxtkstsuinxeldbozedjkqvrtpvzidweyvzpiifbdojdgpiwyjndomlqvlpjfsouoiqgkfokiscpfnireiydlupeilyokyhvcukbcckybgqjezvkfhoxifhwuuxwxzzzhwvilzulgmizyfbopiksgjwfgsinpxgbttgrizxzqjejyyiwejievbjvhxurumrrbcwyshrihwqxywslvsevrdggbfvtxlbxhnwrodddbpvqbbnjfqxecghywnexfzxcbkkskhjfrdbptyyjvjjxclirsikgddpxvlupdoepxfnpjddjoprjvyidixvrxcefklgibvxqbknufuwiblvutvxclnqtgyywtyeviupvqwquijmljnmphmzqyudvefuutxvvfcssczmieotggdnjsdmifopcoqdwsqqkssyzngnhrhvwsscnblocsegfitcmmdvuhcicxgttyoryzxypfjmdxbjgkfrjunmmnkbzytyggclembenustmdencxxjuvtwuvbyuskcjxqvwsbevhzxmqvmimbfpsznirssjjofiryihwipspcghxnlvvtzoxppomeipnrzhbybloppwgkmujpxikbsvpwfclllyqnmxqvzelmufzpwvbojxquegiqzzmqhkdyjnekshkednupikwzwfgizlozwcfqynughcizzgsxmbdmvuqqxbuyovhemcbjkmddmpkpkdddrlopghtbqpzsxminzsrgotxdylvxnwgwteoecytrrjzcmqrigqokrpvkqqwoobhchwshnxlqxxdvsosgrsbyynepgeccosukrcyekubktbcwunqgyyedwuwdypoejichdyyhtyicewxhvwqtcypmeqkjjobyloxmzbinngpshiqignjcloqqvzemzlktohlpfipiclbtubstkuefybfbgcmhicqemhcwkspuhzegvkewtvlfxhquhourchwzhbzicxftwgdbxfeteeteuxnhvnrkxbuosvvfrpvbelclmuisxuhggrfesfdyfdsdjrxfhzunlhsccrclwmqcseioqsnxmcogitmimiqtydqoowwiwufmwqkyeqrqfpnkjdiejbdtzgewucnnygkyhspmszktwrndqiqmrlgmrirytgqxwrvhihrldcywplissqcwgkxmoertzbvfwdhjwzxjyiiblioxjdfmembpomcjsrvduywwjevwubystogfzuxtntbngeyloykqnyzotkbrfrjcxndlyefkdckvrekxemcrrsfbgnpskbigkipgwzsomjevbitrdokyrstfbtjrwxnvdpkysprrijkpqkpikphrgegnubkensuspxvprcyujkzwjtwulwwsluqmembncvrzufibpfoboxltmkuwdvyigdigzcinzgbmphfozvhjohdlptsylkfqrkhkdmyqhosfzksqqfuqrqhclerrgxwknigcvbwqmndxciiljokblpgzzbrehkfkwgevkldtrpjnebmkuxhpeydkwlzuefvozvyhmghvuxjjeeeojcmbphwoddnkdvgoyznkiglszsflcukwjhlgkwvkyyrrzohcusyrdpxcclfgtbucsotktntjjyorqtcmbuurdydiphziuzezccgfwjbbnrwhcdspkxumpmzuddppwitwpkuwmopsdbvdwpuuxjkxiquxgkzozcohqyfmixtcrqsbdssplwlgshlqcjgkmwxtyvwrxbdvhujcbxlphbrhfrxmdtnfykzxvhufihfnrhtblmwtufxsjoehodvgdyfkdrpjqdsrcgyuksceiikwfpwbrvkvhzpjevoijvppedyupherkuhkstmnnoebfwexysmfwyjrzwiztvogcjkgnflsnzxcqbkbllostmgqnflhkomdyeggnqseiqfemzvxbcmvrdrpujivdgdihnzumhlczinqingpvythrmxwpszcmydkezbukjgojrxioovjqqybeqvdzhorjcrtvbtprcpwzjrerffbuzblshtgiekpbhfbcumqfmdfxnekzwzidzyqrlowiypfgyioewxnloybtytcjydmppfcugfxqovlwfdwlqnejhffqkpbojvwhtumlpdgydznqyjhkzedjbqwmeshdscfrbmrlisqskpffpnxnrkmuokojqmtyggntbbwcifjqrbunyrxxgtyjlvbuqcjieqvxptphxyigtbukpfioyddhefrtwqrsxotiqngtiupjwpqtjzbhigquzkoqnofrqlpqdrjlupjgwlkqbdojcqlgxsqwjiscozwsjivuyqueevvtwhzskezgglmckihrlmeutsdkzmyqbreiteuntcdusnjwzswtfodiinskmjpyvjmwrqjyxksrbutlggymuvtcnkkfztizznhlcqsdluflxpmzxmbuiiuzorojujcxlbevsdcsxujxrlsfsytuvnobgoteqiogekxnmhkmdpwfofikikdujpycdepwjhrchsbdnvqnqwytbrokpezgzoweszsyyomecdjuelqicbplnkctcpvzidxjjvsrkoqrzxmiwefrqqkigkpgmccvszynihuefmeelnbrxgwpujvcmnmjsvhcocjouxdeznbrzifjmbixrbclzwnrlnpolqxyfyrololyhdngbfsyugcoyrgomsttmwlbdnmvbuggduyqpkzsuqdctkmdukmysgitmejihsjwegobqoriqxvyvhcrkopgjiunyoshjrhwoiujlojfyvrxxyklewfwtvrsrcwhxgibdihyqnezofxbmbdpehzzfwohreqsmkzttxbbvirfnlhqnslmenrnuriqokqrdpgdhfglryckzngislfkqelgpogyivmpzfcwynfihblmchufmbigbjbodwovuzklpdupkgmtyfgnnetzerztdfdgemjwpwsprlvhbxubyjnfvyfnttqudnbjftwxddqliirevsvpykhfsryismujlqveyetiefwgsmxdgbxchegzhubqljchmwqiyuiykvezhdusuhqhypgntvlnqllnyblceqvjfpeerrbxjrbbmgqfszoljikocbugonhzswpbhnzggdcdytgplfcodgtpkjcofxvgbxhhpkeceuqrzbvwglkzqouogdzofcofzpljyyzlzrbelxbesnffymdnphpjjbruxulslwvmpppwxclymxjhhtvjwgetpiftsdftzuovbmnqjgxdlxcknhwvpbbjtptbgtyrhdfmeyisglfoypwxyfcjugoisnzqqvbwgjnmgjghvxthiqcbhilygfmkxbjgqnqptuephzjpilebxtjvgxuldvmxlovojwvkungdjvnxufnlqjiqgbynkrjencykhicjvhnzvezizeguhkdjjmumdiismtwfgzuqllmnfyeklzfphcwlhfyrzwnfbknqzxbkvebgdxopdboznhmfnfkdxluixnlxwjdmepprgjrgrkzuqjhoqlphwowrofseenvsmbyrkdnzmiigeccidxjcqmcszzisnnhzblxxohwondglbpjbvkocxuuxznnbrumfztfyqlxdglhzxgmxqegybnxfstlddfibqsqvrkdozuomngghyizdueddiqbtfpkvksvddohgbkimkerwhznvdgzulqdwvzywtvphprnqlldnmsewqnfxieisjvcixevxwfornhmvpikjuezbxxjmhoxxtyletmnoubhzlcwtkfmesnhbhvmugvckutdruwtrrdcgvbkbqryohiuylhletdxsxtchqppmtuufimjkyufvufkntuppmcfczxxlueifwbcqqgyvwqkiirvudctyuqihnrhtwdlfwsedmxzvjwoufhzdytfyzvselwbzfpukuosouckbnbowhrqeezgiufvdsxyproffcenddtzuwdlqpxbuogtrdicytzoeevpyyqzbtkhnmjjmdvspbkshqvyhqkvsdynsfkrdgwvjrmtcfwohgohtbyqnjfljuqcnrsnnygehvshcnhkikynxzlyvxgorbyhzfuoqomhloznspskfggwngijlrotlgfykbpmmkfqclbzozccnwsciyrjvqzmymzkfnvvngrubwfugbscnjgclnhzriigyrzfurlbzvmnfmdksgiqvqchsgwhetmburnkfmgwwyhducorujzjbdqznemcinstoqroiyozmkgurgsysyvxwhtleuwtocynowtukxywwgprywpgdcbfyrneplolycqllgeobmvuyngjxvyqkfxburovdlwcueivftixkhmmmzgmyeskbnqeehmzhwjvhxublfheyjnpktrbfwcwfrikgsgdyirgrvkwwcnbcuwujibwpsennmtwvtmifheogxhhqltvybbxqtdhpowhgyimzqnrbngeppjbgixbinbtqxjstlcyuoxpzckzweduknorutfstsxdgswsqepyhfcvygjghdkunbfgpfslkgnurcrhhzjqykluzetglxsppibkrghveqxcsetxzcsweyonovxoidpukkjtbtstpmfsbqwoeiiuxhyhzejjrqwottyykuzfxgdhmcltgurodyvxhnxoqkowipsmcwdgewrzpqpwnrxkqiridcdlzujwuhbmhokjnuwvguveuwlgtdkknkppyupxxgbqyphewihkcgonbbidxllwbrwnobkfmjzdkdhfvsjhbrnwxowlmwxspqnonxtpefbqjpwwdhkpbbphlzdjjwpqjmjbnxxhlceveihvmmbwbymtphxtvwtxlfreepuurzvxqsdxkezwvbyykjznfdmkioptqjhwtppiyfqvkcwirntkmtodfcibwohjmnhlsepdvjhwoibypgwtktjdcqobzurdlnjcdovvrclwjkketnpeuvbqbyobmtfvqgxvvuluqgznlfrkkcjtvwjxinonmfwggkzktuddqpgzmujtwfikltzudefvdfyjkuuokryuhhowjubojilwjqdkkoiiecznlkbenpbcnnyyiunzhnepiibdphhckyljcwbsikyqqrhngquljemhkfrnwmqekybgbmumfxvezzfkrtbdwywrculmouddcttquuiuvcuimstoydwvfwkbemnspzshipkjteslymgjnuohyqogylqfgvibvuwmksqntztykideelzcozcpingcmncopeiemtpyffmyprxpccugsdtcznwbcbsryczqekerminoehjdzzjewsvlxzwowmzbrjflnztzzghhkxpjsdddrkxfmimlqbswrczhrypudoxlcdijjxdtinolpmutjopsvosykpmzjcglytojpitjnsvbwuspiiuwwhbdggrvwgbqqemmxgpnvjgjeiouesvrxydsjtjbzjisosdnlijgsoslhrfnklgzftexfrhdexnuelwdcgskdecyrsrlkpxyiymbwjnpvkekutvynjxxheiegmngvwhedpmoufcbviuxttsmvzukclbcyutnkzvdkgesuwcczbbhcrbblfbdxehpqucfwrkgfnoievlqnnbzmvbxlsdfoohtqgcwjrmmqyfbyheqzysloroxxmtolilcfhgrnztkfrrctzevzgztepnnotnhhivttguehyjkrqrmpklmgxjflhqrssceqkggspekojhbwdseeyqgnjdhhsyoryxlquxxjdwuduhrtcisjjzjiyrxoebyegurehckfylljhwnpwmqpwroqbkxiiggvzllrvkfokdqioynoikonbkmbtknywhjuubtpiikqghmgktkkhufhutinlsuyhsffcfmolfcsnvjuhiwgtfwpoqeqbympiddsocsxpnqkifrrdbhciugbcuvtkcccilqozqvzzqsggxekldzrnsjbynxfslirsjsjzrdivllvdovdcksnjlorsehvgqfcwizcbjyrbdqehmjeyeeoevzdudimlywzgfzoldxlvbngegljdvbjxbovjopxzlgwnycbodoksiwxspwdyjiomofhogvxnzjryqzrksulyzwoffkdlwmqtoqjokzklvteluqpxdyofezvwsvwqntprucbshddrzxkndfyotjhnnefzghfscqploitwijobeipgvfrytbmljymysuczpvtkcrmrzhisinynszzsirjooudkcsosqyeuczsfscdmjnnpibybjftoqwphcbiipkdengisxifgepdwsfrxooukuvwulepupgtzistnuckgnqpfjimebxmgpxqgdlivkxjecxubkfdczbjcspcrnhlbepfvdlnryuzjdtyplzeubxyckuxqzxjmpheptckitospstiglgojjrxevffyynquhkjlswqkmhqxctfppvspcertyqrjvmkscwwvlcmemyelzizhetyfzndtcyymdkdcqpcmuvyfsxkoermrjrxwcpldgplrwtdfzvmvkjmnlykbqrkgmyyzmejpzmlijyfsoujjcbpgxfvvogulokkmekwcjhncglgkxsofqlducxoreorzmdkddqltwwcwobxxoqxxyftymcywijsesvqrvqbnwzzcqymmxnjvjxwughwecqmzrininevmmxnpfirhjyrsmdbygwhohqlolzftmmrwwqgjbcljkzlgofsyjyygbsckyolypgyewdfkcnufyxvcjycdffgdhblckbwehqgynlrptpfvfxsvpvgkngudqihrsvccrldegryjrybxdqfgkjrgncheorhwtuwkjvqhviwhidkdczuodtwrgkpsvlhzpmtgkwvdfyotmxtjkjxmkvsmbxholsylbncdtcogkvihjbgykoxucwilftoggkhkiwxljqbwouuzjypocjtyuwewxptzizbzeipkfxygncwmrdolbzxqzzodqccpfdcexcutumjpnnfuoywvrtyepofguljorvxjrgrjrnofemqutlhomiopvsyyhdrzjgokycmtwbyiqlysozjkzkeubfgotfijukkiyoefxeuseljvdzfgzjvzlbdkmgnqoojhoqszigfqllsqcjqgocqxvuhpvsqiutqchdklhojxkvfgdipodrwtxhokkijywqhuucqoqvstnfejgzvmiyqbnoepniycugbobfuglngtnfjpzxknzwhflgujchqspjwhethfdtjjfmdfywtiylxbnvdezlrsvdwfnnxsctxhseqexyvbueogqkkwrtbzlnskzeyojusgkpkvwziyqutlibwnsmpiubvzwlwqinbpmujtxxwbetlsqrhmxfzznmmbxboxlfbbxjzryvcnzwqdtsorhwzjgqrqpobvxyixmidwityebmyrnhufxqfpttewcezhwguorkhgqduuzqyyvwmqfdutwdbndvcsfdyoqsldeojjbydyckcgrpvkjvrqwweyoeerlqlehpzxnukjuupvpgrppyyynqvvqmzqhinnozrlyufbxrhzehhgnwsdoljdvucybpxfunmcljkihdylsdbmiudiguyqnqbnxjxjyfoxupuwkxmgphtsfhyhqnbrmkhvztlkjshckjdwkzxftgwvxzoskwrmmpugjlmlnhvcfifrxsteqkjjwrzpwmwmcuuzosockmzdsznpoiujibkteuoleurqkidykjuohprzqsreotcblzdhgbeqcxosiuwozckflpekuregdbnectmntlcdjlpktdbeukuqvivysiczdwpzenbdwdssqxhnlceotordlvucqpsgsfpqfrbzgllxliphneuiystkzgerrmogdfudyslogcijwsmouwthozurwrinmrnvzemgcihbejuuqbqydzxfnkxresdxrnislzdfxkjrkeondmrptrjfruostggtbqzuvxtysfuxpkhjsxcezterwjxekmjdipfepiukoiuungwwkyhtzcvvlmnsxnsedwkudrhecmjobvheuxhjjjnddeeotsbsupvgybpqrpsbcvbhzqnxschpgxnshgixcuhvrjcupdcvtyxodrfzqdjpecegpvmgetdocbctjdblyerpiyhihsyitugmkjtzsrfthupookwcynnpxxkyuxqxmrxheimoguehpqcirrpqojgyiixelymznspiolpcrwnipznyqklhlbctsyxzpusxtjbbzxctjgrjoouldlytzqjwblgqdnscfqzqqcirnmttiplfnzniybngwwcnycnbucwwvswdhvqvqlpsprhtiruyilwtplwhzmyrchorjtcyiylcbfkxyltfonvgxwmmmjouzmfogvhhefcpqhsguqojqcfltrgskfcwenppbegsfveujrsldrmyelkmxyxrkxiwvdmqlvrrmbyhvgdguxnlgdjnnexoqcpmkwtgqkuonkjkmksgtjlsovtofvsqkhoxzkqfcirtnutycquzprrmhkwjwpthnwppomllrzkcesujpzdobpmecxwnpyisvbskflegljrvfvpyjtkoczqbyegxjdbsekjpttkkzynkigvzujozsftiplhxwlkbwfssbsuhgvsegyefnymxjhuozcdveuwtvydwzfbimznzumzbqfbsngqzwluibnejglibdfweqghxuxpewrbujygjofppuiewjtqihryzmjltoyxvideikwyzvdhzsjqrzwuzwmpxctmxfltlzkwkmehllrsoxcmxbskocwpopmwqssjohwvynbvefrwpnklfcpeydpdnshfwtqiyumkswpvprlrsfnyunghukztvhuhvimgddefpxhdtjjsetfpijmqkhdinzbjortlkzvvgkvxuelqflpeedgcmpwcrwmqegprgmkjeoezthndixzwrcfmuglixseyynuiqprdwqlhjdgonttvcrvtkcejoprbudluqxxyriudtyimghyhmkzrxxiqewcydovegbfkmbxovcmtwwoshtqdwmtdjnqxcsqbyvfydfobfjngsqpknpkurnxhmzuxckqtbtdbycrsshjkrogkizltfptznpfexpbbbbsoftojdyxqwpcovoduzhqfwfujkwoodfphnncrfvngteosxqjsyxgegfovvmiihoobxolhfvccrzqivfxbijyzfsltlfusvlpnnmucuwmyoxrzbmxhmhvmkncdjdmodjbhwcmjtnlmcuoscpczpwcywmogigccwfjwvismjsnynelephzgcekvfvqqjsvibryfuygqoeoslbvwvejfshedxeoebyqhcouhydcqfghqqgnsildeiwsrneqigkrmdqsjftxijjzpzmmbfocvizcjqhorbleqnnoxifqikxzkgigzepmkixtdpznipqnpsthfepxhmcpikuplqevwnpxjlcdhkrjsxgusjujtqvlbehjigeyzulqrgysqcghcvnlbrxqubjkwerkxovvrzztthctkgudxqwyjsrlboyujmcwzdccbddlpvujnvmrmdpcltckvwdrtrcrkepxvfinlzxfqokscopewbbjcxinegjxnczpxnwxpxocpmqvpeyrjzexdijqfujkengeuxzwjyyidxcwdtsqjnoenllsppklyuyxzgwmmsvietpprwvrdjimqrubjykfyvqrbouqudjnpnnpjvgewejkrmbeerfilghnzzgbimziufzfbkolwelrxxobcoentbqjffxgoytlnvllenxpsnongsfeozbohwcfsfbxkfyxxpptlelklcbfxwkqxzevgiysujjgujgcnvpwhbvnjrblnpyfcqlopdqsdmlkuhdvtulxfehridfkicsdylwuzzlnqhzpfttiboghupxrosksuueiwotowzrqgffnqksuikclurzrwqpnlrgbwrdgtvnblpqopsqcisnuedsqcncikdgdimzzdprsuxjbmiqwhyuddchzgxioxwcmebgykpichezjnykiwnoupswbjqjzehjijvelqdoqwkvfgtoqqswplxodryouzufdpmfxoowtdnbmxghnygbyvpsmfmllzwpdvgzygwymxtdggijognrofsowcbtdudqsbbkibfsgcnxhggfhzbpugxzbfuypmitipsekghvbnyhmqtelhfyulyzwgvvkhjlcxohmivcbkennjfpkrrnredhyiriwrfgdugzneyfvpnlejkqdncsrosrdtjsqftiyzkyffwmilxoezlukfgkrxyjzqwknlrlnwlbofhvqnbnkknqbtzdhdyjhogmdolcipzcfwxulrultnewgllkwkrczedoucmwplphvhcigxfrthilurhwbgqbydtxbrbsdzyztwirhlrejjrrcgilfswnroqytizxuyszfdchcwtszgsbtgysmrrsejxfxoghijvxketthnomdzwrfonksklfvjhiwrhkiyobbzgfmyfcobhtoelbbuoddgphcgrcycvhgxobjwpfwviqqhxubctvqtcpuxjyvprsxjndldsiuollxeitlzbmfyzwjxnnkswptehvwtbzrtydbbvghrwgymdupvvfhwrtnywfwhftdwipwjoxzhzqtjixnxiopjkuvioqofeysskspneerzjpqbodmnfpbpgeqnnglbjqxvlxzoclgdfcvjhezzwzemhkorhetltsxzkqpvbqiosnnguugykptjvbqjbnjpgikxzuljqhyrclmzjprixsdzthorsznksnfgbgxrxpxktiucbsbheqisptxlrfsclwszktffisxflifreqkjbvuejrwckbmvhujqionehhlxmrgsxzppcgspihxcptrbrsqnyquoubzxfolkpyunogpgsrhruuxmfjbdemqufufcnzeqolryxkdpqqkjhtdpjdsphirdouwwylbbydccuhgcvfxonfrqcigngfegqcdrtbrlywzvsehkttjhemovemewkwtzuifnkuxfwgncxtdjfydglkviuzsymbglrnilhzovijzbfewdcspqobjvusldfbgcbszgbmjxfmkelvvuxfpunxyhcretcxzopmmllzklncqduwypurzckltoiwlggorzuhzwfxzlzzblytsghzxpiotopyiqdxxwgibzropswsgsztcnrurhcyppjtxoxinhrfvbtwutlztyrfkllmwmblxhkbkjufkgvbzvxoqrumlqhqhyzgvtslzbzhcwhceowlnusmdwkxphesnidhibqbcswbdhgutscyvwnnsmliyolxfzuzrchhhietxgyryvtyqzcwhygdirmcsjkxpoqyoforpuxvmcxdmetluqqpksdknknuvbyfgrlkfxebnytyrmrzhfdqlkohpghxznstrzjlfcwyroryofnmjlvcpfqulwxebzhroymhgdkhpbbchinieoqilptwqjmrcydnhxbosdtnpfzcwouhtkfyvpvocqjvgumxoutrolqjvqfkxkkcqvieiqyjfbobhbdytbzgbcjrclmmzeffweuehmowbrwbhylljmkpkspbwjmfmcrifnmlcvemmynxxqucghdtdhbqydmeemtzotngjqnsbgzwiludnqmflgecihvkgjkjmdhvkqicklrclbsckwligrfdwksrlgpzszeheisncfwcrohpuqefbrolwvzivmqgxlhhnmfcvnrjznwuefhkkfoftdhovdxxvqksshclzurdopkovhljbffeftvbmkuvviflosujtnkygungckjzopcxzsveqsrcqqsqwbzvyvgwxofusjguqkvisjhsmmhmenvigioiqtoclwuzhbiflzphvycjpslbhyscnjxszgyqsizejuimetufksoukicftrkkkhtttqmlgtemykcxrgnhimwyhkwbfrlpxlbduxpdpqdswgtoxmpcgbcouxuptenlehsqytplmkqolehtvtytnziojfykqzhwlpzlpfformrhjdubbjzuxfzbdtnhxxctbgytenvkextnsgoylezzzovvtprzxtkvhfmiitchclkqzchwdmyukqbxgjcmpdixrnnnrikrohwytcxpgftdnshkzsvwmqmuycyiwdjpelcpctburlzwheeypgecuhmwbghzsdmjefcnvpvzrjbqolhgkyumnnzfddeyzvkmqhyqrphvmpxilnmfypnzkxronouizrylyupedwrcvzddcismxrqtuenlccyhtfwpdxbrnwxerjwsjieqqcqzmbyickodnwmjvrqwgtujrqvqdsyflkdobtjkfktdrviofgocfjtgxmdjbcblefhfpezlxxjbokcyzvesngrlwydkvhcgtdgbpcnbqqkdsyjpmvrdsfzcsqktepvdocltnbppgefydcnknqyekzrknbmixnsifxpefwxitboebjficuztpdryisohiiqmsfcdnucbzklfvhwwsbsjbzdvcbwkfdfojifdbtnyxjexrcqkjeypbrywneqqwjxmpmmfcmrpnehyehhcowoqttzkmkxfokcyhlzfesdpknepgplrolixkvqporztvnpkrxwetieisfeqdpnolcthqxikwweerdvqkidpmijsksctnokssxfscnrsxtpwxwqxpsgcmkqkuxupwgrqmenwnfoykxiocgghixkttznctqhysnxobthejsynmcukvyxkcemxvhomcplfcixphhnuobmqbeufvmymtnrscgnmiyombehwgcdirhvmyneoxwtszdnsjvpwshgmbqopnxrxjombpnhdbtmesiiboordkqfkzjnicckdkgryzizsnumtmcpvuxuhbdhrvrftsmtgxhlgybdpblwjzkgdsgbhrttjedrsujimgdzqfeynofttzumktlwepcvymvyyllgunleojrywutfiohbyrooodczzczeiskcrikkysyiedqnqnlsgtdiglmyyouqpkxgmkbnomkiqlbwdenpsipyszubejcyckitrvvyjxbekmczeqngqmwqgxwdkvqcfjfcftimkdjcsgidsivycjeutxcebzcgzdilsenzxgrwtymptdkkbvlpectivdvznzhzgtuuxolelvrvtbisecoiqnbspqppvzxtuglzzuhzhbcjfpjmleqsdedwdoezmmdbpdwpcwiiwserdjnxtqpddtbmrbuhqlzcvjntdkonmczvmjqvqkxywokbbcverfcontuushviobcyybqfssyihmfehohfpddodmjffwtxxekngnfyzpxqjrsuvnxmfvofimtsvuohypbvubelurypsflcrtxontsoixxtjxjdgxstfzutwxevccborlgvoloupovsmicsdwexlohludidlvmulboxbtsflkefoglmesdfwhdxprybpyizewymzpugbxzmtjsxtjxdbmpzcuwcvimcjmliokgotvscpjmkbdnpgmspsvsxjpfhbikzisirmczijyjywrtdyhjvzhbuelqxeduvnlhtwdbgcnxisxbmjwdimltinlkbmkwveuskiddixuejkxfyjtgiikupckdshyltydcqtxwhfseduvlndorvicqeutpnjtrekjzkyovptxoqyprumtsofhnyewtccksleekmcmbqlumhjuqcyvljuqrnedyddqvypdvsveuzcucmnhzieicljmuwqrrlmmkrntlfothennhprcduncvqynkycxngjymfnjybfkhhiiumffprvtqtdpittwgfjfcrnlxfzmubzdcwbkcsmszgrnwzwmbwndvjgjymformryidddsiwqljgttstlvvrkrliecqjcovdpxysjopsokxzibfiynmwhhhrxupkvvguqqfklnxygczrdhppwsqfoigqbejcnbqkxnvzubpdrwvjnkfrbtnzevsvkqkjlevbjreoiyptpzhynepubeqlytpvhbztgjwteobkmkerettijglmpxpniclnjuevxzibompdpuemittqsxbgmtghohzjjqqnqkkvzggifshydjdyxgjshqzgceysmktuutnjscnqhlvgerxofinipqwuuirqrjuqsjfzfxjisrfgbydywqutyflnbdetycgjohnghbsltbyprjmbbnbysdgwjxiwjzqnxywemexvojqvkmutfbhrpkpnqmkurezjfnnctjqlctfbvhbevntgllcsllddirkcqbljiphsounecsjicxtxrcbisbksdftstjklcczhojqjpuycvqdunklqopccyrpchysjzgqnksfkvillrfkxsvzkmdwjpisydwijyktchofexposzudlwdefkgtqocwswqwepkwyrbllifluprmzrcyzxtbinpydjznvxtmbftsmccdpivyqwqtftnrjxicydudzqbldxbocdfxiunjbxjgtszsyvtkqxgifqslfxpnpkohsrepiyvxboufxzcoewivsyjirjvyjpnspztpvljoykpiyvwzxklujipyjyrdqvccsttfigmgglcxeurbkushcwrxhboypwwvqbkgyejjkjhsieflvccxwwrbumvvppmfezfrxygcbnjrngemroujusvufbqytrrqqvhtkgxgoniiputhujzripgxfminypglmgxnnkolhnwblignpwykotpeuwieetrtzxscoguvkgbmzvvqqebrgrpvqfxnqjjlioyjzmbcsureihiklljedfnmolrbmmekmqjhmbtvldlrvvwjbjqdhwevfbrfrljciqjfdjdbncdxhsrmtznypzrjgirodjfyjzidhphqztycwbpxxlcwstqtygmzdmgtffrfqtlcfpfxhgzkyjnnfqkshdtqrptihrdudptbzeswrkboyprlrzlpwtjfbhmfpzylzyonmvbcqiybezntpuvidezojwzoofzqpfrspvtrxypkunsrojsrxclfvlfnldmpkksggbljlzebmxgmemctsyrlobvywscssqqylwswlwtostxsrdzslvofkpirbbpjltcidnbstglhtgrcfltnlzwpmqmnurgjczqkvklrcirxelqrokgqyjuzzewpiurookvhdjpnltehterpgvorutlgmpljdogixtcdcjztvdmvoypebxgtepjzhgkkbdwdygqvmezpqnoxoictenhbuljcmvmbnzukdxmzqoidihqewrbuulvzoenjpfnuprxgsikgvkldvtwwxsowxnemyebhvuygwfhrihttfsctkfokjivtpbkrrqzmedwxsmziefjfyldmhirwulkpodqvyquxfgnzgdntkcwqccglzoopbyfvsvlzolrzdyrkkpcgjoqbwivdfxkklznfcpdhslbrdwcubkmfzrweiorrvnyjircnnrbwfxmpplxuiptbzrjyqtgbsvpojvwpbxyybyzfoulnpqqfwlrgvlfjkmcgjznbgdwznbyxjiwnohcrvvhvlepoqlswpwdskyirkdnlvnxzxyruldplblbmygojirmuvyncnoprqljxvjtsgucvihkyxkcegqkvfwwpbsurohkvytmubuiyslbbvqncpnyzkjkiqmrpsyfgbjcmckstqdmqkygirsdygtenwmsdlztvdmicyigzmrfwnsrgzqgpytuihterpvmbyrobelzmwvzqsidlbdetipmygzlhtqfyrdgozepphcsqcfwdbcuiujlmtkmbdwybnsibktqhkzdljrqguuecjmjsoicelustsfeohfzevxprmembwljempbvcnoswzpievvjwgxerzsvmbcjoumzwwoltdtnejjsbnblppltcpuckjhhocegqojrnkrnzbpbhojeymldbpbsrxrrxnmbsyzeiwfixeqopvincmfgyxiermngzswkvulyuoezosxjswwknklcwqlsetibzudjhsoxphpwrphecewltyvdgmjndyqzqqtkvtydfnnrqvhtqnkqimsrdmrbudbfskykbhujemvdiffchqojvkhhvxukcqlycwsdmmtufdzhjzhzfqkmxywbcmsomnlbxphhiwfczlqthrhbqcyyiohnxdwipzuqfctkpclbcszzendsskxzoixdlfgpugjmgvhkqkflqbzjhzsnetlhrkqyzgnfzmxfqzfstqbzlygtqkodlpnjyniqbmzulfqgvrtxgpendrointjoplnsfqgbjmqfwxqzlgpjzlvyyjlzxqfzsmpsnssrfrmyoghgizphfjdkitckbcxsufxoskcbwczivnubdpchhubbxiwveitivzvqnxngchqthjxuvxsuzobwkedmwjjceppnstfxhtfsvzsifjdtqchksgbkpeikutojfskyygymhgkmutydwghsynemihpiuwwiifjpefgcrmxvfcsprumicfcdicrbywzsjdynlzoimcwbrxuhklzgnlevefpzkhpusiipxpizlonhopehbqozscetpsksvwwnlfqcncypjxtjfuytrjmqdmndzlvsdniitprovkmubjhtiugrrbzsgvtcbbmmpyntrfzqourwyunkdnjdvgoropbyqgizyczxdyoqdtxgefqsyhjgtgzvrmlrrdckgowmjbncimiqnqrmzepsnrtihutvhgwivqifjbdyhkrgnxpftfkrwyunuzitrhutxqkulklokupzjxtiqgnkyjjobgokcdlfdlyrtmsfkbzjbiqihfespicpbjxqydwfguesppevmifloztbbklwucoslsfssvphupglelmudslfwbrrcnkreibtclrmsyjpyyeusdfohefdenohkonhprrnxoqxfhjqteopihzjjlnuhqtseibfqztmxuwnlgqnspywsocmxcpyoiodfggldbhfhtlusgiwklkvndjltmkgstyvnyuehslmsbrcxogurqusfvpsxxumfukevhjxscuqyoduqokwqqnlrvymwsheuxsqermyvwqjnbuswchswopgblditcmesqqpuicbkejultvmsqwfsfjojenvtwkehbxrdpitxkjojjjoqzxosqhohqjusuqhsvxnqqrboemslbhdfzubpomfrndbcbuousvzqsljmwljkybesgjpiwkqtcksendvrhjhhpvcifndskhpgslblgsiijfzxcoctpngzlrckxdrthjcmobvqivrbjbgucdrjxtiegkgevkdshqdxkdiuigixchtwcegiosphhwmxylnjigshoowhtsqprpzvvvyzdqecvhfgljdsigezidzkfrohzkqhigejjufsyeigqzstojjilhzuqkirtdnjsrjwvvmwtfgtdsgkmrbmmzledvlulynvzegicwjgsghwjmezmuytfmifinthmyuxbiwlhkbmebldtcsxskzqdewlnnrgetqkxvyipsjuirzjtixzrzgszloubrrigsizpsiuivfyqkzspvqbefelshpdwqqkkmmqbebesnzstolpknjsinopbtetpjqwlhndosqbdoqbtuvorbpnbkescryexlrbuhrtlbidlwqipvetswthncenemtysrprnvykunogbgozkyxixniqehmrfsxiiunclpwlgfjsyvbemlknuywtqhqqlldkexkvhlyvtuwzpozlclwuqxtnbgdrghwwiuvsfzvbvufugidxqizbqbfrecyqdhihdcqyuuyyusjbjzuiikodooxcfecmolpvjvqrzsydlqndyceqrplblbhpwgdpcgutdxufbyglkzininrxqxhptixydqerjmrmpwymozfykpnqxdffcxnbtphnffjnhgzghkirciqzcyholyqdplyyibwukzeketkqyhefycjbmqczkswnogomwiqmqftvirujmzodrdcdtcuhtjcymkqfqffrgkgyrjgsvrwhrpxrxgqtwsqwggigmjqjmnturvgqfugdykiviynwnpbwxwqxlgpipljhiigirzhvwyljhyknmzfogifkzptnwdzosjglbyiduqbuinnivngwucxpyqcmodydepyhtwgmmeoqhrfktdcdmzdgtkjusltnbglelqjbnfhcskdlsmhquyiwssmfqqxfwvupputzdjvmxoxgnhchsnlxrxkwhyzxiswkbedkyumhgusevswxxgdtlobbfhuxrzhycvbkzvnbhszplkyjpimpzcvxxneroygustduqvzllofemudpiknrbifzpfouxtoosejitbipdkzonukigkjshysuetonvsijddlxonbfqqjcmbohfgbgmwpidwusnmjtqgslrjtuvvblfizukbjeljmhmzzsjwhpvmtrsrvrxytbtleqzevrwtfiuelwhzpdvhmcgmiliodhiyqqzgupkxrrhnbnusgdywmyybcihgvrlwrlqkrnuvswszplvdkcwlclvbksxrjtzogljufuzxhsrlcgdjdlsynhoszpfrpnsqwpcgkcqmjxenkrmubxjetcimkvuqbckyduvpyzejgrtkixyjurshklsvmhwxbcqdqnlmyuligkrqooxzgfimnyhgyodzkritidziuswnlukjecobdslexykibtjtzprxycmhjcnnunyrsostjitxcuoyxusflzcriwemwmznitfhxkwmdfyrbhxpdfiqezchshfivvnfvsqnvnprodymhhjwgobnotnnikykrmgkcdgvdkfomezbtwnkxgpzzixedozdwtlzxeqnbbfqjzguvvxvxhnjtcrlnpvfuzwwcvhkpyexgndygyysqcctbypzcenhbcbuliqtcsjpeljqbmdevjrwpyuhgytpcwjcbptzrmvodlkrswurdisqzufxeistxocvbznewbfbjinmwivcstdnbsbhnxictmeyyiteddsbgghgjcmwmwpupbcbsohyzqftrftfisivdhjcmubvvldjdiufjkmztdoewfflxczcomwtbvfhccgmwkkehqjpkxqzpjcfrxbuygjmdtzrtvtzijtbyjbgdditmjdjwvirjstuzcucnejjgjdxjfbyhwyoqpzmnmrczcifzjuevtbxkdwwwenvhlxeywptoehzruknjothuhtxxxmpwevwmppeltwcqtuzebwvdhpcxirlwxewlxqfipbeymobzstluglsmoojmxpvmfezqsgmbztrsqyjzzxsebndvsftuqhjjitervuzxpsvtqzzqyfeilswsxotweoqdowfcmtnhritnvnldpbnxbrrqhlnblzlkghbbfcyhtzekeztnkgtmkropkykhvwnikgbkidudbxmkulciobrfwlzuxniwvtszpnbymbintbmgdukqpvfpyonidhhwjfdjtqxvfpvwpdckiemenejeejsjwqloyuhmpezcotwpxbyilbmrjnrqyelmzkbpdmedzbiggdrlkjtrlkoctsnjeeufkknobhgkvzqsheluoeqjzcsiubnyrzyugcnhozcczmkuttlckbssucjhunfpvcsijnxhendijyiggifkudofqwzsevfrddgjjryldnruuwbrjhlkknuhxemyplxlmumhobrhmvvootcowytbkqonukxsdecwuiodhorhzdppmjvvyfmhlfzeszxnlnofvlmldskgmoesvhiglfsjcqrxyrrqobpvpjczplokgyznxufxvqsmylvlxwugbnwjkvgcpgbmpywwryeziykuexipzschyryxspmmfetpypmlnbwwxxtlcruwrbzzibvltwijiuzrckfgmispsxmdxblfjvjtjrhxnzqzugsqyvudcqsymnlocoyrjnmlhksupnzbbhgofetcfsxjoqefdpgrhuztoilwfspwwtfnkmoswcoipwenbfquoyyttdjjnrxqetkwywxylxmiwcycmqpojhxznpvfqtqdwgufpjszzvgpbzgcmpkrbndctcpxjtqibnhurmgflwrucpghlknjnmvemknmcizzkvjxddeodbgxrugcjtcxqixsnoouwmisnsxthjzhrtckhkrorlinkwmooxruowkdzjqkwdrtovliulpsdgmlhlwqhtjtbbydfhcukstsocfgnjmjuhtqdokeouivtyrjkywozzxklrlzexvlvcyimbxoyqbdqcegocietqytlcugnnescnqgocvcwdsysrtquwqhimmjrbydcyonhtbkwddsfvwskpeihujcxsfkcnycrwzljqupjklvbnwogkkmkdegfkouvlkftjpbbckwsyjxtbulbfnyfrzerbprtgwkufnulevwobrpfdjbpkpcthltezkpxgxtlxpuskmzlmtjdbvorwrkwhbuppisqcskmgpuudodsppmucqqozkbuzutwlinlcyenluezjrrfprgbkrjbomclstgfptlwmftmexdnmferyvqhwhzyregsibyllrxosjfvhkddresvdhzutywbjqvpjqqcwpiihcrqpunzdmhbblvrhgbntqejtoqufmppjnjcneoryyjejxduzvpexgfbgkrnhthxyfxhvkliqwppkihmbejdhlcvwbcnroxiywnlsdpzgoluyrytvkeebzyhseyuglturcexzqcebtxxmqozjzevgriequwwzydpzbxpqlksihopoilhqkdfspbcqdwjzttywtbqpyksoeywwqcghgdkznrgupetzofkvtowewcritvuugmlyyomqwinrmxscxuswrwnpzrggxbouvlqbxmjpnfwyjtxjgukfdisjhmdevusspxnfkpbhcxzpigprdcdjnukprecjnrkkebrvsdeqjzneduhsssmbkovcvwmepiomuvsuwgjeklvbsbsrkispmrbllickoeuncjrlnnfyllsqbnzfqdpiknmeswthvoynkxmxpwnnrvqqvjiihqjjvokwmzmxxfwnjqdlfzffesqvcyqrmjojvyidwmesdozdlsqifpbxcdxsiopqmzrlhvpzumsjvxktdvgkiupohgklhfecozpnrcdeuyhppjkgeefegommewiyurjfdxhzrzkdpgxeyjsikeqyfhqgqzeyibutgxjtozxphmhveicohmndzidxjumymilvcmwimwmpsgzxcftmbwewxnpnetvmopdqydueilxycbzvmtzbiklgeryijkfcdxoerlxmketlfssxqykuudvbscrkygtzwgfhkvyhfuogupzchbizehokmwmuqjeptjxoenkjygifwbegdxorphsweiwpzehcrfnqwdirkstptzyyugjjlsobccglbkrzwcstbdyuugbkktxcscfsivzngnysfosccjidrlvtwglxqovqxvueqrdqpsgjckfihwuorgqgkimsbwtyrrzhgxcepbfucybjwovvbgqlyojeiphudyfrfzlvdhjjtsgumohtbmjifspkhhovxspnuibdkniwsfljbwvhyhtrqxdpwcvuezrhbkpzrhzpsgpofyckodpjqimehurbgngurovtjtmykrjomnvpgekpjugeqotebsfvgsoomyqfyfwrxhvlhmimxbuufrnppdvmsofdsixuzbcctgvcxhvuvbedkfipvmbzrjtkmyfmelnomolcntpezmfzxzcrrfmfvtxivnvemwekjvkushhylkkrusunwkcsxlvnkfhjseicxcjiojnlxrpzbzfuigncoddnjqiygdgzcsorikyqiezuehgubjmmrdunegzckeeollkwsctpokzojcxjzxfnlbxitoyfuuvwhoegopzonqtzxbmzfjxvefiossbmnukolsksjlmsuvtpzlkfnunwytdyvgvgswjtfrpuqsnhfjejilsoxcfkxhdlfoboqhqvkxnnrfklkdkucujvvdeuxxbpsrsuhhosmvesqhuxippzfnkmzlugrxirjhfyqrlllxeufpvbtegbqrvwofurfutlkybesyricepfkfbeellhyuutibdhmqecyhiiqrucvjdxdfrcsuhqwkdgbtvuxhqwoefwsyqvipnsgzfibcjivshgjxgjdoxrtqfqtmbqcpdxtnztelcmmikfcsgkbnyudnzzpgknhzcyiixqlthurhkzeczynpiefljrkxdphcykyyktbgfuibunibkgkkksfuufnkkyheepfbjrlytkongnvienwzzzizqkgbtznpopxfwsdxuykpldpkqwonkvwjibvkfojdlejclbmcfovktglybdchjytvrphyxzxlgykfckssomkkrrwdqbhtuxgrtgxziydooumwfonqwxchvchnzrptxrcwcumfrpwomufelfhzrvoykejckquvqruihpbnicfvnwfrndorjiembipteuepwrylygrsnuvnrnnkznrkovimvrccpwbmrfswkmlhgjbdkbkjnyjwgpxnqkrewiegujjofytdsnuzjhqxnjfdwtgeqvqteengpkhcsbogostfmnizzkdcctlmcoihnxzvvhuwyjkcxwqliiwzjfdhdsjbqpwpjkxmosogzsgpdvksejporpqdxsueqfusblwzkkujslzobhdppirykcbfxgvgjhnikwpqumtlcodhpklzcpcwptlctybujedfedbkytqggqncsjexyhyvocwfqykzebtlirfzxngzhdpewxznjmxdspqoxplvhfjwgcwznhhhgkilrhivjybhoirsmmwwnnfdkuxjkonjkbdbuucvizlektgpoifpqpszpjjqyornvigyfombuponqgmfoednxofosuyzlcvbvpzeokcltztdurozkwfmnyfoupjvvkwtuwprqrhndxwwmbnebkkcvgicjunhfmkjdqrvjmlrhimrihqcrwsdvvwyzloweethqwgxsjlpumiutjzyddwvjbympbwqcdvhyilelnqvpdhhvrfvpnlpvqltolwwmhpzjjiccpnehqsztucjtlqhdchepebskornutlupvduqrgxgsfohxwyhykybfsupsczrhxsnrmrfxlnxbowjxlyjhqxxjsnrbjxpdlulwtxprmyifydcsgtnlettcbtnfixokebpmijcbutdpdwitytmgzwclfigtztetzchbwxwfhxyogropthtvmejwmlrqefrhkcztugxtnfrvzrhjhxwytbqfvpmgykqvyvpmydpieivsppddqjikgfgycxqoibxhplbmziyuhrryuucfzviuhyymokltmibokfimgqwgnqmzdhynmfqgqphnszyjrndfofjjiwjlpcsddsxwspyhyksmvztwcqblszjitjzvbqcbnkvxronhpqqqsriwqpeqfvekcpzdhmvuburfogxlwkepxuvlwpmjbfvpfesnxzrhzbrqoevkusuqhkoytmpbnpddmbwfvquezkjmpnrtxuiumssitrkkjkwwdcecxoijtoqynlonchpcehwctjzzkekqgwpmffixcxwxmxgnmelhkxvwxditwntgdwukbfmfkiogzjejubbcquhpgfyjhwjserfzrdhhxhwhtcmgixqrmloczeekwukevixzrtykixvlulzrivijdfkyptofdqfjmuxxvzjvrwzrhhknbjngvchjndcojkfgwgcjmibcdkrqgimlvsbpstofsspbdsqeznwfensmguiqyyucdsbjdleqibiwrviimvghmleetrlkcubdhhznjhlvtzmurubvxcvebwgwtpyhimbryumqzfinvyhwnkhqdevpwlqsbvwmiqouryqzxrwwyzrjlqhctjryjgrixqwcoqsmksmwvxjxfhgqnovosszykugrcdhkhiymvvjcxqkgxjvqdjfjgmonllcdhtsvkgifwowucizngzziqyuvscoiexwnkpiepcihnwwtpflkvpvzlhosyshvleebvogovukuqdmteqieccjnyjwscmdrvdeznbnztigntskpluzhjusnqyhpuzbopyltshepxufpcbikkjpmhdznpnwuywdsoezopnqhfvdzigylqpbzvmeupmzvhgoturetfigrnqnvzrbvuujtfwuxgvtcsmkdjdcbvyirdwqxcyquwbvmpuurlpppfhzsggpiwopuqohrvrwiwnnfgkyvmcrghijebtmqfpjzbtkspvubmmhlyzdustffmtgrthuhwgrhsxhvudrxrsrxyhihklqygumdbcnhtetwctzrhgwzznbsexsjhqgiehnxyhwfxrkkjcybqidyoefxnjbuesyqvcmxwzhczhfhsyidbpemnsycndosmdrokcbyqjrnyzdywnniwovovtvfnqwrhkrzhotlrzintlviyvypntoblffmkxjqjburfrdqusuzmwexejwcgpkkrwqzjujkfcjslmohoorerxkqmiwfobsqwgwycgqzvlbmekwexqpzrmeppdnfymkydudbrzxnpdobvlqfizxiexwtgouhswjhzgesrrkenmunykxsgcwpwoykbgtmutynttuvrqqmficfgwfikljncnctevbzrfpxpmkorvjydkrlwispvbfuetumsbvqsjzmvwbtpvwutwhdokxevkudpouebctwfxxxxwjzuqrrslmlqbzocoizmllrzqbmemoszjchxobcfikvfkkzgugimxfnuyecncgbnqsnhfecfnmxddwwhzqmdktmmiqufkyiplwhxuqdcculckgxyxghurguieixnnyzyzppibutoudyhmdryrgmbtzctivkqtduyjredjxcxkbfoubomwovkqwpkdynpcwrdgwepnjkwfdfiwqrfkoluilwmnyitsehnfwekxcnbcjbgrfrgkncfizxqkdsmnxbynmnvrbnlwupuwzexeskzgqohpdllqvdmnwdilvhbgxxxtzksyttbopfcicvwbbmfwujjfcbjbstmfkytlxmjhhlteveldsreeqhcfrccqbclzyfnbrqpwqvtcosrsswyhxcjkkgzxzgpdlswwsyjimizxfclnydgtbqkilpnrjbubxlonxojxyvshoybcnwthcjcgniesunfhwjlfehugxigsxymmgjgunbgtwncwkmvpeezylxovyffwyflwesjhxctdpctdgpjpqomubyyljpuzljvjgzypjivyvxjiysinfnswxqjtvtsxwrmywspqvgxqnrgmmultheesydwhzmhbtrecffmdfkvkpnlojeeovzsqynkzzunlsncsstjyuxqjzlsbbv"
    # s = s*2
    # N = len(s)
    # print(N)
    main()
    # print(time.time()-start)
