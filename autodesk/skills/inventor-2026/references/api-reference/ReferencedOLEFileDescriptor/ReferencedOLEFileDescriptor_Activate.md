# ReferencedOLEFileDescriptor.Activate Method

Parent Object: [ReferencedOLEFileDescriptor](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor.md)

## Description

Method that causes the OLE file to be activated by the process currently registered to handle that type of document.

## Syntax

ReferencedOLEFileDescriptor.**Activate**( ***Verb*** As [OLEVerbEnum](../OLEVerbEnum.md), ***OLEDocumentObject*** As Unknown )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Verb | [OLEVerbEnum](../OLEVerbEnum.md) | Input value that specifies how OLE should activate the document. Valid values are\: kDefaultOLEVerb\: Perform the default action. kEditOpenOLEVerb\: Open the document is a separate window for editing. kHideOLEVerb\: Open the document but keep its application hidden. kShowOLEVerb\: Open the document and show the application if it's been hidden. Otherwise this has the same behavior as kEditOpenOLEVerb. |
| OLEDocumentObject | Unknown | Output object that if supported by the opening application is the object just opened. For example if an Excel spreadsheet is referenced and is activated this argument will return the WorkBook object for the file just opened. |

## Version

Introduced in version 4
