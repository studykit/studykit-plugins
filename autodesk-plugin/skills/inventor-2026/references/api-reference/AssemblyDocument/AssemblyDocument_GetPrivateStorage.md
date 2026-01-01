# AssemblyDocument.GetPrivateStorage Method

Parent Object: [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md)

## Description

Obtains a private sub-storage within this document with the given name. Can create one, if one does not exist.

## Syntax

AssemblyDocument.**GetPrivateStorage**( ***StorageName*** As String, ***CreateIfNecessary*** As Boolean ) As Unknown

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StorageName | String | Input String that specifies the name of the private sub-storage. |
| CreateIfNecessary | Boolean | Input Boolean that specifies whether to create a private sub-storage if one does not already exist. |

## Version

Introduced in version 4
