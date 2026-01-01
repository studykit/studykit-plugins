# AssemblyComponentDefinition.Joints Property

Parent Object: [AssemblyComponentDefinition](../AssemblyComponentDefinition/AssemblyComponentDefinition.md)

## Description

Read-only property that returns the AssemblyJoints collection object which provides access to the existing joints in the assembly and provides the capability to create new joints.

## Syntax

AssemblyComponentDefinition.**Joints**() As [AssemblyJoints](../AssemblyJoints/AssemblyJoints.md)

## Property Value

This is a read only property whose value is an [AssemblyJoints](../AssemblyJoints/AssemblyJoints.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create rotational assembly joint](../../sample-programs/AssemblyRotationalJoint_Sample.md) | This sample demonstrates creating an assembly joint. It connects the midpoints of the edges of two faces using a rotational joint. To do this it first creates a geometry intent object of the midpoint of the edge and then creates another intent using the face and the midpoint intent. It does this to create to midpoint intents which it then uses to create the rotational connection.  The sample uses and existing part that must be set up to allow it to work correctly. To create the sample part you can use any part that has a planar face and a linear edge connected to that planar face. A simple box is sufficient. In this part Add a mate iMate to the planar face and rename the iMate to "Face1". Also add a mate iMate to a linear edge that is on the face previously named and rename this iMate to "Edge1". Save the part to "C:\Temp\SamplePart.ipt" or any other name and edit the code below to reference the file. You can then run the sample code which will create a new assembly, insert two instances of the part and create a rotational connection between them. Then it will animation the rotation by driving the connection. |

## Version

Introduced in version 2014
