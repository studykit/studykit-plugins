# CommandManager.PostPrivateEvent Method

Parent Object: [CommandManager](../CommandManager/CommandManager.md)

## Description

Method that posts data onto Autodesk Inventor's internal clipboard. Certain commands that usually obtain information using a dialog, i.e. Open, Save, etc., look first to see if data is on the clipboard before displaying the dialog. If valid information is on the clipboard the command will use it instead of displaying the dialog and asking the user to specify the filename.

## Syntax

CommandManager.**PostPrivateEvent**( ***DataType*** As [PrivateEventTypeEnum](../PrivateEventTypeEnum.md), ***Data*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DataType | [PrivateEventTypeEnum](../PrivateEventTypeEnum.md) | Input constant that specifies the type of value being pushed onto Autodesk Inventor's clipboard. Most often this will be kFileNameEvent. |
| Data | Variant | Input Variant that contains the actual data to push onto Autodesk Inventor's clipboard. When set the DateType as kBooleanEvent, then a NameValueMap object including the data name and value should be provided. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Post Private Event Sample](../../sample-programs/PostPrivateEventSample_Sample.md) | This sample demonstrates how to use the PostPrivateEvent to configure the options for placing a part component. |

## Version

Introduced in version 4
