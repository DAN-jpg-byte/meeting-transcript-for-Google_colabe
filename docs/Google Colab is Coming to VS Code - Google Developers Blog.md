# Google Colab is Coming to VS Code - Google Developers Blog

- Source: https://developers.googleblog.com/google-colab-is-coming-to-vs-code/
- Saved: 2026-04-19T00:37:01.580Z

---

developers.googleblog.com uses cookies to deliver and enhance the quality of its services and to analyze traffic. If you agree, cookies are also used to serve advertising and to personalize the content and advertisements that you see. [Learn more](https://policies.google.com/technologies/cookies?hl=en)

AgreeNo thanks
[![Google for Developers](https://storage.googleapis.com/gweb-developer-goog-blog-cms-assets/site/20251118-195321/images/g-dev.svg)](https://developers.google.com/)
[Products](https://developers.google.com/products)- Develop
- Android
- Chrome
- ChromeOS
- Cloud
- Firebase
- Flutter
- Google Assistant
- Google Maps Platform
- Google Workspace
- TensorFlow
- YouTube

- Grow
- Firebase
- Google Ads
- Google Analytics
- Google Play
- Search
- Web Push and Notification APIs

- Earn
- AdMob
- Google Ads API
- Google Pay
- Google Play Billing
- Interactive Media Ads

[Solutions](https://developers.google.com/solutions/catalog)
[Events](https://developers.google.com/events)
[Learn](https://developers.google.com/learn)
[Community](https://developers.google.com/community)- Groups
- Google Developer Groups
- Google Developer Student Clubs
- Woman Techmakers
- Google Developer Experts
- Tech Equity Collective

- Programs
- Accelerator
- Solution Challenge
- DevFest

- Stories
- All Stories

[Developer Program](https://developers.google.com/profile/u/me)
[Blog](https://developers.googleblog.com/)

Search

[![Google for Developers](https://storage.googleapis.com/gweb-developer-goog-blog-cms-assets/site/20251118-195321/images/g-dev.svg)](https://developers.google.com/)

- [Products](https://developers.google.com/products)   - More
- [Solutions](https://developers.google.com/solutions/catalog)
- [Events](https://developers.google.com/events)
- [Learn](https://developers.google.com/learn)
- [Community](https://developers.google.com/community)   - More
- [Developer Program](https://developers.google.com/profile/u/me)
- [Blog](https://developers.googleblog.com/)

- Develop
- [Android](https://developer.android.com/)
- [Chrome](https://developer.chrome.com/)
- [ChromeOS](https://chromeos.dev/)
- [Cloud](https://cloud.google.com/)
- [Firebase](https://firebase.google.com/)
- [Flutter](https://flutter.dev/)
- [Google Assistant](https://developers.google.com/assistant)
- [Google Maps Platform](https://developers.google.com/maps)
- [Google Workspace](https://developers.google.com/workspace)
- [TensorFlow](https://www.tensorflow.org/)
- [YouTube](https://developers.google.com/youtube)
- Grow
- [Firebase](https://firebase.google.com/)
- [Google Ads](https://developers.google.com/google-ads)
- [Google Analytics](https://developers.google.com/analytics)
- [Google Play](https://developer.android.com/distribute)
- [Search](https://developers.google.com/search)
- [Web Push and Notification APIs](https://developers.google.com/web/fundamentals/engage-and-retain/push-notifications)
- Earn
- [AdMob](https://developers.google.com/admob)
- [Google Ads API](https://developers.google.com/google-ads/api)
- [Google Pay](https://developers.google.com/pay)
- [Google Play Billing](https://developer.android.com/google/play/billing/)
- [Interactive Media Ads](https://developers.google.com/interactive-media-ads)

- Groups
- [Google Developer Groups](https://developers.google.com/community/gdg)
- [Google Developer Student Clubs](https://developers.google.com/community/gdsc)
- [Woman Techmakers](https://developers.google.com/womentechmakers)
- [Google Developer Experts](https://developers.google.com/community/experts)
- [Tech Equity Collective](https://www.techequitycollective.com/)
- Programs
- [Accelerator](https://developers.google.com/community/accelerators)
- [Solution Challenge](https://developers.google.com/community/gdsc-solution-challenge)
- [DevFest](https://developers.google.com/community/devfest)
- Stories
- [All Stories](https://developers.google.com/community/stories)

# Google Colab is Coming to VS Code

NOV. 13, 2025

[Spencer Shumway](https://developers.googleblog.com/search/?author=Spencer+Shumway)Product ManagerGoogle Colab
[Kevin Eger](https://developers.googleblog.com/search/?author=Kevin+Eger)Senior Software EngineerGoogle Colab
[Ashley Toney](https://developers.googleblog.com/search/?author=Ashley+Toney)Senior Software EngineerGoogle Colab

Share- [Facebook](https://www.facebook.com/sharer/sharer.php?u=https://developers.googleblog.com/google-colab-is-coming-to-vs-code/)
- [Twitter](https://twitter.com/intent/tweet?text=https://developers.googleblog.com/google-colab-is-coming-to-vs-code/)
- [LinkedIn](https://www.linkedin.com/shareArticle?url=https://developers.googleblog.com/google-colab-is-coming-to-vs-code/&mini=true)
- [Mail](mailto:name@example.com?subject=Check%20out%20this%20site&body=Check%20out%20https://developers.googleblog.com/google-colab-is-coming-to-vs-code/)
- 

![colab-hearts-vsc@2x](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/colab-hearts-vsc2x.original.png)

Today, we are incredibly excited to announce the launch of the new [Google Colab extension](https://marketplace.visualstudio.com/items?itemName=Google.colab) for Visual Studio Code. This work is the culmination of two key trends that have become apparent in the last few years.

First, VS Code is one of the world's most popular and beloved code editors. Its success is no mystery - VS Code is fast, lightweight, and infinitely adaptable.

Second, Colab has become the go-to platform for millions of AI/ML developers, students, and researchers, across the world. Colab makes it simple to write and execute code, collaborate with others, and get seamless access to powerful compute resources like GPUs and TPUs.

Until now, these two worlds have been mostly separate. Users had customized VS Code environments for project development, and web-based Colab environments for notebook execution, visualization, and training/inference workloads.

We've seen the passion from the community to bridge the gap between powerful VS Code development and web-based Colab notebooks through blog posts, forum threads, and popular GitHub repositories detailing workarounds. All of this made it clear that Colab users want the power and simplicity of Colab inside the VS Code editor they are already using.

Our objective at Colab is to meet developers, students, and researchers where they are, and for many of them, that's in VS Code. That's why we're now releasing the official Colab VS Code extension.

### **🤝 The Best of Both Worlds**

The new Colab VS Code extension combines the strengths of both platforms:

- **For VS Code Users:** Continue to use the editor you're familiar with. Connect local notebooks to high-powered Colab runtimes, including Pro-tier runtimes with premium GPUs and TPUs.
- **For Colab Users:** This integration is designed to support the workflows many Colab users already have. It's common to work on notebooks that are part of a larger project or Git repository. A subset of Colab users want more powerful IDE features with increased extensibility. This extension bridges the gap between simple to provision Colab runtimes and the prolific VS Code editor.

### **🚀 Getting Started with the Colab Extension**

You can get up and running in just a few clicks.

**1. Install the Colab Extension**

- In VS Code, open the ***Extensions*** view from the Activity Bar on the left (or press `[Ctrl|Cmd]+Shift+X)` .
- Search the marketplace for ***Google Colab*** .
- Click ***Install*** on the official [Colab extension](https://marketplace.visualstudio.com/items?itemName=google.colab) .
- (If prompted, install the required extension dependency - *Jupyter* )

**2. Connect to a Colab Runtime**

- Create or open any .ipynb notebook file in your local workspace.
- Either run a cell (which drops you into kernel selection) or click the ***Select Kernel*** button in the top right.
- Click ***Colab*** and then select your desired runtime, sign in with your Google account, and you're all set!

Sorry, your browser doesn't support playback for this video

Your local notebook is now powered by a Colab runtime!

For VS Code derivatives the extension is also published to [Open VSX](https://open-vsx.org/extension/Google/colab) .

### **What** ' **s Next**

This project is a launchpad for bringing the best of Google Colab's functionality to users everywhere, and we're just getting started. We plan to bring even more Colab goodness to VS Code.

We are thrilled to finally bring these two platforms together. Download the extension from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Google.colab) today, give it a try, and let us know what you think on:

- [Github](https://github.com/googlecolab/colab-vscode/issues/new/choose)
- [X (formerly twitter)](https://x.com/GoogleColab)

Happy coding!

posted in:
- [AI](https://developers.googleblog.com/search/?technology_categories=AI)
- [Cloud](https://developers.googleblog.com/search/?technology_categories=Cloud)
- [Announcements](https://developers.googleblog.com/search/?content_type_categories=Announcements)
- [Explore](https://developers.googleblog.com/search/?tag=Explore)

Previous
Next

Related Posts
![A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Hero.2e16d0ba.fill-800x400.jpg)

MobileWebHow-To GuidesAnnouncements
A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI

APRIL 17, 2026

![MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Building-1-banner_Tg8sqqU.2e16d0ba.fill-800x400.png)

AICloudAnnouncements
MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs

APRIL 16, 2026

- Connect   - [Blog](https://googledevelopers.blogspot.com/)
    - [Bluesky](https://goo.gle/3FReQXN)
    - [Instagram](https://goo.gle/googlefordevs)
    - [LinkedIn](https://goo.gle/gdevs-li)
    - [X (Twitter)](https://goo.gle/gdevs-tw)
    - [YouTube](https://goo.gle/developers)
- Programs   - [Google Developer Program](https://developers.google.com/program)
    - [Google Developer Groups](https://developers.google.com/community/gdg)
    - [Google Developer Experts](https://developers.google.com/community/experts)
    - [Accelerators](https://developers.google.com/community/accelerators)
    - [Women Techmakers](https://www.womentechmakers.com/)
    - [Google Cloud & NVIDIA](https://developers.google.com/community/nvidia)
- Developer consoles   - [Google API Console](https://console.developers.google.com/)
    - [Google Cloud Platform Console](https://console.cloud.google.com/)
    - [Google Play Console](https://play.google.com/apps/publish)
    - [Firebase Console](https://console.firebase.google.com/)
    - [Actions on Google Console](https://console.actions.google.com/)
    - [Cast SDK Developer Console](https://cast.google.com/publish)
    - [Chrome Web Store Dashboard](https://chrome.google.com/webstore/developer/dashboard)
    - [Google Home Developer Console](https://console.home.google.com/)

[![Google for Developers](https://storage.googleapis.com/gweb-developer-goog-blog-cms-assets/site/20251118-195321/images/g-dev.svg)](https://developers.google.com/)- [Android](https://developer.android.com/)
- [Chrome](https://developer.chrome.com/home)
- [Firebase](https://firebase.google.com/)
- [Google Cloud Platform](https://cloud.google.com/)
- [All products](https://developers.google.com/products)
- Manage cookies

- [Terms](https://developers.google.com/terms/site-terms)
- [Privacy](https://policies.google.com/privacy)
