# ContourFlangeFeatures.CreateDefinition Method

Parent Object: [ContourFlangeFeatures](../ContourFlangeFeatures/ContourFlangeFeatures.md)

## Description

Creates a new ContourFlangeDefinition object.

## Remarks

The object created does not represent a contour flange feature but instead is a representation of the information that defines a contour flange feature. You can use this object as input to the CoutnourFlangeFeatures.Add method to create the actual contour flange feature.
The ContourFlangeDefinition object returned is fully defined and can be used to create a contour flange feature. However, defaults are used for most of the contour flange options so you may want to change some of the property values of the ContourFlangeDefinition object before using it to create a contour flange feature.

## Syntax

ContourFlangeFeatures.**CreateDefinition**( ***Path*** As [Path](../Path/Path.md), [***Operation***] As Variant, [***WidthExtentsFromSketchPlane***] As Variant, [***EdgeSet***] As Variant, [***BendEdges***] As Variant ) As [ContourFlangeDefinition](../ContourFlangeDefinition/ContourFlangeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Path | [Path](../Path/Path.md) | Input Path object that specifies the shape of the contour flange. |
| Operation | Variant | Optional input PartFeatureOperationEnum to specify operation type. Valid values are kJoinOperation and kNewBodyOperation. |
| WidthExtentsFromSketchPlane | Variant | Optional input Boolean to specify width extent type is from sketch plane or along selected edge. This is applicable only when the Operation is set to kJoinOperation. If not specified this defaults to False.   This is an optional argument whose default value is null. |
| EdgeSet | Variant | Optional input EdgeCollection that specifies the edge set to create a contour flange feature on. The first FlangeEdgeSet is created using these edges, it can be queried using ContourFlangeEdgeSetItem. This is applicable only when the WidthExtentsFromSketchPlane is set to False.   This is an optional argument whose default value is null. |
| BendEdges | Variant | Optional input EdgeCollection object that contains the edges that are used to define the adjoining edges for new face.  This is applicable only when the WidthExtentsFromSketchPlane is set to True.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2026

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |