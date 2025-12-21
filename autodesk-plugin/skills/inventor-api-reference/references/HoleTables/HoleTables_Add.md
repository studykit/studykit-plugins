# HoleTables.Add Method

Parent Object: [HoleTables](../HoleTables/HoleTables.md)

## Description

Method that creates a new hole table by including all holes in the input drawing view. Only those feature types specified in the input (or the default) hole table style will be included. The newly created HoleTable is returned.

## Remarks

This method returns an error if the origin indicator is not set for the drawing view. Use the DrawingView.HasOriginIndicator property to query if an origin has already been set and if not, use DrawingView.CreateOriginIndicator method to set the origin of the drawing view. Note that the origin of the drawing view may have already been defined for creating ordinate dimensions or other hole tables based on this view.

## Syntax

HoleTables.**Add**( ***DrawingView*** As [DrawingView](../DrawingView/DrawingView.md), ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), [***HoleTableStyle***] As Variant, [***Layer***] As Variant ) As [HoleTable](../HoleTable/HoleTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DrawingView | [DrawingView](../DrawingView/DrawingView.md) | Input DrawingView object that specifies the drawing view for which the hole table is to be created. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the position of the top left corner of the table on the sheet. |
| HoleTableStyle | Variant | Optional input HoleTableStyle object that specifies the hole table style to use for the table. If not specified, the default style specified by the standard is used. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the table. If not specified, the default layer specified by the standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |