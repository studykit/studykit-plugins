# AngularModelDimensions.CreateDefinition Method

Parent Object: [AngularModelDimensions](../AngularModelDimensions/AngularModelDimensions.md)

## Description

Method that creates an angular dimension definition. This is a not an angular dimension but an object that encapsulates all of the information that defines a dimension. You use the methods an properties of this object to define the dimension you want to create and then provide it as input to the Add method.

## Syntax

AngularModelDimensions.**CreateDefinition**( ***IntentOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***IntentTwo*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***IntentThree*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md), ***TextPosition*** As [Point](../Point/Point.md) ) As [AngularModelDimensionDefinition](../AngularModelDimensionDefinition/AngularModelDimensionDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IntentOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the first geometry to dimension to. The GeometryIntent object can be created using the CreateGeometryIntent method on the PartComponentDefinition or AssemblyComponentDefinition object.  Valid entity combinations for the IntentOne, IntentTwo, and IntentThree arguments are:  * Three points (Vertex, WorkPoint, SketchPoint, or SketchPoint3D objects) * Two linear entities (linear Edge, WorkAxis, SketchLine, SketchLine3D) * A plane (planar face or work plane) and a linear entity (linear Edge, WorkAxis, SketchLine, SketchLine3D).* * Two planes (planar face or work plane) |
| IntentTwo | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input entity that specifies the second geometry to dimension. In the cases where the second entity is not needed this argument should be set to Nothing (null). |
| IntentThree | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input entity that specifies the third geometry to dimension. In the cases where the third entity is not needed this argument should be set to Nothing (null). |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |
| TextPosition | [Point](../Point/Point.md) | Input Point object that specifies the position of the dimension text. The point will be projected onto the orientation plane. |

## Version

Introduced in version 2018
