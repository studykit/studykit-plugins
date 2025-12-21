# Sheet.Status Property

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Property that returns the current status of the sheet and its contents. If the value is equal to kUpToDateDrawingSheet then the drawing sheet is up to date. Any other value means some portion of the sheet is out of date. The returned value can contain status information about several things about the sheet. You can use bitwise operators to determine the status for a particular item. For example the following can be used to see if the precise display for views on sheet are up to date. If (oSheet.Status And kProcessingPreciseDisplayDrawingSheet) = kProcessingPreciseDisplayDrawingSheet Then MsgBox "Processing precise display." End If This is useful when an operation requires the sheet to be up to date. For example, when plotting the sheet.

## Syntax

Sheet.**Status**() As [DrawingSheetStatusBits](../DrawingSheetStatusBits/DrawingSheetStatusBits.md)

## Property Value

This is a read only property whose value is a [DrawingSheetStatusBits](../DrawingSheetStatusBits/DrawingSheetStatusBits.md).

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |