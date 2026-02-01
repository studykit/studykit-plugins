# Sheet.RetrieveAnnotations Method

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Retrieves sketch and/or model annotations into the drawing.

## Syntax

Sheet.**RetrieveAnnotations**( ***ViewOrSketch*** As Object, [***AnnotationsToRetrieve***] As Variant ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewOrSketch | Object | Input object that specifies the DrawingView or the DrawingSketch object to retrieve annotations from. |
| AnnotationsToRetrieve | Variant | Optional input ObjectCollection that specifies the annotations to retrieve.  If not specified, all annotations from the specified view or sketch are retrieved. If specified, the collection can contain sketch constraint objects or their proxies that derive from DimensionConstraint, FeatureDimension objects or FeatureDimensionProxy objects, 3D annotation objects and their proxy objects. The objects must belong to the view or sketch specified in the first argument, else an error will occur. |

## Version

Introduced in version 2025
