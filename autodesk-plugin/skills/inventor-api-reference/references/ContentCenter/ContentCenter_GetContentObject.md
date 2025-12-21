# ContentCenter.GetContentObject Method

Parent Object: [ContentCenter](../ContentCenter/ContentCenter.md)

## Description

Property that returns the specified content center object specified by the content identifier. If the object cannot be found then Nothing is returned. This can return a ContentFamily or ContentRow depending on what the identifier represents.

## Syntax

ContentCenter.**GetContentObject**( ***ContentIdentifier*** As String, [***LibraryId***] As String ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ContentIdentifier | String | Input String that was previously obtained using the ContentIdentifier property of a content center object. |
| LibraryId | String | Not currently supported. |

## Version

Introduced in version 2011
