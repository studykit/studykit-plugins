# UserCoordinateSystemDefinition.SetByThreePoints Method

Parent Object: [UserCoordinateSystemDefinition](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition.md)

## Description

Method that sets the inputs that fully define the coordinate system. This method returns a failure in assembly documents.

## Syntax

UserCoordinateSystemDefinition.**SetByThreePoints**( ***Origin*** As Object, ***XDirectionPoint*** As Object, ***YDirectionPoint*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Origin | Object | Input object that specifies the origin of the coordinate system. This can be one of the following objects: WorkPoint, Vertex, SketchPoint, SketchPoint3D or Edge. If a linear Edge is specified, it's midpoint is used. If circular or elliptical edges are specified, their center is used. |
| XDirectionPoint | Object | Input object that specifies a point defining the x-direction for the coordinate system. The vector from the origin to this point defines the x-direction vector. This can be one of the following objects: WorkPoint, Vertex, SketchPoint, SketchPoint3D or Edge. If a linear Edge is specified, it's midpoint is used. If circular or elliptical edges are specified, their center is used. |
| YDirectionPoint | Object | Input object that specifies a point defining the y-direction for the coordinate system. This can be one of the following objects: WorkPoint, Vertex, SketchPoint, SketchPoint3D or Edge. If a linear Edge is specified, it's midpoint is used. If circular or elliptical edges are specified, their center is used. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [UCS by three points](../../sample-programs/UserCoordinateSystems_Add_Sample.md) | This sample demonstrates the creation of a User Coordinate System (UCS) based on 3 points that define the origin, x-direction and y-direction for the UCS. |

## Version

Introduced in version 2011
