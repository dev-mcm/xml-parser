import pandas as pd
import numpy as np
import untangle

XML = 'data/LandlordTenantExtract2019.xml' #production file
#XML = 'output/2018_first100.xml' #development file

IndexNumberId_list = []
FiledDate_list = []
PropertyType_list = []
Classification_list = []
Status_list = []
DisposedDate_list = []
DisposedReasonNoPersonallyIdentifyingInfo_list = []
FirstPaper_list = []
PrimaryClaimTotal_list = []
City_list = []
State_list = []
PostalCode_list = []


o = untangle.parse(XML)
for Index in o.Extract.Indexes.Index:
    if hasattr(Index, 'IndexNumberId'):
        IndexNumberId = Index.IndexNumberId.cdata
    else: 
        IndexNumberId = None 
    
    if hasattr(Index, 'FiledDate'):
        FiledDate = Index.FiledDate.cdata
    else:
        FiledDate = None
    
    if hasattr(Index, 'PropertyType'):
        PropertyType = Index.PropertyType.cdata
    else:
        PropertyType = None
    
    if hasattr(Index, 'Classification'):
        Classification = Index.Classification.cdata
    else:
        Classification = None
    
    if hasattr(Index, 'Status'):
        Status = Index.Status.cdata
    else:
        Status = None
    
    if hasattr(Index, 'DisposedDate'):
        DisposedDate = Index.DisposedDate.cdata
    else:
        DisposedDate = None
    
    if hasattr(Index, 'DisposedReasonNoPersonallyIdentifyingInfo'):
        DisposedReasonNoPersonallyIdentifyingInfo = Index.DisposedReasonNoPersonallyIdentifyingInfo.cdata
    else:
        DisposedReasonNoPersonallyIdentifyingInfo = None
    
    if hasattr(Index, 'FirstPaper'):
        FirstPaper = Index.FirstPaper.cdata
    else:
        FirstPaper = None
    
    if hasattr(Index, 'PrimaryClaimTotal'):
        PrimaryClaimTotal = Index.PrimaryClaimTotal.cdata
    else:
        PrimaryClaimTotal = None
    
    if hasattr(Index.PropertyAddresses.PropertyAddress, 'City'):
        City = Index.PropertyAddresses.PropertyAddress.City.cdata
    else:
        City = None
    
    if hasattr(Index.PropertyAddresses.PropertyAddress, 'State'):
        State = Index.PropertyAddresses.PropertyAddress.State.cdata
    else:
        State = None
    
    if hasattr(Index.PropertyAddresses.PropertyAddress, 'PostalCode'):
        PostalCode = Index.PropertyAddresses.PropertyAddress.PostalCode.cdata
    else:
        PostalCode = None

    
    IndexNumberId_list.append(IndexNumberId)
    FiledDate_list.append(FiledDate)
    PropertyType_list.append(PropertyType)
    Classification_list.append(Classification)
    Status_list.append(Status)
    DisposedDate_list.append(DisposedDate)
    DisposedReasonNoPersonallyIdentifyingInfo_list.append(DisposedReasonNoPersonallyIdentifyingInfo)
    FirstPaper_list.append(FirstPaper)
    PrimaryClaimTotal_list.append(PrimaryClaimTotal)
    City_list.append(City)
    State_list.append(State)
    PostalCode_list.append(PostalCode)
    
df = pd.DataFrame(
    {
        'IndexNumberId': IndexNumberId_list
        ,'FiledDate': FiledDate_list
        ,'PropertyType': PropertyType_list
        ,'Classification': Classification_list
        ,'Status': Status_list
        ,'DisposedDate': DisposedDate_list
        ,'DisposedReasonNoPersonallyIdentifyingInfo': DisposedReasonNoPersonallyIdentifyingInfo_list
        ,'FirstPaper': FirstPaper_list
        ,'PrimaryClaimTotal': PrimaryClaimTotal_list
        ,'City': City_list
        ,'State': State_list
        ,'PostalCode': PostalCode_list
        
        }
    )

df.to_csv('output/LandlordTenantExtract2019.csv',index=False)

