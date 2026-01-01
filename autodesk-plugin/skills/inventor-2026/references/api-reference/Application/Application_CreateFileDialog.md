# Application.CreateFileDialog Method

Parent Object: [Application](../Application/Application.md)

## Description

Method that creates a new FileDialog object. The FileDialog object is similar to the Microsoft common dialog control and allows you to reuse the Inventor open and save dialogs.

## Syntax

Application.**CreateFileDialog**( ***Dialog*** As [FileDialog](../FileDialog/FileDialog.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Dialog | [FileDialog](../FileDialog/FileDialog.md) | Output FileDialog object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [File Dialog](../../sample-programs/FileDialog_Sample.md) | This sample demonstrates the use of the FileDialog object. The only requirement to run this sample is to have Inventor open. |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |

## Version

Introduced in version 6
