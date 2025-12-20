# CommandManager.DoStopPreSelect Method

Parent Object: [CommandManager](../CommandManager/CommandManager.md)

## Description

Method that causes Autodesk Inventor to go through the stop pre-selection protocol, including firing of corresponding event out the active InteractionEvents object if one is active. If a native Autodesk Inventor command is active and is in a selection mode, it gets the stop pre-select notification just like a native stop pre-selection happened. This method is useful when you want to perform picking outside of the graphic window. For example if you have a browser that has icons that represent selectable objects you can cause the selection behavior to happen as the user navigates through your browser and selects objects.

## Syntax

CommandManager.**DoStopPreSelect**( ***Entity*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Input Autodesk Inventor object, including custom graphics object, that needs to be understood as a candidate for selection by the active selection process in progress. This entity may have been picked by a means not known to native Autodesk Inventor (say a foreign browser). |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |