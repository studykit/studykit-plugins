# DrawingNotes.Item Property

Parent Object: [DrawingNotes](../DrawingNotes/DrawingNotes.md)

## Description

Returns the specified DrawingNote object from the collection.

## Remarks

This property returns all of the ChamferNote, BendNote, and PunchNote objects on the sheet. However, HoleThreadNote objects are not returned by this property and must be obtained explicitly by using the HoleThreadNotes collection object.

## Syntax

DrawingNotes.**Item**( ***Index*** As Long ) As [DrawingNote](../DrawingNote/DrawingNote.md)

## Property Value

This is a read only property whose value is a [DrawingNote](../DrawingNote/DrawingNote.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the index of the object to return. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |