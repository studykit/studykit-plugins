# Sheet.GetRetrievableAnnotations Method

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Returns a collection of objects that represent the valid set of model dimensions that can be retrieved into the input drawing view.

## Syntax

Sheet.**GetRetrievableAnnotations**( ***View*** As [DrawingView](../DrawingView/DrawingView.md), [***SketchAndFeatureDimensions***] As Variant, [***ModelObject***] As Variant, [***DesignView***] As Variant ) As [ObjectCollection](../ObjectCollection/ObjectCollection.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| View | [DrawingView](../DrawingView/DrawingView.md) | Input DrawingView object to get the retrievable annotations from. |
| SketchAndFeatureDimensions | Variant | Optional input Boolean that specifies whether to get the retrievable sketch and feature dimensions. This defaults to True. If not specified or this is set to True, the retrievable sketch constraint objects or their proxies that derive from DimensionConstraint, FeatureDimension objects or FeatureDimensionProxy objects will be returned. If this is set to False, the retrievable 3D annotation objects and their proxy objects will be returned. |
| ModelObject | Variant | Optional input object from the model referenced by the drawing view that specifies a filter for this method. If specified, only the annotations related to this object will be returned. Valid inputs include PlanarSketch, any of the objects that derive from PartFeature, ComponentOccurrence and the proxies to all these objects. If not specified, all the valid annotations for the input view are returned.   This is an optional argument whose default value is null. |
| DesignView | Variant | Optional input String value that specifies a design view of the model document to get the retrievable 3D annotation objects. If SketchAndFeatureDimensions is set to True this will be ignored. If SketchAndFeatureDimensions is set to False and ModelObject is provided then this is ignored also. If not provided the default design view will be used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025
