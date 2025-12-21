# DocumentInterests.Add Method

Parent Object: [DocumentInterests](../DocumentInterests/DocumentInterests.md)

## Description

Method that creates a new DocumentInterest.

## Remarks

The new created DocumentInterest is returned. The method fails if a DocumentInterest with the same ClientId already exists. Note: Clients are strongly warned to store as little data as practicably possible, partly to avoid capacity issues, but mainly because this will affect Inventor's ability to open documents quickly in a 'lightweight' background mode.

## Syntax

DocumentInterests.**Add**( ***ClientId*** As String, ***Name*** As String, ***InterestType*** As [DocumentInterestTypeEnum](../DocumentInterestTypeEnum.md), [***DataVersion***] As Long, [***ClientData***] As Variant ) As [DocumentInterest](../DocumentInterest/DocumentInterest.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input String that uniquely identifies a client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| Name | String | Input String that specifies the name associated with this interest. This is typically a string specifying the document 'sub-type'. |
| InterestType | [DocumentInterestTypeEnum](../DocumentInterestTypeEnum.md) | Input DocumentInterestTypeEnum that specifies the type of interest that the client has in this document. Valid inputs are kInterested and kNotInterested. |
| DataVersion | Long | Optional input Long that specifies the current data version of the document. If not specified, this is assumed to be a 'non-migrating' type of interest. When a document is opened, if this DataVersion value is less than the current DataVersion value of the AddIn (ApplicationAddIn.DataVersion), the 'Migrate' command is enabled. When the user invokes the Migrate command, the OnMigrateDocument event is fired and gives the client an opportunity to migrate their data. |
| ClientData | Variant | Optional input String that contains some additional data that the client would like to store with the interest. This string is not interpreted by Inventor. Clients are expected to use the string with extreme economy.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2008
