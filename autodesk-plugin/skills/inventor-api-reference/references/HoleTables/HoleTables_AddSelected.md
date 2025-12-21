# HoleTables.AddSelected Method

Parent Object: [HoleTables](../HoleTables/HoleTables.md)

## Description

Method that creates a new hole table by including only the specified holes. The newly created HoleTable is returned.

## Remarks

This method returns an error if the origin indicator is not set for the drawing view. Use the DrawingView.HasOriginIndicator property to query if an origin has already been set and if not, use DrawingView.CreateOriginIndicator method to set the origin of the drawing view. Note that the origin of the drawing view may have already been defined for creating ordinate dimensions or other hole tables based on this view.

## Syntax

HoleTables.**AddSelected**( ***Holes*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), [***HoleTableStyle***] As Variant, [***Layer***] As Variant ) As [HoleTable](../HoleTable/HoleTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Holes | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection which specifies the holes to create the table with. The collection may contain DrawingCurve objects that represent hole features or circular extrude cuts, or Centermark objects (which include recovered punch centers). All the holes must belong to the same drawing view, else an error will occur. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the position of the top left corner of the table on the sheet. |
| HoleTableStyle | Variant | Optional input HoleTableStyle object that specifies the hole table style to use for the table. If not specified, the default style specified by the standard is used. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the table. If not specified, the default layer specified by the standard is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2009
