# RuledSurfaceFeatures.CreateDefinition Method

Parent Object: [RuledSurfaceFeatures](../RuledSurfaceFeatures/RuledSurfaceFeatures.md)

## Description

Method that creates a new RuledSurfaceDefinition Object.

## Syntax

RuledSurfaceFeatures.**CreateDefinition**( ***RuledSurfaceType*** As [RuledSurfaceTypeEnum](../RuledSurfaceTypeEnum.md), ***GeneratrixCurves*** As Object, ***Distance*** As Variant, [***Vector***] As Variant ) As [RuledSurfaceDefinition](../RuledSurfaceDefinition/RuledSurfaceDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RuledSurfaceType | [RuledSurfaceTypeEnum](../RuledSurfaceTypeEnum.md) | Input RuledSurfaceTypeEnum to specify the type of the ruled surface. |
| GeneratrixCurves | Object | Input RuledSurfaceEdgeFacePairs object or Path containing the 2D or 3D sketch entities base on which to create the ruled surface. If the RuledSurfaceType is specified as kNormalRuledSurfaceType or kTangentRuledSurfaceType this property should be a RuledSurfaceEdgeFacePairs object including Edge objects which are connected end-to-end with each other. If the RuledSurfaceType is specified as kSweepRuledSurfaceType this property can either be a RuledSurfaceEdgeFacePairs object including Edge objects which are connected end-to-end with each other or an Path object including 2D or 3D sketch curves. |
| Distance | Variant | Input Variant that defines the length of the ruled surface. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Vector | Variant | Optional input object that defines the extend direction of ruled surface. This is required if the RuledSurfaceType is specified as kSweepRuledSurfaceType, otherwise this argument is ignored. Valid inputs are Edge, Face, WorkAxis, WorkPlane, SketchLine, and SketchLine3D . |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |