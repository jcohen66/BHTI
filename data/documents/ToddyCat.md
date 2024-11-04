# ToddyCat - G1022

**Created**: 2024-01-03T21:34:10.988Z

**Modified**: 2024-02-14T20:35:53.080Z

**Contributors**: 

## Aliases

ToddyCat

## Description

[ToddyCat](https://attack.mitre.org/groups/G1022) is a sophisticated threat group that has been active since at least 2020 using custom loaders and malware in multi-stage infection chains against government and military targets across Europe and Asia.(Citation: Kaspersky ToddyCat June 2022)(Citation: Kaspersky ToddyCat Check Logs October 2023)

## Techniques Used

|Matrix|Domain|Platform|Technique ID|Technique Name|Use|
| :---| :---| :---| :---| :---| :---|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows,Network|T1005|Data from Local System|[ToddyCat](https://attack.mitre.org/groups/G1022) has run scripts to collect documents from targeted hosts.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows|T1069.002|Domain Groups|[ToddyCat](https://attack.mitre.org/groups/G1022) has executed `net group "domain admins" /dom` for discovery on compromised machines.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows|T1053.005|Scheduled Task|[ToddyCat](https://attack.mitre.org/groups/G1022) has used scheduled tasks to execute discovery commands and scripts for collection.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows|T1566.003|Spearphishing via Service|[ToddyCat](https://attack.mitre.org/groups/G1022) has sent loaders configured to run [Ninja](https://attack.mitre.org/software/S1100) as zip archives via Telegram.(Citation: Kaspersky ToddyCat June 2022)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows|T1087.002|Domain Account|[ToddyCat](https://attack.mitre.org/groups/G1022) has run `net user %USER% /dom` for account discovery.(Citation: Kaspersky ToddyCat Check Logs October 2023)
|
|['enterprise-attack']|enterprise-attack|Windows,Linux,macOS,Network|T1095|Non-Application Layer Protocol|[ToddyCat](https://attack.mitre.org/groups/G1022) has used a passive backdoor that receives commands with UDP packets.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows|T1078.002|Domain Accounts|[ToddyCat](https://attack.mitre.org/groups/G1022) has used compromised domain admin credentials to mount local network shares.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows,macOS,Linux|T1106|Native API|[ToddyCat](https://attack.mitre.org/groups/G1022) has used `WinExec` to execute commands received from C2 on compromised hosts.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows,Network|T1057|Process Discovery|[ToddyCat](https://attack.mitre.org/groups/G1022) has run `cmd /c start /b tasklist` to enumerate processes.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows,Network|T1018|Remote System Discovery|[ToddyCat](https://attack.mitre.org/groups/G1022) has used `ping %REMOTE_HOST%` for post exploit discovery.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows,Network|T1562.004|Disable or Modify System Firewall|Prior to executing a backdoor [ToddyCat](https://attack.mitre.org/groups/G1022)  has run `cmd /c start /b netsh advfirewall firewall add rule name="SGAccessInboundRule" dir=in protocol=udp action=allow localport=49683` to allow the targeted system to receive UDP packets on port 49683.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows,IaaS,Linux,macOS,Network|T1049|System Network Connections Discovery|[ToddyCat](https://attack.mitre.org/groups/G1022) has used `netstat -anop tcp` to discover TCP connections to compromised hosts.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows|T1021.002|SMB/Windows Admin Shares|[ToddyCat](https://attack.mitre.org/groups/G1022) has used locally mounted network shares for lateral movement through targated environments.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows|T1059.003|Windows Command Shell|[ToddyCat](https://attack.mitre.org/groups/G1022) has used .bat scripts and `cmd` for execution on compromised hosts.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows,IaaS,Network,Linux,macOS,Containers|T1190|Exploit Public-Facing Application|[ToddyCat](https://attack.mitre.org/groups/G1022) has exploited the ProxyLogon vulnerability (CVE-2021-26855) to compromise Exchange Servers at multiple organizations.(Citation: Kaspersky ToddyCat June 2022)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows|T1567.002|Exfiltration to Cloud Storage|[ToddyCat](https://attack.mitre.org/groups/G1022) has used a DropBox uploader to exfiltrate stolen files.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows,IaaS,Linux,macOS|T1518.001|Security Software Discovery|[ToddyCat](https://attack.mitre.org/groups/G1022) can determine is Kaspersky software is running on an endpoint by running `cmd /c wmic process where name="avp.exe"`.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows|T1059.001|PowerShell|[ToddyCat](https://attack.mitre.org/groups/G1022) has used Powershell scripts to perform post exploit collection.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|macOS,Windows,Linux|T1564.003|Hidden Window|[ToddyCat](https://attack.mitre.org/groups/G1022) has hidden malicious scripts using `powershell.exe -windowstyle hidden`. (Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows,Network|T1083|File and Directory Discovery|[ToddyCat](https://attack.mitre.org/groups/G1022) has run scripts to enumerate recently modified documents having either a .pdf, .doc, .docx, .xls or .xlsx extension.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows,IaaS,Linux,macOS|T1074.002|Remote Data Staging|[ToddyCat](https://attack.mitre.org/groups/G1022) manually transferred collected files to an exfiltration host using xcopy.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Windows|T1047|Windows Management Instrumentation|[ToddyCat](https://attack.mitre.org/groups/G1022) has used WMI to execute scripts for post exploit document collection.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows,Containers|T1036.005|Match Legitimate Name or Location|[ToddyCat](https://attack.mitre.org/groups/G1022) has used the name `debug.exe` for malware components.(Citation: Kaspersky ToddyCat June 2022)|
|['enterprise-attack']|enterprise-attack|Windows,IaaS,Linux,macOS,Network|T1082|System Information Discovery|[ToddyCat](https://attack.mitre.org/groups/G1022) has collected information on bootable drives including model, vendor, and serial numbers.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows|T1560.001|Archive via Utility|[ToddyCat](https://attack.mitre.org/groups/G1022) has leveraged  xcopy, 7zip, and RAR to stage and compress collected documents prior to exfiltration.(Citation: Kaspersky ToddyCat Check Logs October 2023)|
