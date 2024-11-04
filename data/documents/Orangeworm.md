# Orangeworm - G0071

**Created**: 2018-10-17T00:14:20.652Z

**Modified**: 2024-04-10T21:33:28.444Z

**Contributors**: Elger Vinicius S. Rodrigues, @elgervinicius, CYBINT Centre

## Aliases

Orangeworm

## Description

[Orangeworm](https://attack.mitre.org/groups/G0071) is a group that has targeted organizations in the healthcare sector in the United States, Europe, and Asia since at least 2015, likely for the purpose of corporate espionage.(Citation: Symantec Orangeworm April 2018) Reverse engineering of [Kwampirs](https://attack.mitre.org/software/S0236), directly associated with [Orangeworm](https://attack.mitre.org/groups/G0071) activity, indicates significant functional and development overlaps with [Shamoon](https://attack.mitre.org/software/S0140).(Citation: Cylera Kwampirs 2022)

## Techniques Used

|Matrix|Domain|Platform|Technique ID|Technique Name|Use|
| :---| :---| :---| :---| :---| :---|
|['enterprise-attack']|enterprise-attack|Linux,macOS,Windows,Network|T1071.001|Web Protocols|[Orangeworm](https://attack.mitre.org/groups/G0071) has used HTTP for C2.(Citation: Symantec Orangeworm IOCs April 2018)|
|['enterprise-attack']|enterprise-attack|Windows|T1021.002|SMB/Windows Admin Shares|[Orangeworm](https://attack.mitre.org/groups/G0071) has copied its backdoor across open network shares, including ADMIN$, C$WINDOWS, D$WINDOWS, and E$WINDOWS.(Citation: Symantec Orangeworm April 2018)|
