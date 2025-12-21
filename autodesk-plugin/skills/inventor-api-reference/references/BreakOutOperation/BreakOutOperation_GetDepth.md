# BreakOutOperation.GetDepth Method

Parent Object: [BreakOutOperation](../BreakOutOperation/BreakOutOperation.md)

## Description

Method that returns the information controlling the depth of the break out.

## Syntax

BreakOutOperation.**GetDepth**( ***DepthSource*** As Object, ***DepthValue*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DepthSource | Object | Graphic object that defines the depth of the break out. Several different types of objects can be returned depending on how the depth of the break out has been defined. The DepthType property can be used to know what type(s) of objects will be returned by this method. Based on the depth type here are the object types you can expect to be returned.    **kFromPointBreakOutType** \* An Edge or Vertex object from the model being displayed in the view is returned. This is different than the GeometryIntent object that would have been provided during creation. Model geometry is returned in this case because in many cases the drawing curve that defines the depth is not visible, and so does not exist in the view containing the break out. \* The DepthValue argument is applicable in this case and gives the offset from this point.  **kToSketchBreakOutType** \* A DrawingSketch object which is associated with a dependant projected view.  **kToHoleBreakOutType** \* A DrawingCurve object that is used to specify a 'hole'. A hole in this case is defined as any geometry from a HoleFeature object or any cylinder or cone in the model. The axis of the hole, cylinder, or cone is parallel to the sheet plane and defines the depth of the hole.  **kThroughPartBreakOutType** \* A PartComponentDefinition object indicates that the entire part is cut. This is only applicable when the drawing view contains a part, not an assembly. \* A ComponentOccurrence (or a ComponentOccurrenceProxy) object in the context of the parent drawing view. The depth is defined by the depth of the associated part. \* An ObjectCollection containing multiple ComponentOccurrence (or ComponentOccurrenceProxy) objects. The depth is defined by the depths of the associated parts. |
| DepthValue | Double | This argument is only applicable when the DepthType is kFromPointBreakOutType otherwise it should be ignored. The depth value is always returned as centimeters. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |