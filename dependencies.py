import base64
exec(base64.b64decode('aW1wb3J0IHRpbWUsIHN5cywgb3MsIHBsYXRmb3JtCmZyb20gdGVybWNvbG9yIGltcG9ydCBjb2xvcmVkCgoKZGVmIGNscygpOgoJaWYgc3lzLnBsYXRmb3JtID09ICJsaW51eCI6CgkgICAgb3Muc3lzdGVtKCJjbGVhciIpCgllbHNlOgoJICAgIG9zLnN5c3RlbSgiY2xzIikKCmNscygpCgoKCiMgaW5zdGFsbCBkZXBlbmRlbmNpZXMgZm9yIFRlcm11eApkZWYgVGVybXV4KCk6CglpZiBzeXMucGxhdGZvcm0gPT0gInRlcm11eCI6CgkJcHJpbnQoY29sb3JlZCgiWyFdIERldGVjdGluZyBUZXJtaW5hbC4uIFshXSIsJ2dyZWVuJykpCgkJdGltZS5zbGVlcCgyKQoJCXByaW50KGNvbG9yZWQoIlshXSBUZXJtdXggVGVybWluYWwgRGV0ZWN0ZWQhIVshXSAiLCdncmVlbicpKQoJCXRpbWUuc2xlZXAoMikKCQlvcy5zeXN0ZW0oInBrZyB1cGRhdGUgJiYgcGtnIHVwZ3JhZGUiKQoJCW9zLnN5c3RlbSgicGtnIGluc3RhbGwgcHl0aG9uMyIpCgkJb3Muc3lzdGVtKCJwaXAzIGluc3RhbGwgbG9sY2F0IikKCQlvcy5zeXN0ZW0oInB5dGhvbjMgLW0gcGlwIGluc3RhbGwgcGlrZXBkZiIpCgkJb3Muc3lzdGVtKCJwaXAgaW5zdGFsbCBjb2xvcmFtYSIpCgkJdGltZS5zbGVlcCgxKQoJCWNscygpCgkJcHJpbnQoY29sb3JlZCgiWypdIFRlcm11eCBEZXBlbmRlbmNpZXMgaGFzIGJlZW4gaW5zdGFsbGVkIFsqXSIsJ2dyZWVuJykpCgkJdGltZS5zbGVlcCgxKQoJCXByaW50KCJcMDMzWzE7OTNtWyFdIE5vdyBydW4gXDAzM1swbVwwMzNbMTs5Mm1weXRob24zIHBkZmJydXRlci5weSAtLWhlbHBcMDMzWzBtXDAzM1sxOzkzbSB0byBzZWUgdGhlIHRvb2wncyBoZWxwIG1lbnVcMDMzWzBtXG4iKQoJCXN5cy5leGl0KCkKCWVsc2U6CgkJcHJpbnQoY29sb3JlZCgiWyFdIERldGVjdGluZyBUZXJtaW5hbC4uLiBbIV0iLCdncmVlbicpKQoJCXRpbWUuc2xlZXAoMikKCQlwcmludChjb2xvcmVkKCJbeF0gVGVybXV4IFRlcm1pbmFsIG5vdCBkZXRlY3RlZCwgS2luZGx5IHVzZSBhIFRlcm11eCBUZXJtaW5hbCEhIFt4XSIsJ3JlZCcpKQoJCXN5cy5leGl0KCkKCgojSW5zdGFsbGluZyBkZXBlbmRlbmNpZXMgZm9yIGxpbnV4CgpkZWYgTGludXgoKToKCXByaW50KGNvbG9yZWQoIlshXSBEZXRlY3Rpbmcgc3lzdGVtISFbIV0gIiwnZ3JlZW4nKSkKCXRpbWUuc2xlZXAoMikKCW9zLnN5c3RlbSgiYmFzaCBzeXN0ZW0uc2giKQoJCQojIEluc3RhbGxpbmcgZGVwZW5kZW5jaWVzIGZvciBVYnVudHUKCmRlZiBVYnVudHUoKToKCWlmIHN5cy5wbGF0Zm9ybSA9PSAidWJ1bnR1IjoKCQlwcmludChjb2xvcmVkKCJbIV0gRGV0ZWN0aW5nIFN5c3RlbSAuLi4gWyFdIiwnZ3JlZW4nKSkKCQl0aW1lLnNsZWVwKDIpCgkJcHJpbnQoY29sb3JlZCgiWytdIERlcGVuZGVuY2llcyBmb3IgVWJ1bnR1IGhhcyBiZWVuIGRldGVjdGVkISFbK10iLCdncmVlbicpKQoJCXRpbWUuc2xlZXAoMikKCQlwcmludCgiXDAzM1sxOzMzbUluc3RhbGxpbmcgUmVxdWlyZWQgZGVwZW5kZW5jaWVzXDAzM1swbVxuIikKCQl0aW1lLnNsZWVwKDEpCgkJb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgaW5zdGFsbCB1cGRhdGUgLXkgJiYgc3VkbyBhcHQtZ2V0IGluc3RhbGwgdXBncmFkZSAteSIpCgkJb3Muc3lzdGVtKCJzdWRvIGFwdC1nZXQgaW5zdGFsbCBweXRob24zIC15IikKCQlvcy5zeXN0ZW0oInN1ZG8gcGlwIGluc3RhbGwgY29sb3JhbWEgJiYgc3VkbyBwaXAgaW5zdGFsbCB0ZXJtY29sb3IiKQoJCW9zLnN5c3RlbSgicHl0aG9uMyAtbSBwaXAgaW5zdGFsbCBwaWtlcGRmIikKCQl0aW1lLnNsZWVwKDEpCgkJY2xzKCkKCQlwcmludChjb2xvcmVkKCJbIV0gRGVwZW5kZW5jaWVzIGZvciBVYnVudHUgaGFzIGJlZW4gaW5zdGFsbGVkIGludG8geW91ciBVYnVudHUgc3lzdGVtIFshXSIsJ2dyZWVuJykpCgkJcHJpbnQoIlwwMzNbMTs5M21bIV0gTm93IHJ1biBcMDMzWzBtXDAzM1sxOzkybXB5dGhvbjMgcGRmYnJ1dGVyLnB5IC0taGVscFwwMzNbMG1cMDMzWzE7OTNtIHRvIHNlZSB0aGUgdG9vbCdzIGhlbHAgbWVudVwwMzNbMG1cbiIpCgkJc3lzLmV4aXQoKQoJZWxzZToKCQlwcmludChjb2xvcmVkKCJbIV0gRGV0ZWN0aW5nIFN5c3RlbSAuLi4gWyFdIiwnZ3JlZW4nKSkKCQl0aW1lLnNsZWVwKDIpCgkJcHJpbnQoY29sb3JlZCgiW3hdIFVidW50dSB0ZXJtaW5hbCBub3QgZGV0ZWN0ZWQsIEtpbmRseSB1c2UgYW4gdWJ1bnR1IGJhc2VkIHN5c3RlbS4uW3hdIiwncmVkJykpCgkJc3lzLmV4aXQoKQoKCmxvZ28gPSAiIiIKX19fICAgICAgICAgICAgICAgICAgICAgIF8gIF8gIF9fICAgIF8gIF8gICAgX19fIF9fIF8gCiB8IF9fICBfIF98XyBfICB8ICB8ICAgIHxfKXwgXHxfIC0tLXxfKXxfKXwgfCB8IHxfIHxfKQpffF98IHxfPiAgfF8oX3wgfCAgfCAgICB8ICB8Xy98ICAgICB8Xyl8IFx8X3wgfCB8X198IFwKCiIiIgoKcHJpbnQobG9nbykKCnByaW50KGNvbG9yZWQoIkluc3RhbGwgRGVwZW5kZW5jaWVzIGJhc2VkIG9uIHlvdXIgc3lzdGVtIiwnYmx1ZScpKQoKcHJpbnQoY29sb3JlZCgiXHRDaG9vc2UgeW91ciB0ZXJtaW5hbCBiZWxvdyIsJ2dyZWVuJykpCmJhbm5lciA9ICIiIlwwMzNbMTszM20KKysrKysrKysrKysrSU5TVEFMTElORyBERVBFTkRFTkNJRVMrKysrKysrClwwMzNbMG1cbiIiIgpiYW5uZXIgKz0gJyBbMV0gVGVybXV4IFxuJwpiYW5uZXIgKz0gJyBbMl0gTGludXggXG4nCmJhbm5lciArPSAnIFszXSBVYnVudHUgXG4nCmJhbm5lciArPSAnIFswXSBFeGl0LiBcMDMzWzE7OTJtKE5vdCBSZWNvbW1lbmRlZClcMDMzWzBtXG4nCnByaW50KGJhbm5lcikKCmNob2ljZSA9IGlucHV0KCIiIlwwMzNbMTs5NG1+PiQgRW50ZXIgTnVtYmVyOiBcMDMzWzBtIiIiKQppZiBjaG9pY2UgPT0gIjAiOgoJcHJpbnQoY29sb3JlZCgiW3hdIFByb2dyYW0gVGVybWluYXRlZCwgR29vZCBCeWUhIVt4XSIsJ3JlZCcpKQoJdGltZS5zbGVlcCgxKQoJc3lzLmV4aXQoKQplbGlmIGNob2ljZSA9PSAiMSI6CglUZXJtdXgoKQplbGlmIGNob2ljZSA9PSAiMiI6CglMaW51eCgpCmVsaWYgY2hvaWNlID09ICIzIjoKCVVidW50dSgpCmVsc2U6CgljbHMoKQoJcHJpbnQoY29sb3JlZCgiW3hdIEludmFsaWQgTnVtYmVyICEhLCBFeGl0aW5nISEuLktpbmRseSBJTlNUQUxMIERFUEVOREVOQ0lFUyBFTFNFIFJFQUwgU0NSSVBUIFdPTlQgV09SS1t4XSIsJ3JlZCcpKQoJdGltZS5zbGVlcCgxKQoJc3lzLmV4aXQoKQoJcXVpdCgpCgkKCgoKCg=='))
