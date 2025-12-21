# HoleTables.AddByFeatureType Method

Parent Object: [HoleTables](../HoleTables/HoleTables.md)

## Description

Method that creates a new hole table by including only the holes that are of the specified type in the input drawing view. The newly created HoleTable is returned.

## Remarks

This method returns an error if the origin indicator is not set for the drawing view. Use the DrawingView.HasOriginIndicator property to query if an origin has already been set and if not, use DrawingView.CreateOriginIndicator method to set the origin of the drawing view. Note that the origin of the drawing view may have already been defined for creating ordinate dimensions or other hole tables based on this view.

## Syntax

HoleTables.**AddByFeatureType**( ***DrawingView*** As [DrawingView](../DrawingView/DrawingView.md), ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), ***IncludeDrilledHoleFeatures*** As Boolean, ***IncludeCounterBoreHoleFeatures*** As Boolean, ***IncludeCounterSinkHoleFeatures*** As Boolean, ***IncludeThreadedHoleFeatures*** As Boolean, ***IncludeCircularCuts*** As Boolean, ***IncludeCentermarks*** As Boolean, ***IncludeRecoveredPunchCenters*** As Boolean, [***HoleTableStyle***] As Variant, [***Layer***] As Variant ) As [HoleTable](../HoleTable/HoleTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DrawingView | [DrawingView](../DrawingView/DrawingView.md) | Input DrawingView object that specifies the drawing view for which the hole table is to be created. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the position of the top left corner of the table on the sheet. |
| IncludeDrilledHoleFeatures | Boolean | Input Boolean that specifies whether to include drilled hole features. |
| IncludeCounterBoreHoleFeatures | Boolean | Input Boolean that specifies whether to include counterbored hole features. |
| IncludeCounterSinkHoleFeatures | Boolean | Input Boolean that specifies whether to include countersunk hole features. |
| IncludeThreadedHoleFeatures | Boolean | Input Boolean that specifies whether to include threaded hole features. |
| IncludeCircularCuts | Boolean | Input Boolean that specifies whether to include circular extruded cuts. Circular cuts are recognized only as drilled thru or drilled blind holes, and do not include mid-plane extrusions. |
| IncludeCentermarks | Boolean | Input Boolean that specifies whether to include center marks. Center marks with visibility turned off are not included in the hole table. |
| IncludeRecoveredPunchCenters | Boolean | Input Boolean that specifies whether to include recovered punch center marks. Punch center marks with visibility turned off are not included in the hole table. |
| HoleTableStyle | Variant | Optional input HoleTableStyle object that specifies the hole table style to use for the table. If not specified, the default style specified by the standard is used. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the table. If not specified, the default layer specified by the standard is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating hole tables](../../sample-programs/HoleTables_Add_Sample.md) | This sample demonstrates the creation of hole tables in a drawing. |

## Version

Introduced in version 2009
