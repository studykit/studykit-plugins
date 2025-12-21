# ReferencedOLEFileDescriptors.Add Method

Parent Object: [ReferencedOLEFileDescriptors](../ReferencedOLEFileDescriptors/ReferencedOLEFileDescriptors.md)

## Description

Method that creates a new ReferencedOLEFileDescriptor by linking/embedding a file. The newly created ReferencedOLEFileDescriptor is returned.

## Remarks

This method will fail if the specified file does not exist. It will also fail if the reference will result in a cyclical dependency. For example, if Drawing1.idw references Part1.ipt, and then within Part1 you attempt to create a reference back to Drawing1.

## Syntax

ReferencedOLEFileDescriptors.**Add**( ***FullFileName*** As String, [***Type***] As [OLEDocumentTypeEnum](../OLEDocumentTypeEnum.md) ) As [ReferencedOLEFileDescriptor](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String value that specifies the full filename of the file. |
| Type | [OLEDocumentTypeEnum](../OLEDocumentTypeEnum.md) | Constant indicating the OLE document type. |

## Version

Introduced in version 9
