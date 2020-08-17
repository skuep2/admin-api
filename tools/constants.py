# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:47:56 2020

@author: Julia Schroeder, julia.schroeder@grammm.com
@copyright: Grammm GmbH, 2020
"""

SERIAL_ENDIAN = "little"  # Endianess used for binary serialization

class _ReverseLookup:
    @classmethod
    def lookup(cls, value, default=None):
        if not hasattr(cls, "_lookup"):
            cls._lookup = {getattr(cls, key): key for key in dir(cls) if not key.startswith("_")}
        return cls._lookup.get(value, default)


class PropTypes(_ReverseLookup):
    UNSPECIFIED = 0x0000
    SHORT = 0x0002
    LONG = 0x0003
    FLOAT = 0x0004
    DOUBLE = 0x0005
    CURRENCY = 0x0006
    FLOATINGTIME = 0x0007
    ERROR = 0x000a
    BYTE = 0x000b
    OBJECT = 0x000d
    LONGLONG = 0x0014
    STRING = 0x001e
    WSTRING = 0x001f
    FILETIME = 0x0040
    GUID = 0x0048
    SVREID = 0x00fb
    RESTRICTION = 0x00fd
    RULE = 0x00fe
    BINARY = 0x0102
    SHORT_ARRAY = 0x1002
    LONG_ARRAY = 0x1003
    LONGLONG_ARRAY = 0x1014
    STRING_ARRAY = 0x101e
    WSTRING_ARRAY = 0x101f
    GUID_ARRAY = 0x1048
    BINARY_ARRAY = 0x1102


class PropTags(_ReverseLookup):
    ABPROVIDERID = 0x36150102
    ACCESS = 0x0FF40003
    ACCESSCONTROLLISTDATA = 0x3FE00102
    ACCESSLEVEL = 0x0FF70003
    ACCOUNT = 0x3A00001F
    ACCOUNT_STRING8 = 0x3A00001E
    ADDITIONALRENENTRYIDS = 0x36D81102
    ADDITIONALRENENTRYIDSEX = 0x36D90102
    ADDRESSBOOKAUTHORIZEDSENDERS = 0x8CD8000D
    ADDRESSBOOKCONTAINERID = 0xFFFD0003
    ADDRESSBOOKDELIVERYCONTENTLENGTH = 0x806A0003
    ADDRESSBOOKDISPLAYNAMEPRINTABLE = 0x39FF001F
    ADDRESSBOOKDISPLAYNAMEPRINTABLE_STRING8 = 0x39FF001E
    ADDRESSBOOKDISPLAYTYPEEXTENDED = 0x8C930003
    ADDRESSBOOKDISTRIBUTIONLISTEXTERNALMEMBERCOUNT = 0x8CE30003
    ADDRESSBOOKDISTRIBUTIONLISTMEMBERCOUNT = 0x8CE20003
    ADDRESSBOOKDISTRIBUTIONLISTMEMBERSUBMITACCEPTED = 0x8073000D
    ADDRESSBOOKDISTRIBUTIONLISTMEMBERSUBMITREJECTED = 0x8CDA000D
    ADDRESSBOOKDISTRIBUTIONLISTREJECTMESSAGESFROMDLMEMBERS = 0x8CDB000D
    ADDRESSBOOKENTRYID = 0x663B0102
    ADDRESSBOOKEXTENSIONATTRIBUTE1 = 0x802D001F
    ADDRESSBOOKEXTENSIONATTRIBUTE10 = 0x8036001F
    ADDRESSBOOKEXTENSIONATTRIBUTE10_STRING8 = 0x8036001E
    ADDRESSBOOKEXTENSIONATTRIBUTE11 = 0x8C57001F
    ADDRESSBOOKEXTENSIONATTRIBUTE11_STRING8 = 0x8C57001E
    ADDRESSBOOKEXTENSIONATTRIBUTE12 = 0x8C58001F
    ADDRESSBOOKEXTENSIONATTRIBUTE12_STRING8 = 0x8C58001E
    ADDRESSBOOKEXTENSIONATTRIBUTE13 = 0x8C59001F
    ADDRESSBOOKEXTENSIONATTRIBUTE13_STRING8 = 0x8C59001E
    ADDRESSBOOKEXTENSIONATTRIBUTE14 = 0x8C60001F
    ADDRESSBOOKEXTENSIONATTRIBUTE14_STRING8 = 0x8C60001E
    ADDRESSBOOKEXTENSIONATTRIBUTE15 = 0x8C61001F
    ADDRESSBOOKEXTENSIONATTRIBUTE15_STRING8 = 0x8C61001E
    ADDRESSBOOKEXTENSIONATTRIBUTE1_STRING8 = 0x802D001E
    ADDRESSBOOKEXTENSIONATTRIBUTE2 = 0x802E001F
    ADDRESSBOOKEXTENSIONATTRIBUTE2_STRING8 = 0x802E001E
    ADDRESSBOOKEXTENSIONATTRIBUTE3 = 0x802F001F
    ADDRESSBOOKEXTENSIONATTRIBUTE3_STRING8 = 0x802F001E
    ADDRESSBOOKEXTENSIONATTRIBUTE4 = 0x8030001F
    ADDRESSBOOKEXTENSIONATTRIBUTE4_STRING8 = 0x8030001E
    ADDRESSBOOKEXTENSIONATTRIBUTE5 = 0x8031001F
    ADDRESSBOOKEXTENSIONATTRIBUTE5_STRING8 = 0x8031001E
    ADDRESSBOOKEXTENSIONATTRIBUTE6 = 0x8032001F
    ADDRESSBOOKEXTENSIONATTRIBUTE6_STRING8 = 0x8032001E
    ADDRESSBOOKEXTENSIONATTRIBUTE7 = 0x8033001F
    ADDRESSBOOKEXTENSIONATTRIBUTE7_STRING8 = 0x8033001E
    ADDRESSBOOKEXTENSIONATTRIBUTE8 = 0x8034001F
    ADDRESSBOOKEXTENSIONATTRIBUTE8_STRING8 = 0x8034001E
    ADDRESSBOOKEXTENSIONATTRIBUTE9 = 0x8035001F
    ADDRESSBOOKEXTENSIONATTRIBUTE9_STRING8 = 0x8035001E
    ADDRESSBOOKFOLDERPATHNAME = 0x8004001F
    ADDRESSBOOKFOLDERPATHNAME_STRING8 = 0x8004001E
    ADDRESSBOOKHIERARCHICALCHILDDEPARTMENTS = 0x8C9A000D
    ADDRESSBOOKHIERARCHICALDEPARTMENTMEMBERS = 0x8C97000D
    ADDRESSBOOKHIERARCHICALISHIERARCHICALGROUP = 0x8CDD000B
    ADDRESSBOOKHIERARCHICALPARENTDEPARTMENT = 0x8C99000D
    ADDRESSBOOKHIERARCHICALROOTDEPARTMENT = 0x8C98001E
    ADDRESSBOOKHIERARCHICALSHOWINDEPARTMENTS = 0x8C94000D
    ADDRESSBOOKHOMEMESSAGEDATABASE = 0x8006001F
    ADDRESSBOOKHOMEMESSAGEDATABASE_STRING8 = 0x8006001E
    ADDRESSBOOKISMASTER = 0xFFFB000B
    ADDRESSBOOKISMEMBEROFDISTRIBUTIONLIST = 0x8008001E
    ADDRESSBOOKMANAGEDISTRIBUTIONLIST = 0x6704000D
    ADDRESSBOOKMANAGER = 0x8005000D
    ADDRESSBOOKMANAGERDISTINGUISHEDNAME = 0x8005001F
    ADDRESSBOOKMEMBER = 0x8009000D
    ADDRESSBOOKMESSAGEID = 0x674F0014
    ADDRESSBOOKMODERATIONENABLED = 0x8CB5000B
    ADDRESSBOOKNETWORKADDRESS = 0x8170101F
    ADDRESSBOOKNETWORKADDRESS_STRING8 = 0x8170101E
    ADDRESSBOOKOBJECTDISTINGUISHEDNAME = 0x803C001F
    ADDRESSBOOKOBJECTDISTINGUISHEDNAME_STRING8 = 0x803C001E
    ADDRESSBOOKOBJECTGUID = 0x8C6D0102
    ADDRESSBOOKORGANIZATIONALUNITROOTDISTINGUISHEDNAME = 0x8CA8001F
    ADDRESSBOOKORGANIZATIONALUNITROOTDISTINGUISHEDNAME_STRING8 = 0x8CA8001E
    ADDRESSBOOKOWNER = 0x800C000D
    ADDRESSBOOKOWNERBACKLINK = 0x8024000D
    ADDRESSBOOKPARENTENTRYID = 0xFFFC0102
    ADDRESSBOOKPHONETICCOMPANYNAME = 0x8C91001F
    ADDRESSBOOKPHONETICCOMPANYNAME_STRING8 = 0x8C91001E
    ADDRESSBOOKPHONETICDEPARTMENTNAME = 0x8C90001F
    ADDRESSBOOKPHONETICDEPARTMENTNAME_STRING8 = 0x8C90001E
    ADDRESSBOOKPHONETICDISPLAYNAME = 0x8C92001F
    ADDRESSBOOKPHONETICDISPLAYNAME_STRING8 = 0x8C92001E
    ADDRESSBOOKPHONETICGIVENNAME = 0x8C8E001F
    ADDRESSBOOKPHONETICGIVENNAME_STRING8 = 0x8C8E001E
    ADDRESSBOOKPHONETICSURNAME = 0x8C8F001F
    ADDRESSBOOKPHONETICSURNAME_STRING8 = 0x8C8F001E
    ADDRESSBOOKPROXYADDRESSES = 0x800F101F
    ADDRESSBOOKPROXYADDRESSES_STRING8 = 0x800F101E
    ADDRESSBOOKPUBLICDELEGATES = 0x8015000D
    ADDRESSBOOKREPORTS = 0x800E000D
    ADDRESSBOOKROOMCAPACITY = 0x08070003
    ADDRESSBOOKROOMCONTAINERS = 0x8C96101F
    ADDRESSBOOKROOMDESCRIPTION = 0x0809001F
    ADDRESSBOOKROOMDESCRIPTION_STRING8 = 0x0809001E
    ADDRESSBOOKSENDERHINTTRANSLATIONS = 0x8CAC101F
    ADDRESSBOOKSENIORITYINDEX = 0x8CA00003
    ADDRESSBOOKTARGETADDRESS = 0x8011001F
    ADDRESSBOOKTARGETADDRESS_STRING8 = 0x8011001E
    ADDRESSBOOKUNAUTHORIZEDSENDERS = 0x8CD9000D
    ADDRESSBOOKX509CERTIFICATE = 0x8C6A1102
    ADDRESSTYPE = 0x3002001F
    ADDRESSTYPE_STRING8 = 0x3002001E
    ALTERNATERECIPIENTALLOWED = 0x0002000B
    ANR = 0x360C001F
    ANR_STRING8 = 0x360C001E
    ARCHIVEDATE = 0x301F0040
    ARCHIVEPERIOD = 0x301E0003
    ARCHIVETAG = 0x30180102
    ASSISTANT = 0x3A30001F
    ASSISTANTTELEPHONENUMBER = 0x3A2E001F
    ASSISTANTTELEPHONENUMBER_STRING8 = 0x3A2E001E
    ASSISTANT_STRING8 = 0x3A30001E
    ASSOCIATED = 0x67AA000B
    ATTACHADDITIONALINFORMATION = 0x370F0102
    ATTACHCONTENTBASE = 0x3711001F
    ATTACHCONTENTBASE_STRING8 = 0x3711001E
    ATTACHCONTENTID = 0x3712001F
    ATTACHCONTENTID_STRING8 = 0x3712001E
    ATTACHCONTENTLOCATION = 0x3713001F
    ATTACHCONTENTLOCATION_STRING8 = 0x3713001E
    ATTACHDATABINARY = 0x37010102
    ATTACHDATAOBJECT = 0x3701000D
    ATTACHENCODING = 0x37020102
    ATTACHEXTENSION = 0x3703001F
    ATTACHEXTENSION_STRING8 = 0x3703001E
    ATTACHFILENAME = 0x3704001F
    ATTACHFILENAME_STRING8 = 0x3704001E
    ATTACHFLAGS = 0x37140003
    ATTACHLONGFILENAME = 0x3707001F
    ATTACHLONGFILENAME_STRING8 = 0x3707001E
    ATTACHLONGPATHNAME = 0x370D001F
    ATTACHLONGPATHNAME_STRING8 = 0x370D001E
    ATTACHMETHOD = 0x37050003
    ATTACHMIMETAG = 0x370E001F
    ATTACHMIMETAG_STRING8 = 0x370E001E
    ATTACHNUMBER = 0x0E210003
    ATTACHPATHNAME = 0x3708001F
    ATTACHPATHNAME_STRING8 = 0x3708001E
    ATTACHPAYLOADCLASS = 0x371A001F
    ATTACHPAYLOADCLASS_STRING8 = 0x371A001E
    ATTACHPAYLOADPROVIDERGUIDSTRING = 0x3719001F
    ATTACHPAYLOADPROVIDERGUIDSTRING_STRING8 = 0x3719001E
    ATTACHRENDERING = 0x37090102
    ATTACHSIZE = 0x0E200003
    ATTACHTAG = 0x370A0102
    ATTACHTRANSPORTNAME = 0x370C001F
    ATTACHTRANSPORTNAME_STRING8 = 0x370C001E
    ATTACHMENTCONTACTPHOTO = 0x7FFF000B
    ATTACHMENTFLAGS = 0x7FFD0003
    ATTACHMENTHIDDEN = 0x7FFE000B
    ATTACHMENTLINKID = 0x7FFA0003
    ATTRIBUTEHIDDEN = 0x10F4000B
    ATTRIBUTESYSTEM = 0x10F5000B
    ATTRIBUTEREADONLY = 0x10F6000B
    AUTOFORWARDCOMMENT = 0x0004001F
    AUTOFORWARDCOMMENT_STRING8 = 0x0004001E
    AUTOFORWARDED = 0x0005000B
    AUTORESPONSESUPPRESS = 0x3FDF0003
    BIRTHDAY = 0x3A420040
    BLOCKSTATUS = 0x10960003
    BODY = 0x1000001F
    BODYCONTENTID = 0x1015001F
    BODYCONTENTID_STRING8 = 0x1015001E
    BODYCONTENTLOCATION = 0x1014001F
    BODYCONTENTLOCATION_STRING8 = 0x1014001E
    BODYHTML = 0x1013001F
    BODYHTML_STRING8 = 0x1013001E
    BODY_STRING8 = 0x1000001E
    BUSINESS2TELEPHONENUMBER = 0x3A1B001F
    BUSINESS2TELEPHONENUMBER_STRING8 = 0x3A1B001E
    BUSINESS2TELEPHONENUMBERS = 0x3A1B101F
    BUSINESSFAXNUMBER = 0x3A24001F
    BUSINESSFAXNUMBER_STRING8 = 0x3A24001E
    BUSINESSHOMEPAGE = 0x3A51001F
    BUSINESSHOMEPAGE_STRING8 = 0x3A51001E
    BUSINESSTELEPHONENUMBER = 0x3A08001F
    BUSINESSTELEPHONENUMBER_STRING8 = 0x3A08001E
    CALLID = 0x6806001F
    CALLID_STRING8 = 0x6806001E
    CALLBACKTELEPHONENUMBER = 0x3A02001F
    CALLBACKTELEPHONENUMBER_STRING8 = 0x3A02001E
    CARTELEPHONENUMBER = 0x3A1E001F
    CARTELEPHONENUMBER_STRING8 = 0x3A1E001E
    CDORECURRENCEID = 0x10C50040
    CHANGEKEY = 0x65E20102
    CHANGENUMBER = 0x67A40014
    CHILDRENSNAMES = 0x3A58101F
    CLIENTACTIONS = 0x66450102
    CLIENTSUBMITTIME = 0x00390040
    PROVIDERSUBMITTIME = 0x00480040
    CODEPAGEID = 0x66C30003
    COMMENT = 0x3004001F
    COMMENT_STRING8 = 0x3004001E
    COMPANYMAINTELEPHONENUMBER = 0x3A57001F
    COMPANYMAINTELEPHONENUMBER_STRING8 = 0x3A57001E
    COMPANYNAME = 0x3A16001F
    COMPANYNAME_STRING8 = 0x3A16001E
    COMPUTERNETWORKNAME = 0x3A49001F
    COMPUTERNETWORKNAME_STRING8 = 0x3A49001E
    CONFLICTENTRYID = 0x3FF00102
    CONTAINERCLASS = 0x3613001F
    CONTAINERCLASS_STRING8 = 0x3613001E
    CONTAINERCONTENTS = 0x360F000D
    CONTAINERFLAGS = 0x36000003
    CONTAINERHIERARCHY = 0x360E000D
    CONTENTCOUNT = 0x36020003
    CONTENTFILTERSPAMCONFIDENCELEVEL = 0x40760003
    CONTENTUNREADCOUNT = 0x36030003
    CONVERSATIONID = 0x30130102
    CONVERSATIONINDEX = 0x00710102
    CONVERSATIONINDEXTRACKING = 0x3016000B
    CONVERSATIONTOPIC = 0x0070001F
    CONVERSATIONTOPIC_STRING8 = 0x0070001E
    COUNTRY = 0x3A26001F
    COUNTRY_STRING8 = 0x3A26001E
    CREATIONTIME = 0x30070040
    CREATORENTRYID = 0x3FF90102
    CREATORNAME = 0x3FF8001F
    CREATORNAME_STRING8 = 0x3FF8001E
    CUSTOMERID = 0x3A4A001F
    CUSTOMERID_STRING8 = 0x3A4A001E
    DAMBACKPATCHED = 0x6647000B
    DAMORIGINALENTRYID = 0x66460102
    DEFAULTPOSTMESSAGECLASS = 0x36E5001F
    DEFAULTPOSTMESSAGECLASS_STRING8 = 0x36E5001E
    DEFERREDACTIONMESSAGEORIGINALENTRYID = 0x674100FB
    RULEFOLDERFID = 0x67420014
    DEFERREDDELIVERYTIME = 0x000F0040
    DEFERREDSENDNUMBER = 0x3FEB0003
    DEFERREDSENDTIME = 0x3FEF0040
    DEFERREDSENDUNITS = 0x3FEC0003
    DELEGATEFLAGS = 0x686B1003
    DELEGATEDBYRULE = 0x3FE3000B
    DELETEAFTERSUBMIT = 0x0E01000B
    SENTMAILENTRYID = 0x0E0A0102
    DEFAULTSTORE = 0x3400000B
    DELETEDCOUNTTOTAL = 0x670B0003
    DELETEDFOLDERTOTAL = 0x66410003
    DELETEDON = 0x668F0040
    DELIVERTIME = 0x00100040
    DEPARTMENTNAME = 0x3A18001F
    DEPARTMENTNAME_STRING8 = 0x3A18001E
    DEPTH = 0x30050003
    DISPLAYBCC = 0x0E02001F
    DISPLAYBCC_STRING8 = 0x0E02001E
    DISPLAYCC = 0x0E03001F
    DISPLAYCC_STRING8 = 0x0E03001E
    DISPLAYNAME = 0x3001001F
    DISPLAYNAMEPREFIX = 0x3A45001F
    DISPLAYNAMEPREFIX_STRING8 = 0x3A45001E
    DISPLAYNAME_STRING8 = 0x3001001E
    DISPLAYTO = 0x0E04001F
    DISPLAYTO_STRING8 = 0x0E04001E
    DISPLAYTYPE = 0x39000003
    DISPLAYTYPEEX = 0x39050003
    EMAILADDRESS = 0x3003001F
    EMAILADDRESS_STRING8 = 0x3003001E
    ENDDATE = 0x00610040
    ENTRYID = 0x0FFF0102
    EXCEPTIONENDTIME = 0x7FFC0040
    EXCEPTIONREPLACETIME = 0x7FF90040
    EXCEPTIONSTARTTIME = 0x7FFB0040
    EXCHANGENTSECURITYDESCRIPTOR = 0x0E840102
    EXPIRYNUMBER = 0x3FED0003
    EXPIRYTIME = 0x00150040
    EXPIRYUNITS = 0x3FEE0003
    EXTENDEDFOLDERFLAGS = 0x36DA0102
    EXTENDEDRULEMESSAGEACTIONS = 0x0E990102
    EXTENDEDRULEMESSAGECONDITION = 0x0E9A0102
    EXTENDEDRULESIZELIMIT = 0x0E9B0003
    FAXNUMBEROFPAGES = 0x68040003
    FLAGCOMPLETETIME = 0x10910040
    FLAGSTATUS = 0x10900003
    FLATURLNAME = 0x670E001F
    FLATURLNAME_STRING8 = 0x670E001E
    FOLDERASSOCIATEDCONTENTS = 0x3610000D
    FOLDERID = 0x67480014
    FOLDERTYPE = 0x36010003
    FOLLOWUPICON = 0x10950003
    FREEBUSYCOUNTMONTHS = 0x68690003
    FREEBUSYENTRYIDS = 0x36E41102
    FREEBUSYMESSAGEEMAILADDRESS = 0x6849001F
    FREEBUSYMESSAGEEMAILADDRESS_STRING8 = 0x6849001E
    FREEBUSYPUBLISHEND = 0x68480003
    FREEBUSYPUBLISHSTART = 0x68470003
    FREEBUSYRANGETIMESTAMP = 0x68680040
    FTPSITE = 0x3A4C001F
    FTPSITE_STRING8 = 0x3A4C001E
    GATEWAYNEEDSTOREFRESH = 0x6846000B
    GENDER = 0x3A4D0002
    GENERATION = 0x3A05001F
    GENERATION_STRING8 = 0x3A05001E
    GIVENNAME = 0x3A06001F
    GIVENNAME_STRING8 = 0x3A06001E
    GOVERNMENTIDNUMBER = 0x3A07001F
    GOVERNMENTIDNUMBER_STRING8 = 0x3A07001E
    HASATTACHMENTS = 0x0E1B000B
    HASDEFERREDACTIONMESSAGES = 0x3FEA000B
    HASNAMEDPROPERTIES = 0x664A000B
    HASRULES = 0x663A000B
    HIERARCHYCHANGENUMBER = 0x663E0003
    HOBBIES = 0x3A43001F
    HOBBIES_STRING8 = 0x3A43001E
    HOME2TELEPHONENUMBER = 0x3A2F001F
    HOME2TELEPHONENUMBER_STRING8 = 0x3A2F001E
    HOME2TELEPHONENUMBERS = 0x3A2F101F
    HOMEADDRESSCITY = 0x3A59001F
    HOMEADDRESSCITY_STRING8 = 0x3A59001E
    HOMEADDRESSCOUNTRY = 0x3A5A001F
    HOMEADDRESSCOUNTRY_STRING8 = 0x3A5A001E
    HOMEADDRESSPOSTOFFICEBOX = 0x3A5E001F
    HOMEADDRESSPOSTOFFICEBOX_STRING8 = 0x3A5E001E
    HOMEADDRESSPOSTALCODE = 0x3A5B001F
    HOMEADDRESSPOSTALCODE_STRING8 = 0x3A5B001E
    HOMEADDRESSSTATEORPROVINCE = 0x3A5C001F
    HOMEADDRESSSTATEORPROVINCE_STRING8 = 0x3A5C001E
    HOMEADDRESSSTREET = 0x3A5D001F
    HOMEADDRESSSTREET_STRING8 = 0x3A5D001E
    HOMEFAXNUMBER = 0x3A25001F
    HOMEFAXNUMBER_STRING8 = 0x3A25001E
    HOMETELEPHONENUMBER = 0x3A09001F
    HOMETELEPHONENUMBER_STRING8 = 0x3A09001E
    HTML = 0x10130102
    ICALENDARENDTIME = 0x10C40040
    ICALENDARREMINDERNEXTTIME = 0x10CA0040
    ICALENDARSTARTTIME = 0x10C30040
    ICONINDEX = 0x10800003
    IMPORTANCE = 0x00170003
    INCONFLICT = 0x666C000B
    INREPLYTOID = 0x1042001F
    INREPLYTOID_STRING8 = 0x1042001E
    INITIALDETAILSPANE = 0x3F080003
    INITIALS = 0x3A0A001F
    INITIALS_STRING8 = 0x3A0A001E
    INSTID = 0x674D0014
    INSTANCEKEY = 0x0FF60102
    INSTANCESVREID = 0x0FF600FB
    INSTANCENUM = 0x674E0003
    INTERNETCODEPAGE = 0x3FDE0003
    INTERNETMAILOVERRIDEFORMAT = 0x59020003
    INTERNETMESSAGEID = 0x1035001F
    INTERNETMESSAGEID_STRING8 = 0x1035001E
    INTERNETREFERENCES = 0x1039001F
    INTERNETREFERENCES_STRING8 = 0x1039001E
    IPMAPPOINTMENTENTRYID = 0x36D00102
    IPMCONTACTENTRYID = 0x36D10102
    IPMDRAFTSENTRYID = 0x36D70102
    IPMJOURNALENTRYID = 0x36D20102
    IPMNOTEENTRYID = 0x36D30102
    IPMTASKENTRYID = 0x36D40102
    ISDNNUMBER = 0x3A2D001F
    ISDNNUMBER_STRING8 = 0x3A2D001E
    JUNKADDRECIPIENTSTOSAFESENDERSLIST = 0x61030003
    JUNKINCLUDECONTACTS = 0x61000003
    JUNKPERMANENTLYDELETE = 0x61020003
    JUNKPHISHINGENABLELINKS = 0x6107000B
    JUNKTHRESHOLD = 0x61010003
    KEYWORD = 0x3A0B001F
    KEYWORD_STRING8 = 0x3A0B001E
    LANGUAGE = 0x3A0C001F
    LANGUAGE_STRING8 = 0x3A0C001E
    LASTMODIFICATIONTIME = 0x30080040
    LASTMODIFIERENTRYID = 0x3FFB0102
    LASTMODIFIERNAME = 0x3FFA001F
    LASTMODIFIERNAME_STRING8 = 0x3FFA001E
    LASTVERBEXECUTED = 0x10810003
    LASTVERBEXECUTIONTIME = 0x10820040
    LISTHELP = 0x1043001F
    LISTHELP_STRING8 = 0x1043001E
    LISTSUBSCRIBE = 0x1044001F
    LISTSUBSCRIBE_STRING8 = 0x1044001E
    LISTUNSUBSCRIBE = 0x1045001F
    LISTUNSUBSCRIBE_STRING8 = 0x1045001E
    LOCALCOMMITTIME = 0x67090040
    LOCALCOMMITTIMEMAX = 0x670A0040
    LOCALEID = 0x66A10003
    LOCALITY = 0x3A27001F
    LOCALITY_STRING8 = 0x3A27001E
    LOCATION = 0x3A0D001F
    LOCATION_STRING8 = 0x3A0D001E
    MAILBOXOWNERENTRYID = 0x661B0102
    MAILBOXOWNERNAME = 0x661C001F
    MAILBOXOWNERNAME_STRING8 = 0x661C001E
    MANAGERNAME = 0x3A4E001F
    MANAGERNAME_STRING8 = 0x3A4E001E
    MAPPINGSIGNATURE = 0x0FF80102
    MAXIMUMSUBMITMESSAGESIZE = 0x666D0003
    MEMBERID = 0x66710014
    MEMBERNAME = 0x6672001F
    MEMBERNAME_STRING8 = 0x6672001E
    MEMBERRIGHTS = 0x66730003
    MESSAGEATTACHMENTS = 0x0E13000D
    MESSAGECCME = 0x0058000B
    MESSAGECLASS = 0x001A001F
    MESSAGECLASS_STRING8 = 0x001A001E
    MESSAGECODEPAGE = 0x3FFD0003
    MESSAGEDELIVERYTIME = 0x0E060040
    MESSAGEEDITORFORMAT = 0x59090003
    MESSAGEFLAGS = 0x0E070003
    ITEMTEMPORARYFLAGS = 0x10970003
    MESSAGEHANDLINGSYSTEMCOMMONNAME = 0x3A0F001F
    MESSAGEHANDLINGSYSTEMCOMMONNAME_STRING8 = 0x3A0F001E
    MESSAGELOCALEID = 0x3FF10003
    MESSAGERECIPIENTME = 0x0059000B
    MESSAGERECIPIENTS = 0x0E12000D
    MESSAGESIZE = 0x0E080003
    NORMALMESSAGESIZE = 0x66B30003
    NORMALMESSAGESIZEEXTENDED = 0x66B30014
    ASSOCMESSAGESIZE = 0x66B40003
    ASSOCMESSAGESIZEEXTENDED = 0x66B40014
    MESSAGESIZEEXTENDED = 0x0E080014
    MESSAGESTATUS = 0x0E170003
    MESSAGESUBMISSIONID = 0x00470102
    MESSAGETOME = 0x0057000B
    MID = 0x674A0014
    MIDDLENAME = 0x3A44001F
    MIDDLENAME_STRING8 = 0x3A44001E
    MIMESKELETON = 0x64F00102
    MOBILETELEPHONENUMBER = 0x3A1C001F
    MOBILETELEPHONENUMBER_STRING8 = 0x3A1C001E
    NATIVEBODY = 0x10160003
    NEXTSENDACCT = 0x0E29001F
    NEXTSENDACCT_STRING8 = 0x0E29001E
    NICKNAME = 0x3A4F001F
    NICKNAME_STRING8 = 0x3A4F001E
    NONDELIVERYREPORTDIAGCODE = 0x0C050003
    NONDELIVERYREPORTREASONCODE = 0x0C040003
    NONDELIVERYREPORTSTATUSCODE = 0x0C200003
    NORMALIZEDSUBJECT = 0x0E1D001F
    NORMALIZEDSUBJECT_STRING8 = 0x0E1D001E
    OBJECTTYPE = 0x0FFE0003
    OFFICELOCATION = 0x3A19001F
    OFFICELOCATION_STRING8 = 0x3A19001E
    OFFLINEADDRESSBOOKCONTAINERGUID = 0x6802001E
    OFFLINEADDRESSBOOKDISTINGUISHEDNAME = 0x6804001E
    OFFLINEADDRESSBOOKMESSAGECLASS = 0x68030003
    OFFLINEADDRESSBOOKNAME = 0x6800001F
    OFFLINEADDRESSBOOKNAME_STRING8 = 0x6800001E
    OFFLINEADDRESSBOOKSEQUENCE = 0x68010003
    OFFLINEADDRESSBOOKTRUNCATEDPROPERTIES = 0x68051003
    ORDINALMOST = 0x36E20003
    ORGANIZATIONALIDNUMBER = 0x3A10001F
    ORGANIZATIONALIDNUMBER_STRING8 = 0x3A10001E
    ORIGINALAUTHORENTRYID = 0x004C0102
    ORIGINALAUTHORNAME = 0x004D001F
    ORIGINALAUTHORNAME_STRING8 = 0x004D001E
    ORIGINALDELIVERYTIME = 0x00550040
    ORIGINALDISPLAYBCC = 0x0072001F
    ORIGINALDISPLAYBCC_STRING8 = 0x0072001E
    ORIGINALDISPLAYCC = 0x0073001F
    ORIGINALDISPLAYCC_STRING8 = 0x0073001E
    ORIGINALDISPLAYTO = 0x0074001F
    ORIGINALDISPLAYTO_STRING8 = 0x0074001E
    ORIGINALENTRYID = 0x3A120102
    ORIGINALMESSAGECLASS = 0x004B001F
    ORIGINALMESSAGECLASS_STRING8 = 0x004B001E
    ORIGINALMESSAGEID = 0x1046001F
    ORIGINALMESSAGEID_STRING8 = 0x1046001E
    ORIGINALSENDERADDRESSTYPE = 0x0066001F
    ORIGINALSENDERADDRESSTYPE_STRING8 = 0x0066001E
    ORIGINALSENDEREMAILADDRESS = 0x0067001F
    ORIGINALSENDEREMAILADDRESS_STRING8 = 0x0067001E
    ORIGINALSENDERENTRYID = 0x005B0102
    ORIGINALSENDERNAME = 0x005A001F
    ORIGINALSENDERNAME_STRING8 = 0x005A001E
    ORIGINALSENDERSEARCHKEY = 0x005C0102
    ORIGINALSENSITIVITY = 0x002E0003
    ORIGINALSENTREPRESENTINGADDRESSTYPE = 0x0068001F
    ORIGINALSENTREPRESENTINGADDRESSTYPE_STRING8 = 0x0068001E
    ORIGINALSENTREPRESENTINGEMAILADDRESS = 0x0069001F
    ORIGINALSENTREPRESENTINGEMAILADDRESS_STRING8 = 0x0069001E
    ORIGINALSENTREPRESENTINGENTRYID = 0x005E0102
    ORIGINALSENTREPRESENTINGNAME = 0x005D001F
    ORIGINALSENTREPRESENTINGNAME_STRING8 = 0x005D001E
    ORIGINALSENTREPRESENTINGSEARCHKEY = 0x005F0102
    ORIGINALSUBJECT = 0x0049001F
    ORIGINALSUBJECT_STRING8 = 0x0049001E
    ORIGINALSUBMITTIME = 0x004E0040
    ORIGINATORDELIVERYREPORTREQUESTED = 0x0023000B
    ORIGINATORNONDELIVERYREPORTREQUESTED = 0x0C08000B
    OSCSYNCENABLED = 0x7C24000B
    OTHERADDRESSCITY = 0x3A5F001F
    OTHERADDRESSCITY_STRING8 = 0x3A5F001E
    OTHERADDRESSCOUNTRY = 0x3A60001F
    OTHERADDRESSCOUNTRY_STRING8 = 0x3A60001E
    OTHERADDRESSPOSTOFFICEBOX = 0x3A64001F
    OTHERADDRESSPOSTOFFICEBOX_STRING8 = 0x3A64001E
    OTHERADDRESSPOSTALCODE = 0x3A61001F
    OTHERADDRESSPOSTALCODE_STRING8 = 0x3A61001E
    OTHERADDRESSSTATEORPROVINCE = 0x3A62001F
    OTHERADDRESSSTATEORPROVINCE_STRING8 = 0x3A62001E
    OTHERADDRESSSTREET = 0x3A63001F
    OTHERADDRESSSTREET_STRING8 = 0x3A63001E
    OTHERTELEPHONENUMBER = 0x3A1F001F
    OTHERTELEPHONENUMBER_STRING8 = 0x3A1F001E
    OUTOFOFFICESTATE = 0x661D000B
    OWNERAPPOINTMENTID = 0x00620003
    PAGERTELEPHONENUMBER = 0x3A21001F
    PAGERTELEPHONENUMBER_STRING8 = 0x3A21001E
    PARENTENTRYID = 0x0E090102
    PARENTSVREID = 0x0E0900FB
    PARENTFOLDERID = 0x67490014
    PARENTKEY = 0x00250102
    PARENTSOURCEKEY = 0x65E10102
    PERSONALHOMEPAGE = 0x3A50001F
    PERSONALHOMEPAGE_STRING8 = 0x3A50001E
    POLICYTAG = 0x30190102
    POSTOFFICEBOX = 0x3A2B001F
    POSTOFFICEBOX_STRING8 = 0x3A2B001E
    POSTALADDRESS = 0x3A15001F
    POSTALADDRESS_STRING8 = 0x3A15001E
    POSTALCODE = 0x3A2A001F
    POSTALCODE_STRING8 = 0x3A2A001E
    PREDECESSORCHANGELIST = 0x65E30102
    PRIMARYFAXNUMBER = 0x3A23001F
    PRIMARYFAXNUMBER_STRING8 = 0x3A23001E
    PRIMARYSENDACCOUNT = 0x0E28001F
    PRIMARYSENDACCOUNT_STRING8 = 0x0E28001E
    PRIMARYTELEPHONENUMBER = 0x3A1A001F
    PRIMARYTELEPHONENUMBER_STRING8 = 0x3A1A001E
    PRIORITY = 0x00260003
    PROCESSED = 0x7D01000B
    PROFESSION = 0x3A46001F
    PROFESSION_STRING8 = 0x3A46001E
    PROHIBITRECEIVEQUOTA = 0x666A0003
    PROHIBITSENDQUOTA = 0x666E0003
    PROVIDERDISPLAY = 0x3006001F
    PROVIDERDISPLAY_STRING8 = 0x3006001E
    PROVIDERUID = 0x300C0102
    PURPORTEDSENDERDOMAIN = 0x4083001F
    PURPORTEDSENDERDOMAIN_STRING8 = 0x4083001E
    RADIOTELEPHONENUMBER = 0x3A1D001F
    RADIOTELEPHONENUMBER_STRING8 = 0x3A1D001E
    READ = 0x0E69000B
    READRECEIPTADDRESSTYPE = 0x4029001F
    READRECEIPTADDRESSTYPE_STRING8 = 0x4029001E
    READRECEIPTEMAILADDRESS = 0x402A001F
    READRECEIPTEMAILADDRESS_STRING8 = 0x402A001E
    READRECEIPTENTRYID = 0x00460102
    READRECEIPTNAME = 0x402B001F
    READRECEIPTNAME_STRING8 = 0x402B001E
    READRECEIPTREQUESTED = 0x0029000B
    READRECEIPTSEARCHKEY = 0x00530102
    READRECEIPTSMTPADDRESS = 0x5D05001F
    READRECEIPTSMTPADDRESS_STRING8 = 0x5D05001E
    RECEIPTTIME = 0x002A0040
    RECEIVEDBYADDRESSTYPE = 0x0075001F
    RECEIVEDBYADDRESSTYPE_STRING8 = 0x0075001E
    RECEIVEDBYEMAILADDRESS = 0x0076001F
    RECEIVEDBYEMAILADDRESS_STRING8 = 0x0076001E
    RECEIVEDBYENTRYID = 0x003F0102
    RECEIVEDBYNAME = 0x0040001F
    RECEIVEDBYNAME_STRING8 = 0x0040001E
    RECEIVEDBYSEARCHKEY = 0x00510102
    RECEIVEDBYSMTPADDRESS = 0x5D07001F
    RECEIVEDBYSMTPADDRESS_STRING8 = 0x5D07001E
    RECEIVEDREPRESENTINGADDRESSTYPE = 0x0077001F
    RECEIVEDREPRESENTINGADDRESSTYPE_STRING8 = 0x0077001E
    RECEIVEDREPRESENTINGEMAILADDRESS = 0x0078001F
    RECEIVEDREPRESENTINGEMAILADDRESS_STRING8 = 0x0078001E
    RECEIVEDREPRESENTINGENTRYID = 0x00430102
    RECEIVEDREPRESENTINGNAME = 0x0044001F
    RECEIVEDREPRESENTINGNAME_STRING8 = 0x0044001E
    RECEIVEDREPRESENTINGSEARCHKEY = 0x00520102
    RECEIVEDREPRESENTINGSMTPADDRESS = 0x5D08001F
    RECEIVEDREPRESENTINGSMTPADDRESS_STRING8 = 0x5D08001E
    RECIPIENTDISPLAYNAME = 0x5FF6001F
    RECIPIENTDISPLAYNAME_STRING8 = 0x5FF6001E
    RECIPIENTENTRYID = 0x5FF70102
    RECIPIENTFLAGS = 0x5FFD0003
    RECIPIENTORDER = 0x5FDF0003
    RECIPIENTPROPOSED = 0x5FE1000B
    RECIPIENTPROPOSEDENDTIME = 0x5FE40040
    RECIPIENTPROPOSEDSTARTTIME = 0x5FE30040
    RECIPIENTREASSIGNMENTPROHIBITED = 0x002B000B
    RECIPIENTTRACKSTATUS = 0x5FFF0003
    RECIPIENTTRACKSTATUSTIME = 0x5FFB0040
    RECIPIENTTYPE = 0x0C150003
    RECORDKEY = 0x0FF90102
    REFERREDBYNAME = 0x3A47001F
    REFERREDBYNAME_STRING8 = 0x3A47001E
    REMINDERSONLINEENTRYID = 0x36D50102
    REMOTEMESSAGETRANSFERAGENT = 0x0C21001F
    REMOTEMESSAGETRANSFERAGENT_STRING8 = 0x0C21001E
    RENDERINGPOSITION = 0x370B0003
    REPLYRECIPIENTENTRIES = 0x004F0102
    REPLYRECIPIENTNAMES = 0x0050001F
    REPLYRECIPIENTNAMES_STRING8 = 0x0050001E
    REPLYREQUESTED = 0x0C17000B
    REPLYTEMPLATEID = 0x65C20102
    REPLYTIME = 0x00300040
    REPORTDISPOSITION = 0x0080001F
    REPORTDISPOSITIONMODE = 0x0081001F
    REPORTDISPOSITIONMODE_STRING8 = 0x0081001E
    REPORTDISPOSITION_STRING8 = 0x0080001E
    REPORTENTRYID = 0x00450102
    REPORTNAME = 0x003A001F
    REPORTNAME_STRING8 = 0x003A001E
    REPORTSEARCHKEY = 0x00540102
    REPORTTAG = 0x00310102
    REPORTTEXT = 0x1001001F
    REPORTTEXT_STRING8 = 0x1001001E
    REPORTTIME = 0x00320040
    REPORTINGMESSAGETRANSFERAGENT = 0x6820001F
    REPORTINGMESSAGETRANSFERAGENT_STRING8 = 0x6820001E
    RESOLVEMETHOD = 0x3FE70003
    RESOURCEFLAGS = 0x30090003
    RESOURCETYPE = 0x3E030003
    RESPONSEREQUESTED = 0x0063000B
    RESPONSIBILITY = 0x0E0F000B
    RETENTIONDATE = 0x301C0040
    RETENTIONFLAGS = 0x301D0003
    RETENTIONPERIOD = 0x301A0003
    RIGHTS = 0x66390003
    ROAMINGDATATYPES = 0x7C060003
    ROAMINGDICTIONARY = 0x7C070102
    ROAMINGXMLSTREAM = 0x7C080102
    ROWTYPE = 0x0FF50003
    ROWID = 0x30000003
    RTFCOMPRESSED = 0x10090102
    RTFINSYNC = 0x0E1F000B
    RULEACTIONNUMBER = 0x66500003
    RULEACTIONTYPE = 0x66490003
    RULEACTIONS = 0x668000FE
    RULECONDITION = 0x667900FD
    RULEERROR = 0x66480003
    RULEFOLDERENTRYID = 0x66510102
    RULEID = 0x66740014
    RULEIDS = 0x66750102
    RULELEVEL = 0x66830003
    RULEMESSAGELEVEL = 0x65ED0003
    RULEMESSAGENAME = 0x65EC001F
    RULEMESSAGENAME_STRING8 = 0x65EC001E
    RULEMESSAGEPROVIDER = 0x65EB001F
    RULEMESSAGEPROVIDERDATA = 0x65EE0102
    RULEMESSAGEPROVIDER_STRING8 = 0x65EB001E
    RULEMESSAGESEQUENCE = 0x65F30003
    RULEMESSAGESTATE = 0x65E90003
    RULEMESSAGEUSERFLAGS = 0x65EA0003
    RULENAME = 0x6682001F
    RULENAME_STRING8 = 0x6682001E
    RULEPROVIDER = 0x6681001F
    RULEPROVIDERDATA = 0x66840102
    RULEPROVIDER_STRING8 = 0x6681001E
    RULESEQUENCE = 0x66760003
    RULESTATE = 0x66770003
    RULEUSERFLAGS = 0x66780003
    RWRULESSTREAM = 0x68020102
    SCHEDULEINFOAPPOINTMENTTOMBSTONE = 0x686A0102
    SCHEDULEINFOAUTOACCEPTAPPOINTMENTS = 0x686D000B
    SCHEDULEINFODELEGATEENTRYIDS = 0x68451102
    SCHEDULEINFODELEGATENAMES = 0x6844101F
    SCHEDULEINFODELEGATENAMESW = 0x684A101F
    SCHEDULEINFODELEGATORWANTSCOPY = 0x6842000B
    SCHEDULEINFODELEGATORWANTSINFO = 0x684B000B
    SCHEDULEINFODISALLOWOVERLAPPINGAPPTS = 0x686F000B
    SCHEDULEINFODISALLOWRECURRINGAPPTS = 0x686E000B
    SCHEDULEINFODONTMAILDELEGATES = 0x6843000B
    SCHEDULEINFOFREEBUSY = 0x686C0102
    SCHEDULEINFOFREEBUSYAWAY = 0x68561102
    SCHEDULEINFOFREEBUSYBUSY = 0x68541102
    SCHEDULEINFOFREEBUSYMERGED = 0x68501102
    SCHEDULEINFOFREEBUSYTENTATIVE = 0x68521102
    SCHEDULEINFOMONTHSAWAY = 0x68551003
    SCHEDULEINFOMONTHSBUSY = 0x68531003
    SCHEDULEINFOMONTHSMERGED = 0x684F1003
    SCHEDULEINFOMONTHSTENTATIVE = 0x68511003
    SCHEDULEINFORESOURCETYPE = 0x68410003
    SCHEDULEPLUSFREEBUSYENTRYID = 0x66220102
    SCRIPTDATA = 0x00040102
    SEARCHFOLDERDEFINITION = 0x68450102
    SEARCHFOLDEREXPIRATION = 0x683A0003
    SEARCHFOLDERID = 0x68420102
    SEARCHFOLDERLASTUSED = 0x68340003
    SEARCHFOLDERRECREATEINFO = 0x68440102
    SEARCHFOLDERSTORAGETYPE = 0x68460003
    SEARCHKEY = 0x300B0102
    SECURITYDESCRIPTORASXML = 0x0E6A001F
    SECURITYDESCRIPTORASXML_STRING8 = 0x0E6A001E
    SELECTABLE = 0x3609000B
    SENDINTERNETENCODING = 0x3A710003
    SENDRICHINFO = 0x3A40000B
    SENDERADDRESSTYPE = 0x0C1E001F
    SENDERADDRESSTYPE_STRING8 = 0x0C1E001E
    SENDEREMAILADDRESS = 0x0C1F001F
    SENDEREMAILADDRESS_STRING8 = 0x0C1F001E
    SENDERENTRYID = 0x0C190102
    SENDERIDSTATUS = 0x40790003
    SENDERNAME = 0x0C1A001F
    SENDERNAME_STRING8 = 0x0C1A001E
    SENDERSEARCHKEY = 0x0C1D0102
    SENDERSMTPADDRESS = 0x5D01001F
    SENDERSMTPADDRESS_STRING8 = 0x5D01001E
    SENDERTELEPHONENUMBER = 0x6802001F
    SENDERTELEPHONENUMBER_STRING8 = 0x6802001E
    SENSITIVITY = 0x00360003
    SENTMAILSVREID = 0x674000FB
    SENTREPRESENTINGADDRESSTYPE = 0x0064001F
    SENTREPRESENTINGADDRESSTYPE_STRING8 = 0x0064001E
    SENTREPRESENTINGEMAILADDRESS = 0x0065001F
    SENTREPRESENTINGEMAILADDRESS_STRING8 = 0x0065001E
    SENTREPRESENTINGENTRYID = 0x00410102
    SENTREPRESENTINGFLAGS = 0x401A0003
    SENTREPRESENTINGNAME = 0x0042001F
    SENTREPRESENTINGNAME_STRING8 = 0x0042001E
    SENTREPRESENTINGSEARCHKEY = 0x003B0102
    SENTREPRESENTINGSMTPADDRESS = 0x5D02001F
    SENTREPRESENTINGSMTPADDRESS_STRING8 = 0x5D02001E
    SMTPADDRESS = 0x39FE001F
    SMTPADDRESS_STRING8 = 0x39FE001E
    SORTLOCALEID = 0x67050003
    SOURCEKEY = 0x65E00102
    SPOKENNAME = 0x8CC20102
    SPOUSENAME = 0x3A48001F
    SPOUSENAME_STRING8 = 0x3A48001E
    STARTDATE = 0x00600040
    STARTDATEETC = 0x301B0102
    STATEORPROVINCE = 0x3A28001F
    STATEORPROVINCE_STRING8 = 0x3A28001E
    STOREENTRYID = 0x0FFB0102
    STOREPROVIDER = 0x34140102
    STORERECORDKEY = 0x0FFA0102
    STORESTATE = 0x340E0003
    STORESUPPORTMASK = 0x340D0003
    STREETADDRESS = 0x3A29001F
    STREETADDRESS_STRING8 = 0x3A29001E
    SUBFOLDERS = 0x360A000B
    SUBJECT = 0x0037001F
    SUBJECTPREFIX = 0x003D001F
    SUBJECTPREFIX_STRING8 = 0x003D001E
    SUBJECT_STRING8 = 0x0037001E
    SUPPLEMENTARYINFO = 0x0C1B001F
    SUPPLEMENTARYINFO_STRING8 = 0x0C1B001E
    SURNAME = 0x3A11001F
    SURNAME_STRING8 = 0x3A11001E
    SWAPPEDTODODATA = 0x0E2D0102
    SWAPPEDTODOSTORE = 0x0E2C0102
    TARGETENTRYID = 0x30100102
    TELECOMMUNICATIONSDEVICEFORDEAFTELEPHONENUMBER = 0x3A4B001F
    TELECOMMUNICATIONSDEVICEFORDEAFTELEPHONENUMBER_STRING8 = 0x3A4B001E
    TELEXNUMBER = 0x3A2C001F
    TELEXNUMBER_STRING8 = 0x3A2C001E
    TEMPLATEDATA = 0x00010102
    TEMPLATEID = 0x39020102
    TEXTATTACHMENTCHARSET = 0x371B001F
    TEXTATTACHMENTCHARSET_STRING8 = 0x371B001E
    THUMBNAILPHOTO = 0x8C9E0102
    TITLE = 0x3A17001F
    TITLE_STRING8 = 0x3A17001E
    TNEFCORRELATIONKEY = 0x007F0102
    TODOITEMFLAGS = 0x0E2B0003
    TRANSMITTABLEDISPLAYNAME = 0x3A20001F
    TRANSMITTABLEDISPLAYNAME_STRING8 = 0x3A20001E
    TRANSPORTMESSAGEHEADERS = 0x007D001F
    TRANSPORTMESSAGEHEADERS_STRING8 = 0x007D001E
    TRUSTSENDER = 0x0E790003
    USERCERTIFICATE = 0x3A220102
    USERENTRYID = 0x66190102
    USERX509CERTIFICATE = 0x3A701102
    VIEWDESCRIPTORBINARY = 0x70010102
    VIEWDESCRIPTORNAME = 0x7006001F
    VIEWDESCRIPTORNAME_STRING8 = 0x7006001E
    VIEWDESCRIPTORSTRINGS = 0x7002001F
    VIEWDESCRIPTORSTRINGS_STRING8 = 0x7002001E
    VIEWDESCRIPTORVERSION = 0x70070003
    VOICEMESSAGEATTACHMENTORDER = 0x6805001F
    VOICEMESSAGEATTACHMENTORDER_STRING8 = 0x6805001E
    VOICEMESSAGESENDERNAME = 0x6803001F
    VOICEMESSAGESENDERNAME_STRING8 = 0x6803001E
    VOICEMESSAGEDURATION = 0x68010003
    WEDDINGANNIVERSARY = 0x3A410040
    WLINKADDRESSBOOKEID = 0x68540102
    WLINKADDRESSBOOKSTOREEID = 0x68910102
    WLINKCALENDARCOLOR = 0x68530003
    WLINKCLIENTID = 0x68900102
    WLINKENTRYID = 0x684C0102
    WLINKFLAGS = 0x684A0003
    WLINKFOLDERTYPE = 0x684F0102
    WLINKGROUPCLSID = 0x68500102
    WLINKGROUPHEADERID = 0x68420048
    WLINKGROUPNAME = 0x6851001F
    WLINKORDINAL = 0x684B0102
    WLINKROGROUPTYPE = 0x68920003
    WLINKRECORDKEY = 0x684D0102
    WLINKSECTION = 0x68520003
    WLINKSTOREENTRYID = 0x684E0102
    WLINKTYPE = 0x68490003
    ASSOCIATEDCONTENTCOUNT = 0x36170003
    FOLDERCHILDCOUNT = 0x66380003
    IPMPUBLICFOLDERSENTRYID = 0x66310102
    CONVERSATIONKEY = 0x000B0102
    CONTACTEMAILADDRESSES = 0x3A56101F
    GENERATEEXCHANGEVIEWS = 0x36E9000B
    LATESTDELIVERYTIME = 0x00190040
    MAILPERMISSION = 0x3A0E000B
    FOLDERFLAGS = 0x66A80003
    HIERREV = 0x40820040
    SETGIVEN = 0x40170003
    CNSETSEEN = 0x67960102
    CNSETSEENFAI = 0x67da0102
    CNSETREAD = 0x67d20102
    SETDELETED = 0x67e50102
    SETNOLONGERINSCOPE = 0x40210102
    SETEXPIRED = 0x67930102
    SETREAD = 0x402d0102
    SETUNREAD = 0x402e0102
    NONRECEIPTNOTIFICATIONREQUESTED = 0x0C06000B
    RESERVED = 0xFFFFFFFF
    COMMONVIEWSENTRYID = 0x35E60102
    DELETEDASSOCMESSAGESIZE = 0x669D0003
    DELETEDASSOCMESSAGESIZEEXTENDED = 0x669D0014
    DELETEDASSOCMSGCOUNT = 0x66430003
    DELETEDMESSAGESIZE = 0x669B0003
    DELETEDMESSAGESIZEEXTENDED = 0x669B0014
    DELETEDMSGCOUNT = 0x66400003
    DELETEDNORMALMESSAGESIZE = 0x669C0003
    DELETEDNORMALMESSAGESIZEEXTENDED = 0x669C0014
    FINDERENTRYID = 0x35E70102
    INTERNETARTICLENUMBER = 0x0E230003
    MIDSTRING = 0x0E23001F
    ARTICLENUMBERNEXT = 0x67510003
    IPMDAFENTRYID = 0x661F0102
    IPMFAVORITESENTRYID = 0x66300102
    IPMOUTBOXENTRYID = 0x35E20102
    IPMSENTMAILENTRYID = 0x35E40102
    IPMSUBTREEENTRYID = 0x35E00102
    IPMWASTEBASKETENTRYID = 0x35E30102
    SCHEDULEFOLDERENTRYID = 0x661E0102
    NONIPMSUBTREEENTRYID = 0x66200102
    STORAGEQUOTALIMIT = 0x3FF50003
    STOREOFFLINE = 0x6632000B
    VALIDFOLDERMASK = 0x35DF0003
    VIEWSENTRYID = 0x35E50102
    EFORMSREGISTRYENTRYID = 0x66210102
    OFFLINEADDRBOOKENTRYID = 0x66230102
    HIERARCHYSERVER = 0x6633001E
    REPLICASERVER = 0x6644001E
    FOLDERPATHNAME = 0x66B5001F
    ASSOCMSGATTACHCOUNT = 0x66AE0003
    NORMALMSGATTACHCOUNT = 0x66AD0003
    TESTLINESPEED = 0x662B0102
    PARENTDISPLAY = 0x0E05001F
    PARENTDISPLAY_STRING8 = 0x0E05001E
    CREATORSID = 0x0E580102


class ConfigIDs(_ReverseLookup):
    MAILBOX_GUID = 1
    CURRENT_EID = 2
    MAXIMUM_EID = 3
    LAST_CHANGE_NUMBER = 4
    LAST_ARTICLE_NUMBER = 5
    LAST_CID = 6
    SEARCH_STATE = 7
    DEFAULT_PERMISSION = 8
    ANONYMOUS_PERMISSION = 9


class PublicFIDs(_ReverseLookup):
    ROOT = 0x01
    IPMSUBTREE = 0x02
    NONIPMSUBTREE = 0x03
    EFORMSREGISTRY = 0x04
    CUSTOM = 0x05


class PrivateFIDs(_ReverseLookup):
    ROOT = 0x01
    DEFERRED_ACTION = 0x02
    SPOOLER_QUEUE = 0x03
    SHORTCUTS = 0x04
    FINDER = 0x05
    VIEWS = 0x06
    COMMON_VIEWS = 0x07
    SCHEDULE = 0x08
    IPMSUBTREE = 0x09
    SENT_ITEMS = 0x0a
    DELETED_ITEMS = 0x0b
    OUTBOX = 0x0c
    INBOX = 0x0d
    DRAFT = 0x0e
    CALENDAR = 0x0f
    JOURNAL = 0x10
    NOTES = 0x11
    TASKS = 0x12
    CONTACTS = 0x13
    QUICKCONTACTS = 0x14
    IMCONTACTLIST = 0x15
    GALCONTACTS = 0x16
    JUNK = 0x17
    LOCAL_FREEBUSY = 0x18
    SYNC_ISSUES = 0x19
    CONFLICTS = 0x1a
    LOCAL_FAILURES = 0x1b
    SERVER_FAILURES = 0x1c
    CONVERSATION_ACTION_SETTINGS = 0x1d
    CUSTOM = 0x1e


class Permissions:
    NONE = 0x00000000
    READANY = 0x00000001
    CREATE = 0x00000002
    SENDAS = 0x00000004 #  self defined
    EDITOWNED = 0x00000008
    DELETEOWNED = 0x00000010
    EDITANY = 0x00000020
    DELETEANY = 0x00000040
    CREATESUBFOLDER = 0x00000080
    FOLDEROWNER = 0x00000100
    FOLDERCONTACT = 0x00000200
    FOLDERVISIBLE = 0x00000400
    FREEBUSYSIMPLE = 0x00000800
    FREEBUSYDETAILED = 0x00001000

    @classmethod
    def domainDefault(cls):
        return cls.READANY | cls.CREATE | cls.FOLDERVISIBLE | cls.EDITOWNED | cls.DELETEOWNED

class Misc:
    ALLOCATED_EID_RANGE = 0x10000
    CHANGE_NUMBER_BEGIN = 0x800000000000

class FolderNames:
    IPM = "Top of Information Store"
    INBOX = "Inbox"
    DRAFT = "Drafts"
    OUTBOX = "Outbox"
    SENT = "Sent Items"
    DELETED = "Deleted Items"
    CONTACTS = "Contacts"
    CALENDAR = "Calendar"
    JOURNAL = "Journal"
    NOTES = "Notes"
    TASKS = "Tasks"
    JUNK = "Junk E-mail"
    SYNC = "Sync Issues"
    CONFLICT = "Conflicts"
    LOCAL = "Local Failures"
    SERVER = "Server Failures"
