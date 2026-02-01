# UserCoordinateSystemDefinition.GetByThreePoints Method

Parent Object: [UserCoordinateSystemDefinition](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition.md)

## Description

Method that gets the inputs that fully define the coordinate system. The objects returned will be Nothing if the coordinate system was not parametrically defined (i.e. if the DefinitionType property returns kTransformationDefinitionType). This method returns a failure in assembly documents.

## Syntax

UserCoordinateSystemDefinition.**GetByThreePoints**( ***Origin*** As Object, ***XDirectionPoint*** As Object, ***YDirectionPoint*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Origin | Object | Output object that specifies the origin of the coordinate system. This can be one of the following objects: WorkPoint, Vertex, SketchPoint, SketchPoint3D or Edge. If a linear Edge is specified, it's midpoint is used. If circular or elliptical edges are specified, their center is used. |
| XDirectionPoint | Object | Output object that specifies a point defining the x-direction for the coordinate system. The vector from the origin to this point defines the x-direction vector. This can be one of the following objects: WorkPoint, Vertex, SketchPoint, SketchPoint3D or Edge. If a linear Edge is specified, it's midpoint is used. If circular or elliptical edges are specified, their center is used. |
| YDirectionPoint | Object | Output object that specifies a point defining the y-direction for the coordinate system. This can be one of the following objects: WorkPoint, Vertex, SketchPoint, SketchPoint3D or Edge. If a linear Edge is specified, it's midpoint is used. If circular or elliptical edges are specified, their center is used. |

## Version

Introduced in version 2011
