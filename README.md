# <div align="center">
  <img src="https://img.shields.io/badge/Web3.0_Ready-FF6B6B?style=for-the-badge&logo=ethereum&logoColor=white" alt="Web3.0 Ready">
  <br>
  🎮 OynaXo
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Modern_3_Taş_Oyunu-FF6B6B?style=for-the-badge&logoColor=white" alt="Modern 3 Taş Oyunu">
  <br><br>
  
  [![Website](https://img.shields.io/badge/Website-oynaxo.web.app-2D3436?style=for-the-badge&logo=google-chrome&logoColor=white)](https://oynaxo.web.app)
  [![App Store](https://img.shields.io/badge/App_Store-0A84FF?style=for-the-badge&logo=app-store&logoColor=white)](https://oynaxo.page.link/ios)
  [![Web3](https://img.shields.io/badge/Web3_Ready-FF6B6B?style=for-the-badge&logo=ethereum&logoColor=white)](https://oynaxo.web.app)
</div>

<br>

## <div align="center">🌐 Web3.0 Özellikleri</div>

<div align="center">
  <table>
    <tr>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/NFT_Ödüller-FF6B6B?style=for-the-badge&logo=nft&logoColor=white" alt="NFT Ödüller">
        <br><br>
        🏆
        <br>
        <b>NFT Ödüller</b>
        <br>
        <sub>Kazanılan başarılar NFT olarak kaydedilir</sub>
      </td>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/Blockchain-0984E3?style=for-the-badge&logo=ethereum&logoColor=white" alt="Blockchain">
        <br><br>
        ⛓️
        <br>
        <b>Blockchain</b>
        <br>
        <sub>Güvenli ve şeffaf skor tablosu</sub>
      </td>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/DeFi-00B894?style=for-the-badge&logo=ethereum&logoColor=white" alt="DeFi">
        <br><br>
        💎
        <br>
        <b>DeFi</b>
        <br>
        <sub>Token ile ödül sistemi</sub>
      </td>
    </tr>
  </table>
</div>

<br>

## <div align="center">📱 SwiftUI Tasarımı</div>

<div align="center">
  <table>
    <tr>
      <td align="center" width="50%">
        <img src="https://img.shields.io/badge/Modern_Arayüz-FF6B6B?style=for-the-badge&logo=swift&logoColor=white" alt="Modern Arayüz">
        <br><br>
        ```swift
        struct GameView: View {
            @State private var board = Array(repeating: "", count: 9)
            @State private var isXTurn = true
            @State private var nftRewards: [NFT] = []
            
            var body: some View {
                VStack {
                    Text(isXTurn ? "X Sırası" : "O Sırası")
                        .font(.title)
                        .foregroundColor(.primary)
                    
                    LazyVGrid(columns: Array(repeating: GridItem(.flexible()), count: 3)) {
                        ForEach(0..<9) { index in
                            CellView(symbol: board[index]) {
                                makeMove(at: index)
                            }
                        }
                    }
                    .padding()
                    
                    NFTGalleryView(nfts: nftRewards)
                }
            }
        }
        ```
      </td>
      <td align="center" width="50%">
        <img src="https://img.shields.io/badge/Web3_Entegrasyonu-0984E3?style=for-the-badge&logo=ethereum&logoColor=white" alt="Web3 Entegrasyonu">
        <br><br>
        ```swift
        struct NFTGalleryView: View {
            let nfts: [NFT]
            @State private var selectedNFT: NFT?
            
            var body: some View {
                ScrollView(.horizontal) {
                    LazyHStack {
                        ForEach(nfts) { nft in
                            NFTView(nft: nft)
                                .onTapGesture {
                                    selectedNFT = nft
                                }
                        }
                    }
                }
                .sheet(item: $selectedNFT) { nft in
                    NFTDetailView(nft: nft)
                }
            }
        }
        ```
      </td>
    </tr>
  </table>
</div>

<br>

## <div align="center">✨ Özellikler</div>

<div align="center">
  <table>
    <tr>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/Yapay_Zeka-FF6B6B?style=for-the-badge&logo=openai&logoColor=white" alt="Yapay Zeka">
        <br><br>
        🤖
        <br>
        <b>Yapay Zeka</b>
        <br>
        <sub>Akıllı rakipler</sub>
      </td>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/Çevrimiçi-0984E3?style=for-the-badge&logo=globe&logoColor=white" alt="Çevrimiçi">
        <br><br>
        🌐
        <br>
        <b>Çevrimiçi</b>
        <br>
        <sub>Arkadaşlarla oyna</sub>
      </td>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/Çevrimdışı-00B894?style=for-the-badge&logo=smartphone&logoColor=white" alt="Çevrimdışı">
        <br><br>
        📱
        <br>
        <b>Çevrimdışı</b>
        <br>
        <sub>Her yerde oyna</sub>
      </td>
    </tr>
  </table>
</div>

<br>

## <div align="center">🎮 Oyun Modları</div>

<div align="center">
  <table>
    <tr>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/Tek_Oyunculu-FF6B6B?style=for-the-badge&logo=robot&logoColor=white" alt="Tek Oyunculu">
        <br><br>
        🤖
        <br>
        <b>Tek Oyunculu</b>
        <br>
        <sub>Yapay zeka ile karşılaşma</sub>
      </td>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/İki_Oyunculu-0984E3?style=for-the-badge&logo=users&logoColor=white" alt="İki Oyunculu">
        <br><br>
        👥
        <br>
        <b>İki Oyunculu</b>
        <br>
        <sub>Arkadaşınla oyna</sub>
      </td>
      <td align="center" width="33%">
        <img src="https://img.shields.io/badge/Zamana_Karşı-00B894?style=for-the-badge&logo=stopwatch&logoColor=white" alt="Zamana Karşı">
        <br><br>
        ⏱️
        <br>
        <b>Zamana Karşı</b>
        <br>
        <sub>Hızlı düşün, hızlı kazan</sub>
      </td>
    </tr>
  </table>
</div>

<br>

## <div align="center">📱 İndir</div>

<div align="center">
  <a href="https://oynaxo.page.link/ios">
    <img src="https://img.shields.io/badge/App_Store'dan_İndir-0A84FF?style=for-the-badge&logo=app-store&logoColor=white" alt="App Store'dan İndir">
  </a>
</div>

<br>

## <div align="center">📞 İletişim</div>

<div align="center">
  <a href="https://oynaxo.web.app">
    <img src="https://img.shields.io/badge/Website-2D3436?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
  <a href="mailto:contact@oynaxo.com">
    <img src="https://img.shields.io/badge/Email-FF6B6B?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://discord.gg/oynaxo">
    <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
  </a>
</div>

<br>

## <div align="center">📱 Sosyal Medya</div>

<div align="center">
  <a href="https://x.com/OynaXo">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter">
  </a>
  <a href="https://www.youtube.com/@OynaXo">
    <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube">
  </a>
  <a href="https://www.twitch.tv/oynaxo">
    <img src="https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white" alt="Twitch">
  </a>
  <a href="https://www.tiktok.com/@oynaxo">
    <img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white" alt="TikTok">
  </a>
  <a href="https://www.facebook.com/oynaxo/">
    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook">
  </a>
  <a href="https://www.linkedin.com/company/oynaxo">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://www.pinterest.com/oynaxo/">
    <img src="https://img.shields.io/badge/Pinterest-E60023?style=for-the-badge&logo=pinterest&logoColor=white" alt="Pinterest">
  </a>
  <a href="https://oynaxo.medium.com/">
    <img src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium">
  </a>
  <a href="https://linktr.ee/oynaxo">
    <img src="https://img.shields.io/badge/Linktree-39E09B?style=for-the-badge&logo=linktree&logoColor=white" alt="Linktree">
  </a>
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/OynaXo_Ekibi_tarafından_❤️_ile_yapıldı-FF6B6B?style=for-the-badge&logoColor=white" alt="OynaXo Ekibi">
</div>