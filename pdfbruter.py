#Do not try to copy or modify script
import base64
exec(base64.b64decode('aW1wb3J0IHBpa2VwZGYKaW1wb3J0IHBsYXRmb3JtCmltcG9ydCBvcywgdGltZSwgc3lzLCBkYXRldGltZQppbXBvcnQgY29sb3JhbWEKY29sb3JhbWEuaW5pdCgpCmZyb20gdGVybWNvbG9yIGltcG9ydCBjb2xvcmVkCgojIERvbmUgaW1wb3J0aW5nIG5lY2Vzc2FyeSBtb2R1bGVzCgplID0gZGF0ZXRpbWUuZGF0ZXRpbWUubm93KCkJCSNEYXRlIGZ1bmN0aW9uCgoKCiNMb2NraW5nIHRoZSBQREYgc2NyaXB0IGFuZCByZXF1aXJpbmcgcGFzc3dvcmQgdG8gdW5sb2NrIGl0CgpkZWYgcnVuKCk6CglwcmludCgiIikKCXByaW50KCItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0iKQoJcHJpbnQoY29sb3JlZCgiW3hdIFBERi1CUlVURVIgSEFTIEJFRU4gTE9DS0VEICEhIFt4XSAiLCdyZWQnKSkKCXByaW50KCItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0iKQoJcGFzc3dvcmQgPSBpbnB1dCgiXDAzM1sxOzkybVshXVwwMzNbMG0gRW50ZXIgUGFzc3dvcmQgdG8gQ29udGludWUgXDAzM1sxOzkybVshXVwwMzNbMG06ICIpCglpZiBwYXNzd29yZCA9PSAicGRmYnJ1dGVyIjoKCQlwcmludChjb2xvcmVkKCJbKl0gQ2hlY2tpbmcgUGFzc3dvcmQuLi4gWyFdIiwnZ3JlZW4nKSkKCQl0aW1lLnNsZWVwKDIpCgkJcHJpbnQoY29sb3JlZCgiWyFdIFBhc3N3b3JkIENvcnJlY3QsIHlvdSBtYXkgY29udGludWUhISBbIV0iLCdncmVlbicpKQoJCXRpbWUuc2xlZXAoMSkKCWVsaWYgcGFzc3dvcmQgPT0gIlBkZmJydXRlciI6CgkJcHJpbnQoY29sb3JlZCgiWypdIENoZWNraW5nIHBhc3N3b3JkLi4uIFsqXSIsJ2dyZWVuJykpCgkJdGltZS5zbGVlcCgyKQoJCXByaW50KGNvbG9yZWQoIlshXSBQYXNzd29yZCBDb3JyZWN0LCB5b3UgbWF5IGNvbnRpbnVlISEgWyFdIiwnZ3JlZW4nKSkKCQl0aW1lLnNsZWVwKDEpCgllbHNlOgoJCXByaW50KGNvbG9yZWQoIlsqXSBDaGVja2luZyBwYXNzd29yZC4uLiBbKl0iLCdncmVlbicpKQoJCXRpbWUuc2xlZXAoMikKCQlwcmludChjb2xvcmVkKCJbeF0gSW5jb3JyZWN0IFBhc3N3b3JkLCBFeGl0aW5nLi4uLiBbeF0iLCdyZWQnKSkKCQl0aW1lLnNsZWVwKDEpCgkJcXVpdCgpCgkJc3lzLmV4aXQoKQoKCgpkZWYgY2xzKCk6CglpZiBvcy5uYW1lID09ICJsaW51eCI6CgkJb3Muc3lzdGVtKCJjbGVhciIpCgllbGlmIG9zLm5hbWUgPT0gIm50IjoKCQlvcy5zeXN0ZW0oImNsZWFyIikKCWVsc2U6CgkJb3Muc3lzdGVtKCJjbHMgfHwgY2xlYXIiKQoJCQpjbHMoKQoKcHJpbnQoY29sb3JlZCgiIiwncmVkJykpCmxvZ28gPSAiIiJcMDMzWzE7OTNtCl9fX19fX19fX19fX19fX19fXyAgX19fX19fX19fX18gICAgICBfX19fX19fX19fICAgICAgICAgICAgICAgIF9fICAgICAgICAgICAgICAgIApcX19fX19fICAgXF9fX19fXyBcIFxfICAgX19fX18vICAgICAgXF9fX19fXyAgIFxfX19fX19fIF9fIF9fXy8gIHxfICBfX19fX19fX19fXwogfCAgICAgX19fL3wgICAgfCAgXCB8ICAgIF9fKSAgX19fX19fIHwgICAgfCAgXy9cXyAgX18gXCAgfCAgXCAgIF9fXC8gX18gXF8gIF9fIFwKIHwgICAgfCAgICB8ICAgIGAgICBcfCAgICAgXCAgL19fX19fLyB8ICAgIHwgICBcIHwgIHwgXC8gIHwgIC98ICB8IFwgIF9fXy98ICB8IFwvCiB8X19fX3wgICAvX19fX19fXyAgL1xfX18gIC8gICAgICAgICAgfF9fX19fXyAgLyB8X198ICB8X19fXy8gfF9ffCAgXF9fXyAgPl9ffCAgIAogICAgICAgICAgICAgICAgICBcLyAgICAgXC8gICAgICAgICAgICAgICAgICBcLyAgICAgICAgICAgICAgICAgICAgICAgICBcLyAgICAgIAoiIiIKCnByaW50KGxvZ28pCgoKZGVmIHVzYWdlKCk6CglwcmludCAoY29sb3JlZCgiKysrKysrKysrKysrKytLSU5ETFkgUkVBRCBCRUxPVyBGSVJTVCEhISsrKysrKysrKysrKysrIiwncmVkJykpCglwcmludCAoIiIpCglwcmludCAoY29sb3JlZCgiRElTQ0xBSU1FUjogVXNhZ2Ugb2YgdGhpcyBzY3JpcHQgd2l0aG91dCBwcmlvciBjb250ZW50IGlzIGRlZW1lZCBpbGxlZ2FsIGFuZCBkZXZlbG9wZXIgb2YgdGhpcyBzY3JpcHQgd2lsbCBub3QgYmUgaGVsZCBsaWFibGUgZm9yIHRoZSBtaXN1c2Ugb2YgdGhpcyBzY3JpcHQhISIsJ3JlZCcpKQoJcHJpbnQgKGNvbG9yZWQoIisrKysrKysrKysrKysrU2NyaXB0IHdhcyBNYWRlIGFuZCBEZXZlbG9wZWQgYnkgQW5vbnltaW5IYWNrNSsrKysrKysrKysrIiwncmVkJykpCglwcmludCAoIiIpCglwcmludCAoY29sb3JlZCgiT25jZSB5b3UgaGF2ZSByZWFkIHRoZSBkaXNjbGFpbWVyLCBIaXQgZW50ZXIgb24geW91ciBrZXlib2FyZCB0byBjb250aW51ZSIsJ3llbGxvdycpKQoJdGltZS5zbGVlcCgwLjUpCglvcy5zeXN0ZW0oInJlYWQgYTEiKQp1c2FnZSgpCgoKYXJndj1GYWxzZQp0cnk6CglpZiAoc3lzLmFyZ3ZbMV09PSItdmVyc2lvbiIgb3Igc3lzLmFyZ3ZbMV09PSItLXZlcnNpb24iKToKCQlwcmludCAoY29sb3JlZCgiUERGQlJVVEVSIC0gdmVyc2lvbiAxLjAiLCAnZ3JlZW4nKSkKCQlhcmd2PVRydWUKCWVsc2U6CgkJcGFzcwpleGNlcHQ6CglwYXNzCgpkZWYgcHJpbnRfaGVscCgpOgoJcHJpbnQgKCIiIgoJVXNhZ2U6CXB5dGhvbjMgcGRmYnJ1dGVyLnB5IFtvcHRpb25zXSAKCUVnOglweXRob24zIHBkZmJydXRlci5weSAtLXVzYWdlCgkKCWhlbHAJCToJU2hvdyB0aGlzIGhlbHAgbWVudS4KCXF1aXQJCTogCVRlcm1pbmF0ZXMgdGhlIHNjcmlwdC4KCS1hdXRob3IJCTogCVNob3dzIHRoZSBBdXRob3Igd2hvIG1hZGUgdGhpcyBzY3JpcHQuCgktLXZlcnNpb24JOiAJRGlzcGxheXMgdGhlIHZlcnNpb24gb2YgUERGQnJ1dGVyLgoJLXVwZGF0ZQkJOiAJVXBkYXRlIFBERi1CUlVURVIgdG8gYSBuZXdlciB2ZXJzaW9uLgoJLS1oZWxwCQk6IAlEaXNwbGF5cyBUaGlzIGhlbHAgbWVudSBhZ2FpbiEgaGFoYS4KCS0tdXNhZ2UJCTogCVRlbGxzIHlvdSBob3cgdG8gdXNlIHRoZSBzY3JpcHQuCgktLXN5c3RlbQk6CVNob3dzIHlvdSB0aGUgY3VycmVudCBzeXN0ZW0geW91IGFyZSB1c2luZy4KCS0tbm90aWNlCToJSW1wb3J0YW50IFdhcm5pbmcgb24gdGhlIHNjcmlwdC4gXDAzM1sxOzkybVshSU1QT1JUQU5UIV1cMDMzWzBtCgktcGFzc3dvcmQJOglEaXNwbGF5cyB0aGUgcGFzc3dvcmQgZm9yIHRoZSBzY3JpcHQuXDAzM1sxOzkybVshSU1QT1JUQU5UIV1cMDMzWzBtCgkKCUtpbmRseSByZXBvcnQgYnVncyB0byBtZSBhdCA6IEFub255bWluSGFjazVAcHJvdG9ubWFpbC5jb20KCSIiIikKCQp0cnk6CglpZiAoc3lzLmFyZ3ZbMV09PSItaGVscCIgb3Igc3lzLmFyZ3ZbMV09PSItLWhlbHAiKToKCQlwcmludF9oZWxwKCkKCQlhcmd2PVRydWUKCWVsc2U6CgkJcGFzcwpleGNlcHQ6CglwYXNzCgppZiAoYXJndj09VHJ1ZSk6CglzeXMuZXhpdCgpCmVsc2U6CglwYXNzCgkKb3Muc3lzdGVtKCJjbGVhciB8fCBjbHMiKQoKdHJ5OgoJaWYgKHN5cy5hcmd2WzFdPT0iLWF1dGhvciIgb3Igc3lzLmFyZ3ZbMV09PSItLWF1dGhvciIpOgoJCXByaW50ICgiVGhpcyBzY3JpcHQgd2FzIGNvZGVkIGJ5IEFub255bWluSGFjazUgOiBGb2xsb3cgaGlzIGNvZGUgb24gR2l0aHViOiBUZXJtdXhIYWNreiIpCgkJYXJndj1UcnVlCgllbHNlOgoJCXBhc3MKZXhjZXB0OgoJcGFzcwoKaWYgKGFyZ3Y9PVRydWUpOgoJc3lzLmV4aXQoKQplbHNlOgoJcGFzcwoJCm9zLnN5c3RlbSgiY2xlYXIgfHwgY2xzIikKCnRyeToKCWlmIChzeXMuYXJndlsxXT09Ii1zeXN0ZW0iIG9yIHN5cy5hcmd2WzFdPT0iLS1zeXN0ZW0iKToKCQlpZiBzeXMucGxhdGZvcm0gPT0gImxpbnV4IjoKCQkJb3Muc3lzdGVtKCJmaWdsZXQgTGludXggU3lzdGVtIikKCQllbGlmIHN5cy5wbGF0Zm9ybSA9PSAidWJ1bnR1IjoKCQkJb3Muc3lzdGVtKCJmaWdsZXQgVWJ1bnR1IFN5c3RlbSIpCgkJZWxpZiBzeXMucGxhdGZvcm0gPT0gIndpbjMyIjoKCQkJb3Muc3lzdGVtKCJmaWdsZXQgV2luZG93cyBTeXN0ZW0iKQoJCWVsaWYgc3lzLnBsYXRmb3JtID09ICJ0ZXJtdXgiOgoJCQlvcy5zeXN0ZW0oImZpZ2xldCBUZXJtdXggU3lzdGVtIikKCQllbHNlOgoJCQlvcy5zeXN0ZW0oImZpZ2xldCBPdGhlciBTeXN0ZW0iKQoJCQoJCgkJCgkJYXJndj1UcnVlCgllbHNlOgoJCXBhc3MKZXhjZXB0OgoJcGFzcwoKaWYgKGFyZ3Y9PVRydWUpOgoJc3lzLmV4aXQoKQplbHNlOgoJcGFzcwoJCgoKdHJ5OgoJaWYgKHN5cy5hcmd2WzFdPT0icXVpdCIgb3Igc3lzLmFyZ3ZbMV09PSItcXVpdCIpOgoJCXByaW50KGNvbG9yZWQoIlByb2dyYW0gd2lsbCBiZSBUZXJtaW5hdGVkIG5vdyEhLi4uQ29tZSBiYWNrIHNvb24hISIsJ3JlZCcpKQoJCXRpbWUuc2xlZXAoMC43KQoJCW9zLnN5c3RlbSgiZmlnbGV0IC1mIHNsYW50IEJZRSEhIHwgbG9sY2F0IikKCQlhcmd2PVRydWUKCWVsc2U6CgkJcGFzcwpleGNlcHQ6CglwYXNzCgppZiAoYXJndj09VHJ1ZSk6CglzeXMuZXhpdCgpCmVsc2U6CglwYXNzCgkKdHJ5OgoJaWYgKHN5cy5hcmd2WzFdPT0iLXVzYWdlIiBvciBzeXMuYXJndlsxXT09Ii0tdXNhZ2UiKToKCQlvcy5zeXN0ZW0oImZpZ2xldCBVU0FHRSB8IGxvbGNhdCIpCgkJcHJpbnQgKCJcMDMzWzE7MzZtW1wwMzNbMG1cMDMzWzE7OTJtIVwwMzNbMG1cMDMzWzE7MzZtXSBUeXBlIFwwMzNbMG1cMDMzWzE7OTJtcHl0aG9uMyBwZGZicnV0ZXIucHlcMDMzWzBtIFwwMzNbMTszNm10byBzdGFydCB0aGUgUERGQlJVVEVSIFNjcmlwdCBbXDAzM1swbVwwMzNbMTs5Mm0hXDAzM1swbVwwMzNbMTszNm1dXDAzM1swbVxuIikKCQl0aW1lLnNsZWVwKDAuNikKCQlhcmd2PVRydWUKCWVsc2U6CgkJcGFzcwpleGNlcHQ6CglwYXNzCgppZiAoYXJndj09VHJ1ZSk6CglzeXMuZXhpdCgpCmVsc2U6CglwYXNzCgoKdHJ5OgoJaWYgKHN5cy5hcmd2WzFdPT0iLW5vdGljZSIgb3Igc3lzLmFyZ3ZbMV09PSItLW5vdGljZSIpOgoJCXByaW50KGNvbG9yZWQoIktJTkRMWSBNYWtlIHN1cmUgdGhlIFBERiBmaWxlIHBhdGggY3VycmVudGx5IGV4aXN0cyBzbyB0aGF0IFNjcmlwdCB3aWxsIHdvcmsgYW5kIHdpbGwgYnJ1dGVmb3JjZSBpdCB3ZWxsLiBJZiBub3Qgc2NyaXB0IHdpbGwgY29udGludWUgdG8gYnJ1dGVmb3JjZSBub3RoaW5nLiEhISEiLCdyZWQnKSkKCQlwcmludChjb2xvcmVkKCIrKysrKysrKysrK0kgSE9QRSBZT1UgTElTVEVOIEFORCBIRUVEIFRPIElOU1RSVUNUSU9OUysrKysrKysrKysrIiwncmVkJykpCgkJYXJndj1UcnVlCgllbHNlOgoJCXBhc3MKZXhjZXB0OgoJcGFzcwoKaWYgKGFyZ3Y9PVRydWUpOgoJc3lzLmV4aXQoKQplbHNlOgoJcGFzcwoJCgp0cnk6CglpZiAoc3lzLmFyZ3ZbMV09PSItcGFzc3dvcmQiIG9yIHN5cy5hcmd2WzFdPT0iLS1wYXNzd29yZCIpOgoJCXByaW50ICgiXDAzM1sxOzM0bVRoZSBwYXNzd29yZCBpczogPT4gXDAzM1swbVwwMzNbMTs5Mm1wZGZicnV0ZXJcMDMzWzBtIikKCQlwcmludChjb2xvcmVkKCJLaW5kbHkgU3RhciBhbmQgRm9yayB0aGlzIHJlcG8gdG8gc3VwcG9ydCBBbm9ueW1pbkhhY2s1IGRldmVsb3BlciBvZiB0aGlzIFNjcmlwdCIsJ2dyZWVuJykpCgkJdGltZS5zbGVlcCgxKQoJCWFyZ3Y9VHJ1ZQoJZWxzZToKCQlwYXNzCmV4Y2VwdDoKCXBhc3MKCmlmIChhcmd2PT1UcnVlKToKCXN5cy5leGl0KCkKZWxzZToKCXBhc3MKCgp0cnk6CglpZiAoc3lzLmFyZ3ZbMV09PSItdXBkYXRlIiBvciBzeXMuYXJndlsxXT09Ii0tdXBkYXRlIik6CgkJY2xzKCkKCQlwcmludChjb2xvcmVkKCJbKl0gQ2hlY2tpbmcgVXBkYXRlcyAuLiEhWypdIiwnZ3JlZW4nKSkKCQl0aW1lLnNsZWVwKDIpCgkJcHJpbnQoIlshXSBJbnN0YWxsaW5nIG5ldyB2ZXJzaW9uIG9mIFBERi1CUlVURVIgaW50byB5b3VyIHRlcm1pbmFsIFshXSIpCgkJdGltZS5zbGVlcCgxKQoJCXByaW50KCItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSIpCgkJb3Muc3lzdGVtKCJjZCAkSE9NRSIpCgkJaWYgb3MubmFtZSA9PSAiTGludXgiOgoJCQlvcy5zeXN0ZW0oInN1ZG8gcm0gLXJmIHBkZmJydXRlIikKCQllbHNlOgoJCQlvcy5zeXN0ZW0oInJtIC1yZiBwZGZicnV0ZSIpCgkJb3Muc3lzdGVtKCJnaXQgY2xvbmUgaHR0cHM6Ly9naXRodWIuY29tL1Rlcm11eEhhY2t6L3BkZmJydXRlIikKCQlvcy5zeXN0ZW0oImNkIHBkZmJydXRlIikKCQlpZiBvcy5uYW1lID09ICJMaW51eCI6CgkJCW9zLnN5c3RlbSgic3VkbyBjaG1vZCAreCAqIikKCQllbHNlOgoJCQlvcy5zeXN0ZW0oImNobW9kIDc3NyAqIikKCQlvcy5zeXN0ZW0oInB5dGhvbjMgZGVwZW5kZW5jaWVzLnB5IikKCQlzeXMuZXhpdCgpCgkJcXVpdCgpCgkJYXJndj1UcnVlCgllbHNlOgoJCXBhc3MKZXhjZXB0OgoJcGFzcwoKaWYgKGFyZ3Y9PVRydWUpOgoJc3lzLmV4aXQoKQplbHNlOgoJcGFzcwkKCgpzbWFsbGxvZ28gPSAiIiJcMDMzWzE7OTRtCuKVreKUgeKUs+KUgeKUgeKUs+KUgeKUgeKVruKVseKVreKUgeKUgeKUs+KUgeKUs+KUs+KUs+KUgeKUgeKUs+KUgeKUs+KUgeKVrgrilIPilYvilKPila7ila7ilIPilIHilLPilLvilIHilKvila3ila7ilIPilYvilIPilIPilKPila7ila3ilKvilLPilKvilYvilIMK4pSD4pWt4pWL4pS74pWv4pSD4pWt4pS74pSB4pSB4pSr4pWt4pWu4pSD4pWu4pSr4pSD4pSD4pSD4pSD4pSD4pS74pSr4pWu4pSrCuKVsOKVr+KVsOKUgeKUgeKUu+KVr+KVseKVseKVseKVsOKUgeKUgeKUu+KUu+KUu+KUgeKVr+KVsOKVr+KVsOKUgeKUu+KUu+KVrwoiIiIKCnByaW50KHNtYWxsbG9nbykKCmZpbGUgPSBvcGVuKCJyb2NreW91LnR4dCIpCnByaW50KGNvbG9yZWQoIlshXSBNYWtlIHN1cmUgUERGIFBhdGggZmlsZSBleGlzdHMgYmVmb3JlIHlvdSBTdGFydCwgZWxzZSB3b250IHdvcmsgWyFdIiwncmVkJykpCnByaW50KCIiKQpmaWxlX3BhdGggPSBpbnB1dCgiXDAzM1sxOzk2bVt+XVB1dCBpbiBwYXRoIG9mIFBERiBmaWxlIFt+XX4+OiBcMDMzWzBtIikKcnVuKCkKCgpwcmludCAoIiIpCnByaW50ICgiXDAzM1sxOzM3bSsrKysrKysrK1N0YXJ0aW5nIFRpbWUgb2YgQnJ1dGVGb3JjZTogJXM6JXM6JXMrKysrKysrKytcMDMzWzBtIiAlIChlLmhvdXIsIGUubWludXRlLCBlLnNlY29uZCkpCnRpbWUuc2xlZXAoMikKcHJpbnQgKCIiKQpwcmludCAoIlx0SGl0IHRoZSBlbnRlciBidXR0b24gd2hlbiB5b3UgYXJlIHJlYWR5ISEiKQpvcy5zeXN0ZW0oInJlYWQgYTEiKQpwcmludCAoIiIpCnByaW50KGNvbG9yZWQoIlsqXSBCcnV0ZUZvcmNlIEhhcyBTdGFydGVkIFsqXSIsJ2dyZWVuJykpCnRpbWUuc2xlZXAoMikKCnByaW50ICgiIikKZm9yIHBhc3N3b3JkIGluIGZpbGU6Cgl0cnk6CgkJd2l0aCBwaWtlcGRmLm9wZW4oZmlsZV9wYXRoLHBhc3N3b3JkLnN0cmlwKCkpIGFzIHBkZjoKCQkJcHJpbnQoY29sb3JlZCgiUGFzc3dvcmQgRm91bmQ6IHt9Ii5mb3JtYXQocGFzc3dvcmQpLCdncmVlbicpKSAjR2V0cyB0aGUgcGFzc3dvcmQgYWxyZWFkeQoJCQlwcmludCAoIlwwMzNbMTszNG1bKl0gQnJ1dGVGb3JjZSBIYXMgRW5kZWQgYXQ6ICVzOiVzOiVzIFsqXVwwMzNbMG0iICUgKGUuaG91ciwgZS5taW51dGUsIGUuc2Vjb25kKSkKCQkJYnJlYWsKCQkJCglleGNlcHQ6CgkJCXByaW50KGNvbG9yZWQoIlRyeWluZyB0aGVzZSBQYXNzd29yZHM6IHt9Ii5mb3JtYXQocGFzc3dvcmQpLCdyZWQnKSkgIyBHZXR0aW5nIGxpc3RzIG9mIHBvc3NpYmxlIHBhc3N3b3Jkcy4KCQkJY29udGludWUK'))