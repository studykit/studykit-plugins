# FileManager.GetFileNameFromIdentifier Method

Parent Object: [FileManager](../FileManager/FileManager.md)

## Description

Property that returns the fully qualified name of a file using its unique identifier. The identifier must have been obtained from the GetIdentifierFromFileName method.

## Syntax

FileManager.**GetFileNameFromIdentifier**( ***Identifier***() As Byte, ***FullFileName*** As String, [***AbsolutePath***] As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Identifier | Byte | The identifier obtained from the GetIdentifierFromFileName method. |
| FullFileName | String | Output String value that specifies the full filename of the file. |
| AbsolutePath | String | String specifying the absolute path to the file. |

## Version

Introduced in version 9
