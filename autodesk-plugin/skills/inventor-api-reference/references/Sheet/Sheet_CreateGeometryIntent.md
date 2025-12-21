# Sheet.CreateGeometryIntent Method

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Method that creates a GeometryIntent object for use in various annotation and view creations.

## Syntax

Sheet.**CreateGeometryIntent**( ***Geometry*** As Object, [***Intent***] As Variant ) As [GeometryIntent](../GeometryIntent/GeometryIntent.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | Object | Input object that specifies the geometry. Valid \input objects are DrawingCurve, sketch entities from a sheet sketch, DrawingDimension, Centerline, and Centermark objects. If a DrawingDimension object is input, a Point2d on the dimension must be provided in the Intent argument. A Point object can be provided for true dimensions in an iso\-view. Use the DimensionLine, ExtensionLineOne and ExtensionLineTwo properties on the dimension objects to get points on the dimension. |
| Intent | Variant | Input object that specifies the intent point on the input geometry. This can be a value from PointIntentEnum, a geometry if the intent is the intersection of two geometries, a Point2d object that specifies a sheet point on the geometry or a double value (0 to 1) indicating the parameter on the input curve geometry. The range of valid parameter values can be obtained using the GetParamExtents method on the curve's evaluator. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |
| [Chain dimensions sets](../../sample-programs/ChainDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a chain dimension set in a drawing. |
| [Add detail drawing view](../../sample-programs/DrawingViews_AddDetailView_Sample.md) | This sample demonstrates the creation of a detail drawing view with an attach point. |
| [Create a feature control frame symbol](../../sample-programs/FeatureControlFrames_Add_Sample.md) | This sample demonstrates the creation of a feature control frame symbol. |
| [Creating hole tables](../../sample-programs/HoleTables_Add_Sample.md) | This sample demonstrates the creation of hole tables in a drawing. |
| [Create ordinate dimension](../../sample-programs/OrdinateDimensions_Add_Sample.md) | This sample demonstrates the creation of ordinate dimensions in a drawing document. |
| [create punch note](../../sample-programs/PunchNotes_Add_Sample.md) | This sample demonstrates the creation of a punch note on the drawing view of a flat pattern. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |
| [Add surface texture symbol to dimension](../../sample-programs/SurfaceTextureSymbols_Add_Sample.md) | This sample demonstrates the creation of a surface texture symbol attached to the extension line of a drawing dimension. |

## Version

Introduced in version 11
