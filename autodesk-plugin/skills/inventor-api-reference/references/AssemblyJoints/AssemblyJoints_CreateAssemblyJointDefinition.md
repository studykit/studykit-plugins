# AssemblyJoints.CreateAssemblyJointDefinition Method

Parent Object: [AssemblyJoints](../AssemblyJoints/AssemblyJoints.md)

## Description

Method that creates a new AssemblyJointDefinition object.

## Syntax

AssemblyJoints.**CreateAssemblyJointDefinition**( ***JointType*** As [AssemblyJointTypeEnum](../AssemblyJointTypeEnum.md), ***OriginOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***OriginTwo*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md) ) As [AssemblyJointDefinition](../AssemblyJointDefinition/AssemblyJointDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| JointType | [AssemblyJointTypeEnum](../AssemblyJointTypeEnum.md) | Input AssemblyJointTypeEnum value that specifies the type of AssemblyJoint. |
| OriginOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the first origin and origin direction of the connection on an occurrence that being connected with others. Valid geometries for defining the first origin and origin direction are:  * Linear edge or sketch line on which the start/mid/end point can be specified as origin. The direction of the linear object defines the origin direction. * Circular/elliptical edge or sketch entity which the center will be used as origin. The normal of the object defines the origin direction. * Cylindrical/conical/elliptical-cylindrical face which the start/mid/end point on the axis of the face can be specified as origin. The axis of the face defines the origin direction. * Toroidal/spherical face which the center will be used as origin. The axis of the toroidal face defines the origin direction. * Planar face that has linear/circular/elliptical edges which the start/mid/end point of linear edge or center of circular/elliptical edge can be specified as origin. The normal of the planar face defines the origin direction. |
| OriginTwo | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the second origin and origin direction of the connection on an occurrence that the first occurrence will be connected to. Refer to OriginOne for the valid geometries for defining the second origin and origin direction. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create planar AssemblyJoint with offset to origins](../../sample-programs/AssemblyJointDefinition_SetOriginOneAsOffset_Sample.md) | This sample demonstrates how to create a planar AssemblyJoint with offset to the OriginOne and OriginTwo. |
| [Create rotational assembly joint](../../sample-programs/AssemblyRotationalJoint_Sample.md) | This sample demonstrates creating an assembly joint. It connects the midpoints of the edges of two faces using a rotational joint. To do this it first creates a geometry intent object of the midpoint of the edge and then creates another intent using the face and the midpoint intent. It does this to create to midpoint intents which it then uses to create the rotational connection.  The sample uses and existing part that must be set up to allow it to work correctly. To create the sample part you can use any part that has a planar face and a linear edge connected to that planar face. A simple box is sufficient. In this part Add a mate iMate to the planar face and rename the iMate to "Face1". Also add a mate iMate to a linear edge that is on the face previously named and rename this iMate to "Edge1". Save the part to "C:\Temp\SamplePart.ipt" or any other name and edit the code below to reference the file. You can then run the sample code which will create a new assembly, insert two instances of the part and create a rotational connection between them. Then it will animation the rotation by driving the connection. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |