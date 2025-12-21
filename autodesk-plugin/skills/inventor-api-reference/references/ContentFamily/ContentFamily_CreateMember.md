# ContentFamily.CreateMember Method

Parent Object: [ContentFamily](../ContentFamily/ContentFamily.md)

## Description

Method that creates a member part for the specified table row. The full filename of the created member is returned. If the creation fails the FailureReason argument indicates the reason for failure.

## Syntax

ContentFamily.**CreateMember**( ***Row*** As Variant, ***FailureReason*** As [MemberManagerErrorsEnum](../MemberManagerErrorsEnum.md), ***FailureMessage*** As String, [***Refresh***] As [ContentMemberRefreshEnum](../ContentMemberRefreshEnum.md), [***Custom***] As Boolean, [***FileName***] As String, [***CustomInput***] As Variant, [***Options***] As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Row | Variant | Input Variant that specifies which row to use to create the member. The row index can be specified by a Long (row index), a ContentTableRow object, or the internal name of a ContentTableRow object. |
| FailureReason | [MemberManagerErrorsEnum](../MemberManagerErrorsEnum.md) | Output MemberManagerErrorsEnum that indicates the reason for failure, if the creation of the member did fail. |
| FailureMessage | String | Output String that contains a message describing the reason for failure, if the creation of the member did fail. If it didn"t fail this will return an empty String. |
| Refresh | [ContentMemberRefreshEnum](../ContentMemberRefreshEnum.md) | Optional Input ContentMemberRefreshEnum that specifies the behavior to use if the member already exists locally. kUseDefaultRefreshSetting indicates that the method should use whatever the default setting is as set by the user using the "Content Center" tab of the Application options dialog. kRefreshOutOfDateParts indicates that if the part already exists in the local cache and is out of date if it should be replaced with an up to date version of the part. kDoNotRefreshOutOfDateParts indicates that the existing part will be used and not overridden. |
| Custom | Boolean | Optional Input Boolean that indicates if this part should be created as a custom or standard part. A value of True indicates it will be a custom member.   This is an optional argument whose default value is False. |
| FileName | String | Optional Input String that defines the filename of the resulting member. This argument is only used in the case of a custom family (ContentFamily.IsCustom is true) and is ignored for a standard family. In the case of a custom factory the filename must be specified and is not optional.   This is an optional argument whose default value is "". |
| CustomInput | Variant | Optional input NameValueMap that specifies the input to use for the custom input. If the family is custom and this is not supplied, the default values for custom values are used. For each input value you use the NameValueMap to specify the Column ID as the name and the custom value as the new value . If the factory is not a custom factory this argument is ignored.   This is an optional argument whose default value is null. |
| Options | Variant | Optional Input NameValueMap that specifies additional options for this method. This is not currently being used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Place Content Center Parts](../../sample-programs/PlaceContentCenterPart_Sample.md) | Places all of the items in a specified family within an assembly. The specific family is identified by the strings where it's setting the HexHeadNode variable. |

## Version

Introduced in version 2010
