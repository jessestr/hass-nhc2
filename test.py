import json
from nhc2device import generateNHC2Device, NHC2Device, NHC2DeviceStatusProperty

all = json.loads('{"Method":"devices.list","Params":[{"Devices":[{"Properties":[{"Status":"Off"}],"Name":"Licht Atelier","Technology":"nikohomecontrol","Uuid":"61daf045-fcfa-407b-ac79-d224748ed0c3","Identifier":"3a10cea2-e35c-46fb-8c3d-7ec783901721","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"light","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Zolder","Technology":"nikohomecontrol","Uuid":"3e48a7b6-ff82-40e4-a4c5-4720049b19ad","Identifier":"f7335332-5942-4c57-b217-d0c2e8af2e9e","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"light","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Keuken Hoofdlicht","Technology":"nikohomecontrol","Uuid":"1ac3ebca-8ff0-4420-8bd4-1bf382c1d869","Identifier":"fc10043a-e82d-48a8-9628-1a606a73b494","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Gang Toggle","Technology":"nikohomecontrol","Uuid":"f89c1c84-432b-4048-bfa5-8291d20dc643","Identifier":"57741c33-3843-4a40-8ea5-92f30d1fcfe8","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"On"}],"Name":"basisactie 3","Technology":"nikohomecontrol","Uuid":"bcb0da59-b164-4de6-b19e-2d4e62ffbbea","Identifier":"da4e2c9c-e8b4-4a3c-b1d7-1ce212cf48eb","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"light","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Garagepoort","Technology":"nikohomecontrol","Uuid":"aaab1623-c708-4019-9c47-42b192ae3ce2","Identifier":"f0bbbfa9-1e79-4c0f-9a9a-e3e1f25b4f6e","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Keuken Aanrecht","Technology":"nikohomecontrol","Uuid":"ba4ef58a-0d77-4b98-9a2a-1104a0fca2a9","Identifier":"5bb4f4a4-bd11-4e18-89cb-7e2df5391b25","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Voordeur Licht Token","Technology":"nikohomecontrol","Uuid":"7494695f-467b-444d-841f-478c77e00591","Identifier":"caf5119f-d3f9-4afc-af60-78a1ec41cacf","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Keuken Dampkap","Technology":"nikohomecontrol","Uuid":"48a3bc18-d8a9-426d-a9d7-77276abab83b","Identifier":"a37b4905-98ee-4aec-831f-e4413e0d33f8","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Keuken Pompbak","Technology":"nikohomecontrol","Uuid":"57dfef4b-f724-4b0b-a0e1-0968488bb019","Identifier":"69f3a184-bea8-482c-b20b-562e6cb2bd6f","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"all off","Technology":"nikohomecontrol","Uuid":"bcc60cde-328f-4675-b3e8-1f41f72b704d","Identifier":"0f852cb0-ef30-4700-b3b0-4abc8820b515","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"basisactie 1","Technology":"nikohomecontrol","Uuid":"d65ecf24-bd85-4c1b-b420-8cb4b204ba24","Identifier":"5c97dd46-5e0a-4043-8a27-ba6271c77774","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Garage Licht","Technology":"nikohomecontrol","Uuid":"6bc5525d-fca4-4e5c-a1a6-2078b33ace82","Identifier":"f7d36665-3bc0-4810-a3b4-4cd2b5c7c201","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"switched-generic","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]},{"Properties":[{"Status":"Off"}],"Name":"Badkamer","Technology":"nikohomecontrol","Uuid":"dbee14a0-bfd4-485b-b5ef-16691eef446f","Identifier":"1f4b84ee-c835-4bd2-9281-044065b0369a","PropertyDefinitions":[{"Status":{"Description":"Choice(On,Off)","HasStatus":"true","CanControl":"true"}}],"Online":"True","Model":"light","Traits":[],"Type":"action","Parameters":[{"LocationId":"7460267e-77c5-4500-9e4b-1b1f6390a558"},{"LocationName":"Thuis"},{"LocationIcon":"general"}]}]}]}')
dev = all['Params'][0]['Devices'][0]
hadev: NHC2Device = generateNHC2Device(dev)
print(hadev.Properties)
for x in hadev.Properties:
    print(type(x))
    print(type(NHC2DeviceStatusProperty))

print(next(filter(lambda x: type(x) is type(NHC2DeviceStatusProperty), hadev.Properties), None))
