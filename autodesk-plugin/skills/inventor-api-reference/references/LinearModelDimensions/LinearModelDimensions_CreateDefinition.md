# LinearModelDimensions.CreateDefinition Method

Parent Object: [LinearModelDimensions](../LinearModelDimensions/LinearModelDimensions.md)

## Description

Method that creates a linear dimension definition. This is a not a linear dimension but an object that encapsulates all of the information that defines a dimension. You use the methods an properties of this object to define the dimension you want to create and then provide it as input to the Add method.

## Syntax

LinearModelDimensions.**CreateDefinition**( ***IntentOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***IntentTwo*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md), ***TextPosition*** As [Point](../Point/Point.md), ***DimensionType*** As [DimensionTypeEnum](../DimensionTypeEnum.md) ) As [LinearModelDimensionDefinition](../LinearModelDimensionDefinition/LinearModelDimensionDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IntentOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the first geometry to dimension to. The GeometryIntent object can be created using the CreateGeometryIntent method on the PartComponentDefinition or AssemblyComponentDefinition object.  Valid entity combinations for the IntentOne and IntentTwo arguments are:  * Two points. * Two linear entities. (Non-parallel lines will result in an angular dimension.) * A linear entity and a point. * A point and a linear entity. * One linear entity. * One circular entity (with DimensionType set to kAlignedDimensionType for chord length and kArcLengthDimensionType for arc length) |
| IntentTwo | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input entity that specifies the second geometry to dimension. In the cases where there is only one entity needed this argument should be set to Nothing (null); |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |
| TextPosition | [Point](../Point/Point.md) | Input Point object that specifies the position of the dimension text. The point will be projected onto the orientation plane. |
| DimensionType | [DimensionTypeEnum](../DimensionTypeEnum.md) | Input DimensionTypeEnum that specifies the linear dimension type. Valid values (based on the input intents) are kAlignedDimensionType, kHorizontalDimensionType, kVerticalDimensionType, kArcLengthDimensionType, kSymmetricDimensionType, kDiametricDimensionType, and kArcLengthDimensionType  An error will occur if the specified type is invalid for the input intents. For instance, kSymmetricDimensionType & kDiametricDimensionType are valid only when two intents are providedone intent is provided as input. the first intent (an edge) is specified. kArcLengthDimensionType is only valid if two intents are supplied and they represent end points of an arc or a single intent is supplied and it represents an arc. |

## Version

Introduced in version 2018
